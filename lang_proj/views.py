from django.shortcuts import render, redirect
from django.core.cache import cache
from . import terms_work
from . import quiz
from lang_proj.views_functions import *
from lang_proj.models import Courses, Terms
import copy


def index(request):
    return render(request, "index.html")


def show_all_courses(request):
    courses = get_all_courses()
    return render(request, "all_courses.html", context={"courses": courses})


def show_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    terms = get_terms_by_id(course_id)
    context = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "terms": terms
    }
    return render(request, "course.html", context)


def delete_course(request, course_id):
    terms = Terms.objects.filter(course_id=course_id)
    for t in terms:
        t.delete()
    Courses.objects.get(id=course_id).delete()
    return redirect('/courses')


def add_course(request):
    return render(request, "course_add.html")


def create_course(request):
    if request.method == "POST":
        cache.clear()
        course_name = request.POST.get("course_name")
        description = request.POST.get("description", "")
        terms = request.POST.get("terms", "")
        context = {"name": course_name}
        if len(terms) == 0:
            context["success"] = False
            context["comment"] = "Список слов должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            write_course(course_name, description, terms)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "course_request.html", context)
    else:
        add_course(request)


"""Глобальная переменная, в которой хранится словарь:
ключи -- ключи сессий, значения -- объекты Quiz."""
global quizzes


def start_quiz(request):
    if not request.session.session_key:
        request.session.create()

    global quizzes
    if 'quizzes' in globals():
        quizzes[request.session.session_key] = quiz.Quiz()
    else:
        quizzes = dict()
        quizzes[request.session.session_key] = quiz.Quiz()
    context = {
        "terms": quizzes[request.session.session_key].qna,
        "quiz_start": True
    }
    return render(request, "quiz.html", context)


def check_quiz(request):
    global quizzes
    if 'quizzes' not in globals():
        return redirect("/quiz")
    if request.method == "POST" and request.session.session_key in quizzes:
        for i in range(1, 5+1):  #TODO: вынести количество вопросов в .env
            quizzes[request.session.session_key].record_user_answer(request.POST.get("answer" + "-" + str(i)))
        terms = copy.copy(quizzes[request.session.session_key].qna)
        answers = copy.copy(quizzes[request.session.session_key].get_user_answers())
        marks = copy.copy(quizzes[request.session.session_key].check_quiz())
        del quizzes[request.session.session_key]
        context = {
            "terms": terms,
            "quiz_start": False,
            "answers": answers,
            "marks": marks
        }
        return render(request, "quiz.html", context=context)
    return redirect("/quiz")


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

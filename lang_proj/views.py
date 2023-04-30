from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from lang_proj.views_functions import *
from lang_proj.models import Courses, Terms
from django.shortcuts import redirect


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
    return render(request, "course.html", context=context)


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


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

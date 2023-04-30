from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from lang_proj.models import Courses, Terms

def index(request):
    return render(request, "index.html")


def show_all_courses(request):
    # courses = terms_work.get_terms_for_table()
    courses = []
    for course in Courses.objects.all():
        terms_num = len(Terms.objects.filter(course_id=course.id))
        courses.append([str(course.id), str(course.name), terms_num])
    return render(request, "all_courses.html", context={"courses": courses})


def show_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    terms = Terms.objects.filter(course_id=course_id)
    terms_list = []
    for t in terms:
        terms_list.append([t.id, t.word, t.translation])
    return render(request, "course.html", context={"name": course.name, "comment": course.comment, "terms": terms_list})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

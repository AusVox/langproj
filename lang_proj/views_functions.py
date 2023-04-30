from lang_proj.models import Courses, Terms


def get_all_courses():
    courses = []
    for i, course in enumerate(Courses.objects.all()):
        terms_num = len(Terms.objects.filter(course_id=course.id))
        courses.append([i+1, str(course.id), str(course.name), terms_num])
    return courses


def get_terms_by_id(course_id: int):
    terms = Terms.objects.filter(course_id=course_id)
    terms_list = []
    for i, t in enumerate(terms):
        terms_list.append([i+1, t.word, t.translation])
    return terms_list


def write_course(name, description, terms: str):
    course = Courses(name=name, description=description)
    course.save()
    terms = terms.splitlines()
    for t in terms:
        word = t.split('-')[0].strip()
        translation = t.split()[1].strip()
        term = Terms(course_id=course.id, word=word, translation=translation)
        term.save()

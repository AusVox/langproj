"""lang_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.show_all_courses),
    path('courses/<int:course_id>/', views.show_course),
    path('courses/<int:course_id>/delete', views.delete_course),
    path('add-course', views.add_course),
    path('create-course', views.create_course),
    path('quiz', views.start_quiz),
    path('check-quiz', views.check_quiz),
    path('stats', views.show_stats)
]

from django.urls import path

from . import views

urlpatterns = [
    path('user_details', views.user_details, name='user_details'),
    path('classes_enrolled', views.classes_enrolled, name='classes_enrolled'),
    path('classes_teaching', views.ListCreateClassroom.as_view(), name='classes_teaching'),
    path('classes/<str:code>', views.classes, name='classes'),
    path('classes/<str:code>/announcements', views.announcements, name='announcements'),
    path('classes/<str:code>/students', views.students, name='students'),
    path('classes/<str:code>/announcements/<int:id>/comments', views.announcement_comments, name='announcement_comments'),
    path('join_class', views.join_class, name='join_class'),
]

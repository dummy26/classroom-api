from django.urls import include, path

from . import views

urlpatterns = [
    path('users/', include('user.urls')),

    path('classes', views.AllClasses.as_view(), name='classes'),
    path('classes_enrolled', views.ClassesEnrolled.as_view(), name='classes_enrolled'),
    path('classes_teaching', views.ListCreateTeachingClassroom.as_view(), name='classes_teaching'),

    path('classes/<str:code>/', include('classroom.urls')),

    path('all_assignments_to_do', views.AllAssignmentsToDo.as_view(), name='all_assignments_to_do'),
    path('all_to_review', views.AllToReview.as_view(), name='all_to_review'),
]

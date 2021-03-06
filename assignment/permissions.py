from classroom.models import Classroom
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from assignment.models import Assignment, Submission


class IsTeacherOrStudentReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        classroom = get_object_or_404(Classroom, code=view.kwargs['code'])

        if request.method == 'GET':
            return classroom.is_user_part_of_classroom(user)

        if request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT':
            return classroom.is_user_a_teacher(user)


class IsAssignmentPartOfClassroom(BasePermission):
    def has_permission(self, request, view):
        code = view.kwargs['code']
        assignment_id = view.kwargs['assignment_id']
        classroom = get_object_or_404(Classroom, code=code)
        assignment = get_object_or_404(Assignment, id=assignment_id)

        return assignment.classroom == classroom


class IsSubmissionPartOfAssignment(BasePermission):
    def has_permission(self, request, view):
        submission_id = view.kwargs['submission_id']
        assignment_id = view.kwargs['assignment_id']
        assignment = get_object_or_404(Assignment, id=assignment_id)
        submission = get_object_or_404(Submission, id=submission_id)

        return submission.assignment == assignment


class IsTeacherOrStudentReadOnlyAssignmentDetail(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        code = view.kwargs['code']
        classroom = get_object_or_404(Classroom, code=code)

        if request.method == 'GET':
            return classroom.is_user_part_of_classroom(user)

        if request.method == 'DELETE' or request.method == 'PUT':
            return classroom.is_user_a_teacher(user)


class IsTeacherOrStudentPostOnlySubmissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        code = view.kwargs['code']
        classroom = get_object_or_404(Classroom, code=code)

        if request.method == 'GET' or request.method == 'PATCH':
            return classroom.is_user_a_teacher(user)

        if request.method == 'POST':
            return classroom.is_user_a_student(user)


class IsStudentReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        code = view.kwargs['code']
        classroom = get_object_or_404(Classroom, code=code)

        if request.method == 'GET':
            return classroom.is_user_a_student(user)

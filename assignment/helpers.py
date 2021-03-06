from datetime import datetime, timezone


def get_submission_data(due_date_time, student, submission):
    if submission is not None:
        status = submission.status

    elif due_date_time > datetime.now(timezone.utc):
        status = 'Assigned'
    else:
        status = 'Missing'

    return {'student': student, 'submission': submission, 'status': status}


def get_student_submission_data(assignment, student, submission):
    if submission is not None:
        status = submission.status

    elif assignment.due_date_time > datetime.now(timezone.utc):
        status = 'Assigned'
    else:
        status = 'Missing'

    return {'student': student, 'submission': submission, 'assignment': assignment, 'status': status}

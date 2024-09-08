from django.urls import path
from .views import (
    GradeView, SendMessageView, MessageView, SelectedLessonView,
    SubmitLessonsView,
    StudentFutureView,
    DeleteMessageView,
    UpdateCapacityView,
    CourseApprovalView,
    LessonSelectionView,
    UpdateWeekTableView,
)

urlpatterns = [
    path('course/<slug:slug>/', GradeView.as_view(), name='teacher_grading'),
    path('lesson-selection/', LessonSelectionView.as_view(),
         name='lesson_selection'),
    path('update_capacity/', UpdateCapacityView.as_view(),
         name='update_capacity'),
    path('update_week_table/', UpdateWeekTableView.as_view(),
         name='update_week_table'),
    path('submit_lessons/', SubmitLessonsView.as_view(),
         name='submit_lessons'),
    path('selected_lessons/', SelectedLessonView.as_view(),
         name='selected_lessons'),
    path('send_message/', SendMessageView.as_view(), name='send_message'),
    path('message/', MessageView.as_view(), name='message'),
    path('delete_message/<int:id>', DeleteMessageView.as_view(),
         name='delete_message'),
    path('course_approval/', CourseApprovalView.as_view(),
         name='course_approval'),
    path('my_future/',
         StudentFutureView.as_view(),
         name='student_future'),
]

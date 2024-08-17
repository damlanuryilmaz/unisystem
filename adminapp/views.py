from .forms import DepartmentRequestForm, AssignAdviserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from accountapp.models import Student
from django.views import View


class AssignLesson(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "adminapp/assign_lesson.html")


class DepartmentRequest(LoginRequiredMixin, View):
    def get(self, request):
        students = Student.objects.filter(department_request=True)
        students_wo_adviser = Student.objects.filter(adviser=None)
        form = DepartmentRequestForm()
        adviserform = AssignAdviserForm()
        print(students_wo_adviser)

        context = {
            'form': form,
            'adviserform': adviserform,
            'students': students,
            'students_wo_adviser': students_wo_adviser
        }

        return render(request, "adminapp/department_request.html", context)

    def post(self, request):

        form = DepartmentRequestForm(request.POST)

        if form.is_valid():
            student_id = request.POST.get('student')
            student = Student.objects.get(id=student_id)
            student.department_of_student = form.cleaned_data[
                'department_of_student']
            student.department_request = False
            student.save()
            return redirect('department_request')

        else:
            students = Student.objects.filter(department_request=True)

            context = {
                'students': students,
                'form': form
            }
            return render(request, "adminapp/department_request.html", context)


class AssignAdviser(LoginRequiredMixin, View):
    def post(self, request):
        form = AssignAdviserForm(request.POST)
        
        if form.is_valid():
            student_id = request.POST.get('student')
            student = Student.objects.get(id=student_id)
            student.adviser = form.cleaned_data['adviser']
            student.save()
            
        return redirect('department_request')

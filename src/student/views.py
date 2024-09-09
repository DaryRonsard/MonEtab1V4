from django.shortcuts import render, redirect

from student.forms.Student_forms import StudentForm
from student.models import StudentModel


def index(request):
    student = StudentModel.objects.all()
    student_user = student.count()
    context = {
        'student': student,
        'student_user': student_user
    }
    return render(request, 'listStudent.html', context)




# Create your views here.
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirigez vers une page où vous listez les étudiants
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.forms.student_forms import StudentForm
from student.models.student_model import StudentModel

@login_required(login_url='dashboard:sign_in')
def list_students(request):
    student = StudentModel.objects.all()

    context = {
        'student': student
    }
    return render(request, "liststudent.html", context)

@login_required(login_url='dashboard:sign_in')
def create_student(request):
    context = {
        'title': 'Ajouter un Elève',
        'submit_value': 'Ajouter',
        'h1': 'Nouvel Elève',
    }

    if request.method == 'POST':
        form = StudentForm(request.POST)
        # user_form = UserForm(request.POST)
        if form.is_valid():
            student_instance = form.save(commit=False)
            student_instance.active = True
            student_instance.save()
            # user_instance = user_form.save(commit=False)
            # user_instance.student = student_instance
            # user_instance.save()
            messages.success(request, 'L\'élève a été ajouté avec succès.')
            return redirect("student:list-students")
        else:
            print('erreur')
    else:
        form = StudentForm()
        # user_form = UserForm()
    context['form'] = form
    # context['forms'] = user_form

    return render(request, "formsStudent.html", context)

@login_required(login_url='dashboard:sign_in')
def update_student(request, id):
    student = StudentModel.objects.get(id=id)
    # user = get_object_or_404(UserModel, student=student)
    context = {
        'title': 'Modifier l\'Elève',
        'submit_value': 'Modifier',
        'h1': 'Modifier Elève',
    }
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        # user_form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # user_form.save()
            return redirect("student:list-student")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")

    student_form = StudentForm(instance=student)
    # user_form = UserForm(instance=user)
    context['form'] = student_form
    # context['forms'] = user_form

    return render(request, "formsStudent.html", context)

@login_required(login_url='dashboard:sign_in')
def delete_student(request, id):
    student = get_object_or_404(StudentModel, id=id)
    # user = get_object_or_404(UserModel, student=student)
    student.status = False
    student.active = False
    student.save()
    # user.is_active = False
    # user.save()

    return redirect('student:list-student')
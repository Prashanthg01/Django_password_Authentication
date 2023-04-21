from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Student

@user_passes_test(lambda u: u.is_staff)
def home(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password == '123456':
            students = Student.objects.all()
            return render(request, 'home.html', {'students': students})
        else:
            messages.error(request, 'Incorrect password, please try again.')
            return redirect('home')
    else:
        return render(request, 'password.html')
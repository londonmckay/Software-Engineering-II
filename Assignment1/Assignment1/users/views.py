from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.vary import vary_on_cookie
from .forms import RegistrationForm


@vary_on_cookie
def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        return redirect('mysite:main')
    return render(request, 'users/login.html', {
        'form': form
    })


def profile(request):
    return render(request, 'users/profile.html')


def calendar(request):
    return render(request, 'users/calendar.html')


def courses(request):
    return render(request, 'users/courses.html')


def image(request):
    return render(request, 'users/image.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')

            messages.success(request, f'Registration Successful {firstname} {lastname}!')
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def image(request):
    if request.method == 'POST' and request.FILES['image']:
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'users/image.html', {'file_url': file_url})
    return render(request, 'users/image.html')

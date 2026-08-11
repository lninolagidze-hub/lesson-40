from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserUpdateForm



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(
        request,
        'users/register.html',
        {
            'form': form,
        }
    )


@login_required
def profile(request):
    user = request.user

    return render(
        request,
        'users/profile.html',
        {
            'user': user,
        }
    )


@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=user)

    return render(
        request,
        'users/update_profile.html',
        {
            'form': form,
        }
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            return render(
                request,
                'users/login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(
        request,
        'users/login.html'
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
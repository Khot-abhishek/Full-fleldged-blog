from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegiterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegiterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            messages.success(
                request, f"Account sucessfully created! Now you can Log In here.")
            form.save()
            return redirect('login')
    else:
        form = UserRegiterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

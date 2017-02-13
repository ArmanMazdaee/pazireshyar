from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

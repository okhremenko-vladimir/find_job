from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

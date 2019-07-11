from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegistrationForm
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'myapp/index.html')


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        ctx = {'form': form}
        return render(request, 'myapp/register.html', ctx)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Konto użytkownika zostało utworzone!')
            return redirect('index')
        else:
            form = UserRegistrationForm()
            ctx = {'form': form}
            return render(request, 'myapp/register.html', ctx)


class AdminProfileView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.filter(is_superuser=True)
        return render(request, 'myapp/admin_site.html', {'users': users})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserRegistrationForm(instance=request.user)
        ctx = {'form': form}
        return render(request, 'myapp/user_site.html', ctx)
    def post(self, request):
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dane zostały zmienione!')
            return redirect('index')
        else:
            form = UserRegistrationForm(instance=request.user)
            ctx = {'form': form}
            return render(request, 'myapp/user_site.html', ctx)


class RedirectUserView(LoginRequiredMixin, View):
    def get(self, request):
        if self.request.user.is_superuser == True:
            return redirect('admin-profile')
        else:
            return redirect('user-profile')

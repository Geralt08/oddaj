from django.shortcuts import render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'myapp/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'myapp/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'myapp/register.html')

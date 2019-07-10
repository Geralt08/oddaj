from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'myapp/index.html')


# class LoginView(View):
#     def get(self, request):
#         return render(request, 'myapp/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'myapp/register.html')

    def post(self, request):
        pass


class AdminProfileView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.filter(is_superuser=True)
        return render(request, 'myapp/admin_site.html', {'users': users})


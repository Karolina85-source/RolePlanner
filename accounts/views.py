from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import DeleteView
from django.shortcuts import render


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_register.html'

    def form_valid(self, form):
        messages.success(self.request, "Rejestracja zakończona sukcesem. Możesz się zalogować.")
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'registration/user_confirm_delete.html'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Twoje konto zostało usunięte.")
        return super().delete(request, *args, **kwargs)

#class UserDeleteView(LoginRequiredMixin, DeleteView):
#   model = User
#   template_name = 'registration/user_confirm_delete.html'
#   success_url = reverse_lazy('user-deleted')
#
#    def get_object(self, queryset=None):
#        return self.request.user

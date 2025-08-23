from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Script
from .models import Character
from .models import Scene
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RoleAssignment, SceneRole
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required

class ScriptList(LoginRequiredMixin, ListView):
    model = Script
    template_name = 'scripts/script_list.html'
    context_object_name = 'scripts'

    def get_queryset(self):
        # pokazujemy scenariusze tylko zalogowanego użytkownika
        return Script.objects.filter(owner=self.request.user)

class ScriptCreate(LoginRequiredMixin, CreateView):
    model = Script
    fields = ['title', 'description']
    template_name = 'scripts/script_form.html'
    success_url = reverse_lazy('script_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CharacterList(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'scripts/character_list.html'
    context_object_name = 'characters'

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = ['name', 'bio']
    template_name = 'scripts/character_form.html'
    success_url = reverse_lazy('character_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SceneList(LoginRequiredMixin, ListView):
    model = Scene
    template_name = 'scripts/scene_list.html'
    context_object_name = 'scenes'

class SceneCreate(LoginRequiredMixin, CreateView):
    model = Scene
    fields = ['script', 'title', 'summary']
    template_name = 'scripts/scene_form.html'
    success_url = '/scenes/'

# Szczegóły scenariusza
class ScriptDetail(LoginRequiredMixin, DetailView):
    model = Script
    template_name = 'scripts/script_detail.html'
    context_object_name = 'script'

# Edycja scenariusza
class ScriptUpdate(LoginRequiredMixin, UpdateView):
    model = Script
    fields = ['title', 'description']
    template_name = 'scripts/script_form.html'
    success_url = reverse_lazy('script_list')

# Szczegóły postaci
class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character
    template_name = 'scripts/character_detail.html'
    context_object_name = 'character'

# Edycja postaci
class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ['name', 'bio']
    template_name = 'scripts/character_form.html'
    success_url = reverse_lazy('character_list')

# Szczegóły sceny
class SceneDetail(LoginRequiredMixin, DetailView):
    model = Scene
    template_name = 'scripts/scene_detail.html'
    context_object_name = 'scene'

# Edycja sceny
class SceneUpdate(LoginRequiredMixin,UpdateView):
    model = Scene
    fields = ['script', 'title', 'summary']
    template_name = 'scripts/scene_form.html'
    success_url = reverse_lazy('scene_list')

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'scripts/note_list.html'
    context_object_name = 'notes'

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['body', 'script', 'scene', 'character']
    template_name = 'scripts/note_form.html'
    success_url = '/notes/'

class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'scripts/note_detail.html'
    context_object_name = 'note'

class RoleAssignmentList(LoginRequiredMixin, ListView):
    model = RoleAssignment
    template_name = 'scripts/roleassignment_list.html'
    context_object_name = 'role_assignments'

class RoleAssignmentCreate(LoginRequiredMixin, CreateView):
    model = RoleAssignment
    fields = ['script', 'character']
    template_name = 'scripts/roleassignment_form.html'
    success_url = '/roleassignments/'

class SceneRoleList(LoginRequiredMixin, ListView):
    model = SceneRole
    template_name = 'scripts/scenerole_list.html'
    context_object_name = 'scene_roles'

class SceneRoleCreate(LoginRequiredMixin, CreateView):
    model = SceneRole
    fields = ['scene', 'character']
    template_name = 'scripts/scenerole_form.html'
    success_url = '/sceneroles/'

@login_required
def dashboard(request):
    return render(request, 'scripts/dashboard.html')

class LogoutGetView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Po rejestracji przekierowanie do logowania
    template_name = 'registration/account_register.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'scripts/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
def home(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'scripts/home.html')

class ScriptDelete(LoginRequiredMixin, DeleteView):
    model = Script
    template_name = 'scripts/script_confirm_delete.html'
    success_url = reverse_lazy('script_list')

class SceneUpdate(LoginRequiredMixin, UpdateView):
    model = Scene
    fields = ['script', 'title', 'summary']
    template_name = 'scripts/scene_form.html'
    success_url = reverse_lazy('scene_list')

class SceneDelete(LoginRequiredMixin, DeleteView):
    model = Scene
    template_name = 'scripts/scene_confirm_delete.html'
    success_url = reverse_lazy('scene_list')

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ['name', 'bio']
    template_name = 'scripts/character_form.html'
    success_url = reverse_lazy('character_list')

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    template_name = 'scripts/character_confirm_delete.html'
    success_url = reverse_lazy('character_list')

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['body', 'script', 'scene', 'character']
    template_name = 'scripts/note_form.html'
    success_url = reverse_lazy('note_list')

class RoleAssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = RoleAssignment
    fields = ['script', 'character']
    template_name = 'scripts/roleassignment_form.html'
    success_url = reverse_lazy('roleassignment_list')

class RoleAssignmentDelete(LoginRequiredMixin, DeleteView):
    model = RoleAssignment
    template_name = 'scripts/roleassignment_confirm_delete.html'
    success_url = reverse_lazy('roleassignment_list')

class SceneRoleUpdate(LoginRequiredMixin, UpdateView):
    model = SceneRole
    fields = ['scene', 'character']
    template_name = 'scripts/scenerole_form.html'
    success_url = reverse_lazy('scenerole_list')

class SceneRoleDelete(LoginRequiredMixin, DeleteView):
    model = SceneRole
    template_name = 'scripts/scenerole_confirm_delete.html'
    success_url = reverse_lazy('scenerole_list')




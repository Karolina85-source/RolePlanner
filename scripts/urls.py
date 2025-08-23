from django.urls import path
from . import views
from .views import NoteDeleteView


urlpatterns = [
    path('scripts/', views.ScriptList.as_view(), name='script_list'),
    path('scripts/add/', views.ScriptCreate.as_view(), name='script_add'),
    path('characters/', views.CharacterList.as_view(), name='character_list'),
    path('characters/add/', views.CharacterCreate.as_view(), name='character_add'),
    path('scenes/', views.SceneList.as_view(), name='scene_list'),
    path('scenes/add/', views.SceneCreate.as_view(), name='scene_add'),
    path('scenes/<int:pk>/', views.SceneDetail.as_view(), name='scene_detail'),
    path('scenes/<int:pk>/edit/', views.SceneUpdate.as_view(), name='scene_edit'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='character_detail'),
    path('characters/<int:pk>/edit/', views.CharacterUpdate.as_view(), name='character_edit'),
    path('scripts/<int:pk>/', views.ScriptDetail.as_view(), name='script_detail'),  # to musisz mieć
    path('scripts/<int:pk>/edit/', views.ScriptUpdate.as_view(), name='script_edit'),
    path('notes/', views.NoteList.as_view(), name='note_list'),
    path('notes/add/', views.NoteCreate.as_view(), name='note_add'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('roleassignments/', views.RoleAssignmentList.as_view(), name='roleassignment_list'),
    path('roleassignments/add/', views.RoleAssignmentCreate.as_view(), name='roleassignment_add'),
    path('sceneroles/', views.SceneRoleList.as_view(), name='scenerole_list'),
    path('sceneroles/add/', views.SceneRoleCreate.as_view(), name='scenerole_add'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('scripts/<int:pk>/delete/', views.ScriptDelete.as_view(), name='script_delete'),
    path('scenes/<int:pk>/delete/', views.SceneDelete.as_view(), name='scene_delete'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
    path('notes/<int:pk>/edit/', views.NoteUpdate.as_view(), name='note_edit'),
    path('roleassignments/<int:pk>/edit/', views.RoleAssignmentUpdate.as_view(), name='roleassignment_edit'),
    path('roleassignments/<int:pk>/delete/', views.RoleAssignmentDelete.as_view(), name='roleassignment_delete'),
    path('sceneroles/<int:pk>/edit/', views.SceneRoleUpdate.as_view(), name='scenerole_edit'),
    path('sceneroles/<int:pk>/delete/', views.SceneRoleDelete.as_view(), name='scenerole_delete'),


]


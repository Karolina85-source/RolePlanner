from django.contrib import admin
from .models import Script, Character, Scene, RoleAssignment, SceneRole, Note

admin.site.register(Script)
admin.site.register(Character)
admin.site.register(Scene)
admin.site.register(RoleAssignment)
admin.site.register(SceneRole)
admin.site.register(Note)

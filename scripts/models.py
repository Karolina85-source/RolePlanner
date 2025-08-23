from django.db import models
from django.contrib.auth.models import User

class Script(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # wiele do jednego
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Scene(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, related_name='scenes')
    title = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RoleAssignment(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character} in {self.script}"

class SceneRole(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character} in scene {self.scene}"

class Note(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    script = models.ForeignKey(Script, on_delete=models.CASCADE, null=True, blank=True)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, null=True, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.body[:30]



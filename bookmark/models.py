from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    roles = models.ManyToManyField('Rol', related_name="roles_user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Rol(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class Bookmark(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    url = models.URLField(max_length=500, blank=False, null=False)
    private = models.BooleanField(default=False, verbose_name='Privado')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+',
                                   blank=True, null=True, verbose_name="Creado por", on_delete=models.PROTECT)

    class Meta:
        ordering = ['-id']
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"

    def active(self):
        self.private = True
        self.save()

    def deactive(self):
        self.private = False
        self.save()

    def __str__(self):
        return self.title

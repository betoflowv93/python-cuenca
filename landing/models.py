from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

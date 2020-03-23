from django.db import models

class User(models.Model):
    # Django automatically adds primary keys
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

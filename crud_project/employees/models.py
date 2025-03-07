from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)

    department = models.CharField(max_length=100)
    age = models.IntegerField(default=30)  # ✅ Set default value

    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

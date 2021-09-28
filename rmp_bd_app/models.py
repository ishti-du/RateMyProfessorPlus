from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country

class University(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    university = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'universities'


    def __str__(self):
        return self.university


class Department(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'departments'


    def __str__(self):
        return self.department



class Faculty(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'faculties'


    def __str__(self):
        return self.faculty


class Feedback(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    feedback = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'feedbacks'


    def __str__(self):
        return f"{self.feedback[:20]}..."

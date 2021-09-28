from django.contrib import admin

# Register your models here.
from .models import Country
from .models import University
from .models import Department
from .models import Faculty
from .models import Feedback

admin.site.register(Country)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Feedback)

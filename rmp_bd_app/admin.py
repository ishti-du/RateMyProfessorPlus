

from django.contrib import admin

from .models import Campus
from .models import Campus_Professor
# Register your models here.
from .models import Country
from .models import Course
from .models import Department
from .models import Prereq
from .models import Professor
from .models import Professor_Course
from .models import Review
from .models import Review_Tag
from .models import Tag
from .models import University
from .models import User

# from .models import Faculty
# from .models import Feedback

admin.site.register(Country)
admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Campus_Professor)
admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(Professor_Course)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Review_Tag)


# admin.site.register(Faculty)
# admin.site.register(Feedback)

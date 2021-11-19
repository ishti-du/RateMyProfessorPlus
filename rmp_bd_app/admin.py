from django.contrib import admin

# Register your models here.
from .models import University
from .models import Campus
from .models import Department
from .models import Professor
from .models import UniversityProfessor
from .models import Course
from .models import Prereq
from .models import ProfessorCourse
from .models import Review
from .models import Tag
from .models import ReviewTag
from .models import StudentProfile
from .models import ProfessorProfile


admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(UniversityProfessor)
admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(ProfessorCourse)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(ReviewTag)
admin.site.register(StudentProfile)
admin.site.register(ProfessorProfile)

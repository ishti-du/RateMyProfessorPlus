from django.db import models
import datetime

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

#from django_countries.fields import CountryField

from django_countries.fields import CountryField


# for year in Review model https://stackoverflow.com/questions/49051017/year-field-in-django/54791915
def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class University(models.Model):
    country = CountryField(blank_label='(Select a Country)')
    university_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'universities'

    def __str__(self):
        return self.university_name


class Campus(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    campus_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'campuses'

    def __str__(self):
        return self.campus_name


class Department(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.department_name


class Professor(models.Model):
    current_university = models.ForeignKey(
        University, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    honorific = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'professors'

    def __str__(self):
        if self.honorific:
            return self.honorific + " " + self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name


# Enables accessing past universities (campuses and campuses if provided) a professors taught at
class UniversityProfessor(models.Model):
    professor = models.ForeignKey(University, on_delete=models.CASCADE)
    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    course_number = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_university = models.ForeignKey(University, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.course_title


class Prereq(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_id')
    prereq = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='prereq_id')

    class Meta:
        verbose_name_plural = 'prerequisites'


# junction table (how to deal with many-to-many relation)
# a professor can teach many different courses
# a course can be taught by many different professors
class ProfessorCourse(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


# storing ip address https://stackoverflow.com/questions/1038950/what-is-the-most-appropriate-data-type-for-storing-an-ip-address-in-sql-server
class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile")
    university = models.ForeignKey(
        University, on_delete=models.CASCADE, blank=True, null=True)
    ip_address = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)


class ProfessorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professor_profile")
    faculty_directory_url = models.CharField(max_length=255, blank=True)
    faculty_phone_number = models.CharField(max_length=255, blank=True)
    ip_address = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    GRADES = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('D-', 'D-'),
        ('F', 'F'),
        ('Drop/Withdrawal', 'Drop/Withdrawal'),
        ('Incomplete', 'Incomplete'),
        ('Not sure yet', 'Not sure yet'),
        ('Rather not say', 'Rather not say'),
        ('Audit/No Grade', 'Audit/No Grade'),
    )

    SEMESTERS = (
        ('WNTR', 'Winter'),
        ('SPR', 'Spring'),
        ('SMR', 'Summer'),
        ('FALL', 'Fall'),
    )

    # professor_course = models.ForeignKey(Professor_Course, default=None)
    # if the professor associated with the review is deleted the review will be deleted as well
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    # if the course associated with the review is deleted the review has no associated course
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    university = models.ForeignKey(University, on_delete=CASCADE)
    campus = models.ForeignKey(
        Campus, on_delete=CASCADE, blank=True, null=True)

    campus = models.ForeignKey(Campus, on_delete=CASCADE)
    # if the user associated with the review is deleted the review will be deleted as well
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.CharField(max_length=15)
    grade = models.CharField(max_length=15, choices=GRADES)
    mad_text = models.CharField(max_length=350, null=True, blank=True)
    sad_text = models.CharField(max_length=350, null=True, blank=True)
    glad_text = models.CharField(max_length=350, null=True, blank=True)
    thumbs_up = models.PositiveIntegerField(default=0)
    thumbs_down = models.PositiveIntegerField(default=0)
    report_flag = models.PositiveIntegerField(default=0)

    mad_text = models.CharField(max_length=350)
    sad_text = models.CharField(max_length=350)
    glad_text = models.CharField(max_length=350)
    # for setting a range on difficulty_level and score https://stackoverflow.com/questions/33772947/django-set-range-for-integer-model-field-as-constraint
    difficulty_level = models.IntegerField(
        default=0,
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    )
    professor_score = models.IntegerField(
        default=0,
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    )
    semester = models.CharField(max_length=4, choices=SEMESTERS)
    year = models.IntegerField(choices=year_choices(), default=current_year())
    # was a textbook used
    is_textbook = models.BooleanField()
    # was attendance mandatory
    is_attendance = models.BooleanField()
    # was the class taken for credit
    is_credit = models.BooleanField()
    # was the class online
    is_online = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)


    #https://stackoverflow.com/questions/1372016/django-models-custom-functions
    # function: returns a dictionary of sorted reviews based on mad, sad, glad, or all category
    @staticmethod
    def mad_reviews(curr_professor):
        return [r.mad_text for r in Review.objects.filter(professor = curr_professor, mad_text__isnull = False)]

    @staticmethod
    def sad_reviews(curr_professor):
        return [r.sad_text for r in Review.objects.filter(professor = curr_professor, sad_text__isnull = False)]


    @staticmethod
    def glad_reviews(curr_professor):
        return [r.glad_text for r in Review.objects.filter(professor = curr_professor, glad_text__isnull = False)]

    @staticmethod

    def all_reviews(curr_professor):
        return [r.glad_text + " " + r.sad_text + " " + r.mad_text for r in Review.objects.all()]

    class Meta:
        verbose_name_plural = 'reviews'


class FlagManager(models.Manager):

    def get_queryset(*args, **kwargs):
        return Review.objects.get(
            report_flags=10
        )


class Tag(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.text


# tag and review junction table
class ReviewTag(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class ThumbUp(models.Model):
    ''' Review Thumb Up '''

    review = models.OneToOneField(
        Review, related_name="thumb_ups", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='thumb_ups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ThumbDown(models.Model):
    ''' Review Thumb Down '''

    review = models.OneToOneField(
        Review, related_name="thumb_downs", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='thumb_downs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReportFlag(models.Model):
    ''' Review Report Flags '''

    review = models.OneToOneField(
        Review, related_name="report_flags", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='report_flags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

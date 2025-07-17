from django.db import models
from django.contrib.auth.models import User  # Use Django's default User model


# Program details linked to a specific user
class ProgramDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="program_details", default=1)  # Link to the user
    nba_code = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_target = models.CharField(max_length=100)
    academic_year = models.IntegerField()
    num_students = models.IntegerField()
    faculty_name = models.CharField(max_length=100)
    program_title = models.CharField(max_length=100)
    semester_section = models.CharField(max_length=100)
    max_see_marks = models.IntegerField()
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.program_title} ({self.academic_year})'


# Course outcomes (generic or user-specific if needed)
class CourseOutcome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_outcomes", null=True, blank=True)  # Optional user link
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code



class COPOMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="copo_mappings", null=True, blank=True)
# Link to the user
    co_number = models.CharField(max_length=10)  # e.g., CO1, CO2, etc.
    po1 = models.IntegerField(null=True, blank=True)
    po2 = models.IntegerField(null=True, blank=True)
    po3 = models.IntegerField(null=True, blank=True)
    po4 = models.IntegerField(null=True, blank=True)
    po5 = models.IntegerField(null=True, blank=True)
    po6 = models.IntegerField(null=True, blank=True)
    po7 = models.IntegerField(null=True, blank=True)
    po8 = models.IntegerField(null=True, blank=True)
    po9 = models.IntegerField(null=True, blank=True)
    po10 = models.IntegerField(null=True, blank=True)
    po11 = models.IntegerField(null=True, blank=True)
    po12 = models.IntegerField(null=True, blank=True)
    pso1 = models.IntegerField(null=True, blank=True)
    pso2 = models.IntegerField(null=True, blank=True)
    pso3 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.co_number


# Student information linked to a user
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students", default=1)  # Link to the user
    usn = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usn} - {self.name}"


# CIE data linked to a user
class CIEData(models.Model):
  # Link to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    question = models.CharField(max_length=10)
    first_ia = models.CharField(max_length=10)
    second_ia = models.CharField(max_length=10)
    third_ia = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.question} - {self.first_ia} | {self.second_ia} | {self.third_ia}'

from django import forms
from .models import ProgramDetail
from .models import CourseOutcome
from .models import COPOMapping
from .models import Student
from .models import CIEData

class ProgramDetailForm(forms.ModelForm):
    class Meta:
        model = ProgramDetail
        fields = ['nba_code', 'department', 'course_name', 'academic_year', 
                  'num_students', 'faculty_name', 'program_title', 
                  'semester_section', 'max_see_marks', 'hod_name']
        widgets = {
            'nba_code': forms.TextInput(attrs={'placeholder': 'Enter NBA code'}),
            'department': forms.TextInput(attrs={'placeholder': 'Enter department'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Enter course name'}),
            'academic_year': forms.NumberInput(attrs={'placeholder': 'Enter year'}),
            'num_students': forms.NumberInput(attrs={'placeholder': 'Enter number of students'}),
            'faculty_name': forms.TextInput(attrs={'placeholder': 'Enter faculty name'}),
            'program_title': forms.TextInput(attrs={'placeholder': 'Enter program title'}),
            'semester_section': forms.TextInput(attrs={'placeholder': 'Enter semester & section'}),
            'max_see_marks': forms.NumberInput(attrs={'placeholder': 'Enter max SEE marks'}),
            'hod_name': forms.TextInput(attrs={'placeholder': 'Enter HoD name'}),
        }


class CourseOutcomeForm(forms.ModelForm):
    class Meta:
        model = CourseOutcome
        fields = ['code', 'description']


class COPOMappingForm(forms.ModelForm):
    class Meta:
        model = COPOMapping
        fields = ['co_number', 'po1', 'po2', 'po3', 'po4', 'po5', 'po6', 
                  'po7', 'po8', 'po9', 'po10', 'po11', 'po12', 'pso1', 'pso2', 'pso3']
        widgets = {
            'co_number': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['usn', 'name']




class CIEDataForm(forms.ModelForm):
    class Meta:
        model = CIEData
        fields = ['question', 'first_ia', 'second_ia', 'third_ia']
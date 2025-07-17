from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('program-details/', views.program_details, name='program_details'),
    path('course_outcomes/', views.course_outcomes, name='course_outcomes'),
    path('display/', views.display, name='display'),  # Correct route for displaying data
    path('edit/<int:id>/', views.edit_program_detail, name='edit'),
    path('delete/<int:id>/', views.delete_program_detail, name='delete'),
    path('edit_course_outcome/<int:id>/', views.edit_course_outcome, name='edit_course_outcome'),
    path('delete_course_outcome/<int:id>/', views.delete_course_outcome, name='delete_course_outcome'),
    path('copopso/', views.copopso_mapping, name='copopso_mapping'),
    path('edit_copopso_mapping/', views.edit_copopso_mapping, name='edit_copopso_mapping'),
    # Changed parameter name from mapping_id to id for consistency
    path('delete_copopso_mapping/<int:id>/', views.delete_copopso_mapping, name='delete_copopso_mapping'),
    path('student-details/', views.student_details, name='student_details'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('cie/', views.cie_view, name='cie'),  # Form submission page  # Display the stored data
    path('edit_cie/<int:pk>/', views.edit_cie_view, name='edit_cie'),  # Add this for editing rows
    path('delete_cie/<int:pk>/', views.delete_cie_view, name='delete_cie'),
    path('download-program-details/', views.generate_docx, name='generate_docx'),
]



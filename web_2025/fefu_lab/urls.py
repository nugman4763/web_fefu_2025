from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  # Статический маршрут для главной
    path('about/', views.about_page, name='about'),  # Статический маршрут "О нас"
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),  # Динамический с int
    path('course/<slug:course_slug>/', views.CourseView.as_view(), name='course_detail'),  # Динамический с slug

    # Новые маршруты для форм
    path('feedback/', views.feedback_view, name='feedback'),
    path('register/', views.register_view, name='register'),
]
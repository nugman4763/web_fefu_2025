from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View

# Function-Based Views
def home_page(request):
    """Главная страница"""
    return render(request, 'fefu_lab/home.html')

def about_page(request):
    """Страница 'О нас'"""
    return render(request, 'fefu_lab/about.html')

def student_profile(request, student_id):
    """Профиль студента"""
    # Пример данных студентов
    students = {
        1: {"name": "Иван Иванов", "group": "Б9120-01.03.02пр"},
        2: {"name": "Петр Петров", "group": "Б9120-01.03.02пр"},
        3: {"name": "Мария Сидорова", "group": "Б9121-01.03.02пр"},
    }
    
    student = students.get(student_id)
    if not student:
        raise Http404("Студент не найден")
    
    context = {
        'student_id': student_id,
        'student_name': student['name'],
        'student_group': student['group']
    }
    return render(request, 'fefu_lab/student.html', context)

# Class-Based View
class CourseView(View):
    """Информация о курсе"""
    
    def get(self, request, course_slug):
        # Пример данных курсов
        courses = {
            'web-development': {
                'title': 'Веб-разработка',
                'description': 'Курс по основам веб-разработки на Django',
                'duration': '1 семестр'
            },
            'python-basics': {
                'title': 'Основы Python',
                'description': 'Введение в программирование на Python',
                'duration': '1 семестр'
            },
            'databases': {
                'title': 'Базы данных',
                'description': 'Изучение реляционных баз данных и SQL',
                'duration': '1 семестр'
            }
        }
        
        course = courses.get(course_slug)
        if not course:
            raise Http404("Курс не найден")
        
        context = {
            'course_slug': course_slug,
            'course_title': course['title'],
            'course_description': course['description'],
            'course_duration': course['duration']
        }
        return render(request, 'fefu_lab/course.html', context)

def handler404(request, exception):
    """Обработчик для несуществующих страниц"""
    return render(request, 'fefu_lab/404.html', status=404)
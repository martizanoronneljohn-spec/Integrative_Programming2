from django.shortcuts import render
from .models import Student
from django.db.models import Count

def dashboard(request):
    data = Student.objects.values('course').annotate(total=Count('course'))
    
    courses = [item['course'] for item in data]
    totals = [item['total'] for item in data]
    
    context = {
        'courses': courses,
        'totals': totals,
    }
    return render(request, 'analytics/dashboard.html', context)
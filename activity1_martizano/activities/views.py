from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from django.http import HttpResponse



class ActivityViewSet(viewsets.ModelViewSet):
    queryset=Activity.objects.all()
    serializer_class = ActivitySerializer

def home(request):
    return HttpResponse("API is running")

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InstructorSerializer
from instrtuctors.models import Instructor

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


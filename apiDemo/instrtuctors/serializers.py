from rest_framework import serializers
from instrtuctors.models import Instructor

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name','dept_name','salary','age','dependants']
        
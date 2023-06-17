from rest_framework import serializers
from .validators import start_with_r
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return self.update(instance, validated_data)
    
    def validate(self, data):

        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'john' and ct.lower() != 'New York':
            raise serializers.ValidationError('City must be New York')
        
        return data
    
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        #read_only_fields = ['name']

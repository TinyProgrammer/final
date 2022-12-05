from undergraduate_app.models import *
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class DepartmentHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentHead
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class CollegianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collegian
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    specialized_fields_value = serializers.ReadOnlyField()

    class Meta:
        model = Professor
        fields = ('specialized_fields_value', 'specialized_fields', 'first_name', 'last_name')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class FinalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalProject
        fields = '__all__'

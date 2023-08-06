from undergraduate_app.models import *
from rest_framework import serializers


class AuthorizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}



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
    weekly_reports = serializers.SerializerMethodField()
    study_field_value = serializers.ReadOnlyField()
    requests = serializers.SerializerMethodField()
    final_projects = serializers.SerializerMethodField()
    proposals = serializers.SerializerMethodField()

    @staticmethod
    def get_proposals(collegian):
        init_data = Proposal.objects.filter(collegian_id=collegian.id)
        return ProposalSerializer(init_data, many=True).data

    @staticmethod
    def get_weekly_reports(collegian):
        init_data = WeeklyReport.objects.filter(collegian_id=collegian.id)
        return WeeklyReportSerializer(init_data, many=True).data

    @staticmethod
    def get_requests(collegian):
        init_data = Request.objects.filter(collegian=collegian.id)
        return WeeklyReportSerializer(init_data, many=True).data

    @staticmethod
    def get_final_projects(collegian):
        init_data = FinalProject.objects.filter(collegian_id=collegian.id)
        return WeeklyReportSerializer(init_data, many=True).data

    class Meta:
        model = Collegian
        fields = '__all__'


class WeeklyReportSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = WeeklyReport
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = Proposal
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    specialized_fields_value = serializers.ReadOnlyField()
    weekly_reports = serializers.SerializerMethodField()
    requests = serializers.SerializerMethodField()
    final_projects = serializers.SerializerMethodField()
    proposals = serializers.SerializerMethodField()

    @staticmethod
    def get_proposals(professor):
        init_data = Proposal.objects.filter(professor_id=professor.id)
        return ProposalSerializer(init_data, many=True).data

    @staticmethod
    def get_weekly_reports(professor):
        init_data = WeeklyReport.objects.filter(professor_id=professor.id)
        return WeeklyReportSerializer(init_data, many=True).data

    @staticmethod
    def get_requests(professor):
        init_data = Request.objects.filter(professor_id=professor.id)
        return WeeklyReportSerializer(init_data, many=True).data

    @staticmethod
    def get_final_projects(professor):
        init_data = FinalProject.objects.filter(professor_id=professor.id)
        return WeeklyReportSerializer(init_data, many=True).data

    class Meta:
        model = Professor
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = Report
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = Report
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = Request
        fields = '__all__'


class FinalProjectSerializer(serializers.ModelSerializer):
    collegian_name = serializers.ReadOnlyField()
    professor_name = serializers.ReadOnlyField()

    class Meta:
        model = FinalProject
        fields = '__all__'

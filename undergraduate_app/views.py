from rest_framework import generics
from .serializers import *
from undergraduate_app.models import *
from .permissions import *


class ListProfessorView(generics.ListCreateAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()


class RetrieveUpdateProfessorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()
    permission_classes = [ReadOnlyUser | IsAdmin]


class ListCollegianView(generics.ListCreateAPIView):
    serializer_class = CollegianSerializer
    queryset = Collegian.objects.all()
    permission_classes = [ReadOnlyUser | IsAdmin]


class RetrieveUpdateCollegianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollegianSerializer
    queryset = Collegian.objects.all()
    permission_classes = [ReadOnlyUser | IsAdmin]


class ListStatusView(generics.ListCreateAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class RetrieveUpdateStatusView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class ListDepartmentHeadView(generics.ListCreateAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = DepartmentHeadSerializer
    queryset = DepartmentHead.objects.all()


class RetrieveUpdateDepartmentHeadView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentHeadSerializer
    queryset = DepartmentHead.objects.all()
    permission_classes = [ReadOnlyUser | IsAdmin]


class ListWeeklyReportsView(generics.ListCreateAPIView):
    queryset = DepartmentHead.objects.all()
    serializer_class = WeeklyReportSerializer
    permission_classes = [ReadOnlyUser | IsAdmin]


class RetrieveWeeklyReportView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = WeeklyReportSerializer
    queryset = DepartmentHead.objects.all()


class ListRequestsView(generics.ListCreateAPIView):
    queryset = DepartmentHead.objects.all()
    serializer_class = RequestsSerializer
    permission_classes = [ReadOnlyUser | IsAdmin]


class RetrieveRequestView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = RequestsSerializer
    queryset = DepartmentHead.objects.all()


class ListFinalProjectView(generics.ListCreateAPIView):
    serializer_class = FinalProjectSerializer
    queryset = FinalProject.objects.all()
    permission_classes = [ReadOnlyUser | IsAdmin]


class RetrieveFinalProjectView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyUser | IsAdmin]
    serializer_class = FinalProjectSerializer
    queryset = FinalProject.objects.all()


from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView

from .serializers import *
from undergraduate_app.models import *
from .permissions import *
from .models import *


class Authorization(GenericAPIView):
    serializer_class = AuthorizeSerializer
    queryset = Person.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.get('username')
        password = request.get('password')

        u = Person.objects.filter(username=username, password=password)
        if u.exists():
            if Collegian.objects.filter(username=username).exists():
                return Response({'role': 'collegian'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


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
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializer
    # permission_classes = [ReadOnlyUser | IsAdmin]


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

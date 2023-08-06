from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .permissions import *
from .models import *


class Authorization(GenericAPIView):
    authentication_classes = []
    serializer_class = AuthorizeSerializer
    queryset = Person.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        raw_password = request.data.get('password')

        hashed_password =  bcrypt.hashpw(raw_password.encode('utf8'), SALT)

        u = Person.objects.filter(username=username, password=hashed_password)
        if u.exists():
            token = RefreshToken.for_user(u.first())
            role = None
            if Collegian.objects.filter(username=username).exists():
                role = 'collegian'
            return Response({'role': role,
                             'access': str(token.access_token),
                             }, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ListProfessorView(generics.ListCreateAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

    def get(self, request, **kwargs):
        return Response(status=status.HTTP_200_OK)


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

from django.urls import path
from .views import *

urlpatterns = [
    path('authorize/', Authorization.as_view(), name='Authorization'),

    path('professors/', ListProfessorView.as_view(), name='create and list Professors'),
    path('professor/<str:pk>', RetrieveUpdateProfessorView.as_view(), name='detail Professor'),

    path('collegians/', ListCollegianView.as_view(), name='create and list collegians'),
    path('collegian/<str:pk>', RetrieveUpdateCollegianView.as_view(), name='detail collegian'),

    path('statuses/', ListStatusView.as_view(), name='create and list Status'),
    path('status/<str:pk>', RetrieveUpdateStatusView.as_view(), name='detail Status'),

    path('department-heads/', ListDepartmentHeadView.as_view(), name='create and list Department head'),
    path('department-head/<str:pk>', RetrieveUpdateDepartmentHeadView.as_view(), name='detail Department Heads'),

    path('weekly_report/<str:pk>', RetrieveWeeklyReportView.as_view(), name='detail weekly report'),
    path('weekly_reports/', ListWeeklyReportsView.as_view(), name='create and list weekly reports'),

    path('final_project/<str:pk>', RetrieveFinalProjectView.as_view(), name='detail final project'),
    path('final_projects/', ListFinalProjectView.as_view(), name='create and list final projects'),

    path('request/<str:pk>', RetrieveRequestView.as_view(), name='detail request'),
    path('requests/', ListRequestsView.as_view(), name='create and list requests')

]

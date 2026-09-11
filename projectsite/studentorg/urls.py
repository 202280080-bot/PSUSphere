from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizations, name='organizations'),
    path('<int:pk>/',views.organization_detail, name='organization_detail'),
    path('organization_list', views.OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', views.OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('orgmember_list/<pk>/delete', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    path('organization_list/<pk>/delete', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    path('orgmember_list', views.OrgMemberList.as_view(),  name='orgmember-list'),
    path('orgmember_list/add', views.OrgMemberCreateView.as_view(),  name='orgmember-add'),
    path('orgmember_list/<pk>', views.OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<pk>/delete', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    path('student_list', views.StudentList.as_view(), name='student-list'),
    path('college_list',views.CollegeList.as_view(),name='college-list'),
    path('student_list/add',views.StudentCreateView.as_view(),name='student-add'),
    path('student_list/<pk>',views.StudentUpdateView.as_view(),name='student-update'),
    path('student_list/<pk>/delete',views.StudentDeleteView.as_view(),name='student-delete'),
    path('college_list/add',views.CollegeCreateView.as_view(),name='college-add'),
    path('college_list/<pk>',views.CollegeUpdateView.as_view(),name='college-update'),
    path('college_list/<pk>/delete',views.CollegeDeleteView.as_view(),name='college-delete'),
    path('program_list',views.ProgramList.as_view(),name='program-list'),
    path('program_list/add',views.ProgramCreateView.as_view(),name='program-add'),
    path('program_list/<pk>',views.ProgramUpdateView.as_view(),name='program-update'),
    path('program_list/<pk>/delete',views.ProgramDeleteView.as_view(),name='program-delete'),
]
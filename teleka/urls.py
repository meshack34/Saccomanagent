from django.urls import path

from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('create-member/',CreateMember.as_view(),name='create-member'),
    path('view-members/',ViewMembers.as_view(),name='view-members'),
    path('member-update/<int:pk>/', MemberUpdate.as_view(), name='member-update'),
    path('member-delete/<int:pk>/', MemberDelete.as_view(), name='member-delete'),
    path('member/<int:pk>/', MemberDetails.as_view(), name='member'),
    path('create-deposit/',CreateDeposit.as_view(),name='create-deposit'),
    path('view-deposits/',ViewDeposit.as_view(), name='view-deposits'),
    path('deposit-update/<int:pk>/', DepositUpdate.as_view(), name='deposit-update'),
    path('deposit-delete/<int:pk>/', DepositDelete.as_view(), name='deposit-delete'),
    path('create-withdraw/',CreateWithdraw.as_view(),name='create-withdraw'),
    path('view-withdraws/',ViewWithdraw.as_view(), name='view-withdraws'),
    path('withdraw-update/<int:pk>/', WithdrawUpdate.as_view(), name='withdraw-update'),
    path('withdraw-delete/<int:pk>/', WithdrawDelete.as_view(), name='withdraw-delete'),
    path('create-loan/',CreateLoan.as_view(),name='create-loan'),
    path('view-loans/',ViewLoan.as_view(), name='view-loans'),
    path('loan-update/<int:pk>/', LoanUpdate.as_view(), name='loan-update'),
    path('loan-delete/<int:pk>/', LoanDelete.as_view(), name='loan-delete'),
    path('loan-pending/',PendingLoan.as_view(),name='loan-pending'),
    path('loan-complete/',CompletedLoan.as_view(),name='loan-complete'),


    ]



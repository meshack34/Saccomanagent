from django.shortcuts import render, redirect 

from .models import *

from django.views import View

from django.contrib.auth.views import LoginView

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin # used for add / edit

from django.contrib import messages # used for delete


class CustomLoginView(LoginView):
    template_name = 'teleka/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(Self):
        return reverse_lazy('dashboard')


class RegisterPage(FormView):
    template_name = 'teleka/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(RegisterPage, self).get(*args, **kwargs)


class DashboardView(LoginRequiredMixin,ListView):
    model = Member
    model = User
    model = Loan
    model = Withdraw
    model = Deposit
    context_object_name = 'dashboard'
    template_name = 'teleka/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members_count'] = Member.objects.all().count()
        context['withdraw_count'] = Withdraw.objects.all().count()
        context['deposit_count'] = Deposit.objects.all().count()
        context['loan_count'] = Loan.objects.all().count()
        context['recent_loans'] = Loan.objects.all()
        


        return context
    
    
    def get_success_url(Self):
        return reverse_lazy('dashboard')


class CreateMember(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Member
    fields = '__all__'
    template_name = 'teleka/createMember.html'
    success_url = reverse_lazy('view-members')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMember, self).form_valid(form)
    
    success_message = "Member Created Successfully !"


class ViewMembers(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model= User
    model = Member
    context_object_name = 'members'
    template_name = 'teleka/viewMembers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = context['members'].filter(user=self.request.user)

        
        return context


class MemberUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= User
    model = Member
    fields = [
       "firstname", "lastname", "id_type", "id_number", "gender", "date_of_birth",
       "district", "county", "subcounty", "parish", "village", "account_number",
       "opening_balance", "email", "phone", "next_of_keen_first_name", 
       "next_of_keen_last_name", "next_of_keen_phone", "next_of_keen_relationship",
       "status"
    ]
    template_name = 'teleka/createMember.html'
    success_url = reverse_lazy('view-members')
    success_message = "Member Updated successfully !"


class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    context_object_name = 'members'
    success_url = reverse_lazy('view-members')
    template_name = 'teleka/memberConfrim.html'

    def get_success_url(self):
        messages.success(self.request, "Member Deleted Succesfully !")
        return reverse('view-members')


class MemberDetails(LoginRequiredMixin, DetailView):
    model = Loan
    model = Member
    context_object_name = 'member'
    template_name = 'teleka/memberDetails.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     loans = Loan.objects.get(id='1')
    #     member_loan_count = loans.count()
    #     context['member_loan_count'] = context['member_loan_count']
        





class CreateDeposit(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    model = Deposit
    fields = '__all__'
    template_name = 'teleka/createDeposit.html'
    success_url = reverse_lazy('view-deposits')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateDeposit, self).form_valid(form)
    
    success_message = "Deposit Successful !"



class ViewDeposit(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model= User
    model = Deposit
    context_object_name = 'deposits'
    template_name = 'teleka/viewDeposits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposits'] = context['deposits']    #.filter(user=self.request.user)

        
        return context


class DepositUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= User
    model = Deposit
    fields = [
       "member_name", "account_number", "amount", "deposited_by", "status"
    ]
    template_name = 'teleka/createDeposit.html'
    success_url = reverse_lazy('view-deposits')
    success_message = "Deposit Updated Successfully !"


class DepositDelete(LoginRequiredMixin, DeleteView):
    model = Deposit
    context_object_name = 'deposit'
    success_url = reverse_lazy('view-deposits')
    template_name = 'teleka/depositConfirm.html'

    def get_success_url(self):
        messages.success(self.request, "Deposit Deleted Succesfully !")
        return reverse('view-deposits')


class CreateWithdraw(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    model = Withdraw
    fields = '__all__'
    template_name = 'teleka/createWithdraw.html'
    success_url = reverse_lazy('view-withdraws')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateWithdraw, self).form_valid(form)
    
    success_message = "Withdraw Successful !"


class ViewWithdraw(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model= User
    model = Withdraw
    context_object_name = 'withdraws'
    template_name = 'teleka/viewWithdraws.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['withdraws'] = context['withdraws']    #.filter(user=self.request.user)

        
        return context


class WithdrawUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= User
    model = Withdraw
    fields = [
       "member_name", "account_number", "amount", "withdrawn_by", "status"
    ]
    template_name = 'teleka/createWithdraw.html'
    success_url = reverse_lazy('view-withdraws')
    success_message = "Withdraw Updated Successfully !"


class WithdrawDelete(LoginRequiredMixin, DeleteView):
    model = Withdraw
    context_object_name = 'withdraws'
    success_url = reverse_lazy('view-withdraws')
    template_name = 'teleka/withdrawConfirm.html'

    def get_success_url(self):
        messages.success(self.request, "Withdraw Deleted Succesfully !")
        return reverse('view-withdraws')




class CreateLoan(LoginRequiredMixin,SuccessMessageMixin,CreateView):

    model = Loan
    fields = '__all__'
    template_name = 'teleka/createLoan.html'
    success_url = reverse_lazy('view-loans')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateLoan, self).form_valid(form)
    
    success_message = "Loan Created Successful !"


class ViewLoan(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model= User
    model = Loan
    context_object_name = 'loans'
    template_name = 'teleka/viewLoan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loans'] = context['loans']    #.filter(user=self.request.user)

        
        return context

class LoanUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= User
    model = Loan
    fields = [
       "member_name", "account_number", "amount",
       "intrest_rate", "repay_in", "status", "collateral1", "collateral2", "reason"
    ]
    template_name = 'teleka/createLoan.html'
    success_url = reverse_lazy('view-loans')
    success_message = "Loan Updated Successfully !"


class LoanDelete(LoginRequiredMixin, DeleteView):
    model = Loan
    context_object_name = 'loans'
    success_url = reverse_lazy('view-loans')
    template_name = 'teleka/confrimLoan.html'

    def get_success_url(self):
        messages.success(self.request, "Loan Deleted Succesfully !")
        return reverse('view-loans')


class PendingLoan(LoginRequiredMixin,ListView):
    model= User
    model = Loan
    context_object_name = 'pending_loans'
    template_name = 'teleka/pendingLoans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_loans'] = Loan.objects.all().filter(status='PENDING')

        
        return context


class CompletedLoan(LoginRequiredMixin,ListView):
    model= User
    model = Loan
    context_object_name = 'completed_loans'
    template_name = 'teleka/completedLoans.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_loans'] = Loan.objects.all().filter(status='COMPLETE')

        
        return context
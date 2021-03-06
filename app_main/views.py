from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView

from .models import Thread, Delegate, Voter, Proposal, ProposalVote

class ThreadListView(ListView):
    model = Thread

class ThreadCreate(CreateView):
    model = Thread
    fields = ['title','description']
    success_url = '/thread/success'


class ProposalView(CreateView):
    model = Proposal
    fields = ('thread', 'summary', 'rule', 'expiration_date')


class DelegateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(DelegateView, self).get_context_data(**kwargs)
        context['delegates'] = Delegate.delegates(self.request.user)
        context['promminentVoters'] = Voter.mostPromminentVoters(10)
        return context


class VoteView(TemplateView):

    def get(self, request, proposal_id, *args, **kwargs):
        self.proposal_id = proposal_id

        return super(VoteView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VoteView, self).get_context_data(**kwargs)
        context['results'] = ProposalVote.results(self.proposal_id)
        return context

    def vote(self):
        voter = Voter.objects.get(self.request.user)
        ProposalVote.vote(voter, proposal=self.request.proposal, agree=self.request.agree)
        return redirect('/proposals/rule')

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Activity


# Create your views here.
class ActivityCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Activity
    template_name = 'organization/activity.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.over_seer:
            return True
        return False


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'organization/activity.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.over_seer:
            return True
        return False

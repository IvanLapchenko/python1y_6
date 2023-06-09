from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib import messages


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        print(form)
        print(form.errors)
        for errors in form.errors.values():
            for error in errors:
                messages.warning(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


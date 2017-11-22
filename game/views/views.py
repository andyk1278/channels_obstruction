from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class HomeView(TemplateView):
    template_name = 'home.html'

class CreateUserView(CreateView):
    template_name = 'register.jtml'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        vaid = super(CreateUserView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_dat.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return validCC
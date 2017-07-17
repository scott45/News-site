from django.views.generic import ListView, CreateView, DetailView
from .models import Link
from django.contrib.auth import authenticate, logout
from .forms import UserForm
from django.shortcuts import render
from gossip.forms import LinkForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'gossip/link_list.html')
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'gossip/link_list.html')
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)


class LinkListView(ListView):
    model = Link
    template_name = 'gossip/link_list.html'
    paginate_by = 5

    def get_query_set(self):
        return Link.with_votes.all(self)


class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()

        return super(CreateView, self).form_valid(form)


class LinkDetailView(DetailView):
    model = Link


class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("home")

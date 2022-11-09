from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post1
# Create your views here.


def index(request):
    # context = {
    #      'posts': Post1.objects.all(),
    #      'movies': Movies.objects.all()
    #  }
    return render(request, 'index.html', {'movies': Movies.objects.all()})


def about(request):
    return render(request, 'aboutus.html')


def log(request):
    return render(request, 'log.html')


def document(request):
    return render(request, 'document.html')


def series(request):
    return render(request, 'series.html')

def test2(request):
    return render(request,'test2.html')


"""def login(request):
    return render(request,'login.html')"""


class PostListView(ListView):
    model = Post1
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post1
    template_name = 'post1_detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post1
    fields = ['title', 'content']
    template_name = 'post1_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post1
    fields = ['title', 'content']
    template_name = 'post1_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
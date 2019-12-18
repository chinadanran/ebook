from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import BaseDeleteView

from ebook.apps.book.models import Book, Article


class BookListView(ListView):
    model = Book
    template_name = 'movielist.html'
    paginate_by = 18
    ordering = ['-date_created']
    extra_context = {
        'name_space': 'book:book_list'
    }


class ArticleListView(ListView):
    model = Article
    template_name = 'movie_update.html'
    paginate_by = 100
    ordering = ['title']

    def get_queryset(self):
        queryset = Article.objects.select_related('book').filter(book_id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['book'] = Book.objects.get(pk=self.kwargs['pk'])
        return context

# Edit web/views.py
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from. models import Book
from django.urls import reverse_lazy



class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
    
    
class Form(TemplateView):
    template_name = "pages/basic_elements.html"
    
    
class Icon(TemplateView):
    template_name = "pages/icon.html"
    
    
class Button(TemplateView):
    template_name = "pages/buttons.html"
    
    
class Typography(TemplateView):
    template_name = "pages/typography.html"
    
    
class Chart(TemplateView):
    template_name = "pages/chartjs.html"
    
    
class Table(TemplateView):
    template_name = "pages/tables.html"
    
    
class Error(TemplateView):
    template_name = "pages/error-404.html"
    
 
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "books/book_create.html"
    fields="__all__"
    # success_url = reverse_lazy('web:book_list',)
    

    
    
    
class BookList(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Book List"
        return context
    
    

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    
    
class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = "__all__"
        
    
class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = "/book_list/"
    


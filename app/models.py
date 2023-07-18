from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=100,help_text="min 20 characters")
    slug = models.SlugField(max_length=100, unique=True)
    year = models.IntegerField()
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name="books")
    cover = models.ImageField("Book Cover",upload_to="covers/", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def get_absolute_url(self):
        return reverse_lazy('web:book_detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse_lazy('web:book_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('web:book_delete', kwargs={'pk': self.pk})
    
    
class FavoriteBook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return str(self.user)

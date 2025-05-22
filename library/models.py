from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from datetime import datetime ,timedelta
from django.urls import reverse
# Create your models here.

class author(models.Model):
    Author_id = models.CharField(max_length=10)
    fistname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    class Meta:
        ordering = ['lastname']

    def __str__(self):
        return self.lastname


class category(models.Model):
    category_name = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.category_name


class books(models.Model):
    serialno = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=101)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    author = models.ForeignKey(author, on_delete=models.CASCADE) 
    publication_date = models.DateField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(max_length=200, default='description of the book')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    totalstock = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})


def get_due_date():
    return datetime.today() + timedelta(days=14)


class issuedbooks(models.Model):
    booksid = models.ForeignKey(books, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    issuedate = models.DateTimeField(default=datetime.today)
    due_date = models.DateTimeField(default=get_due_date)

    def __str__(self):
        return self.booksid.title


class issuebookhistory(models.Model):
    booksid = models.ForeignKey(books, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    issuedate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.booksid.title


class reservedbooks(models.Model):
    bookid = models.ForeignKey(books, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    datereserved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bookid.title


class searchedcontent(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    searchedinfo = models.CharField(max_length=200)
    datesearched = models.DateField(default=timezone.now)

    def __str__(self):
        return self.searchedinfo

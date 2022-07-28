from tkinter import CASCADE
from django.db import models
from django.forms import DateTimeField
class Post(models.Model):
    Tittle=models.CharField(max_length=200)
    Text= models.TextField
    Create_date=models.DateTimeField
    Published_date=models.DateTimeField


class get_user_model(models.Model):
    Author= models.ForeignKey(Post, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

import datetime

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class author(models.Model):

    name = models.CharField(max_length=64)

    birth_year = models.IntegerField()

    nationality = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ebook(models.Model):

    name = models.CharField(max_length=64)

    author = models.ForeignKey(author, on_delete=models.CASCADE)

    year_published = models.IntegerField(max_length=64)

    loan_type = models.IntegerField(default=1,
                                    validators=[
                                        MaxValueValidator(3),
                                        MinValueValidator(1)
                                    ])

    ebook_content = models.CharField(max_length=2560)

    def __str__(self):
        return self.name

class loan(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    ebook = models.ForeignKey(ebook,  on_delete=models.CASCADE)

    loan_date = models.DateField()

    #aka loan expiration date, loan_date + ebook.loan_type
    loan_delete = models.DateField()

    def __str__(self):
        return str(self.id)

class review(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    ebook = models.ForeignKey(ebook,  on_delete=models.CASCADE)

    rating = models.IntegerField(validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                        ])
    
    text_field = models.CharField(max_length=500)

    date = models.DateField(default=datetime.date.today)

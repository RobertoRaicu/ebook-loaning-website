"""ebook_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from library_layout import views

app_name = 'library_layout'

urlpatterns = [
    # index
    path('', views.index, name='index'),

    # user login and registraion
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    # user settings
    path('userdelete/', views.delete_user, name='delete_user'),
    path('profile/', views.user_profile, name='user_profile'),

    # ebook urls
    path('books/', views.display_books, name='display_books'),
    path('book_profile/<bookname>/', views.book_profile, name='book_profile'),
    path('book_profile/<bookname>/<ratefilter>', views.book_profile, name='book_profile'),
    path('addbook/',views.add_book,name='add_book'),
    path('addbook/<book_id>',views.update_book,name='update_book'),
    path('deletebook/<book_id>/',views.delete_book,name='delete_book'),

    # loan urls
    path('loanbook/<bookname>/<loan_type>/', views.loan_book, name='loan_book'),
    path('deleteloan/<bookname>/',views.delete_loan,name='delete_loan'),

    # author urls
    path('authors/', views.display_authors, name='display_authors'),
    path('author/<authorname>/', views.author_profile, name='author_profile'),
    path('addauthor/',views.add_author,name='add_author'),
    path('addauthor/<author_id>/',views.update_author,name='update_author'),
    path('deleteauthor/<author_id>/',views.delete_author,name='delete_author'),

    # review urls
    path('deletereview/<review_id>/',views.delete_review,name='delete_review'),
    path('updatereview/<review_id>/',views.update_review,name='update_review'),
    
    # terms
    path('tos/',views.terms,name='terms')

]

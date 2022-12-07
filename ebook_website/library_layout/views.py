from django.shortcuts import render, redirect
from library_layout.forms import UserForm, ReviewForm
from library_layout.models import author, ebook, loan, review

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import random
import datetime

# Create your views here.


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            registered = True

        else:
            print(user_form.errors)
            return render(request,'library_layout/registration.html',
                          {'user_form':user_form,
                           'registered':registered,})

    else:
        user_form = UserForm()
         
    return render(request,'library_layout/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('/library/profile')

        else:
            dict = {"error":"Incorrect username or password"}
            return render(request, 'library_layout/login.html',context=dict)

    else:
        return render(request, 'library_layout/login.html',{})

def display_books(request):
    if request.method == "POST":
        search = request.POST.get('searched')
        ebook_list = ebook.objects.filter(name__contains=search)
        books_dict = {'book_records':ebook_list}
        return render(request,'library_layout/ebooks.html',context=books_dict)
    elif request.method == "GET":
        ebook_list = ebook.objects.order_by('id')
        books_dict = {'book_records':ebook_list}
        return render(request,'library_layout/ebooks.html',context=books_dict)


def display_authors(request):
    if request.method == "POST":
        search = request.POST.get('searchedauthor')
        author_list = author.objects.filter(name__contains=search)
        authors_dict = {'author_records':author_list}
        return render(request,'library_layout/authors.html',context=authors_dict)
    elif request.method == "GET":
        author_list = author.objects.order_by('name')
        authors_dict = {'author_records':author_list}
        return render(request,'library_layout/authors.html',context=authors_dict)

def index(request):
    try:
        loans = loan.objects.filter(user=request.user)
        for i in loans:
            if i.loan_delete < datetime.date.today():
                loan.objects.filter(id=i.id).delete()
    except:
        pass

    author_list = author.objects.order_by('name')
    ebook_list = ebook.objects.order_by('id')
    items_dict = {'book_records':ebook_list,'author_records':author_list}
    return render(request,'library_layout/index.html',context=items_dict)

@login_required
def loan_book(request,bookname,loan_type):
    if int(loan_type) == 2:
        loan_delete = datetime.date.today() + datetime.timedelta(days=7)
    elif int(loan_type) == 3:
        loan_delete = datetime.date.today() + datetime.timedelta(days=3)
    else:
        loan_delete = datetime.date.today() + datetime.timedelta(days=14)
    ebookdata = ebook.objects.get(name=bookname)
    loan.objects.get_or_create(user=request.user,ebook=ebookdata,loan_date=datetime.date.today(),loan_delete=loan_delete)
    bookname = bookname.replace(' ','%20')
    return redirect(f"/library/book_profile/{bookname}/")

def book_profile(request, bookname, ratefilter=False):
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        review_rate = request.POST.get('inlineRadioOptions')
        if review_form.is_valid():
            clean_text = review_form.cleaned_data['text_field']
            ebookdata = ebook.objects.get(name=bookname)
            review.objects.create(user=request.user,ebook=ebookdata,rating=review_rate,text_field=clean_text)
            print("review saved")
        else:
            print("error: review not saved")

    book_info = ebook.objects.get(name=bookname)

    if ratefilter:
        reviews = review.objects.filter(rating=ratefilter,ebook=book_info)
    else:
        reviews = review.objects.filter(ebook=book_info).order_by('-date')

    loaned = False
    try:
        loans = loan.objects.filter(user=request.user,ebook=book_info)
    except:
        loans = []
    if len(loans) != 0:
        loans = loans[0]
        loaned = True

    rating_sum = (0)
    for i in reviews:
        rating_sum += i.rating
    try:
        rating_avg = round(rating_sum / len(reviews),2)
    except:
        rating_avg = 0

    review_form = ReviewForm()
    info_dict = {'book_info':book_info,'random':random.randint(0,300),"review_form":review_form,"reviews":reviews,"reviews_amount":len(reviews),"loaned":loaned,"loans":loans,'rating_avg':rating_avg}
    return render(request, 'library_layout/book_profile.html',context=info_dict)

def author_profile(request, authorname):
    author_info = author.objects.get(name=authorname)
    book_info = ebook.objects.filter(author=author_info.id)
    info_dict = {'author_info':author_info,'book_info':book_info}
    return render(request, 'library_layout/author_profile.html',context=info_dict)

@login_required
def user_profile(request):
    emptyloan = False
    emptyreview = False
    updated = False
    user_info = request.user

    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=user_info)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            updated = True

    user_form = UserForm()

    user_loans = loan.objects.filter(user=user_info)
    for i in user_loans:
        if i.loan_delete < datetime.date.today():
            loan.objects.filter(id=i.id).delete()
    if len(user_loans) == 0: emptyloan = True
    user_reviews = review.objects.filter(user=user_info)
    if len(user_reviews) == 0:  emptyreview = True

    user_dict = {'userinfo':user_info,'userloans':user_loans,'userreviews':user_reviews,'loans':emptyloan,'reviews':emptyreview,'user_form':user_form,'updated':updated}
    return render(request, 'library_layout/user_profile.html',context=user_dict)

@login_required
def delete_loan(request, bookname):
    bookname = ebook.objects.get(name=bookname)
    loan.objects.filter(user=request.user,ebook=bookname).delete()
    return redirect('/library/profile')

@login_required
def delete_review(request,review_id):
    review.objects.filter(id=review_id).delete()
    return redirect(request. META['HTTP_REFERER'])

@login_required
def update_review(request,review_id):
    if request.method == 'POST':
        new_text = request.POST.get('review')
        new_rating = request.POST.get('inlineRadioOptions')
        review.objects.filter(user=request.user,id=review_id).update(rating=new_rating,text_field=new_text)
        return redirect('/library/profile')
    reviews = review.objects.filter(user=request.user,id=review_id)
    dict = {'review':reviews[0],}
    return render(request, 'library_layout/review_update_form.html',context=dict)

@login_required
def delete_user(request):
    if request.method == 'POST':
        value = request.POST.get('button')
        if value == "abort":
            return redirect('/library/profile')
        elif value == "delete":
            user = request.user
            user.delete()
            return redirect('index')
    return render(request, 'library_layout/user_delete.html')
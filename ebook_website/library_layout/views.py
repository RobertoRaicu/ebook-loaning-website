from django.shortcuts import render
from library_layout.forms import UserForm, UserProfileInfoForm
from library_layout.models import author, ebook, loan, review

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,'library_layout/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))

        else:
            # use HttpResponse incase raise does not work
            # return HttpResponse('Incorrect username or password')
            dict = {"error":"Incorrect username or password"}
            return render(request, 'library_layout/login.html',context=dict)

    else:
        return render(request, 'library_layout/login.html',{})

def display_books(request):
    ebook_list = ebook.objects.order_by('id')
    books_dict = {'book_records':ebook_list}
    return render(request,'library_layout/ebooks.html',context=books_dict)

def display_authors(request):
    author_list = author.objects.order_by('name')
    authors_dict = {'author_records':author_list}
    return render(request,'library_layout/authors.html',context=authors_dict)

def index(request):
    author_list = author.objects.order_by('name')
    ebook_list = ebook.objects.order_by('id')
    items_dict = {'book_records':ebook_list,'author_records':author_list}
    return render(request,'library_layout/index.html',context=items_dict)





import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ebook_website.settings')

import django
django.setup()

import random
from library_layout.models import author, ebook, review
from django.contrib.auth import get_user_model
from faker import Faker
import random

fake = Faker()

'''it is advised to first create one or more users before running this script.
   running this script without users data will result in generation of fake books without fake reviews
   as well as display a "population failed" error!'''

def populate_authors(n=3):
    for i in range(n):
        #author
        fake_author_name = fake.name()
        fake_year = random.randint(-1000,3000)
        fake_nationality = fake.country()

        auth = author.objects.get_or_create(name=fake_author_name,birth_year=fake_year,nationality=fake_nationality)[0]
    return True


def populate_books(N=10):

    for i in range(N):
        

        #ebook
        fake_book_name = ' '.join(fake.words(3))
        fake_ebook_year = random.randint(-1000,3000)
        fake_loan_type = random.randint(1,3)
        fake_text = fake.paragraph(nb_sentences=500)

        #authors list
        auth = author.objects.all()
        
        try:
            #ebook population
            book = ebook.objects.get_or_create(name=fake_book_name,author=random.choice(auth),year_published=fake_ebook_year,loan_type=fake_loan_type,ebook_content=fake_text)[0]
        except IndexError as e:
                    print(f"[!] Error: {e}; No authors in database [!]")
                    return False
    return True

def populate_reviews(n=300):

    for i in range(n):

        fake_text = fake.paragraph(nb_sentences=3)

        fake_rating = random.randint(1,5)

        User = get_user_model()
        users = User.objects.all()

        book = ebook.objects.all()

        try:
            rev = review.objects.create(user=random.choice(users),ebook=random.choice(book),text_field=fake_text,rating=fake_rating)
        except IndexError as e:
                    print(f"[!] Error: {e}; No Users registered in database [!]")
                    return False
    return True


if __name__ == '__main__':
    #DO NOT CHANGE FUNTION CALL ORDER. THE FUNCTIONS ARE CODEPENDEDNT!!
    #number in parentheses defines amount of items populated
    author_populate = populate_authors(20)
    book_populate = populate_books(200)
    review_populate = populate_reviews(700)

    
    print("script complete")
        

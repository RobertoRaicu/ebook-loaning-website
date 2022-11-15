import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ebook_website.settings')

import django
django.setup()

import random
from library_layout.models import author, ebook
from faker import Faker
import random

fake = Faker()

def populate(N=5):

    for i in range(N):
        #author
        fake_author_name = fake.name()
        fake_year = random.randint(-1000,3000)
        fake_nationality = fake.country()

        #ebook
        fake_book_name = ' '.join(fake.words(3))
        fake_ebook_year = random.randint(-1000,3000)
        fake_loan_type = random.randint(1,3)
        fake_text = fake.paragraph(nb_sentences=100)

        #author population
        auth = author.objects.get_or_create(name=fake_author_name,birth_year=fake_year,nationality=fake_nationality)[0]

        #ebook population
        book = ebook.objects.get_or_create(name=fake_book_name,author=auth,year_published=fake_ebook_year,loan_type=fake_loan_type,ebook_content=fake_text)[0]


if __name__ == '__main__':
    populate(2)
    print("population complete")
        

# ebook-loaning-website
# README.MD LOOKS UGLY. DESIGNING THIS FILE WILL BE DONE LATER


django models (Tables):

# default django user model with 'OneToOneField' function for extra variables
---user model---

-Username
-Email
-Password
-First Name
-Surname
# -- extra user variables (blank=True)
-City of residence
-Country of residence
-Date of birth
-Profile picture

---author model---

-name
-birth year
-nationality

---book model---

-name
# ForeignKey author
-author
-year published
# loan type 1: ebook removed from library after 14 days
# type 2: after 7 days
# type 3: after 3 days
-loan type
# ebook content
-ebook content

---loan---
# Foreignkey AUTH_USER_MODEL
-user
# foreignkey ebook
-ebook
-loan date
# loan expiration date, loan_date + ebook.loan_type
-loan delete

---review---
# Foreignkey AUTH_USER_MODEL
-user
# foreignkey ebook
-ebook
# 1 to 5
-rating
-text_field
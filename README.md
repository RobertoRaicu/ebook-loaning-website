# john bryce project no.2
>###### by Roberto Raicu Meer

## <ins>Installation of the project:

1. download project:  
      1. go into your preferred code editor
      2. open a new folder 
      3. open terminal
      4. download project using the following command:
      ```
      git clone https://github.com/RobertoRaicu/ebook-loaning-website.git
      ```
2. create a virtual environment:
      ```
       python -m venv <virtual-environment-name>
      ```
      or
      ```
      conda create <virtual-environment-name>
      ```
3. activate virtual environment (on windows):
      ```
      <virtual-environment-name>\Scripts\activate.bat
      ```
      or
      ```
      conda activate <virtual-environment-name>
      ```
4. donwloading packages:
      1. location of the requirements file:
      - ```
        cd .\ebook-loaning-website\ebook_website\
        ```
      ![requirments](./readme-imgs/Screenshot%202022-12-11%20112424.png)  

      2. donwload requirments:
      - ```
        pip install -r requirements.txt
        ```
5. security configuration:
      1. go to:
     - ```
       cd .\ebook-loaning-website\ebook_website\ebook_website\
       ```
      2. in that same directory type:
      - ```
        type nul > .env
        ```
      - this command will create a file which we will edit shortly.

      <sub> this command may thorw an error: ignore the error.</sub>

      ![env](./readme-imgs/Screenshot%202022-12-11%20115651.png)

      3. inside the .env file add this content:
      - ```
        SECRET_KEY=n)i)2$u=os%cdp$webb_e-c43kdhled9sjd27=_awo4f*62q2i
        DEBUG=True
        ```
      - It is highly recommended you change the secret key via a secret key generator!<br>
      <br>

6. we can now work on the activation of the website it self!  
      (check that you're in the right directory)
      ```
      cd .\ebook-loaning-website\ebook_website\
      ```
      1. migrate models:
            1. ```
                  python.exe .\manage.py migrate
                  ```
            2. ```
                  python.exe .\manage.py makemigrations
                  ```
            3. ```
                  python.exe .\manage.py migrate
                  ```
      2. create super user (admin):
      - ```
        python.exe .\manage.py createsuperuser
        ```
      
      3. run population script (optional):  
      > this step requires at least one user to be registered (the more users the better) in the data base (hence section 6.2)  

      - to run script (in the same directory):
      - ```
        python.exe .\populate_library_layout.py
        ```
        - > script may take some time to run depedning on functions range (which you can change in the file)  
        and/or computing power
        - > once script is complete a 'script complete' message will apear in the terminal console
      
      4. **run server:**
      - ```
        python.exe ./manage.py runserver
        ```

## <ins> Project models:

There are 5 models as part of the project:<br>
1. User
      - username <sup>(primary key)</sup>
      - password
2. Author
      - name <sup>(primary key)</sup>
      - birth_year
      - nationality
3. Ebook
      - name <sup>(primary key)</sup>
      - author <sup>(foreign key)</sup>
      - year_published
      - loan_type
      - ebook_content
4. Loan
      - id <sup>(primary key)</sup>
      - user <sup>(foreign key)</sup>
      - ebook <sup>(foreign key)</sup>
      - loan_date
      - loan_delete
5. Review
      - id <sup>(primary key)</sup>
      - user <sup>(foreign key)</sup>
      - ebook <sup>(foreign key)</sup>
      - rating
      - text_field
      - date

![models](./readme-imgs/Screenshot%202022-12-11%20104626.png)

## <ins> Project functionalty / project requirements:

- [x] utilise the django framework
- [x] interfaces for each model including: creation, update, deletion and addition of new objects.
- [x] search functionality for both books and authors
- [x] login and registration
- [x] deletion and update functionality to staff users only
- [x] filter book reviews based on ratings of said book
- [x] display average ratings on each book's page
- [x] display reviews on book's page
- [x] logged in user can review/comment on books
- [x] user profile page inclduing deletion and password update
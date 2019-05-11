# Fullstack Frameworks with Django Milestone 5 Project

## Classic Car Parts Webshop Triumphant Triumphs
Heroku App:  <br>
Heroku git:  <br>
GitHub:      <br>

This is the milestone project that I have created for the **“Fullstack Frameworks with Django”** module, which is part of  “Full Stack Web Development Course” offered by Code Institute.

## Step1 Creating Django Project Enviroment 
1. Create the project Clould9 Workspace **fullstack-frameworks-django-project**  <span style="color:green">Done</span> <br>

2. Install Django 1.11.20 <span style="color:green">Done</span> <br>
    ```python 
    sudo pip3 install django==1.11.20 
    ``` 
    This installs **django 1.11.20** and **pytz 2018.9** 
    
    output from bash terminal 
    ```python
    bennettpe:~/workspace $ sudo pip3 install django==1.11.20
    Downloading/unpacking django==1.11.20
    Downloading Django-1.11.20-py2.py3-none-any.whl (6.9MB): 6.9MB downloaded
    Downloading/unpacking pytz (from django==1.11.20)
    Downloading pytz-2018.9-py2.py3-none-any.whl (510kB): 510kB downloaded
    Installing collected packages: django, pytz
    Successfully installed django pytz
    Cleaning up...
    ```

3. Initalise Git repository <span style="color:green">Done</span> <br>
    ```python
    git init
    ```
    output from bash terminal
    ```python
    bennettpe:~/workspace $ git init
    Initialized empty Git repository in /home/ubuntu/workspace/.git/
    ```
    
4. Create `.gitignore` and `README.md` files <span style="color:green">Done</span>

5. Create `requirements.txt` file <span style="color:green">Done</span> <br>
   ```python
   sudo pip freeze --local > requirements.txt
   ```
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip freeze --local > requirements.txt
   ```
6. Go to Github https://github.com and Create new repository called `fullstack-frameworks-django-website` <span style="color:green">Done</span>
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ git add .
   bennettpe:~/workspace (master) $ git commit -m "first commit"
   [master (root-commit) 7fd944a] first commit
    4 files changed, 71 insertions(+)
    create mode 100644 .gitignore
    create mode 100644 README.md
    create mode 100644 WORKING.md
    create mode 100644 requirements.txt
   bennettpe:~/workspace (master) $ git remote add origin https://github.com/bennettpe/fullstack-frameworks-django-website.git
   bennettpe:~/workspace (master) $ git push -u origin master
   Username for 'https://github.com': bennettpe
   Password for 'https://bennettpe@github.com': 
   Counting objects: 5, done.
   Delta compression using up to 8 threads.
   Compressing objects: 100% (4/4), done.
   Writing objects: 100% (5/5), 1.40 KiB | 1.40 MiB/s, done.
   Total 5 (delta 0), reused 0 (delta 0)
   To https://github.com/bennettpe/fullstack-frameworks-django-website.git
    * [new branch]      master -> master
   Branch master set up to track remote branch master from origin.
   ```
   Heroku Git URL https://git.heroku.com/fullstack-frameworks-project.git

7. Go to Heroku https://dashboard.heroku.com/apps and <br> Create new app called `fullstack-frameworks-project` <span style="color:green">Done</span> <br>
   Click on `Create New App` fill in `App name`   
   Click on `Choose a region` and select `Europe`   
   Click on `Create app` button

8. Install Gunicorn
   ```python
   sudo pip3 install gunicorn
   ```
   This installs **gunicorn 19.9.0** 
   
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip3 install gunicorn
   Downloading/unpacking gunicorn
   Downloading gunicorn-19.9.0-py2.py3-none-any.whl (112kB): 112kB downloaded
   Installing collected packages: gunicorn
   Successfully installed gunicorn
   Cleaning up...
   ```

9. Install Psycopg2
   ```python
   sudo pip3 install psycopg2
   ```
   This installs **psycopg2 2.8**  

   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip3 install psycopg2
   Downloading/unpacking psycopg2
   Downloading psycopg2-2.8.tar.gz (367kB): 367kB downloaded
   Running setup.py (path:/tmp/pip_build_root/psycopg2/setup.py) egg_info for package psycopg2
     /usr/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'project_urls'
       warnings.warn(msg)
     /usr/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'python_requires'
       warnings.warn(msg)
    
   Installing collected packages: psycopg2
   Running setup.py install for psycopg2
     building 'psycopg2._psycopg' extension
     
   ....    
   Successfully installed psycopg2
   Cleaning up...    
   ```
10.  Create `requirements.txt` file <span style="color:green">Done</span> <br>
   ```python
   sudo pip freeze --local > requirements.txt
   ```
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip freeze --local > requirements.txt
   ``` 

11. Create a new PostgreSQL database on Heroku
    Click on `Resources`   
    Scroll down to `Add-ons` type `Postgres` select `Heroku Postgres` select `Hobby Dev - Free plan` click on `Provision` button
    This creates a empty database

12. Install dj-database-url
    ```python
    sudo pip3 install dj-database-url
    ```
    This installs **dj-database-url 0.5.0** 

    ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install dj-database-url
    Downloading/unpacking dj-database-url
    Downloading dj_database_url-0.5.0-py2.py3-none-any.whl
    Installing collected packages: dj-database-url
    Successfully installed dj-database-url
    Cleaning up...
    ```

13. Create Django project called `Triumphant-Triumphs` in the root directory by adding .
    ```python
    django-admin startproject triumphant_triumphs .
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ django-admin startproject triumphant_triumphs .  
    ```
    
    The following django files have been created
    ```
    fullstack-frameworks-django-project
    │
    ├── triumphant_triumphs
    │   │
    │   ├── __init__.py   # An empty file that tells Python that this directory should be considered a Python package. 
    │   ├── settings.py   # Settings/configuration for this Django project.
    │   ├── urls.py       # The URL declarations for this Django project; a “table of contents” of your Django-powered site.
    │   └── wsgi.py       # An entry-point for WSGI-compatible web servers to serve your project.
    │
    └── manage.py         # A command-line utility that lets you interact with this Django project in various ways.
    ```

14. Open `settings.py` and add the following to `ALLOWED_HOSTS` to allow Cloud9 as allowed host
    ```python
    ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')]
    ```

15. Run the following command to check running server is ok
    ```python
    python3 manage.py runserver SIP:$C9_PORT
    ```

    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py runserver $IP:$C9_PORT
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

    April 06, 2019 - 08:18:51
    Django version 1.11.20, using settings 'triumphant_triumphs.settings'
    Starting development server at http://0.0.0.0:8080/
    Quit the server with CONTROL-C.
    ```
    
    Click on link `your code is running at  https://fullstack-frameworks-django-project-bennettpe.c9users.io`
    and you see the following 
    ```python
    It worked!
    Congratulations on your first Django-powered page.
    Next, start your first app by running python manage.py startapp [app_label].

    You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!
    ```
    
    output from bash terminal
    ```python
    Not Found: /favicon.ico
    [06/Apr/2019 08:21:15] "GET /favicon.ico HTTP/1.1" 404 2017
    [06/Apr/2019 08:21:17] "GET / HTTP/1.1" 200 1716
    ```
16. Click on COG in workspace and click on `Show home in Favourites` 
    In workspace folder open up `.bash_aliases` file and add the following new alias to the bottom of the file.
    ```python
    alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"
    ```
    Close the bash terminal and reopen it to make the alias avaliable or Type `. ~/.bash_aliases`
    Type `run` to look at app.

17. Add `*.sqlite3 .~c9*files` files to ignore in `.gitignore`

18. Run `git status` to check which files will be added and commited to Git. 

19. Run the following command to initialize our databases and get table ready.
    ```python
    python3 manage.py migrate
    ```
    
    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying sessions.0001_initial... OK
    ```

20. Run the following commands to Commit changes to git.
    ```python
    git add .
    git commit -m "git commit -m "Initial commit for django project"
    ```

    output from bash terminal
    ```python
    [master 5dfdc88] Initial commit for django project
    8 files changed, 392 insertions(+), 4 deletions(-)
    create mode 100755 manage.py
    create mode 100644 triumphant_triumphs/__init__.py
    create mode 100644 triumphant_triumphs/settings.py
    create mode 100644 triumphant_triumphs/urls.py
    create mode 100644 triumphant_triumphs/wsgi.py
    ```
    
## Step2 Authentication App - Authentication and Authorisation 

This section is for setting up an **authentication mechanism** to allow users to register and log in.

1. **Create** Django app called **account** 
    ```python
    django-admin startproject accounts
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ django-admin startapp accounts 
    ```
    
    The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── accounts
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```    
2. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **accounts** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',                   <== this line added.
    ]
   ```

3. **Create** admin superuser
   ```python
   python3 manage.py createsuperuser
   ```

   ouput from bash terminal
   ```python
   bennettpe:~/workspace (master) $ python3 manage.py createsuperuser
   Username (leave blank to use 'ubuntu'): admin
   Email address: admin@gmail.com
   Password: 
   Password (again): 
   Superuser created successfully.
   ```
   
4. Log into Django admin 
   **Go to** https://fullstack-frameworks-django-project-bennettpe.c9users.io/admin <br>
   Enter **Username** and **Password** created in admin superuser. <br>
   Your now have access to the Django admin panel.

5. Create a **templates** folder in the **accounts** app <br>
   Create a new file called **index.html**
   ```python
   <!DOCTYPE html>
    <html>
        <head>
            <title> Django Auth </title>
        </head>
        <body>
            <nav>
               <ul>
                <li> <a href="#"> Login </a></li>
                <li> <a href="#"> Logout </a></li>
                <li> <a href="#"> Register </a></li>
                <li> <a href="#"> Profile </a></li>
               </ul>
            </nav>
        </body>
     </html>
   ```

6. Create a view function called **index** in **views.py**
   ```python
   def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')
   ```

7. Create a url pattern in **triumphant_triumphs/urls.py**
   ```python
   from accounts.views import index   
   url(r'^$', index),
   ```

8. Linking hrefs to URLs
   update file called **index.html**
   ```python
    <li> <a href="#"> Logout </a></li>
   ```
   change to
   ```python
    <li> <a href="{% url 'logout' %}"> Logout </a></li>
   ```

9. Create a view function called **logout** in **views.py**
   ```python
   from django.shortcuts import render, redirect, reverse <== add redirect, reverse
   from django.contrib import auth                        <== add this line
   # The 'logout' view allows users to logout
     def logout(request):
     """Log the user out"""
     auth.logout(request)
     return redirect(reverse('index'))
   ```

10. Create a url pattern in **triumphant_triumphs/urls.py**
    ```python
    from accounts.views import index, logout <== add logout
    url(r'^accounts/logout/$', logout, name="logout")
    ```
    
    amend
    ```python
    url(r'^$', index),               <== change from 
    url(r'^$', index, name="index"), <== change to
    ``` 

11. Add Django messages 
    in **accounts/views.py**
    amend
    ```python
    from django.contrib import auth            <== change from
    from django.contrib import auth, messages  <== change to
    ```
    add
    ```python
     messages.success(request, "You have successfully been logged out!")
    ```

    in **accounts/templates/index.html**
    add
    ```html
    {% if messages %}
    <div>
         {% for message in messages %}
             {{ messages }}
         {% endfor %}
    </div>
        {% endif %}
    ```
    
    Update **settings.py** file
    ```python
    MESSAGE_STORAGE ="django.contrib.messages.storage.session.SessionStroage"
    ```

12. Create a view function called **login** in **accounts/views.py**
    ```python
    # The 'logoin' view allows users to login 
    def login(request):
    """Log the user in"""
    return render(request, 'login.html')
    ```

13. Linking hrefs to URLs
    update **accounts/template/index.html**
    ```python
     <li> <a href="#"> Logoin </a></li>                   <== change from
     <li> <a href="{% url 'logoin' %}"> Logoin </a></li>  <== change to
    ```

14. Copy contents of **accounts/templates/index.html**   
    Create           **accounts/templates/login.html**   
    Amend H1 heading to `User Login`

15. Create a url pattern in **triumphant_triumphs/urls.py**
    ```python
    from accounts.views import index, logout, login <== add login
    url(r'^accounts/login/$', login, name="login")
    ```

16. Create login form in **accounts**
    ```python
    from django import forms

    class UserLoginForm(forms.Form):
    """Form to be used to log users in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    ```

17. Update **accounts/view.py**
    Add 
    ```python
    from accounts.forms import UserLoginForm
    ```
    Amend in view function called **login**
    ```python
     login_form = UserLoginForm() <== add this line
     return render(request, 'login.html') <== change from 
     return render(request, 'login.html', {"login_form": login_form}) <== change to
    ```
  
18. Update **accounts/templates/login.html
    Add
    ```python
    <form method="POST">
            {% csrf_token %}
            {{ login_form.as_p }}
            <button type="submit"> Login </button>
        </form> 
        
        {% if messages %}
            <div>
                {% for messages in messages %}
                    {{ message }}
                {% endfor %}
            </div>
        {% endif %}
    ```

19. Backend logic to authenticate user in **accounts/views.py**
    Add
    ```python
    # The 'logoin' view allows users to login 
    def login(request):
    """Log the user in"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!") 
            else:
                login_form.add_error(None, "Your username or password is incorrect")
                
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    ```

20. Apply template inheritance
    Create **template** folder in fullstack-frameworks_dgango-project
    Create **base.html** file  in fullstack-frameworks-django-project/templates
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title> {% block page_title %} {% endblock %} </title>
    </head>
    
    <body>
        <h1> {% block page_heading %} {% endblock %} </h1>
        <nav>
            <ul>
              <li> <a href="{% url 'login' %}" > Login </a></li>
              <li> <a href="{% url 'logout' %}"> Logout </a></li>
              <li> <a href="#"> Register </a></li>
              <li> <a href="#"> Profile </a></li>
            </ul>
        </nav>
        <hr>
        {% if messages %}
        <div>
            {% for messages in messages %}
                {{ messages }}
            {% endfor %}
        </div>
            {% endif %}
            {% block content %} {% endblock %}
    </body>
    </html>
    ```

    Update **index.html** in **fullstack-frameworks-django-project/templates**
    ```html
    {% extends 'base.html' %}

    {% block page_title %} Home Page {% endblock %}
    {% block page_heading %} Home    {% endblock %} 
    ```
    
    Update DIRS= in **settings.py** 
    ```python
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ```
    
    Update **login.html** in **fullstack-frameworks-django-project/templates**
    ```html
    {% extends 'base.html' %}

    {% block page_title %} Login Page {% endblock %}
    {% block page_heading %} User Login {% endblock %} 

    {% block content %}
    <form method="POST">
     {% csrf_token %}
        {{ login_form.as_p }}
        <button type="submit"> Login </button>
    </form> 
    {% endblock %}
    ```
    
21. Apply If user is not logged in show Register / Login options
    update **base.html** in **fullstack-frameworks-django-project/templates**
    ```html
    <ul>
        {% if user.is_authenticated %}  
            <li> <a href="#"> Profile </a></li>
            <li> <a href="{% url 'logout' %}"> Logout </a></li>
        {% else %}
            <li> <a href="#"> Register </a></li>
            <li> <a href="{% url 'login' %}" > Login </a></li>
        {% endif %}      
    </ul>
    ```

22. Allow logging out of users to only logged in users 
    Update **views.py** in **fullstack-frameworks-django-project/accounts**
    add if request.user_is_authenticated:
    ```python
    def login(request):
    """Log the user in"""
    if request.user.is_authenticated:
         return redirect(reverse('index')) #Redirect to index page
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
    ```

    add
    ```python
    from django.contrib.auth.decorators import login_required
    
    @login_required <== add this line
    def logout(request):
    ```

##### Setting up registration View and template    

1. Create a view function called **registration** in **views.py**
   ```python
   # The 'registration' view allows user to register
    def registration(request):
    """Manages the registration pages"""
    return render(request, 'registration.html')
   ```

   in **fullstack-freameworks-django-project\triumphant_triumphs\urls.py**
   ```python 
   from accounts.views import index, logout, login                <== change from 
   from accounts.views import index, logout, login, registration  <== change to
   ```
    
   in **fullstack-freameworks-django-project\triumphant_triumphs\templates\base.html** <br>
   Update
   ```python
   <li> <a href="{% url 'registration' %}" > Register </a></li>
   ```
    
   in **fullstack-freameworks-django-project\triumphant_triumphs\templates** <br>
   Create **registration.html** and copy content of **login.html** <br>
   Update **registration.html**
   ```html
   % extends 'base.html' %}

   {% block page_title %} Registration Page {% endblock %}
   {% block page_heading %} User Registration {% endblock %} 

   {% block content %}
   <p> If you have an account, Please log in <a href="{% url 'login' %}"> Sign in </a> </p>
   {% endblock %}
   ```
   
2. Add User registration form to **fullstack-frameworks-django-project\accounts\** <br>
   In **forms.py** <br>
   Add
   ```python
   from django.contrib.auth.models import User
   from django.contrib.auth.forms import UserCreationForm
   from django.core.exceptions import ValidationError  
   
   class UserRegistrationForm(UserCreationForm):  
    """Form used to register a new user"""
    
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
   ```

   In **views.py** <br>
   Update
   ```python
   from accounts.forms import UserLoginForm                        <== change from 
   from accounts.forms import UserLoginForm, UserRegistrationForm  <== change to
   
   return render(request, 'registration.html', {"registration_form": registration_form})
   ```
   
   Copy from **login.html** into **registration.htnl** 
   ```python
   <form method="POST">
    {% csrf_token %}
    {{ registration_form.as_p }}
    <button type="submit"> Register </button>
   </form>  
   ```
   
3. Django form validation
   Create the following in **forms.py**
   ```python
   from django import forms
   from django.contrib.auth.models import User
   from django.contrib.auth.forms import UserCreationForm
   from django.core.exceptions import ValidationError

   class UserLoginForm(forms.Form):
    """Form to be used to log users in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
   class UserRegistrationForm(UserCreationForm):  
    """Form used to register a new user"""
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
   
    def clean_email(self):  
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
            
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
    ```

4. View logic for registration
   Update a view function called **registration** in views.py
   ```python
   # The 'registration' view allows user to register
   def registration(request):
    """Manages the registration pages"""
    if request.user.is_authenticated:
        return redirect(reverse('index')) #Redirect to index page
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have sucessfully registered")
                return redirect(reverse('index')) #Redirect to index page
            else:
                messages.error(request, "Unable to register your account at this time")
    else:      
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": registration_form})
    ```
5. Create User Profile
   Create a view function called **user_profile** in views.py
   ```python
    from django.contrib.auth.models import User
    def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
   ```

    update **base.html** in **fullstack-frameworks-django-project/templates**
    ```html
    <li> <a href="{%url 'profile' %}"> Profile </a></li>
    ```
    
    In **urls.py** <br>
    Update
    ```python
    from accounts.views import index, logout, login, registration               <== change from
    from accounts.views import index, logout, login, registration, user_profile <== change to
    ```
    Add
    ```python
    url(r'^accounts/profile/$', user_profile, name="profile")
    ```
    
    Create a html page called **profile.html** in **fullstack-frameworks-django-project/templates**
    ```python
    {% extends 'base.html' %}

    {% block page_title %} {{ user }}'s Profile {% endblock %}
    {% block page_heading %} {{ user }}'s Profile   {% endblock %} 
    ```
    
##### Password Reset

1. Create new file **url_reset.py** in **fullstack-frameworks-django-project/accounts/**
   ```python
   # Reset Password

   from django.urls.conf import url
   from django.core.urlresolvers import reverse_lazy
   from django.contrib.auth.views import password_reset, password_reset_done,\
     password_reset_confirm, password_reset_complete

   urlpatterns = [
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', password_reset_complete, name='password_reset_complete')
   ]
   ```

2. Create new file **urls.py** in **fullstack-frameworks-django-project/accounts/**
   Cut urls for accounts from **urls.py** in **fullstack-frameworks-django-project**
   Add `include` 
   ```python
   # Accounts related urls

   from django.conf.urls import url, include                                    
   from accounts.views import index, logout, login, registration, user_profile
   import url_reset

   urlpatterns = [
       url(r'^logout/$', logout, name="logout"),
       url(r'^login/$', login, name="login"),
       url(r'^register/$', registration, name="registration"),
       url(r'^profile/$', user_profile, name="profile"),
       url(r'^password-reset/', include(url_reset)) <== remove $
   ]    
   ```
3. Update file **urls.py** in **fullstack-frameworks-django-project**
   Remove accounts urls
   ```python
   from django.conf.urls import url, include  <== add include
   from django.contrib import admin
   from accounts.views import index           <== add this line
   from accounts import urls as accounts_urls <== add this line

   urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^$', index, name="index"),
      url(r'^accounts/', include(accounts_urls)) <== add this line
   ]
   ```

##### Sending email to Console
    
1.  Add to **settings.py**
    ```python
    EMAIL_BACKEND ="django.core.mail.backends.console.EmailBackend"
    ```

##### Password Reset Templates
1.  Create new folder **registration** in **fullstack-frameworks-django-project/templates/** <br>
    Create new file   **password_reset_form.html** in **fullstack-frameworks-django-project/templates/registration**
    ```python
     <!--Password Reset Form --> 

    {% extends 'base.html' %}
    {% block page_title %} Password reset page {% endblock %}
    {% block page_heading %} Reset Password {% endblock %}

    {% block content %}
    <form method="POST">
    <p> Please enter your email address </p>
    
    {% csrf_token %}
    {{ form.email.errors }}
    <p>
        <label for="id_email"> Email address: </label>
        {{ form.email }}
        
        <buttton> Reset Password </buttton>
    </p>
    </form>
    {% endblock %}
    ```

    Update file **login.html** in **fullstack-frameworks-django-project/templates**
    Add
    ```python
    <p><a href="{% url 'password_reset' %}"> Reset Password </a></p>
    ```

##### Sending a Real Email  
1.  Add the following to **settings.py** in **fullstack-frameworks-django-project/triumphant_triumphs** 
    ```python
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com' 
    EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    EMAIL_PORT = 587
    ```

##### Email Authentication
1. Add the following to **settings.py** in **fullstack-frameworks-django-project/triumphant_triumphs** 
    ```python
    AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
    ]
    ```
2.  Create new file   **backends.py** in **fullstack-frameworks-django-project/accounts**
    ```python
    # Email Authentication 

    from django.contrib.auth.models import User

    class EmailAuth:
    """Authenticate a user by an exact match on the email and password"""
    
    def authenticate(self, username=None, password=None):
        """ Get an instance of `User` based off the email and verify the password """
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """ Used by the Django authentication sysytem to receive a user instance """
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
    ```

##### Adding Bootstrap Styling
1. Add bootstrap cdn links to **base.html** **fullstack-frameworks-django-project/templates**

#### Adding Django-forms-bootstrap
1.Install django-forms-bootstrap
    ```python
    sudo pip3 install django-forms-bootstrap
    ```
    This installs **dj-forms-bootstrap 3.1.0** 

    ouput from bash terminal
    ```python
    Downloading/unpacking django-forms-bootstrap
    Downloading django_forms_bootstrap-3.1.0-py2.py3-none-any.whl
    Installing collected packages: django-forms-bootstrap
    Successfully installed django-forms-bootstrap
    Cleaning up...
    ```
    
2. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **django_forms_bootstrap** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',     <== this line added.
    'accounts',                  
    ]
   ```

3.  Update `requirements.txt` file <br>
   ```python
   sudo pip freeze --local > requirements.txt
   ```
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip3 freeze --local > requirements.txt
   ``` 

4. in **registration.html** 
Add
```python
{% load bootstrap_tags %}
```

Amend to
```python
{{ registration_form | as_bootstrap }}
```
5. in **login.html** 
Add
```python
{% load bootstrap_tags %}
```

Amend to
```python
{{ login_form | as_bootstrap }}
```

#### Adding Static Files
1. Create new folder **static**     in **fullstack-frameworks-django-project**
2. Create new folder **css**        in **fullstack-frameworks-django-project/static**
3. Create new file   **styles.css** in **fullstack-frameworks-django-project/static/css**
4. Add to file **base.html**        in **fullstack-frameworks-django-project/templates**
    ```python
    {% load staticfiles %}
    ```
5. Add to file *settings.py**       in **fullstack-frameworks-django-project/triumphant_triumphs**
    ```python
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )
    ```
6. Add to file **styles.css** in **fullstack-frameworks-django-project/static/css**
    ```html
    form {
    width: 50%;
    }
    ```

#### Install Travis
1. Go to https://travis-ci.org/
2. Go to https://travis-ci.org/account/repositories and click toggle switch for required repository **fullstack-frameworks-django-project**
3. Click on repository name
4. Click on Build Unknown
5. Click on Image URL dropdown box
6. Choose Markdown
7. Copy Code that appears
8. Paste Code into top of README.md file
9. Create new file **.travis.yml** 
10. Add the following to **.travis.yml**
    ```python
    language: python
    python:
         - "3.4"
    install: "pip install -r requirements.txt"
    script:
    - SECRET_KEY="blah" ./manage.py test
    ```
11. Git commit changes
12. Push changes to github
    ```python
    bennettpe:~/workspace (master) $ git add .
    bennettpe:~/workspace (master) $ git commit -m "Commit Travis changes"
    [master 7991b24] Commit Travis changes
    11 files changed, 199 insertions(+), 48 deletions(-)
    create mode 100644 .travis.yml
    create mode 100644 static/css/styles.css
    create mode 100644 templates/footer.html
    create mode 100644 templates/navbar.html
    rewrite templates/registration/password_reset_form.html (65%)
    bennettpe:~/workspace (master) $ git push
    Username for 'https://github.com': bennettpe
    Password for 'https://bennettpe@github.com': 
    Counting objects: 84, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (79/79), done.
    Writing objects: 100% (84/84), 23.61 KiB | 1.82 MiB/s, done.
    Total 84 (delta 30), reused 0 (delta 0)
    remote: Resolving deltas: 100% (30/30), completed with 1 local object.
    To https://github.com/bennettpe/fullstack-frameworks-django-website.git
    7fd944a..7991b24  master -> master
    ```

#### Install Stripe
1.  Install stripe
    ```python
    sudo pip3 install stripe
    ```
    This installs **stripe 2.24.1** 
                  **requests-2.21.0**
                  **chardet-3.0.4**
                  **urllib3-1.24.1**
                  **idna-2.8**
                  **certifi-2019.3.9**

    ouput from bash terminal
    ```python
    Downloading/unpacking stripe
    Downloading stripe-2.24.1-py2.py3-none-any.whl (194kB): 194kB downloaded
    Downloading/unpacking requests>=2.20 (from stripe)
    Downloading requests-2.21.0-py2.py3-none-any.whl (57kB): 57kB downloaded
    Downloading/unpacking chardet>=3.0.2,<3.1.0 (from requests>=2.20->stripe)
    Downloading chardet-3.0.4-py2.py3-none-any.whl (133kB): 133kB downloaded
    Downloading/unpacking urllib3>=1.21.1,<1.25 (from requests>=2.20->stripe)
    Downloading urllib3-1.24.1-py2.py3-none-any.whl (118kB): 118kB downloaded
    Downloading/unpacking idna>=2.5,<2.9 (from requests>=2.20->stripe)
    Downloading idna-2.8-py2.py3-none-any.whl (58kB): 58kB downloaded
    Downloading/unpacking certifi>=2017.4.17 (from requests>=2.20->stripe)
    Downloading certifi-2019.3.9-py2.py3-none-any.whl (158kB): 158kB downloaded
    Installing collected packages: stripe, requests, chardet, urllib3, idna, certifi
    Found existing installation: requests 2.2.1
    Not uninstalling requests at /usr/lib/python3/dist-packages, owned by OS
    Found existing installation: chardet 2.2.1
    Not uninstalling chardet at /usr/lib/python3/dist-packages, owned by OS
    Found existing installation: urllib3 1.7.1
    Not uninstalling urllib3 at /usr/lib/python3/dist-packages, owned by OS
    Successfully installed stripe requests chardet urllib3 idna certifi
    Cleaning up...
    ```
    
2.  Update `requirements.txt` file <br>
   ```python
   sudo pip3 freeze --local > requirements.txt
   ```
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ sudo pip3 freeze --local > requirements.txt
   ``` 

1  Go to https://dashboard.stripe.com and either login or create an account
2. Add to file **settings.py** in **fullstack-frameworks-django-project/triumphant_triumphs**
    ```python
    STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
    STRIPE_SECRET = os.getenv('STRIPE_SECRET')
    ```
3. Create file **env.py** in **fullstack-frameworks-django-project/triumphant_triumphs**
   Copy Publishable key and Secret key from your stripe dashboard
   NB Do not push these keys to github as anyone thats gets these keys can hack into your account
   Make sure you add env.py to your .gitignore file
   
   ```python
   import os

   os.environ.setdefault("STRIPE_PUBLISHABLE", "add key here")
   os.environ.setdefault("STRIPE_SECRET", "add key here")
   ```
4. Add to file **.gitignore** in **fullstack-frameworks-django-project/triumphant_triumphs**   
   eny.py
5. Do a `git status` to make sure **eny.py** is exclude
6. Add to file **settings.py** in **fullstack-frameworks-django-project/triumphant_triumphs**   
   import env
7. git commit changes

## Products App 

This section is for setting up an **products** to allow users ability to select products.

1. **Create** Django app called **products** 
    ```python
    python3 manage.py startapp products
    ```

    ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py startapp products 
    ```
    
     The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── products
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```  
    
2. Add to **models.py** in **fullstack-frameworks-django-project/products** 
    ```python
    from django.db import models

    # Create your models here.
    class Product(models.Model):
    category = models.CharField(max_length=254)
    part_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=30)
    vehicle_model = models.CharField(max_length=25)
    required = models.DecimalField(max_digits=3, decimal_places=0)
    diagram_number = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
    def __str__(self):
        return self.part_name
    ```

3. Add to **admin.py** in **fullstack-frameworks-django-project/products**      
   To allow products to be added through the admin panel
   ```python
   from django.contrib import admin
   from .models import Product

   # Register your models here.
   admin.site.register(Product)
   ```

4. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **products** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',     
    'accounts',  
    'products',               <== this line added.
    ]
   ```

5. Install pillow
    Have to install pillow 5.4.1 as clould9 uses python3.4
    
    Backwards Incompatible Changes
    Python 3.4 dropped
    Python 3.4 is EOL since 2019-03-16 and no longer supported.    
    We will not be creating binaries, testing, or retaining compatibility with this version.   
    The final version of Pillow for Python 3.4 is 5.4.1.
    
    ```python
    sudo pip3 install pillow==5.4.1 
    ```
    
    This installs **pillow 5.4.1** 

    ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install pillow==5.4.1 
    Downloading/unpacking pillow==5.4.1
    Downloading Pillow-5.4.1.tar.gz (16.0MB): 16.0MB downloaded
    Running setup.py (path:/tmp/pip_build_root/pillow/setup.py) egg_info for package pillow
    /usr/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'python_requires'
      warnings.warn(msg)
    ....
    --------------------------------------------------------------------
    PIL SETUP SUMMARY
    --------------------------------------------------------------------
    version      Pillow 5.4.1
    platform     linux 3.4.3 (default, Nov 17 2016, 01:08:31)
                 [GCC 4.8.4]
    --------------------------------------------------------------------
    --- JPEG support available
    *** OPENJPEG (JPEG2000) support not available
    --- ZLIB (PNG/ZIP) support available
    *** LIBIMAGEQUANT support not available
    *** LIBTIFF support not available
    --- FREETYPE2 support available
    *** LITTLECMS2 support not available
    *** WEBP support not available
    *** WEBPMUX support not available
    --------------------------------------------------------------------
    To add a missing option, make sure you have the required
    library and headers.
    See https://pillow.readthedocs.io/en/latest/installation.html#building-from-source
    
    To check the build, run the selftest.py script.
    
    Successfully installed pillow
    Cleaning up...
    ```
    
6. Update `requirements.txt` file <br>
    ```python
    sudo pip3 freeze --local > requirements.txt
    ```

    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 freeze --local > requirements.txt
    ``` 
    
7. Run the following command to makemigrations.
    ```python
    python3 manage.py makemigrations products
    ```

    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py makemigrations products
    Migrations for 'products':
    products/migrations/0001_initial.py
    - Create model Product
    ```

8. Run the following command to migrate and create table in our database.
    ```python
    python3 manage.py migrate products
    ```
    
    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py migrate products
    Operations to perform:
    Apply all migrations: products
    Running migrations:
    Applying products.0001_initial... OK
    ```
    
#### Create Produts view and urls 
1. Create a view function called **products** in **fullstack-frameworks-django-project/products/views.py**
   ```python
   from django.shortcuts import render
    from products.models import Product

    # Create your views here.
    def products(request):
    return render(request, 'categories.html')

    # Product.objects.filter() will find all the product entries in the database whose category=engine
    # Then assign them to a 'products_list' variable and send that variable to engine.html template

    #ENGINE
    def engine(request):
    return render(request, 'engine.html', 
    {'products_list': Product.objects.filter(category='engine')})
    #CLUTCH
    def clutch(request):
    return render(request, 'clutch.html', 
    {'products_list': Product.objects.filter(category='clutch')})
    #GEARBOX
    def gearbox(request):
    return render(request, 'gearbox.html', 
    {'products_list': Product.objects.filter(category='gearbox')})
    #COOLING SYSTEM
    def cooling(request):
    return render(request, 'cooling.html', 
    {'products_list': Product.objects.filter(category='cooling')})
    #FUEL SYSTEM
    def fuel(request):
    return render(request, 'fuel.html', 
    {'products_list': Product.objects.filter(category='fuel')})   
    #STEERING
    def steering(request):
    return render(request, 'steering.html', 
    {'products_list': Product.objects.filter(category='steering')})     
    #FRONT SUSPENSION
    def suspfront(request):
    return render(request, 'suspfront.html', 
    {'products_list': Product.objects.filter(category='suspfront')})   
    #REAR SUSPENSION
    def susprear(request):
    return render(request, 'susprear.html', 
    {'products_list': Product.objects.filter(category='susprear')})  
    #BRAKE SYSTEM
    def brake(request):
    return render(request, 'brake.html', 
    {'products_list': Product.objects.filter(category='brake')})  
    #EXHAUST SYSTEM
    def exhaust(request):
    return render(request, 'exhaust.html', 
    {'products_list': Product.objects.filter(category='exhaust')}) 
    #ELECTRICS
    def electrics(request):
    return render(request, 'electrics.html', 
    {'products_list': Product.objects.filter(category='electrics')})      
    #INTERIOR
    def interior(request):
    return render(request, 'interior.html', 
    {'products_list': Product.objects.filter(category='interior')})     
    #EXTERIOR
    def exterior(request):
    return render(request, 'exterior.html', 
    {'products_list': Product.objects.filter(category='exterior')}) 
    #BODY & CHASSIS
    def body(request):
    return render(request, 'body.html', 
    {'products_list': Product.objects.filter(category='body')})    
    ```

2. Create urls **urls.py** in **fullstack-frameworks-django-project/products**
    ```python
    # Products related urls

    from django.conf.urls import url, include
    from products.views import products, engine, clutch, gearbox, cooling, fuel, steering, suspfront, susprear, brake, \
                           exhaust, electrics, interior, exterior, body

    urlpatterns = [
    url(r'^categories/$', products, name='categories'),
    url(r'^engine/$', engine, name='engine'),
    url(r'^clutch/$', clutch, name='clutch'),
    url(r'^gearbox/$', gearbox, name='gearbox'),
    url(r'^cooling/$', cooling, name='cooling'),
    url(r'^fuel/$', fuel, name='fuel'),
    url(r'^steering/$', steering, name='steering'),
    url(r'^suspfront/$', suspfront, name='suspfront'),
    url(r'^susprear/$', susprear, name='susprear'),
    url(r'^brake/$', brake, name='brake'),
    url(r'^exhaust/$', exhaust, name='exhaust'),
    url(r'^electrics/$', electrics, name='electrics'), 
    url(r'^interior/$', interior, name='interior'),
    url(r'^exterior/$', exterior, name='exterior'),
    url(r'^body/$', body, name='body')
    ]
    ```

3. Update file **urls.py** in **fullstack-frameworks-django-project\triumphant_triumphs**
   Add product urls
   ```python
   from django.conf.urls import url, include
   from django.contrib import admin
   from accounts.views import index
   from accounts import urls as accounts_urls
   from products import urls as products_urls   <== add this line

   urlpatterns = [
       url(r'^admin/', admin.site.urls),
       url(r'^$', index, name="index"),
       url(r'^accounts/', include(accounts_urls)),
       url(r'^products/', include(products_urls))  <== add this line
   ]
   ```

4. Create html files ***.html** in **fullstack-frameworks-django-project\products\templates**

5. Update **settings.py** in **fullstack-frameworks-django-project\triumphant_triumphs**
     go to **TEMPLATES** section and add the following line
     ```python
     TEMPLATES = [
     {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',              <== Add this line
                 ],
             },
         },
     ]
     ```

     add the following lines
     ```python
     MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
     MEDIA_URL = '/media/'
     ```
     
6. Update **urls.py** in **fullstack-frameworks-django-project\triumphant_triumphs**
     add the following line
     ```python   
     from django.views import static
     from .settings import MEDIA_ROOT
     url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
     ```

7. Create Media folder in **fullstack-frameworks-django-project**
   Create Images folder in **fullstack-frameworks-django-project**

## Checkout App - using Stripe

This section is for setting up an **customer payment mechanism** to allow users ability to pay.

1. **Create** Django app called **cart** 
    ```python
    python3 manage.py startapp cart
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py startapp cart 
    ```
    
    The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── cart
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```

2. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **cart** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'cart',             <== this line added.
    ]
   ```

3. Create file **contexts.py** in <i>fullstack-frameworks-django-project/checkout/cart</i>

4. In **setting.py** 
   go to **TEMPLATES** section and add line containing **'cart.contexts.cart_contents',** 
   ```python

   TEMPLATES = [
    {
            'context_processors': [
                'cart.contexts.cart_contents', <== Add this line
                ],
            },
        },
    ]
   ```

5. Create **urls.py** in <i>fullstack-frameworks-django-project/cart</i>  
    ```python
    from django.conf.urls import url
    from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart


    urlpatterns = [
        url(r'^$', view_cart, name="view_cart"),
        url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
        url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
        url(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove_from_cart'),
    ]
    ```

6. Update **views.py** in <i>fullstack-frameworks-django-project/cart</i>  

7. Update file **urls.py** in <i>fullstack-frameworks-django-project\triumphant_triumphs</i> <br>
   Add cart urls
   ```python
    from cart import urls as cart_urls  <== Add this line
    url(r'^cart/', include(cart_urls)), <== Add this line
   ```

8. Run the following command to makemigrations.
    ```python
    python3 manage.py makemigrations cart
    ```
    
    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py makemigrations cart
    No changes detected in app 'cart'
    ```

9.  Run the following command to migrate.
    ```python
    python3 manage.py migrate cart
    ```
    
    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py migrate cart
    Operations to perform:
    Apply all migrations: (none)
    Running migrations:
    No migrations to apply.
    ```

10. Create folder **templates** in <i>fullstack-frameworks-django-project/cart/</i> 
11. Create file **cart.html** in <i>fullstack-frameworks-django-project/cart/template</i> 

#### Create Checkout Models
1. In **models.py** in <i>fullstack-frameworks-django-project/checkout</i>     
    Add   
    ```python
    from django.db import models
    from products.models import Product

    # Create your models here.
    class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True) #Can be left blank
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

    class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} {2} @ {3}".format(self.quantity, self.product.part_name, self.product.part_number, self.product.price)
    ```

2. Add Models to Admin
   In **admin.py** in <i>fullstack-frameworks-django-project/checkout</i> 
   Add
   ```python
   from django.contrib import admin
   from .models import Order, OrderLineItem

   # Register your models here.
   class OrderLineAdminInline(admin.TabularInline):
     model = OrderLineItem

   class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)

   admin.site.register(Order, OrderAdmin)
   ```

3. Run the following command to makemigrations.
    ```python
    python3 manage.py startapp checkout
    ```

4. Run the following command to migrate.
    ```python
    python3 manage.py makemigrations checkout
    ```

   ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py makemigrations checkout
    Migrations for 'checkout':
    checkout/migrations/0001_initial.py
    - Create model Order
    - Create model OrderLineItem
    ```

5. Run the following command to migrate.
    ```python
    python3 manage.py migrate checkout
    ```

    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $  python3 manage.py migrate checkout
    Operations to perform:
    Apply all migrations: checkout
    Running migrations:
    Applying checkout.0001_initial... OK
    ```
    
#### Create Checkout Forms
1. Create **forms.py** in <i>fullstack-frameworks-django-project/checkout</i>    
    ```python
   from django import forms
   from .models import Order

   class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        ) 
    ```
#### Create Checkout Forms
1. Create **Views.py** in <i>fullstack-frameworks-django-project/checkout</i> 

#### Create Checkout html
1. Create **urls.py** in <i>fullstack-frameworks-django-project/checkout</i>  
    ```python
    from django.conf.urls import url
    from .views import checkout

    urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    ]
    ```
    
2. Update file **urls.py** in <i>fullstack-frameworks-django-project\triumphant_triumphs</i> <br>
   Add checkout urls
   ```python
    from checkout import urls as checkout_urls  <== Add this line
    url(r'^checkout/', include(checkout_urls)), <== Add this line
   ```

3. Create **checkout.html** in <i>fullstack-frameworks-django-project/checkout/templates</i> 

4. Update file **base.html** in <i>fullstack-frameworks-django-project/checkout/templates</i> <br>
   to include stripe js in head section
    ```python 
    <!-- STRIPE -->          <== add this section
    {% block head_js %}
    {% endblock head_js %}
    </head>
    ```

#### Create javascript for Stripe
1. Create folder **js** in <i>fullstack-frameworks-django-project/checkout/static</i> <br>
2. Create file **stripe.js** in <i>fullstack-frameworks-django-project/checkout/static/js</i> 
3. Test Stripe using Test Credit Card details as follows 
    ```
    Name:   Test Customer
    Credit card number: 4242424242424242
    Security code(CVV): 111
    Month:  1
    Year: 2020
    ```

#### Create contact app
1. **Create** Django app called **contact** 
    ```python
    python3 manage.py startapp contact
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py startapp contact 
    ```
    
    The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── contact
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```

2. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **contact** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'contact',             <== this line added.
    ]
   ```
3. Install django-phonenumber-field
    Have to install pillow 5.4.1 as clould9 uses python3.4
    
    ```python
    sudo pip3 install django-phonenumber-field
    ```
    
    This installs **phonenumberfield** 

    ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install django-phonenumber-field                                                                                                              
    Downloading/unpacking django-phonenumber-field
    Downloading django_phonenumber_field-2.3.1-py2.py3-none-any.whl (45kB): 45kB downloaded
    Downloading/unpacking babel (from django-phonenumber-field)
    Downloading Babel-2.6.0-py2.py3-none-any.whl (8.1MB): 8.1MB downloaded
    Requirement already satisfied (use --upgrade to upgrade): Django>=1.11.3 in /usr/local/lib/python3.4/dist-packages (from django-phonenumber-field)
    Requirement already satisfied (use --upgrade to upgrade): pytz>=0a in /usr/local/lib/python3.4/dist-packages (from babel->django-phonenumber-field)
    Installing collected packages: django-phonenumber-field, babel
    Successfully installed django-phonenumber-field babel
    Cleaning up...
    ```
    
4. Update `requirements.txt` file <br>
    ```python
    sudo pip3 freeze --local > requirements.txt
    ```

    output from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 freeze --local > requirements.txt
    ```    

5. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **phonenumber_field** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'phonenumber_field',     <== this line added.
    ]
   ```   

   Also add the following lines 
   ```python
   # PhoneNumberField Django library; allowing the use of GB numbers for contact app
     PHONENUMBER_DB_FORMAT = 'NATIONAL'
     PHONENUMBER_DEFAULT_REGION = 'GB'
   ```
   
4. Create **forms.py** in **fullstack-frameworks-django-project/contact** 
5. Add to **views.py** in **fullstack-frameworks-django-project/contact** 
6. Create **templates** in **fullstack-frameworks-django-project/contact** 
7. Update root **urls.py** in 
8. Create templates folder in **fullstack-frameworks-django-project/contact** 
8. Create **contact.html** in templates folder
9. Create **urls.py** **fullstack-frameworks-django-project/contact** 

#### Create contact about
1. **Create** Django app called **about** 
    ```python
    python3 manage.py startapp about
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py startapp about 
    ```
    
    The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── about
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```

5. Add to **views.py** in **fullstack-frameworks-django-project/about** 
6. Create **templates** in **fullstack-frameworks-django-project/about** 
7. Update root **urls.py** in 
8. Create templates folder in **fullstack-frameworks-django-project/about** 
8. Create **about.html** in templates folder
9. Create **urls.py** **fullstack-frameworks-django-project/about** 
10. 


#### Github vulnerablility message

1. I just pushed my changes to git hub and got a message saying github had found a vulnerability which was `urllib3`  
   needs to be upgraded to 1.24.2 or later, `urllib3` is downloaded when you `pip3 install stripe` should I just reinstall `stripe` ?

2. Upgrade  Urllib3 to 1.24.2
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install urllib3==1.24.2                                                                                                                       
    Downloading/unpacking urllib3==1.24.2
    Downloading urllib3-1.24.2-py2.py3-none-any.whl (131kB): 131kB downloaded
    Installing collected packages: urllib3
    Found existing installation: urllib3 1.24.1
    Uninstalling urllib3:
    Successfully uninstalled urllib3
    Successfully installed urllib3
    Cleaning up...
    ```

3.  Update `requirements.txt` file <br>
    ```python
    sudo pip3 freeze --local > requirements.txt
    ```

4. 'requirements.txt' now updated to urllib3 1.24.2
    ```python
    Babel==2.6.0
    Django==1.11.20
    Pillow==5.4.1
    certifi==2019.3.9
    chardet==3.0.4
    dj-database-url==0.5.0
    django-forms-bootstrap==3.1.0
    django-phonenumber-field==2.3.1
    gunicorn==19.9.0
    idna==2.8
    phonenumbers==8.10.10
    psycopg2==2.8
    pytz==2018.9
    requests==2.21.0
    stripe==2.24.1
    urllib3==1.24.2
    ```

#### Travis error 
1. Travis failed with the following error message `ImportError: No module named 'env'` added the following to the `settings.py` file
    ```python
    # Used locally and not in Heroku
    if os.path.exists('env.py'):
    import env
    ```

#### Email autentication error
1. DO the following
    go to the console
    1. touch secrets.sh
    2. chmod +x secrets.sh
    3. open secrets.sh
    4. add `export EMAIL_ADDRESS="xxxxxxxxxxxxx" and `export EMAIL_PASSWORD="xxxxxxx"`

2. So I have added my email address and email password as follows for my django project , but am still getting the following error message `SMTPSenderRefused at /accounts/password-reset/
(530, b'5.5.1 Authentication Required. Learn more at\n5.5.1  https://support.google.com/mail/?p=WantAuthError u11sm19169248wmu.15 - gsmtp', 'webmaster@localhost')` ?

3. decided to remove `secrets.sh` file and added email address and password to `env.py` and it all works ok.

#### Stripe api key none
1. problem due to settings.py file where it was not picking up `import env` 

#### Setting up AWS Buckets
1. see word document `Create new S3 Bucket.docx`

#### Adding S3 to django
1. see word document `Create new S3 Bucket.docx` Adding S3 to Django section.

2. Install django-storages
    
    ```python
    sudo pip3 install django-storages
    ```
    
    This installs **django-storages** 

    ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install django-storages
    Downloading/unpacking django-storages
    Downloading django_storages-1.7.1-py2.py3-none-any.whl (44kB): 44kB downloaded
    Requirement already satisfied (use --upgrade to upgrade): Django>=1.11 in /usr/local/lib/python3.4/dist-packages (from django-storages)
    Installing collected packages: django-storages
    Successfully installed django-storages
    Cleaning up...
    ```
    
3. Update `requirements.txt` file <br>
    ```python
    sudo pip3 freeze --local > requirements.txt
    ```

4. Install boto3

     ```python
    sudo pip3 install boto3
    ```
    
    This installs **boto3** 

    ouput from bash terminal
    
    ```python
    bennettpe:~/workspace (master) $ sudo pip3 install boto3
    Downloading/unpacking boto3
    Downloading boto3-1.9.144-py2.py3-none-any.whl (128kB): 128kB downloaded
    Downloading/unpacking botocore>=1.12.144,<1.13.0 (from boto3)
    Downloading botocore-1.12.144-py2.py3-none-any.whl (5.4MB): 5.4MB downloaded
    Downloading/unpacking jmespath>=0.7.1,<1.0.0 (from boto3)
    Downloading jmespath-0.9.4-py2.py3-none-any.whl
    Downloading/unpacking s3transfer>=0.2.0,<0.3.0 (from boto3)
    Downloading s3transfer-0.2.0-py2.py3-none-any.whl (69kB): 69kB downloaded
    Downloading/unpacking python-dateutil>=2.1,<3.0.0 (from botocore>=1.12.144,<1.13.0->boto3)
    Downloading python_dateutil-2.8.0-py2.py3-none-any.whl (226kB): 226kB downloaded
    Downloading/unpacking docutils>=0.10 (from botocore>=1.12.144,<1.13.0->boto3)
    Downloading docutils-0.14-py3-none-any.whl (543kB): 543kB downloaded
    Requirement already satisfied (use --upgrade to upgrade): urllib3>=1.20,<1.25 in /usr/local/lib/python3.4/dist-packages (from botocore>=1.12.144,<1.13.0->boto3)
    Requirement already satisfied (use --upgrade to upgrade): six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.1,<3.0.0->botocore>=1.12.144,<1.13.0->boto3)
    Installing collected packages: boto3, botocore, jmespath, s3transfer, python-dateutil, docutils
    Successfully installed boto3 botocore jmespath s3transfer python-dateutil docutils
    Cleaning up...
    ```
    
5. Update `requirements.txt` file <br>
    ```python
    sudo pip3 freeze --local > requirements.txt
    ``` 

6. In **setting.py** 
   go to **INSTALLED_APPS** section and add line containing **storages** 
   ```python
   # Application definition

   INSTALLED_APPS = [
    'storages',     <== this line added.
    ]
   ```
7. Make changes to `settings.py` to connect to AWS
   go to **Static files**  and add the following lines  
    ```python
    AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'pauls-fullstack-frameworks-django-project'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    ```
8. Then do a collectstatic
    ```python
    python3 manage.py collectstatic
    ```

    This uploads the static files

    ouput from bash terminal
    
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py collectstatic
    Database URL not found. Using SQLite instead
    /usr/local/lib/python3.4/dist-packages/storages/backends/s3boto3.py:282: UserWarning: The default behavior of S3Boto3Storage is insecure and will change in django-storages 2.0. By default files and new buckets are saved with an ACL of 'public-read' (globally publicly readable). Version 2.0 will default to using the bucket's ACL. To opt into the new behavior set AWS_DEFAULT_ACL = None, otherwise to silence this warning explicitly set AWS_DEFAULT_ACL.
    "The default behavior of S3Boto3Storage is insecure and will change "

    You have requested to collect static files at the destination
    location as specified in your settings.

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes
    Copying '/home/ubuntu/workspace/static/js/stripe.js'
    Copying '/home/ubuntu/workspace/static/js/custom.js'
    Copying '/home/ubuntu/workspace/static/js/bootstrap-magnify.js'
    Copying '/home/ubuntu/workspace/static/font-awesome/css/all.css'
    Copying '/home/ubuntu/workspace/static/font-awesome/css/all.min.css'
    ....
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/img/icon-deletelink.svg'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/img/icon-changelink.svg'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/img/gis/move_vertex_on.svg'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/img/gis/move_vertex_off.svg'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/fonts/Roboto-Light-webfont.woff'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/fonts/README.txt'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/fonts/Roboto-Bold-webfont.woff'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/fonts/LICENSE.txt'
    Copying '/usr/local/lib/python3.4/dist-packages/django/contrib/admin/static/admin/fonts/Roboto-Regular-webfont.woff'

    252 static files copied.
    ```
9. When I did a run to check everything was working get the following UserWarning message
    ```python
    /usr/local/lib/python3.4/dist-packages/storages/backends/s3boto3.py:282: UserWarning: 
    The default behavior of S3Boto3Storage is insecure and will change in django-storages 2.0. 
    By default files and new buckets are saved with an ACL of 'public-read' (globally publicly readable). 
    Version 2.0 will default to using the bucket's ACL. 
    To opt into the new behavior set AWS_DEFAULT_ACL = None, otherwise to silence this warning explicitly set AWS_DEFAULT_ACL.
    "The default behavior of S3Boto3Storage is insecure and will change "
    ```

    Added `AWS_DEFAULT_ACL = 'public-read'` to settings.py file to stop warning message.
    
#### 403 issue with Background issue 
1.
    ```css
    /* ----- Changes to Header ----- */
    /* ADD background */
    .masthead {
    width:100%; 
    height: 100%; 
    background: url("/static/img/vehicles/Triumph_Spitfire_MKIV_colors.svg") no-repeat center; 
    background-attachment: scroll; 
    background-size: cover; 
   
    }
    ```
    
    issue was due to background url not being correct , shoild have been 
    ```css
    background: url("../img/vehicles/Triumph_Spitfire_MKIV_colors.svg") no-repeat center; 
    ```
    
#### 404 issue with media images
1. have added images for fuel_pipes and fuel-tank but am getting 404's as they dont seem to be added to media folder, 
   have changed static folder to be on S3 so not sure if thats causing the issue.
   problem was due to having the following line in my **setting.py** file 
   ```python
   DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
   ```
   so removed this and the media file are now created ok.

#### Create app charts
1. **Create** Django app called **charts** 
    ```python
    python3 manage.py startapp charts
    ```
 
     ouput from bash terminal
    ```python
    bennettpe:~/workspace (master) $ python3 manage.py startapp chart
    ```
    
    The following django files have been **created**
    ```
    fullstack-frameworks-django-project
    │
    └── chart
        ├── migrations
        │   └── __init__.py # Python file to allow app packages to be imported from other directories.  
        │
        ├── __init__.py     # Python file to allow app packages to be imported from other directories. 
        ├── admin.py        # File with admin definitions for the app. 
        ├── apps.py         # File with configuration parameters for the app.
        ├── models.py       # File with database definitions (i.e., model classes) for the app.
        ├── tests.py        # File with test definitions for the app.
        └── views.py        # File with view definitions (i.e., controller methods) for the app.
    ```
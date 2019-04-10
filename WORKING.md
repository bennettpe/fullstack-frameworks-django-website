# Fullstack Frameworks with Django Milestone 5 Project

## Classic Car Parts Webshop
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

19. Run the following command toinitialize our databases and get table ready.
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

3. in **registration.html** 
Add
```python
{% load bootstrap_tags %}
```

Amend to
```python
{{ registration_form | as_bootstrap }}
```
4. in **login.html** 
Add
```python
{% load bootstrap_tags %}
```

Amend to
```python
{{ login_form | as_bootstrap }}
```

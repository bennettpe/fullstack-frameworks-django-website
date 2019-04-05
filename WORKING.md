# Fullstack Frameworks with Django Milestone 5 Project

## Classic Car Parts Webshop
Heroku App:  <br>
Heroku git:  <br>
GitHub:      <br>

This is the milestone project that I have created for the **“Fullstack Frameworks with Django”** module, which is part of  “Full Stack Web Development Course” offered by Code Institute.

## Step1 Creating Project Enviroment 
1. Create the project Clould9 Workspace **fullstack-frameworks-django-project**  <span style="color:green">Done</span> <br>

2. Install Django 1.11.20 <span style="color:green">Done</span> <br>
    ```python 
    sudo pip3 install django==1.11.20 
    ``` 
    This installs django 1.11.20 and pytz 2018.9 
    
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
   Note requirements.txt file is empty.
   ```python
   pip freeze --local > requirements.txt
   ```
   output from bash terminal
   ```python
   bennettpe:~/workspace (master) $ pip freeze --local > requirements.txt
   ```
6. Go to Github https://github.com and Create new repository called `fullstack-frameworks-django-website` <span style="color:green">Done</span>


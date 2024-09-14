
[PYTHON__BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[DJANGO__BADGE]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white

[DAJNGOREST__BADGE]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray

[GPT__BADGE]: https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white



<h1 align="center" style="font-weight: bold;">SmartTasker 🎯</h1>


![Python][PYTHON__BADGE]
![Django][DJANGO__BADGE]
![DjangoREST][DAJNGOREST__BADGE]
![ChatGPT][GPT__BADGE]


<p align="center">
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#nextsteps">Next Steps</a>
</p>

<p align="center">
  <b>Imagine a task application; it's a simple app, isn't it? But if this app could talk to you and give you advice about your tasks, it would be even more interesting, right? The SmarterTask app will provide users with advice on their projects based on the comments made within the app, using artificial intelligence.</b>
</p>

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

You have to install Python 3 and Git 2 in your system. Click on the links below:

- [Python](https://www.python.org/downloads/)
- [Git 2](https://github.com/git-guides/install-git)


<h3>Cloning</h3>

 

```bash
#Open the command prompt on your computer and choose a folder to place the project copy. Inside your folder, use this command:

git clone https://github.com/rodrigonoronha/SmartTasker_app.git
```

<h3> Environment Variables</h2>

<p>You need to create an API key with OpenAI. After that, you'll need to purchase some credits for your account. </p>

Inside the project, you'll see a folder called 'app'. Inside it, you'll find a file named '.env-example'. You need to rename it to '.env' and update the variable 'OPENAI_API_KEY' with your key. Then, update the variable 'OPENAI_MODEL' by choosing the model you prefer.


```yaml
PENAI_API_KEY = 'OPENAI API KEY'
OPENAI_MODEL = 'GPT MODEL'
```

<h3>Starting</h3>

The first step is to create a virtual environment (venv) inside a folder:

```bash
#create a virtual environment (venv) inside a folder
python -m venv venv

#activate venv (Windows)
.\venv\Scripts\activate

#install the requirements
pip install -r requirements.txt

#create a database (SQLite).
python manage.py migrate

#create a Django superuser
python manage.py createsuperuser

#start the application
python manage.py runserver
``````

You can access it in the browser at http://localhost:8000

Obs: We can access http://localhost:8000/admin/ and log in using the user and password created earlier. After that, we can create more users for using the app.

<h2 id="routes">📍 API Endpoints</h2>

​Using port 8000 and accessing the endpoints, you have access to the information

Exemplo: http://localhost:8000/api/v1/authentication/token/

With this route, you can create an authentication token and use it to access the information.

| authentication routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /api/v1/authentication/token/</kbd>     | authentication user info see [auth details](#post-auth-token)
| <kbd>POST /api/v1/authentication/token/verify/</kbd>     | verify API user info see [verify details](#post-auth-verify)
| <kbd>POST /api/v1/authentication/token/refresh/</kbd>     | refresh API user info see [refresh details](#post-auth-refresh)

<h3 id="post-auth-token">POST /api/v1/authentication/token/</h3>

**REQUEST**
```json
{
  "username": "user123",
  "password": "123456"
}
```

**RESPONSE**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjg0MjAxMywiaWF0IjoxNzI2MjM3MjEzLCJqdGkiOiIyMmM4MTU0N2QxYzU0ZjM2Yjk4NWEzMTYwNTk1MzAzOSIsInVzZXJfaWQiOjJ9.A67hbuQHDsM5y8AHnhg9_apXCZw9iAD5l3GiDlrrG6I",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MzIzNjEzLCJpYXQiOjE3MjYyMzcyMTMsImp0aSI6ImFiYjI5M2NhOWE5NzRlNGZiYWE0MWQxNzU3ZjcxZTI2IiwidXNlcl9pZCI6Mn0.mFDf5OdgPlQ3EMLazXsiHziBUlbciNFLsgpvFSRcLmI"
}
```

<h3 id="post-auth-token">POST /api/v1/authentication/token/verify/</h3>

**REQUEST**
```json
{
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MzIzNjEzLCJpYXQiOjE3MjYyMzcyMTMsImp0aSI6ImFiYjI5M2NhOWE5NzRlNGZiYWE0MWQxNzU3ZjcxZTI2IiwidXNlcl9pZCI6Mn0.mFDf5OdgPlQ3EMLazXsiHziBUlbciNFLsgpvFSRcLmI"
}
```

**RESPONSE**
```json
{}
```

<h3 id="post-auth-refresh">POST /api/v1/authentication/token/refresh/</h3>

**REQUEST**
```json
{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjg0MjAxMywiaWF0IjoxNzI2MjM3MjEzLCJqdGkiOiIyMmM4MTU0N2QxYzU0ZjM2Yjk4NWEzMTYwNTk1MzAzOSIsInVzZXJfaWQiOjJ9.A67hbuQHDsM5y8AHnhg9_apXCZw9iAD5l3GiDlrrG6I"
}
```

**RESPONSE**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MzIzOTU0LCJpYXQiOjE3MjYyMzcyMTMsImp0aSI6ImQ5YWM4NDA4OTZlZjQwYWRhODQ5MGMyYWExMDM1ODUyIiwidXNlcl9pZCI6Mn0.pHqfr8wdMNYe2hR4TYXXNTIlL7caBjmjJVbOLhZzy3Q"
}
```


| categories routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET/POST /api/v1/categories/</kbd>     | list-create categories info see [list-create-details](#list-create-categories)
| <kbd>GET/PATCH/PUT/DELETE /api/v1/categories/5/</kbd>     | retrieve-update-delete categories user info see [retrieve-update-delete-details](#retrieve-update-delete-categories)


<h3 id="list-create-categories">GET /api/v1/categories/</h3>

**RESPONSE**
```json
[
    {
        "id": 1,
        "name": "Work",
        "description": "Work-raleted tasks."
    },
    {
        "id": 2,
        "name": "Personal",
        "description": "Personal tasks."
    },
    {
        "id": 3,
        "name": "Financial",
        "description": "Financial tasks."
    }
]
```

<h3 id="list-create-categories">POST /api/v1/categories/</h3>

**REQUEST**
```json
{
    "name":"Travels",
    "description":"Plans for vacation..."
}
```

**RESPONSE**
```json
{
    "id": 12,
    "name": "Travels",
    "description": "Plans for vacation..."
}
```

<h3 id="retrieve-update-delete-categories">GET /api/v1/categories/5/</h3>

**RESPONSE**
```json
{
    "id": 5,
    "name": "Health",
    "description": "Health activits"
}
```

<h3 id="retrieve-update-delete-categories">PATCH/PUT /api/v1/categories/5/</h3>

**REQUEST**
```json
{
    "name":"Fitness"
}
```

**RESPONSE**
```json
{
    "id": 5,
    "name": "Fitness",
    "description": "Health activits"
}
```

<h3 id="retrieve-update-delete-categories">DELETE /api/v1/categories/5/</h3>

**RESPONSE**
```json

```

| projects routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET/POST /api/v1/projects/</kbd>     | list-create projects info see [list-create-details](#list-create-projects)
| <kbd>GET/PATCH/PUT/DELETE /api/v1/projects/4/</kbd>     | retrieve-update-delete projects user info see [retrieve-update-delete-details](#retrieve-update-delete-projects)

<h3 id="list-create-projects">GET /api/v1/projects/</h3>

**RESPONSE**
```json
[
    {
        "id": 4,
        "name": "Get a new job",
        "priority": "High",
        "description": "I need to get a new job to provide for my family.",
        "created_at": "2024-09-13T17:17:36.388397Z",
        "updated_at": "2024-09-13T17:17:36.388397Z",
        "due_date": "2024-11-05",
        "completed": false,
        "project_category": 3
    }
]
```

<h3 id="list-create-projects">POST /api/v1/projects/</h3>

**REQUEST**
```json
{
    "name":"Get a new job",
    "priority":"High",
    "description":"I need to get a new job to provide for my family.",
    "due_date":"2024-11-05",
    "project_category":"3"
}
```

**RESPONSE**
```json
{
    "id": 4,
    "name": "Get a new job",
    "priority": "High",
    "description": "I need to get a new job to provide for my family.",
    "created_at": "2024-09-13T17:17:36.388397Z",
    "updated_at": "2024-09-13T17:17:36.388397Z",
    "due_date": "2024-11-05",
    "completed": false,
    "project_category": 3
}
```

<h3 id="retrieve-update-delete-projects">GET /api/v1/projects/4/</h3>

**RESPONSE**
```json
{
    "id": 4,
    "name": "Get a new job",
    "priority": "High",
    "description": "I need to get a new job to provide for my family.",
    "created_at": "2024-09-13T17:17:36.388397Z",
    "updated_at": "2024-09-13T17:17:36.388397Z",
    "due_date": "2024-11-05",
    "completed": false,
    "project_category": 3
}
```

<h3 id="retrieve-update-delete-projects">PATCH/PUT /api/v1/projects/4/</h3>

**REQUEST**
```json
{
    "name":"Open a company",
    "description":"I need to create a way to earn money to provide for my family"
}
```

**RESPONSE**
```json
{
    "id": 4,
    "name": "Open a company",
    "priority": "High",
    "description": "I need to create a way to earn money to provide for my family",
    "created_at": "2024-09-13T17:17:36.388397Z",
    "updated_at": "2024-09-13T17:36:54.998578Z",
    "due_date": "2024-11-05",
    "completed": false,
    "project_category": 3
}
```

<h3 id="retrieve-update-delete-projects">DELETE /api/v1/projects/4/</h3>

**RESPONSE**
```json

```

| tasks routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET/POST /api/v1/tasks/</kbd>     | list-create tasks info see [list-create-details](#list-create-tasks)
| <kbd>GET/PATCH/PUT/DELETE /api/v1/tasks/1/</kbd>     | retrieve-update-delete tasks user info see [retrieve-update-delete-details](#retrieve-update-delete-tasks)

<h3 id="list-create-tasks">GET /api/v1/tasks/</h3>

**RESPONSE**
```json
[
    {
        "id": 3,
        "name": "Create a resume",
        "description": "I need to create a resume to send to some companies in order to get a job.",
        "created_at": "2024-09-13T17:44:04.303792Z",
        "updated_at": "2024-09-13T17:44:04.303792Z",
        "due_date": "2024-12-06T00:00:00Z",
        "completed": false,
        "project": 4,
        "task_category": 1
    }
]
```

<h3 id="list-create-tasks">POST /api/v1/tasks/</h3>

**REQUEST**
```json
{
    "name":"Create a resume",
    "description":"I need to create a resume to send to some companies in order to get a job.",
    "due_date":"2024-12-06T00:00:00Z",
    "project":"4",
    "task_category":"1"
}
```

**RESPONSE**
```json
{
    "id": 3,
    "name": "Create a resume",
    "description": "I need to create a resume to send to some companies in order to get a job.",
    "created_at": "2024-09-13T17:44:04.303792Z",
    "updated_at": "2024-09-13T17:44:04.303792Z",
    "due_date": "2024-12-06T00:00:00Z",
    "completed": false,
    "project": 4,
    "task_category": 1
}
```

<h3 id="retrieve-update-delete-tasks">GET /api/v1/tasks/3/</h3>

**RESPONSE**
```json
{
    "id": 3,
    "name": "Create a resume",
    "description": "I need to create a resume to send to some companies in order to get a job.",
    "created_at": "2024-09-13T17:44:04.303792Z",
    "updated_at": "2024-09-13T17:44:04.303792Z",
    "due_date": "2024-12-06T00:00:00Z",
    "completed": false,
    "project": 4,
    "task_category": 1
}
```

<h3 id="retrieve-update-delete-tasks">PATCH/PUT /api/v1/tasks/3/</h3>

**REQUEST**
```json
{
    "description":"I need to create a resume"
}
```

**RESPONSE**
```json
{
    "id": 3,
    "name": "Create a resume",
    "description": "I need to create a resume",
    "created_at": "2024-09-13T17:44:04.303792Z",
    "updated_at": "2024-09-13T17:53:38.870017Z",
    "due_date": "2024-12-06T00:00:00Z",
    "completed": false,
    "project": 4,
    "task_category": 1
}
```

<h3 id="retrieve-update-delete-tasks">DELETE /api/v1/tasks/3/</h3>

**RESPONSE**
```json

```

| subtasks routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET/POST /api/v1/subtasks/</kbd>     | list-create subtasks info see [list-create-details](#list-create-subtasks)
| <kbd>GET/PATCH/PUT/DELETE /api/v1/subtasks/4/</kbd>     | retrieve-update-delete subtasks user info see [retrieve-update-delete-details](#retrieve-update-delete-subtasks)

<h3 id="list-create-subtasks">GET /api/v1/subtasks/</h3>

**RESPONSE**
```json
[
    {
        "id": 4,
        "name": "Open the computer and search for resume templates",
        "completed": false,
        "task": 3
    }
]
```

<h3 id="list-create-subtasks">POST /api/v1/subtasks/</h3>

**REQUEST**
```json
{
    "name":"Open the computer and search for resume templates",
    "task":"3"
}
```

**RESPONSE**
```json
{
    "id": 4,
    "name": "Open the computer and search for resume templates",
    "completed": false,
    "task": 3
}
```

<h3 id="retrieve-update-delete-subtasks">GET /api/v1/subtasks/4/</h3>

**RESPONSE**
```json
{
    "id": 4,
    "name": "Open the computer and search for resume templates",
    "completed": false,
    "task": 3
}
```

<h3 id="retrieve-update-delete-subtasks">PATCH/PUT /api/v1/subtasks/4/</h3>

**REQUEST**
```json
{
    "name":"Open the computer"
}
```

**RESPONSE**
```json
{
    "id": 4,
    "name": "Open the computer",
    "completed": false,
    "task": 3
}
```

<h3 id="retrieve-update-delete-tasks">DELETE /api/v1/subtasks/4/</h3>

**RESPONSE**
```json

```

| comments routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET/POST /api/v1/comments/</kbd>     | list-create comments info see [list-create-details](#list-create-comments)
| <kbd>GET/PATCH/PUT/DELETE /api/v1/comments/18/</kbd>     | retrieve-update-delete comments user info see [retrieve-update-delete-details](#retrieve-update-delete-comments)

<h3 id="list-create-comments">GET /api/v1/comments/</h3>

**RESPONSE**
```json
[
    {
        "id": 18,
        "content": "I want to open my own company, but I don't know what to do first.",
        "created_at": "2024-09-13T18:27:18.851112Z",
        "project": 4
    }
]
```

<h3 id="list-create-comments">POST /api/v1/comments/</h3>

**REQUEST**
```json
{
    "content":"I want to open my own company, but I don't know what to do first.",
    "project":"4"
}
```

**RESPONSE**
```json
{
    "id": 18,
    "content": "I want to open my own company, but I don't know what to do first.",
    "created_at": "2024-09-13T18:27:18.851112Z",
    "project": 4
}
```

<h3 id="retrieve-update-delete-comments">GET /api/v1/comments/18/</h3>

**RESPONSE**
```json
{
    "id": 18,
    "content": "I want to open my own company, but I don't know what to do first.",
    "created_at": "2024-09-13T18:27:18.851112Z",
    "project": 4
}
```

<h3 id="retrieve-update-delete-comments">PATCH/PUT /api/v1/comments/18/</h3>

**REQUEST**
```json
{
    "content":"How can I start my project about build a company?"
}
```

**RESPONSE**
```json
{
    "id": 18,
    "content": "How can I start my project about build a company?",
    "created_at": "2024-09-13T18:27:18.851112Z",
    "project": 4
}
```

<h3 id="retrieve-update-delete-comments">DELETE /api/v1/comments/18/</h3>

**RESPONSE**
```json

```

| ai routes               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /api/v1/ai/</kbd>     | list-create ai info see [list-details](#list-ai)

<h3 id="list-create-ai">GET /api/v1/ai/</h3>

**RESPONSE**
```json
[
    {
    "result": "Hey there! Starting a project to build a company sounds exciting! Here are some steps you can take to kickstart your project:\n\n1. **Define Your Business Idea**: Clearly outline what products or services your company will offer and identify your target market.\n\n2. **Market Research**: Conduct thorough research to understand your industry, market trends, and competitors.\n\n3. **Create a Business Plan**: Outline your business goals, operational structure, marketing strategies, and financial projections.\n\n4. **Register Your Company**: Choose a suitable business structure and register your company with the necessary authorities.\n\n5. **Build a Team**: Surround yourself with talented individuals who can contribute their skills and expertise to help grow your company.\n\n6. **Set Up Your Work Space**: Create a conducive environment where you can focus on developing and growing your business.\n\n7. **Take Action**: Break down your project into smaller tasks and start working on them gradually to bring your business idea to life.\n\nRemember, building a company requires dedication, hard work, and persistence. Good luck with your project, and feel free to reach out if you need any more guidance! 🚀"
    }
]
```

<h2 id='nextsteps'> 👟 Next steps </h2>

- Create the front end for the application

- Create the API for the user to register in the app

- Create automated tests to fix potential issues
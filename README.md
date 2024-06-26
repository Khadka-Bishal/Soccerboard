 # Soccerboard

Soccerboard is a responsive and dynamic web application built in Python using the Django framework. You can play soccer quizzes, get the latest match stats of your favorite teams in the top 5 leagues, and also view the current league tables.


## 🆕 Updates

- The free credit from Microsoft Azure for Students has expired. Since the web application was hosted on an Azure VM, the web app is no longer accessible. (June 04, 2024)

## 📜 Description

Web scraping is an integral part of this project. The data for the league tables are scraped from the web using the BeautifulSoup library and served to the user directly without storing it in the database. The stats, however, are stored in the PostgreSQL database and are queried from the Django models using Django ORM commands. The data collection process for stats runs automatically every hour using APScheduler. To speed up the data collection and avoid memory leaks, the project uses multi-threading techniques. Function-based views are predominantly used rather than class-based views to avoid too much abstraction.

The project includes a quiz game that is written entirely in HTML, CSS, and JS. The questions are randomly selected and the options are shuffled.

The contact form included has both client-side and server-side validation to validate and sanitize user input. It is ensured that the input conforms to the expected format and does not contain any malicious content that would otherwise allow an attacker to inject HTTP headers which could be a serious security vulnerability. The form also ensures that the user is not providing an empty name and message or special characters such as spaces in the required field.

The templates follow a well-structured approach. The project uses a base template that contains the common elements of the web pages such as HTML introduction and Bootstrap. The other templates extend the base template and add their own content. The static files, such as images, CSS, and JavaScript, are stored in a separate folder following the industry standards to facilitate static file collection during deployment. The templates and static files have been minified before deployment for better rendering. However, the static files pushed to GitHub are not minified for readability purposes. 

The project also provides APIs for users to access the data about the teams. The APIs return JSON responses that contain the team name, rank, points, goals scored, goals conceded, etc. 

The project follows the Python PEP 8 conventions for code style and formatting. The code is well commented and documented using docstrings and comments.

## ☁️ Deployment 

I have deployed the Django web application on an Azure Virtual Machine running Ubuntu, using Gunicorn as the Python WSGI HTTP server and Nginx as the web server (reverse proxy). I have used PostgreSQL as a database backend.

The cryptographic layer (SSL/TLS) has been enabled to encrypt the data transmitted between the user's browser and the web server. This is done to ensure that sensitive information, such as login credentials of the admin and emails/messages in the contact form, is not intercepted and read by unauthorized individuals, thus preventing man-in-the-middle attacks.

Here is the link to the website on my
[studio](http://bishalkhadka.studio/soccer/). 

## 📐 Architecture
<img width="860" alt="Screenshot 2023-07-12 at 15 56 15" src="https://github.com/BishKhadka/Soccerboard/assets/12107885/386851d6-2f36-4683-8e45-981436df6cd9">


## ⚙️ API Reference
I used Django REST Framework to create REST APIs and execute CRUD operations.

#### Get all data
Returns all the data of all the teams in the top 5 league

```http
  GET /soccer/api/all-data/
```


#### Get team names
Returns the names of all the clubs in the top 5 league
```http
  GET /soccer/api/teams/
```

#### Post results
Create data and add it to the model (requires admin privilege)

```http
  POST /soccer/api/add/
```

#### Remove model
Remove the entire model (requires admin privilege)


```http
  DELETE /soccer/api/delete-entire-model/
```

## 🧰 Languages and Tools

<a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> 
<a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> 
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> 
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> 
</a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> 
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> 
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> 
<a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> 
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> 
<a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="40"/> </a><a href="https://www.django-rest-framework.org" target="_blank" rel="noreferrer"> <img src="https://www.django-rest-framework.org/img/logo.png" alt=“djangorestframework” width="80" height="60"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://download.logo.wine/logo/Nginx/Nginx-Logo.wine.png" alt=“Ngnix” width="80" height="40"/> </a>
<a href="https://gunicorn.org" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Gunicorn_logo_2010.svg/1280px-Gunicorn_logo_2010.svg.png" alt=“gunicorn width="100" height="40"/></a>

**Front-end**: HTML, CSS, Bootstrap, JavaScript

**Back-end**: Python, Django, Django REST Framework

**Database**: PostgreSQL

**API Testing**: Postman

**Deployment**: Azure, Ngnix, Gunicorn

**Version Control**: GitHub



## 🛠 Skills

I acquired these skills through this project. 

- Full-stack web development skill

- Cloud computing skills

- API testing skills

- Version control skills

- Web scraping skills

- Automation skills

## 📱 Responsive Web Design Demo

https://github.com/BishKhadka/Soccerboard/assets/12107885/4c09560f-cd65-4c31-aa36-c5a63ffc2ef5




## 🫶 Acknowledgements

 [Click Here](https://bishalkhadka.studio/soccer/acknowledgement)
 
## 🏛️ Other Projects

Check out some of my other projects [here](https://github.com/Khadka-Bishal). 


## 🔗 Connect
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khadka-bishal/)

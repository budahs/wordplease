# [WORDPLEASE]

[ DEVELOPING LANGUAGE ] Python Django

Project to create a multiple blog interface, and its capability to deliver data through rest Framework
___
## [INITIAL CONFIGURATION]
___

### [1] Clone this repo:

```
https://github.com/budahs/wordplease.git
```

### [2] setup environment:

```bash
virtualenv env
source env/bin/activate
```

### [3] Install dependencies needed:

```
pip install -r requirements.txt
```

### [4] Create .env file with basic variables:

```
DEBUG=on
SECRET_KEY=yoursecretkey
SQLITE_URL=yourdatabase url
```

### [5] setup databases and create supersuser and run dev server:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

___
## [WEB INTERFACE] Wordplease
___
| Feature | URL | Note |
| ------- | --- | ---- |
| Home | `/` | List of latest published posts |
| Admin panel | `/admin/` | Login administration |
| Log in | `/login/` | User Login |
| Logout | `/logout/` | WordPlease logout |
| Register | `/register/` | User registration |
| Blogs | `/blogs/` | List of blogs available |
| User blog | `/blogs/<str:username>` | List of posts in a blog |
| Post detail | `/blogs/<str:username>/<int:pk>` | Post detailed view from post |
| Create new post | `/new/` | You need to be logged |

___
## [WEB INTERFACE] Wordplease
___

### [1] Users

| Methods | URL |
| ------ | ------ | 
| GET POST| `/api/users/` | 
| POST | `/api/users/`
| GET POST UPDATE DELETE| `/api/users/<int:pk>` |

### [2] Posts
| Method | URL |
| ------ | --- |
| POST |  `/api/posts/` |
| GET |  `api/posts/<str:username>/` |
| GET POST UPDATE DELETE|  `api/posts/<int:pk>` |
| GET|  `api/blogs/` |

### [3] Files
| GET POST |  `api/files/` |

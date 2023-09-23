import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbusers',
        'USER': 'root',
        'PASSWORD': 'wltn',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
SECRET = {
         'secret':'django-insecure-u8k6cu%7@nsl9i*a%7$a%q2&ot8i_yb_2rp*vxxz&j0u5nw28w'
}
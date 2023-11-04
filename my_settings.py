import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database-1',
        'USER': 'admin',
        'PASSWORD': 'urop2023',
        'HOST': 'database-1.ccgwtelz3n2i.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
        'OPTINS': {
            'init_command': 'SET sql_mode="STRIC_TRANS_TABLES"'
        }
    }
}
SECRET = {
         'secret':'django-insecure-u8k6cu%7@nsl9i*a%7$a%q2&ot8i_yb_2rp*vxxz&j0u5nw28w'
}


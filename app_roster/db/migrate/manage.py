#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(debug='False',url='postgresql://rrkwiepojqjmww:172d2d30c807aeca359c780861f63bcaa276bd8b9c25e2e6444ab6b8ec5dbf2c@ec2-35-172-16-31.compute-1.amazonaws.com:5432/de5q7mpd4qi77e',repository='.')

    # postgres://ユーザ名:パスワード@ホスト名:5432/データベース名
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'de5q7mpd4qi77e',
    #         'USER': 'rrkwiepojqjmww',
    #         'PASSWORD': '172d2d30c807aeca359c780861f63bcaa276bd8b9c25e2e6444ab6b8ec5dbf2c',
    #         'HOST': 'ec2-35-172-16-31.compute-1.amazonaws.com',
    #         'PORT': '5432',
    #     }
    # }
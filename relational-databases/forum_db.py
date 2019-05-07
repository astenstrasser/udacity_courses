# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    data_base = psycopg2.connect("dbname=forum")
    cursor = data_base.cursor()
    cursor.execute("update posts set content = 'safe content, not spam!' where content like '%spam%'")
    cursor.execute('select content, time from posts order by time desc')
    POSTS = cursor.fetchall()
    data_base.close()
    return POSTS


def add_post(content):
    data_base = psycopg2.connect("dbname=forum")
    cursor = data_base.cursor()
    # important to protect code from SQL injections!
    cursor.execute('insert into posts values (%s)', (content,))
    data_base.commit()
    data_base.close()

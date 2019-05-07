# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    data_base = psycopg2.connect("dbname=forum")
    cursor = data_base.cursor()
    cursor.execute("update posts set content = 'this_was_spam' where content like '%spam%'")
    cursor.execute("delete from posts where content = 'this_was_spam' or content = ''")
    cursor.execute("select content, time from posts order by time desc")
    POSTS = cursor.fetchall()
    data_base.close()
    return POSTS


def add_post(content):
    data_base = psycopg2.connect("dbname=forum")
    cursor = data_base.cursor()
    cursor.execute("insert into posts values (%s)", (bleach.clean(content),) )  # important to use bleach to protect code from SQL injections!
    data_base.commit()
    data_base.close()

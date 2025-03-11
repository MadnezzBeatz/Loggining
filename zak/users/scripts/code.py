from django.contrib.auth.hashers import check_password
import psycopg2
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zak.zak.settings")


def create_connection(dbname, user, password, host):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        print("Есть контакт")
    except:
        print("Не контачит")

    return connection

def app_auth(username,enteredpassword):
    con = create_connection('accounts', 'savely', 'savely', 'localhost')
    cur = con.cursor()
    cur.execute(f"SELECT username, password FROM auth_user WHERE username='{username}';")
    # cur.execute("SELECT * FROM auth_user")
    user = cur.fetchall()
    auth = check_password(enteredpassword,user[0][1])
    # print(auth)
    return auth
# app_auth("testuser3", "DJVeeS10")
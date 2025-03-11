from steampy.guard import generate_one_time_code
import psycopg2
from ..models import *

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

def get_code(share):
    shared_secret = share
    one_time_authentication_code = generate_one_time_code(shared_secret)
    return one_time_authentication_code

def get_games():
    games = Id.objects.all()
    game_dict = {}
    for game in games:
        id = game.number
        name = game.name
        game_dict[name] = id
    return game_dict



def get_accounts(gamename, gameclub):
    accounts_list = {}
    accounts = Steam.objects.all()
    accounts = accounts.filter(status = 0, game_list = gamename)
    for i in accounts:
        if str(i.gameclub) == gameclub:
            auth_code = get_code(i.secret_key)
            accounts_date = [i.login, i.password, auth_code]
            accounts_list[i.login] = accounts_date


    return accounts_list

def change_status_true(login):
    account = Steam.objects.all()
    account = account.filter(login = login)
    if account:
        for i in account:
            i.status = True
            i.save()


def change_status_false(login):
    account = Steam.objects.all()
    account = account.filter(login=login)
    if account:
        for i in account:
            i.status = False
            i.save()

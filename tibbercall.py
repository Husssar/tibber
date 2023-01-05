import requests
import cred
import pymysql

URL = 'https://api.tibber.com/v1-beta/gql'
KEY = cred.key
USER = cred.user
PASSWORD = cred.password
HOST = cred.host
DATABASE = cred.database

def insert_data(value):
    cnx = None
    qry = []
    try:
        cnx = pymysql.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        cnx.autocommit = True
        for r in value:
            qry = (f"INSERT IGNORE INTO grid_cost (when_price, price, tax, totalprice) "
                   f"VALUES (\"{r['startsAt']}\", {r['energy']}, {r['tax']}, {r['total']})")
            print(qry)
            cur = cnx.cursor()
            cur.execute(qry)
            cnx.commit()
    except Exception as e:
        print(e)
    finally:
        cnx.close()


# KEY registerd at tibber.se
def get_data(when):
    headers = {
        'Authorization': 'Bearer '+ KEY +'',
        'Content-Type': 'application/json',
    }

    json_data = {
        'query':
            '{viewer '
                 '{homes '
                 '{currentSubscription '
                     '{priceInfo '
                         '{' + when + ' '
                            '{total energy tax startsAt }'
                            '}'
                        '}'
                    '}'
                 '}'
            '}',
    }
    response = requests.post(URL, headers=headers, json=json_data)
    data = response.json()
    price = data['data']['viewer']['homes'][0]['currentSubscription']['priceInfo'][when]
    return price


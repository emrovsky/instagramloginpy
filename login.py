from datetime import datetime

import loguru
import requests


def login(username,password):
    s = requests.session()
    s.headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'pragma': 'no-cache',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1010561150',
        'x-requested-with': 'XMLHttpRequest',
    }

    s.get("https://www.instagram.com/")

    s.headers.update({'x-csrftoken':s.cookies.get_dict()['csrftoken']})

    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{password}',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': username,
    }

    response = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data)
    if response.json()["authenticated"] == False:
        loguru.logger.error("wrong password or smth")
        return None
    if response.json()["authenticated"] == True:
        return response.cookies.get_dict()

cookies = login("username","password")
print(cookies)

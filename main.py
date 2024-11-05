import random

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from test import get_client_numbers

options = webdriver.ChromeOptions()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=C:\Users\hvati\OneDrive\Рабочий стол\rassilka\Profile') # УКАЖИТЕ ПУТЬ ГДЕ ЛЕЖИТ ВАШ ФАЙЛ. Советую создать отдельную папку.
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--profiling-flush=n')
options.add_argument('--enable-aggressive-domstorage-flushing')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)


# numbers = ["+71111123123123123", "+79283911520"]
text = """
*Привет!* 😍 На связи твой мастер перманентного макияжа 😅😅😅 Я немного соскучилась 😏%0A%0A

У меня для тебя есть интересное%0A
предложение (тссссс🤫, это только для моих любимых клиентов)%0A%0A

А именно *любая процедура со скидкой 25%*🔥🔥🔥%0A%0A

К примеру,  если первичная процедура стоит 6000₽ то для тебя будет 4500₽%0A%0A

Обновление моей работы 4000₽, то сейчас будет 3000₽🔥🔥🔥...Мне кажется очень крутое предложение!!!%0A%0A

*Что для этого нужно сделать* 👇%0A%0A

Просто внести предоплату 1000р и скидка зафиксирована.  Дату можно выбрать в любое время до конца ноября!%0A%0A

*Хотела бы воспользоваться таким предложением?*😉%0A
😍%0A%0A

P.s : У тебя есть 3 дня на принятие решения, скидка сгорит и такого шанса больше не будет 😅%0A
"""
# get_client_numbers()[:150]
for number in get_client_numbers()[800:1050]:

    try:
        url = f"https://web.whatsapp.com/send?phone={number}&text={text}"
        driver.get(url)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button')))
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button').click()
        print('Я отправил сообщение')
        sleep(random.randint(3, 6))
    except:
        continue




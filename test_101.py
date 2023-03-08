import time
import urllib
from urllib.request import urlopen
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import authLocators

name = 'Тестовая линия'
tel = 1111111111
name2 = 'Автотест'
url = "https://piter-online.net/"


def test_101():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    time.sleep(2)
    WebDriverWait(pytest.driver, 15).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/span')))
    pytest.driver.find_element(*authLocators.auth_street_field).click()
    time.sleep(1)
    # Листаем до нужного элемента
    e = pytest.driver.find_element(*authLocators.just_scroll)
    actions = ActionChains(pytest.driver)
    actions.scroll_to_element(e).perform()
    # Заполняем поля
    pytest.driver.find_element(*authLocators.auth_street_field).send_keys(name)
    time.sleep(1)
    pytest.driver.find_element(*authLocators.auth_street_field).send_keys(Keys.RETURN)
    pytest.driver.find_element(*authLocators.auth_home_field).click()
    time.sleep(1)
    pytest.driver.find_element(*authLocators.auth_home_field).send_keys(1)
    time.sleep(1)
    pytest.driver.find_element(*authLocators.auth_home_field).send_keys(Keys.RETURN)
    time.sleep(1)
    # Выбираем значение "квартира"
    pytest.driver.find_element(*authLocators.auth_value_list_apart).click()
    # Жмем кнопку "найти"
    pytest.driver.find_element(*authLocators.auth_btn_find).click()
    time.sleep(4)
    # Закрываем всплывающее окно
    pytest.driver.find_element(*authLocators.auth_x).click()
    time.sleep(1)
    # листаем до нужного элемента
    c = pytest.driver.find_element(*authLocators.auth_btn_connect)
    actions = ActionChains(pytest.driver)
    actions.scroll_to_element(c).perform()
    time.sleep(2)
    # Жмем кнопку "подключить"
    pytest.driver.find_element(*authLocators.auth_btn_connect).click()
    time.sleep(2)
    # Заполняем поля
    pytest.driver.find_element(*authLocators.auth_name_field).click()
    time.sleep(2)
    pytest.driver.find_element(*authLocators.auth_name_field).send_keys(name2)
    pytest.driver.find_element(*authLocators.auth_tel_field).send_keys(tel)
    pytest.driver.find_element(*authLocators.auth_request).click()
    time.sleep(2)
    # Получаем адрес страницы и его статус код
    link = urllib.request.urlopen(pytest.driver.current_url)
    link = link.getcode()
    assert link == 201 or link == 200
    print(link)
    pytest.driver.quit()


count = 0
while count < 4:
    test_101()
    count += 1
    print(count)

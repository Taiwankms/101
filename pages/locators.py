from selenium.webdriver.common.by import By


class authLocators:
    just_scroll = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div > div > div > a > div')
    auth_tel_field = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(4) > div > div:nth-of-type(2) > div > form > div > div:nth-of-type(3) > div > div:nth-of-type(2) > input')
    auth_street_field = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(2) > div > div > div > div > div > div > div > div > div > input')
    auth_home_field = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > div > div > div > input')
    auth_value_list_apart = (By.XPATH, '//*[@id="forSelectField"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]')
    auth_value_list = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > div > div > div > div > span')
    auth_btn_find = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(2) > div > div > div > div:nth-of-type(3) > div > div')
    auth_name_field = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(4) > div > div:nth-of-type(2) > div > form > div > div:nth-of-type(2) > div > div:nth-of-type(2) > input')
    auth_btn_result = (By.CLASS_NAME, 'app198 app228 app226 app222 app210 app227')
    auth_x = (By.CSS_SELECTOR, 'div#root > div > div:nth-of-type(4) > div > div > div > div > div')
    auth_btn_connect = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(4) > div:nth-of-type(4) > div > div > div > div:nth-of-type(2) > div > div:nth-of-type(6) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > a')
    auth_request = (By.CSS_SELECTOR, 'div#root > div > div > div:nth-of-type(4) > div > div:nth-of-type(2) > div > form > div > div:nth-of-type(5) > div')
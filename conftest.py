import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# подключаем драйвер chrome и входим в аккаунт
@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/drivers/chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.maximize_window()
    pytest.driver.find_element(By.ID, 'email').send_keys('elvira.khisamova@gmail.com')
    pytest.driver.find_element(By.ID, 'pass').send_keys('test123')
    pytest.driver.implicitly_wait(10)
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Мои питомцы')]"))).click()

    yield
    pytest.driver.quit()
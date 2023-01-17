import pytest
from selenium.webdriver.common.by import By

# проверяем соответствует ли количество питомев в таблице количеству питомцев в блоке "test user"
def test_all_pets_here():
    pytest.driver.implicitly_wait(10)
    plan = pytest.driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
    fact = int(
        pytest.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>div').text.split("\n")[1].split(":")[1].strip())
    assert plan == len(fact)

# проверяем что хотя бы у половины питомцев есть фото
def test_half_pets_have_img():
    pytest.driver.implicitly_wait(10)
    img = pytest.driver.find_elements(By.TAG_NAME, 'img')
    fact = int(
        pytest.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>div').text.split("\n")[1].split(";")[1].strip())
    no_img = 0
    for i in range(len(img)):
        if img[i].get_attribute('src') == "":
            no_img += 1
    assert fact / 2 >= no_img

# проверяем что у всех питомцев прописано имя, возраст и порода
def test_all_pets_have_name_age_breed():
    pytest.driver.implicitly_wait(10)
    fact = int(
        pytest.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>div').text.split("\n")[1].split(":")[1].strip())
    name = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[1]')
    breed = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[2]')
    age = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[3]')
    for i in range(len(name)):
        assert name[i].text != ""
        assert breed[i].text != ""
        assert age[i].text != ""
    assert fact == len(name) == len(breed) == len(age)

# проверяем что имена всех питомцев отличаются
def test_all_names_are_different():
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[1]')
    names_list = []

    for i in range(len(names)):
        names_list.append(names[i].text)
    unigue_names = set(names_list)
    assert len(names_list) == len(unigue_names)

# проверяем что животные не повторяются
def test_no_repeating_pets():
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[1]')
    breed = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[2]')
    ages = pytest.driver.find_elements(By.XPATH, '//tr/th/following-sibling::td[3]')
    list_names = []
    list_breed = []
    list_ages = []
    list_pets = []
    list = []

    for i in range(len(names)):
        list_names.append(names[i].text)
        list_breed.append(breed[i].text)
        list_ages.append(ages[i].text)
    for j in range(len(names)):
        list_pets.append(list_names[j])
        list_pets.append(list_breed[j])
        list_pets.append(list_ages[j])
        list.append(list_pets)
        list_pets = []

    for k in range(len(names)):
        n = k + 1
        while n < len(names):
            assert list[k] != list[n]
            n += 1
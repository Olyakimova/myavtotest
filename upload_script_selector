from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/Register.html")

# Заполнение всех полей
first_name = driver.find_element_by_xpath(
    "//input[@ng-model='FirstName']")
first_name.send_keys("Olga")
last_name = driver.find_element_by_xpath(
    "//input[@placeholder='Last Name']")
last_name.send_keys("Yakimova")
email = driver.find_element_by_xpath(
    "//input[@ng-model = 'EmailAdress']")
email.send_keys("tester@gmail.com")
phone = driver.find_element_by_xpath(
    "//input[@ng-model = 'Phone']")
phone.send_keys("0991234567")
gender = driver.find_element_by_xpath(
    "//input[@value='FeMale']")
gender.click()

# Загрузка файла
file = ("C:\workspace\Python\picture.jpg")
imagesrc = driver.find_element_by_id("imagesrc")
imagesrc.send_keys(file)
time.sleep(2)

# Заполнение селекторов country, date of birth
country = driver.find_element_by_id("countries")
select = Select(country)
select.select_by_value("Russia")

yearbox = driver.find_element_by_id("yearbox")
select = Select(yearbox)
select.select_by_value("2000")

monthbox = driver.find_element_by_css_selector("[ng-model='monthbox']")
# или так: driver.find_element_by_css_selector("div:nth-child(3) > select")
select = Select(monthbox)
select.select_by_value("November")

daybox = driver.find_element_by_id("daybox")
select = Select(daybox)
select.select_by_value("30")

# Заполнение пароля
firstpassword = driver.find_element_by_id("firstpassword")
firstpassword.send_keys("Tester123")
secondpassword = driver.find_element_by_id("secondpassword")
secondpassword.send_keys("Tester123")

# Скролл страницы
driver.execute_script("window.scrollBy(0, 300);")

#  Подтверждение регистрации
submit_btn = driver.find_element_by_id("submitbtn")
submit_btn.click()
time.sleep(3)

# Проверкa что произошёл переход на ожидаемый адрес страницы
# http://demo.automationtesting.in/WebTable.html
print("находимся на странице:")
current_page = driver.current_url 	# здесь без “()” на конце
assert current_page == "http://demo.automationtesting.in/WebTable.html"
# Расширенная проверка адреса
expected_address = "http://demo.automationtesting.in/WebTable.html"
if current_page == "http://demo.automationtesting.in/WebTable.html":
    print("Адрес страницы совпадает")
else:
    print("Адрес не совпадает, фактический: ", current_page)
    print("Ожидаемый: ", expected_address)
driver.quit()

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# логин
login = driver.find_element_by_css_selector("input#txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_name("Submit")
login_btn.click()

# переход на вкладку PIM
pim = driver.find_element_by_id("menu_pim_viewPimModule")
pim.click()
time.sleep(3)

# переход в раздел Employee List
employee_list = driver.find_element_by_id("menu_pim_viewEmployeeList")
employee_list.click()
time.sleep(2)

# переход в карточку пользователя
employee = driver.find_element_by_link_text("Lisa")
employee.click()
time.sleep(1)

# проверка недоступности радиокнопки Gender противоположного пола сотрудника
gender_male = driver.find_element_by_id("personal_optGender_1")
gender_male_disabled = gender_male.get_attribute("disabled")
print("value of radiobutton Gender: ", gender_male_disabled)
if gender_male_disabled is not None:
    print("Радиокнопка недоступна для выбора")
else:
    print("Радиокнопка доступна")

# проверка недоступности селектора nationality сотрудника
nationality_selector = driver.find_element_by_id("personal_cmbNation")
nationality_selector_disabled = nationality_selector.get_attribute("disabled")
print("value of selector: ", nationality_selector_disabled)
if nationality_selector_disabled is None:
    print("Атрибута нет, селектор доступен")
else:
    print("Атрибут есть, селектор отключен")

# переход в режим редактирования сотрудника
save_edit_btn = driver.find_element_by_id("btnSave")
save_edit_btn.click()
time.sleep(2)

# выбор и проверка что выбрана радиокнопка противоположного пола
gender_male.click()
time.sleep(3)
gender_male_checked = gender_male.get_attribute("checked")
print("value of gender male: ", gender_male_checked)
if gender_male_checked is not None:
    print("Радиокнопка изменена")
else:
    print("Радиокнопка не изменена")

# выбор самой последней страны в селекторе nationality
nationality_selector.click()
nationality_selector_zimbabwean = driver.find_element_by_css_selector(
    "option:nth-child(194)")
# или так: driver.find_element_by_css_selector("[value='193']").click()
nationality_selector_zimbabwean.click()
# или так:
# select = Select(nationality_selector)
# select.select_by_value("193")

# проверка что в селекторе nationality выбрана самая последняя страна в списке
nationality_selector_zimbabwean = nationality_selector.get_attribute("value")
if nationality_selector_zimbabwean == "193":
    print("Выбрана последняя страна в списке")
else:
    print("Выбрана НЕ последняя страна в списке")
time.sleep(2)

# возврат первоначальных данных сотрудника и сохранение
gender_female = driver.find_element_by_id("personal_optGender_2")
gender_female.click()
time.sleep(3)
nationality_selector = driver.find_element_by_id("personal_cmbNation")
nationality_selector.click()
nationality_selector_select = driver.find_element_by_css_selector(
    "[value='0']")
nationality_selector_select.click()
# или так:
# select.select_by_value("0")
save_edit_btn.click()
# save_edit_btn = driver.find_element_by_id("btnSave").click()

driver.quit()

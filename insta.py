from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()


driver.get('https://passport.yandex.ru/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1')
time.sleep(1)

name_tag = driver.find_element(By.XPATH, """//input[@id="firstname"]""")
name_tag.send_keys("Майкл")
time.sleep(1)

surname_tag = driver.find_element(By.XPATH, """//input[@id="lastname"]""")
surname_tag.send_keys("Джексон")
time.sleep(1)


muzh = driver.find_element(By.XPATH, """/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span""")
muzh.click()
time.sleep(1)


mail_tag = driver.find_element(By.XPATH, """//input[@id="login"]""")
mail_tag.send_keys("examplemail4412")
time.sleep(1)


passw_tag = driver.find_element(By.XPATH, """//input[@id="password"]""")
passw_tag.send_keys("examplepassword")
time.sleep(1)

passw_confirm_tag = driver.find_element(By.XPATH, """//input[@id="password_confirm"]""")
passw_confirm_tag.send_keys("examplepassword")
time.sleep(1)

uvedomy = driver.find_element(By.XPATH, """//*[@id="keep_unsubscribed"]""")
uvedomy.click()
time.sleep(1)


otvet = driver.find_element(By.XPATH, """//input[@id="hint_answer"]""")
otvet.send_keys("Петруччи")
time.sleep(30)


c = input()
capcha = driver.find_element(By.XPATH, """//input[@id="captcha"]""")
capcha.send_keys(c)
time.sleep(1)


reg = driver.find_element(By.XPATH, """/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button""")
reg.click()
time.sleep(15)


# skip = driver.find_element(By.XPATH, """/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a""")
# skip.click()
# time.sleep(1)

driver.quit()


#теперь инста
driver = webdriver.Firefox()

driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(1)


pochta_tag = driver.find_element(By.XPATH, """//input[@class="_2hvTZ pexuQ zyHYP"]""")
pochta_tag.send_keys("ivan0ivanov0ivanych@yandex.ru")
time.sleep(1)


name_tag = driver.find_element(By.XPATH, """//input[@class="_2hvTZ pexuQ zyHYP"]""")
name_tag.send_keys("Иван Иванов")
time.sleep(1)


muzh = driver.find_element(By.XPATH, """/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span""")
muzh.click()
time.sleep(1)


tag = driver.find_element(By.XPATH, """//input[@name="password"]""")
tag.send_keys("example")
time.sleep(1)


rege = driver.find_element(By.XPATH, """/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button""")
rege.click()
time.sleep(1)


driver.quit()
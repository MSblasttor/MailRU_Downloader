# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


def main():
    driver = webdriver.Chrome()
    #driver.get("https://cloud.mail.ru/public/1Swo/65ww21Q3G")
    #driver.implicitly_wait(10)
    driver.get("https://cloud.mail.ru/public/kZkB/WR6UL8w3n")
    #files = driver.find_elements(By.CLASS_NAME,"VirtualList__colItem*")
    #sleep(10)
    try:
        files = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'VirtualList__colItem')]"))
        )
    finally:
        print("We here!")
        btns_dwl = driver.find_elements(By.XPATH, "//div[contains(@class, 'DataListControl__icon')]")
    #files = driver.find_elements(By.XPATH, "//div[contains(@class, 'VirtualList__colItem')]")

    cnt = 0
    for file in files:
        file.click()
        print(file)
        sleep(1)
        btn_dwl = btns_dwl[cnt]
        cnt += 1
        print(cnt)
        btn_dwl.click()
        try:
            checkbox = driver.find_element(By.XPATH, "//div[contains(@class, 'Checkbox__root')]")
            checkbox.click()
            btn = driver.find_element(By.XPATH, "//button[@data-name='action']")
            btn.click()
        except NoSuchElementException:
            print("Not alert window")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

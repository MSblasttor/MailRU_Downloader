# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


def main():
    driver = webdriver.Chrome()
    driver.get("https://cloud.mail.ru/public/1Swo/65ww21Q3G")
    #files = driver.find_elements(By.CLASS_NAME,"VirtualList__colItem*")

    while not driver.find_elements(By.XPATH, "//div[contains(@class, 'VirtualList__colItem')]"): sleep(1)
    files = driver.find_elements(By.XPATH, "//div[contains(@class, 'VirtualList__colItem')]")
    btns_dwl = driver.find_elements(By.XPATH, "//div[contains(@class, 'DataListControl__icon-')]")
    cnt = 0
    for file in files:

        file.click()
        #print(file.get_property())
        sleep(1)
        btn_dwl = btns_dwl[cnt]
        cnt += 1
        print(cnt)
        #btn_dwl = driver.find_element(By.XPATH, "//div[contains(@class, 'DataListControl__icon-')]")
        btn_dwl.click()
        while not driver.find_element(By.XPATH, "//div[contains(@class, 'Checkbox__root')]"): sleep(1)
        checkbox = driver.find_element(By.XPATH, "//div[contains(@class, 'Checkbox__root')]")
        checkbox.click()
        btn = driver.find_element(By.XPATH, "//button[@data-name='action']")
        btn.click()
        sleep(10)
        #print(btn_dwl)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from selenium.webdriver.common.by import By
import constant

driver = constant.driver

def openURL(url):
    try:
        driver.get(url)
        driver.maximize_window()
    except Exception as e:
        print("error in opening URL")


def byLocator(element_type, elem_str):
    if element_type == "XPATH":
        element = driver.find_element(By.XPATH, elem_str)
    if element_type == "Name":
        element = driver.find_element(By.NAME, elem_str)
    return element


def take_screenshot(str_path):
    constant.save_screenshot(str_path)


def manage_alert(driver):
    alert = driver.switch_to.alert
    print(alert.text)
    alert.send_keys("hello")
    alert.accept()


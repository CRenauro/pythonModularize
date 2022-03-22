import function
import constant
driver = constant.driver

def click(element, msg):
    try:
        element.click()
        print("clicked" + msg)

    except Exception:
        print("error")
        function.take_screenshot(constant.screenshot_path)


def type_keys(element, str_msg):
    element.send_keys(str_msg)
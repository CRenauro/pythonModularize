import time
import constant
import function as fb
import action as at

fb.openURL(constant.fbUrl)

element = fb.byLocator("XPATH", "//input[@id='email']")
at.type_keys(element, "hello@gmail.com")
time.sleep(5)

element = fb.byLocator("XPATH", "//input[@aria-label='Password']")
at.type_keys(element, "6qLyX2huW")
time.sleep(5)

element = fb.byLocator("XPATH", "//button[.='Log In']")
at.click(element, "Logged in")
time.sleep(5)

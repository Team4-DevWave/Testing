import sys
sys.path.append('E:\Spring2024\SW\Phase3\mobile_tests\MobileTesting\Phase_4')
from main import *

el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(2)")
el5.click()
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="My profile")
el6.click()
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(2)")
el7.click()

el10 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el10.click()
el10.send_keys("hell")
el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="r/hello world")
el11.click()
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Join")
el12.click()
el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(2)")
el13.click()
el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Leave")
el14.click()
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Leave Community")
el15.click()

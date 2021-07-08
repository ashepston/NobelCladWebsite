from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_presence(test_object1, test_object2=True, test_object3=True, test_object4=True, test_object5=True):
    element1 = test_object1
    element2 = test_object2
    element3 = test_object3
    element4 = test_object4
    element5 = test_object5
    if element1 and element2 and element3 and element4 and element5:
        return True
    else:
        return False


def remove_cookies():
    print('placeholder')
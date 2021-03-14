import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" #work
#link = "http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/" #does not work

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    try:
        button = browser.find_element_by_css_selector("#add_to_basket_form > .btn-add-to-basket")
        button.click()
    except NoSuchElementException:
        assert False, print("Dont find button add to basket")

    #else:
        #button = browser.find_element_by_css_selector("#add_to_basket_form > .btn-add-to-basket")

    # button = browser.find_element_by_css_selector("#add_to_basket_form > .btn-add-to-basket")
    # button.click()
    # time.sleep(5)
    # assert browser.find_element_by_css_selector("#add_to_basket_form > .btn-add-to-basket") < 1
    #result = browser.find_element_by_class_name("alertinner ").text
    #assert "Coders at Work" in result, print("Not added to basket")

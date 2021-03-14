import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_check_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    button.click()
    time.sleep(5)
    result = browser.find_element_by_class_name("alertinner ").text
    assert "Coders at Work" in result, print(result)
#    browser.find_element_by_css_selector("#login_link")

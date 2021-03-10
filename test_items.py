link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_check_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    button.click()
    result = browser.find_element_by_class_name("alertiner").text
    assert "Coders at Work" in result, print(result)
#    browser.find_element_by_css_selector("#login_link")

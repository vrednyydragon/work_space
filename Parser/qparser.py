from selenium import webdriver

class ProgHubParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        '''Вызов этого метода запускает парсер'''
        self.go_to_tests_page()

    def go_to_tests_page(self):
        self.driver.get("https://proghub.ru/tests")
        elems = self.driver.find_elements_by_tag_name('a')

        for elem in elems:
            # print(elem.get_attribute("href"))
            lang_link = elem.get_attribute("href")
            print(lang_link)
            if self.lang in lang_link:
                language = lang_link.split("/")[-1]
                print(language)
                self.driver.get("https://proghub.ru/q/554428")
                break

def main():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, "python")
    parser.parse()
    return driver


# def main():
#     """создаем обьект селениум, через который будем взаимодействовать с браузером."""
#     # webdriver.Chrome() # вызвали браузер и больше ничего. он закрылся
#     driver = webdriver.Chrome()
#     driver.get("https://proghub.ru")
#     # btn_elem = driver.find_element_by_class_name("btn-primary")
#     # print(btn_elem)  # получили элемент
#     # btn_elem.click()  # нажать на кнопку
#     text_h1 = driver.find_element_by_tag_name("h1")
#     print(text_h1.text)
#     return driver  # возвращаем ссылку, чтобы не закрывался браузер

# чтоб не запускался код, который нам не нужен
if __name__ == '__main__':
    tmp = main()

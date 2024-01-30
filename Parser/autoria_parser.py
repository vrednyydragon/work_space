from selenium import webdriver
import csv
from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CarParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang


def main():
    driver = webdriver.Chrome()
    #driver.get("https://auto.ria.com/uk/legkovie/?page=1")
    # driver.get("https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&spareParts=0&confiscated=0&options.id[0]=189&options.id[1]=104&page=0&size=100")
    # driver.get("https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.USD.lte=10000&price.currency=1&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&spareParts=0&confiscated=0&options.id[0]=189&options.id[1]=104&page=212&size=100")
    filename = f'myfile_{datetime.now().strftime("%d%m%Y_%H%M%S")}.csv'
    i = 344
    while i <= 600:
        # time.sleep(5)
        delay = 5  # seconds
        driver.get(f"https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.USD.lte=10000&price.currency=1&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&spareParts=0&confiscated=0&options.id[0]=189&options.id[1]=104&page={i}&size=100")
        try:
            # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'content')))
            # myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
            print(f"Page {i} is ready!")
        except TimeoutException:
            print(f"Loading took too much time!, page {i}")
            continue
        car_block = driver.find_elements_by_class_name("content")
        car_info_csv_list = []
        for elem in car_block:
            car_name_obj = elem.find_element_by_class_name("address")
            # print(car_name_obj.text)
            car_name = car_name_obj.find_element_by_class_name("blue").text
            car_link = car_name_obj.get_attribute("href")
            car_id = car_link[-13:-5:1]
            # print(car_link, car_id)
            # print(f'car_name = {car_name}')
            car_year = car_name_obj.text[-4:]
            # print(f'car_year = {car_year}')
            price_obj = elem.find_element_by_class_name("price-ticket")
            price_value = price_obj.get_attribute("data-main-price")
            price_currency = price_obj.get_attribute("data-main-currency")
            # print(f'price = {price_value}, currency = {price_currency}')
            date_of_add_list = elem.find_elements_by_tag_name("span")
            car_date = 0
            for date in date_of_add_list:
                if date.get_attribute("data-update-date"):
                    car_date = date.get_attribute("data-update-date")
            car_mileage = elem.find_element_by_class_name('js-race').text
            # print(f"car_mileage = {car_mileage}")
            if price_value is not None:
                # print(f'{car_name} \t {car_year}\t {price_value}\t {price_currency}\t {car_date}\t {car_mileage}')
                # str_to_file = f'{car_name} \t {car_year}\t {price_value}\t {price_currency}\t {car_date}\t {car_mileage}'
                data = [car_name, car_year, price_value, price_currency, car_date, car_mileage, car_link, car_id]
                car_info_csv_list.append(data)
        # print(car_info_csv_list)
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(car_info_csv_list)
            print(f"{i} - Writing complete")
        btn_next = driver.find_element_by_class_name("js-next")
        next_page_link = btn_next.get_attribute("href")
        # print(next_page_link)
        # driver.get(next_page_link)
        i += 1
    return driver


if __name__ == '__main__':
    tmp = main()

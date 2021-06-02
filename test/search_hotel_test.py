from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://e-nocleg.pl/")
driver.find_element_by_id("basic-location").click()
driver.find_element_by_id("basic-location").send_keys("Zakopane")
driver.find_element_by_xpath("/html/body/ul/li/p").click()
driver.find_element_by_id("basic-date_start").send_keys("2021-06-05")
driver.find_element_by_id("basic-date_end").send_keys("2021-06-10")
driver.find_element_by_id("basic-guest").click()
driver.find_element_by_xpath("/html/body/div[2]/section[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div/div/select/option[2]").click()
driver.find_element_by_id("basic-search_button").click()

hotels = driver.find_elements_by_xpath("//div[contains(@class,'details')]//h3//a")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)

prices = driver.find_elements_by_xpath("//div[contains(@class,'price')]//span")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Cena to: " + price)


assert hotel_names[0] == 'Grand Podhale Resort&Spa*** - Noclegi Zakopane'
assert price_values[0] == '750'

driver.quit()

class SearchHotelLocators:

    search_hotel_id = "basic-location"
    search_hotel_input = "basic-location"
    location_match = "/html/body/ul/li/p"
    check_in_input = "basic-date_start"
    check_out_input = "basic-date_end"
    travellers_input_id = "basic-guest"
    person_input_xpath = "/html/body/div[2]/section[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div/div/select/option[2]"
    search_button_xpath = "basic-search_button"

class SearchResultLocators:

    hotel_names_xpath = "//div[contains(@class,'details')]//h3//a"
    hotel_prices_xpath = "//div[contains(@class,'price')]//span"


class TestData:
    CHROME_EXECUTEABLE_PATH = r"C:\Users\Weronika\OWASP ZAP\webdriver\windows\32"
    FIREFOX_EXECUTEABLE_PATH = r"C:\Users\Weronika\Desktop\Aplikacje-testowanie\testowanie aplikacji mobilnych\Katalon_Studio_Windows_64\configuration\resources\drivers\firefox_win64\geckodriver"


    BASE_URL = "https://panel.e-nocleg.pl/login"
    USER_NAME = "zaliczenie@gmail.com"
    USER_PASSWORD = "Uczelnia123!"

    LOGIN_PAGE_TITLE = "https://panel.e-nocleg.pl/login"
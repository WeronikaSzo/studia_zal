import pytest
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_hotel import SearchHotelPage
from pages.search_results import SearchResultPage


class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("https://e-nocleg.pl/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Zakopane")
        search_hotel_page.set_date_range("2021-06-25", "2021-06-30")
        search_hotel_page.set_travellers("2")
        search_hotel_page.perform_search()

        results_page = SearchResultPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        hotel_prices = results_page.get_hotel_prices()

        assert hotel_names[0] == 'Grand Podhale Resort&Spa*** - Noclegi Zakopane'
        assert hotel_prices[0] == '70'

#Testy strony internetowej
####Wstęp
Test zostały przeprowadzone na stronie www.e-nocleg.pl. Testy zostały napisane przy w języku Python z użyciem narzędzia Selenium.
Podjęto próbę napisania testów zgodnie ze wzorcem projektowym Page Object Pattern.
####O stronie
E-nocleg jest to ogólnopolska Baza Noclegowa. Na stronie można znaleźć nocleg w różnych częściach Polski.

####Środowisko testowe, dane konfiguracyjne

    *  Windows 10
    *  Intel Core i7, 2.70GHz, 2.90GHz
    *  Procesor x64

|Pycharm      |    Python     |   Selenium   | WebDriver | Przeglądarka Chrome |           
|:-----------: |: ------------- :|: -------------:|: ----------:|: -------------:| 
    2019.3   |   Python 3.8  |    3.141.59  |91.0.4472.19| 91.0.4472.77       |

#### Klasy

* locators
    * locators.py - potrzebne dane do wykonania testu z szukaniem hotelu
    * LoginPage.py - potrzebne dane do wykonania testu z logowaniem
    
* pages
    * login_up - zawiera metody potrzebne do wykonania testu logowania
    * search_hotel - zawiera metody potrzebne do wykonania testu z szukaniem hotelu
    * search_result - zawiera metody potrzebne do porównania wyszukań
    
* test - zawiera testy, które nie zostały napisane zgodnie ze wzorcem Page Object Pattern   

* tests
    * test_hotel_search - testy związane z wyszukiwaniem hotelu
    * test_loginPage - test związany z logowaniem
  
 #### Przypadki testowe
 
 1. test_hotel_search
    * Tytuł: Wyszukanie hotelu i sprawdzenie czy nazwa i cena pierwszego obiektu jest zgodna z wprowadzoną
    
    * Warunki wstępne: 
        * Użytkownik posiada dostęp do sieci
    * Dane:
        * nazwa pierwszego wyszukanego hotelu
        * data zameldowania
        * data wymeldowania
        * cena pierwszego wyszukanego hotelu
        
    * Kroki:
    
        * Wejście na stronę
        * Wpisanie w celu podróży: Zakopane
        * Wybranie z rozwijanej listy pierwszego wyszukania
        * Wprowadzenie daty zameldowania [w teście 2021-06-25]
        * Wprowadzenie daty wymeldowania [w teście 2021-06-30]
        * Kliknięcie okienka z wyborem liczby osób
        * Wybranie z rozwijanej listy, dowolnej liczby osób [w teście 2 osoby]
        * Kliknięcie przycisku "Szukaj"
        
     * Oczekiwany rezultat:
        * W terminalu zostaną wyświetlone wszystkie dostępne na pierwszej stronie hotele i ich ceny. Nazwa i cena zgadzają pierwszego wyszukania zgadza się z tym co uzyskano w trakcie testu.
        
    _____________________________________________________-   
     
 2. test_loginPage
     
     **<u>test_signup_link_visible</u>**
     *  Tytuł: Sprawdzenie czy na stronie znajduję się przycisk "Zarejestruj się"
     
     * Warunki wstępne:
       * Użytkownik posiada dostęp do sieci
     * Kroki:
        * Wejście na stronę do logowania
        * Sprawdzenie czy załadował się przycisk "Zarejestruj"
        
     * Rezultat:
        * Na stronie znajduje się przycisk "Zarejestruj"        
           
      **<u>02_test_login_page_title</u>**
      *  Tytuł: Sprawdzenie czy strona nie ma tytułu
     
     * Warunki wstępne:
       * Użytkownik posiada dostęp do sieci
     
      * Kroki:
        * Wejście na stronę do logowania
        * Sprawdzenie czy tytuł istnieje
        
     * Rezultat:
        * Tytuł strony nie istnieje
      
      **<u>03_test_signup_link_visible</u>**
      *  Tytuł: Logowanie się do serwisu
     
     * Warunki wstępne:
       * Użytkownik posiada dostęp do sieci
     * Dane wejściowe:
        * Email i hasło, które nie są zarejestrowane w systemie
     * Kroki:
        * Wejście na stronę do logowania
        * Kliknięcie w pole do wpisywania maila
        * Wpisanie maila
        * Kliknięcie w  pole do wpisywania hasła
        * Wpisanie hasła
        * Kliknięcie przycisku zaloguj
        
     * Rezultat:
        * Użytkownik nie zostaje zarejestrowany do serwisu  
    
      
    
      
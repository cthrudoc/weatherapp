14.04.2024 | 19:50 | #1

Polecenie : 
    Zrób apikacje pogodową w flasku gdzie, w zależności od pogody (deszcz, zachmurzenie, słonecznie itp) zmienia się obrazek na stronie, 
    po zmianie obrazku przechodzimy do następnej strony gdzie są pozostałe informacje pogodowe np. siła wiatru, temperatura itp.

    Obrazek ma być klikalny --> szczególniejsze informacje 

    tip : 
    from flask import request (request.method)
    from flask import jsonify
    w app py na początku będzie ściągał się cały Json, ogarnąć formularze GET i POST na razie na stałe (szerokość i długość geograficzna) 

Komentarz : 

    - Łącznie 6 godzin roboty, ale nie zrobiłem nic z CSS.
    - Nie jest potrzebne pobieranie żadnych dodatkowych bibliotek oprócz flaska.
      Urllib użyte do wywoływania API jest zawarte w Pythonie.   
    - Nie użyłem ani POST/GET, ani jsonify. Albo zrobiłem coś źle, albo inną drogą.
      Chyba że chodzi o to, żeby w aplikacji na przykład dało się wybierać miasto/
      współżędne geograficzne. Wtedy byłoby potrzebne. Da się zrobić. 

To do : 

1.  Strona nie ma nawet pliku CSS. Ogarnąć wizualnie : czcionka, np wyśrodkować tekst
    na obrazku, może animację strzelić po kliknięciu żeby pokazać szczegóły. 
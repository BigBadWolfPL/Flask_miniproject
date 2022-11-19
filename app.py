from flask import Flask, render_template, url_for, request

app = Flask(__name__)

#@app.route('/')
#def index():

#    return "This is index"

@app.route('/', methods=['GET', 'POST']) # FUNKCJA EXCHANGE ZOSTAŁA WYWOŁANA PRZY POMOCY METODY POST
def exchange():                          # J.W

    # WYŚWIETLENIE FORMULARZA:
    if request.method == 'GET':                           # W zależności od tego czy pracujemy z metodą GET czy POST wyśle jeden lub drugi plik html.
        return render_template("exchange.html")           # Funkcja zwraca wygenerowany tamplate html (i wyświetla go jako główny template???)
    
    # WCZYTANIE CURRENCY I AMOUNT Z DANYCH WPROWADZONYCH W FORMULARZU
    else:
        currency = 'EUR'                                  # to bedzie wartość jeśli if poniżej = False (czyli wartość domyślna)
        if 'currency' in request.form:                    # natomiast jesli 'currency' bedzie również w danych formularza html w sekcji?? <form></form> to zamienię dane na takie jakie przyszły w formularzu np PLN
            currency = request.form['currency']           # tu pobierane dane o wyborze uzytkownika, currency nad if jest nadpisana?
        
        amount = 100                                      # Domyślnie 100
        if 'amount' in request.form:                      # ale jeśli coś przyszło w formularzu to podstawiam wartość na tą z formularza.
            amount = request.form['amount']               # j.w
        # RENDEROWANIE TAMPLATU ( jaki plik połączyć z jakimi zmiennymi)
        return render_template("exchange_results.html", currency=currency, amount=amount) # currency które jest znane w szablonie ma przyjąć wratość currency ktore jest znane w skrypcie (tutaj w kodzie tej funkcji).
                                                          # zwracamy wygenerowane dane w nowym szablonie (exchange_results.html)
                                                          # trzeba wskazać funkcji render_template że pewne części w szablonie exchange_results.html należy zamienić wartościami
                                                          # znajdującymi się w funkcji exchange.

if __name__ == '__main__':
    app.run()
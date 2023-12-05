from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to fetch exchange rates from the API
def get_exchange_rates():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    return data['rates']

@app.route('/', methods=['GET', 'POST'])
def index():
    # Fetch exchange rates
    exchange_rates = get_exchange_rates()

    if request.method == 'POST':
        # Get user input
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        # Convert the amount
        rate_from = exchange_rates[from_currency]
        rate_to = exchange_rates[to_currency]
        converted_amount = amount * (rate_to / rate_from)

        return render_template('index.html', exchange_rates=exchange_rates, converted_amount=converted_amount,
                               from_currency=from_currency, to_currency=to_currency, amount=amount)

    return render_template('index.html', exchange_rates=exchange_rates)


if __name__ == '__main__':
    app.run(debug=True)




#from flask import Flask, request

#app = Flask(__name__)

#from_currency = str(
    #input("Enter the currency you want to convert from")).upper()

#to_currency = str(
    #input("Enter the currency you want to convert to")).upper()

#amount = float(input("enter in the amout of money"))

#response = request.get(
    #f"https://api.exchangerate.host/latest?amount={amount}&from={from_currency}&to={to_currency}")

#print(
    #f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
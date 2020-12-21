#importo librerías
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

# descargo dataframe de las 3 criptomonedas
data = yf.download("BTC-USD ETH-USD XRP-USD", period="5y")

#imprimo la informacion
print(data)

# grafico
plt.plot(data["Close"]["BTC-USD"], 'r-', label="BTC-USD")
plt.plot(data["Close"]["ETH-USD"], 'g-', label="ETH-USD")
plt.plot(data["Close"]["XRP-USD"], 'b-', label="XRP-USD")

# Le agrego informacion al grafico
plt.xlabel("Date")
plt.ylabel("USD")
plt.title("Close Prices")
plt.legend(loc='upper left')

# Muestro el gráfico
plt.show()
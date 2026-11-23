# Download monthly adjusted closing prices from Yahoo Finance
import yfinance as yf

tickers = ["ASML.AS", "MC.PA", "SAP.DE", "SIE.DE", "TTE.PA", "MT.AS"]
names = {"ASML.AS": "ASML", "MC.PA": "LVMH", "SAP.DE": "SAP",
         "SIE.DE": "Siemens", "TTE.PA": "TotalEnergies", "MT.AS": "ArcelorMittal"}

# Daily adjusted prices, December 2020 to December 2025
daily = yf.download(tickers, start="2020-12-01", end="2026-01-01", auto_adjust=True)["Close"]

# Keep the last price of each month and rename the columns
monthly = daily.resample("ME").last()
monthly = monthly.rename(columns=names)

# Export to Excel
monthly.to_excel("prices_monthly.xlsx")
print(monthly.shape)
print(monthly.head())

import yfinance as yf

stonk = yf.Ticker("tsla")
print(stonk.info)

# get stock info
# print(stonk.info)

# # get historical market data
# hist = stonk.history(period="max")

# # show actions (dividends, splits)
# stonk.actions

# # show dividends
# stonk.dividends

# # show splits
# stonk.splitsp

# # show financials
# stonk.financials
# stonk.quarterly_financials

# # show major holders
# stonk.major_holders

# # show institutional holders
# stonk.institutional_holders

# # show balance heet
# stonk.balance_sheet
# stonk.quarterly_balance_sheet

# # show cashflow
# stonk.cashflow
# stonk.quarterly_cashflow

# # show earnings
# stonk.earnings
# stonk.quarterly_earnings

# # show sustainability
# stonk.sustainability

# # show analysts recommendations
# stonk.recommendations

# # show next event (earnings, etc)
# stonk.calendar

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# stonk.isin

# # show options expirations
# stonk.options

# # get option chain for specific expiration
# opt = stonk.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts
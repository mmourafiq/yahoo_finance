yahoo_finance
=============

Provides a python interface to yahoo finance to get stock related data

YahooFinance : object that executes queries and returns set of quotes data of stocks, indices or currency exchanges

Usage:

1 - Getting latest quotes for a set of symbols comma separated
----------------------------------------------

The full list of fields follows:

        get_all_quotes(self, symbols)
        get_name(self, symbols)
        get_previous_close(self, symbols)
        get_market_capitalization(self, symbols) 
        get_high_limit(self, symbols)        
        get_annualized_gain(self, symbols)
        get_ask(self, symbols)
        get_bid(self, symbols)
        get_ask_size(self, symbols)
        get_bid_size(self, symbols)
        get_price(self, symbols)
        get_change(self, symbols)
        get_volume(self, symbols)
        get_avg_daily_volume(self, symbols)
        get_stock_exchange(self, symbols)
        get_market_cap(self, symbols)
        get_book_value(self, symbols)
        get_ebitda(self, symbols)
        get_dividend_per_share(self, symbols)
        get_dividend_yield(self, symbols)
        get_earnings_per_share(self, symbols)
        get_earnings_per_share_estimation_year(self, symbols)
        get_52_week_high(self, symbols)
        get_52_week_low(self, symbols)
        get_50day_moving_avg(self, symbols)
        get_200day_moving_avg(self, symbols)
        get_price_earnings_ratio(self, symbols)
        get_price_earnings_growth_ratio(self, symbols)
        get_price_sales_ratio(self, symbols)
        get_price_book_ratio(self, symbols)
        get_short_ratio(self, symbols)


2 - Getting historical quotes
-----------------------------

Here you can specify a date range and a symbols, and retrieve historical data for it. 
The period can be specified as daily, monthly, weekly or dividends_only

get_historical_prices(self, symbols, s_day, s_month, s_year, e_day, e_month, e_year, frequency)

yahoo_finance
=============

Provides a python interface to yahoo finance to get stock related data

YahooFinance : object that executes queries and returns set of quotes data of stocks, indices or currency exchanges

Usage:

1 - Getting latest quotes for a set of symbols comma separated
----------------------------------------------

The full list of possible quotes follows:

        get_all_quotes(self)
        get_name(self)
        get_previous_close(self)
        get_market_capitalization(self) 
        get_high_limit(self)        
        get_annualized_gain(self)
        get_ask(self)
        get_bid(self)
        get_ask_size(self)
        get_bid_size(self)
        get_price(self)
        get_change(self)
        get_volume(self)
        get_avg_daily_volume(self)
        get_stock_exchange(self)
        get_market_cap(self)
        get_book_value(self)
        get_ebitda(self)
        get_dividend_per_share(self)
        get_dividend_yield(self)
        get_earnings_per_share(self)
        get_earnings_per_share_estimation_year(self)
        get_52_week_high(self)
        get_52_week_low(self)
        get_50day_moving_avg(self)
        get_200day_moving_avg(self)
        get_price_earnings_ratio(self)
        get_price_earnings_growth_ratio(self)
        get_price_sales_ratio(self)
        get_price_book_ratio(self)
        get_short_ratio(self)


2 - Getting historical quotes
-----------------------------

Here you can specify a date range and a symbols, and retrieve historical data for it. 

The period can be specified as daily, monthly, weekly or dividends_only:
        
        get_historical_prices(self, start_date, end_date, frequency='d')

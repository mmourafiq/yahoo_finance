# -*- coding: utf-8 -*-
'''
Created on Dec 01, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
import urllib2
import re

base_url_quotes = "http://finance.yahoo.com/d/quotes.csv?"
base_url_historical = "http://ichart.yahoo.com/table.csv?"

class YahooFinance(object):
    """
        YahooF object that executes queries and returns set of quotes data of stocks, indices or currency exchanges
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
        get_historical_prices(self, start_date, end_date, frequency='d')          
    """
    def __init__(self, symbols):        
        self.symbols = set(re.findall('\w+', symbols))        
    
    def get_symbols(self):
        return '+'.join(self.symbols)
    
    def get_plain_symbols(self):
        return self.symbols
    
    def add_symbol(self, symbol):
        self.symbols.add(symbol)
        
    def remove_symbol(self, symbol):
        self.symbols.remove(symbol)
    
    def __quote_for_symbols(self, quote):        
        #symbols
        symbols = "s=%(symbols)s" % {"symbols":self.get_symbols()}          
        #quote
        quote = '&f=%(quote)s' % {"quote" : quote}
        url = base_url_quotes + symbols + quote
        return urllib2.urlopen(url).read().strip().strip('"')
    
    
    def get_all_quotes(self):
        """
        Get all available quote data for the given ticker symbols.
        
        Returns a dictionary.
        """
        values = self.__quote_for_symbols('l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7').split(',')
        data = {}
        data['price'] = values[0]
        data['change'] = values[1]
        data['volume'] = values[2]
        data['avg_daily_volume'] = values[3]
        data['stock_exchange'] = values[4]
        data['market_cap'] = values[5]
        data['book_value'] = values[6]
        data['ebitda'] = values[7]
        data['dividend_per_share'] = values[8]
        data['dividend_yield'] = values[9]
        data['earnings_per_share'] = values[10]
        data['52_week_high'] = values[11]
        data['52_week_low'] = values[12]
        data['50day_moving_avg'] = values[13]
        data['200day_moving_avg'] = values[14]
        data['price_earnings_ratio'] = values[15]
        data['price_earnings_growth_ratio'] = values[16]
        data['price_sales_ratio'] = values[17]
        data['price_book_ratio'] = values[18]
        data['short_ratio'] = values[19]
        return data
        
    def get_name(self):
        return self.__quote_for_symbols('n')
    
    def get_previous_close(self):
        return self.__quote_for_symbols('p0')
    
    def get_annualized_gain(self):
        return self.__quote_for_symbols('g3')
    
    def get_market_capitalization(self):
        return self.__quote_for_symbols('j1')
    
    def get_high_limit(self):
        return self.__quote_for_symbols('l2')    
    
    def get_ask(self):
        return self.__quote_for_symbols('a')
    
    def get_bid(self):
        return self.__quote_for_symbols('b')

    def get_ask_size(self):
        return self.__quote_for_symbols('a5')
    
    def get_bid_size(self):
        return self.__quote_for_symbols('b6')    
    
    def get_price(self): 
        return self.__quote_for_symbols('l1')
    
    
    def get_change(self):
        return self.__quote_for_symbols('c1')
        
        
    def get_volume(self): 
        return self.__quote_for_symbols('v')
    
    
    def get_avg_daily_volume(self): 
        return self.__quote_for_symbols('a2')
        
        
    def get_stock_exchange(self): 
        return self.__quote_for_symbols('x')
        
        
    def get_market_cap(self):
        return self.__quote_for_symbols('j1')
       
       
    def get_book_value(self):        
        return self.__quote_for_symbols('b4')
    
    
    def get_ebitda(self): 
        return self.__quote_for_symbols('j4')
        
        
    def get_dividend_per_share(self):
        return self.__quote_for_symbols('d')
    
    
    def get_dividend_yield(self): 
        return self.__quote_for_symbols('y')
        
        
    def get_earnings_per_share(self): 
        return self.__quote_for_symbols('e')
    
    def get_earnings_per_share_estimation_year(self): 
        return self.__quote_for_symbols('e7')
    
    def get_52_week_high(self): 
        return self.__quote_for_symbols('k')
        
        
    def get_52_week_low(self): 
        return self.__quote_for_symbols('j')
    
    
    def get_50day_moving_avg(self): 
        return self.__quote_for_symbols('m3')
        
        
    def get_200day_moving_avg(self): 
        return self.__quote_for_symbols('m4')
        
        
    def get_price_earnings_ratio(self): 
        return self.__quote_for_symbols('r')
    
    
    def get_price_earnings_growth_ratio(self): 
        return self.__quote_for_symbols('r5')
    
    
    def get_price_sales_ratio(self): 
        return self.__quote_for_symbols('p5')
        
        
    def get_price_book_ratio(self): 
        return self.__quote_for_symbols('p6')
           
           
    def get_short_ratio(self): 
        return self.__quote_for_symbols('s7')
        
        
    def get_historical_prices(self, start_date, end_date, frequency='d'):
        """
        Get historical prices for the given ticker symbols.
        symbols : ticker symbols
        start_date , end_date : YYYYMMDD format
        s_day, s_month, s_year : start day, month, year
        e_day, e_month, e_year : end day, month, year
        frequency :
            daily : d
            weekly : w
            monthly : m
            dividend only : v
        
        Returns a nested list.
        """
        s_day = str(start_date[6:8])
        s_month = str(int(start_date[4:6]) - 1)
        s_year = str(start_date[0:4])
        e_day = str(end_date[6:8])
        e_month = str(int(end_date[4:6]) - 1)
        e_year = str(end_date[0:4])
        for symbol in self.get_plain_symbols():
            #symbol
            symbol = "s=%(symbols)s" % {"symbols":symbol}          
            #start date
            s_date = "&a=%(s_month)s&b=%(s_day)s&c=%(s_year)s" % {"s_day":s_day, 's_month':s_month, 's_year':s_year}
            #end date
            e_date = "&d=%(e_month)s&e=%(e_day)s&f=%(e_year)s" % {"e_day":e_day, 'e_month':e_month, 'e_year':e_year}
            #frequency
            frequency = "&g=%(frequency)s" % {"frequency":frequency}
            url = base_url_historical + symbol + s_date + e_date + frequency
            url += '&ignore=.csv'
            days = urllib2.urlopen(url).readlines()
            data = [day[:-2].split(',') for day in days]
            yield (symbol, data)
    
if __name__ == "__main__":        
    yf = YahooFinance('GOOG,MSFT')
    print yf.get_symbols()    
    yf.add_symbol('AAPL')
    print yf.get_symbols()    
    yf.remove_symbol('GOOG')    
    print yf.get_symbols()         
    for d in yf.get_historical_prices('20120101', '20120201', 'w'):
        print d
    
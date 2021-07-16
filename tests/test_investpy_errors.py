# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

import investpy


def test_stocks_errors():
    """
    This function raises errors on stock retrieval functions.
    """

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_stocks(country=param['country'])
        except:
            pass

        try:
            investpy.get_stocks_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': 'spain',
            'columns': 0,
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_stocks_dict(country=param['country'],
                                     columns=param['columns'],
                                     as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'stock': 'FERR',
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': None,
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'greece',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'as_json': True,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'stock': 'error',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': ['error'],
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': None,
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error'],
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error',
        },
    ]

    for param in params:
        try:
            investpy.get_stock_recent_data(stock=param['stock'],
                                           country=param['country'],
                                           as_json=param['as_json'],
                                           order=param['order'],
                                           interval=param['interval'])
        except:
            pass

    params = [
        {
            'stock': 'FERR',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': None,
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'greece',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'error',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': ['error'],
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/1999',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/1950',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/01/1999',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_stock_historical_data(stock=param['stock'],
                                               country=param['country'],
                                               from_date=param['from_date'],
                                               to_date=param['to_date'],
                                               as_json=param['as_json'],
                                               order=param['order'],
                                               interval=param['interval'])
        except:
            pass

    params = [
        {
            'stock': None,
            'country': 'spain',
            'language': 'spanish'
        },
        {
            'stock': ['error'],
            'country': 'spain',
            'language': 'spanish'
        },
        {
            'stock': 'BBVA',
            'country': None,
            'language': 'spanish'
        },
        {
            'stock': 'BBVA',
            'country': ['error'],
            'language': 'spanish'
        },
        {
            'stock': 'BBVA',
            'country': 'greece',
            'language': 'spanish'
        },
        {
            'stock': 'ALPER',
            'country': 'france',
            'language': 'spanish'
        },
        {
            'stock': 'BBVA',
            'country': 'spain',
            'language': 'error'
        },
        {
            'stock': 'error',
            'country': 'spain',
            'language': 'spanish'
        },
        {
            'stock': ['error'],
            'country': 'spain',
            'language': 'spanish'
        },
    ]

    for param in params:
        try:
            investpy.get_stock_company_profile(stock=param['stock'],
                                               country=param['country'],
                                               language=param['language'])
        except:
            pass

    params = [
        {
            'stock': None,
            'country': 'spain',
        },
        {
            'stock': ['error'],
            'country': 'spain',
        },
        {
            'stock': 'bbva',
            'country': None,
        },
        {
            'stock': 'bbva',
            'country': ['error'],
        },
        {
            'stock': 'bbva',
            'country': 'error',
        },
        {
            'stock': 'error',
            'country': 'spain',
        },
        {
            'stock': 'ALUA',
            'country': 'argentina',
        },
    ]

    for param in params:
        try:
            investpy.get_stock_dividends(stock=param['stock'], country=param['country'])
        except:
            pass

    params = [
        {
            'stock': None,
            'country': 'spain',
            'as_json': False
        },
        {
            'stock': ['error'],
            'country': 'spain',
            'as_json': False
        },
        {
            'stock': 'bbva',
            'country': None,
            'as_json': False
        },
        {
            'stock': 'bbva',
            'country': ['error'],
            'as_json': False
        },
        {
            'stock': 'bbva',
            'country': 'spain',
            'as_json': None
        },
        {
            'stock': 'bbva',
            'country': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_stock_information(stock=param['stock'], country=param['country'], as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'country': 'error',
            'as_json': False,
            'n_results': 2
        },
        {
            'country': None,
            'as_json': False,
            'n_results': 2
        },
        {
            'country': ['error'],
            'as_json': False,
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': None,
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': ['error'],
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': False,
            'n_results': None
        },
        {
            'country': 'spain',
            'as_json': False,
            'n_results': 1001
        },
    ]

    for param in params:
        try:
            investpy.get_stocks_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'stock': None,
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': ['error'],
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': None,
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': ['error'],
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': None,
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': ['error'],
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': 'error',
            'period': 'quarterly'
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': None
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': ['error']
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': 'error'
        },
        {
            'stock': 'aapl',
            'country': 'error',
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': 'error',
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': 'quarterly'
        }
    ]

    for param in params:
        try:
            investpy.get_stock_financial_summary(stock=param['stock'],
                                                 country=param['country'], 
                                                 summary_type=param['summary_type'],
                                                 period=param['period'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'BBVA',
        },
        {
            'by': ['error'],
            'value': 'BBVA',
        },
        {
            'by': 'error',
            'value': 'BBVA',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'isin',
            'value': 'BBVA',
        },
    ]

    for param in params:
        try:
            investpy.search_stocks(by=param['by'], value=param['value'])
        except:
            pass


def test_funds_errors():
    """
    This function raises errors on fund retrieval functions.
    """

    params = [
        {
            'country': ['error'],
        },
    ]

    for param in params:
        try:
            investpy.get_funds(country=param['country'])
        except:
            pass

        try:
            investpy.get_funds_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'country': None,
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': None,
            'columns': 0,
            'as_json': True
        },
        {
            'country': None,
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_funds_dict(country=param['country'],
                                    columns=param['columns'],
                                    as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'fund': None,
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'germany',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': True,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'fund': 'error',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': ['error'],
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_fund_recent_data(fund=param['fund'],
                                          country=param['country'],
                                          as_json=param['as_json'],
                                          order=param['order'],
                                          interval=param['interval'])
        except:
            pass

    params = [
        {
            'fund': None,
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'germany',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'error',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': ['error'],
            'country': 'spain',
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/01/1998',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_fund_historical_data(fund=param['fund'],
                                              country=param['country'],
                                              from_date=param['from_date'],
                                              to_date=param['to_date'],
                                              as_json=param['as_json'],
                                              order=param['order'],
                                              interval=param['interval'])
        except:
            pass

    params = [
        {
            'fund': None,
            'country': 'spain',
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': None,
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': ['error'],
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'error',
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'germany',
            'as_json': False
        },
        {
            'fund': 'quality inversion conservadora fi',
            'country': 'spain',
            'as_json': 'error'
        },
        {
            'fund': 'error',
            'country': 'spain',
            'as_json': True
        },
        {
            'fund': ['error'],
            'country': 'spain',
            'as_json': True
        },
    ]

    for param in params:
        try:
            investpy.get_fund_information(fund=param['fund'],
                                          country=param['country'],
                                          as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'country': 'error',
            'as_json': False,
            'n_results': 2
        },
        {
            'country': None,
            'as_json': False,
            'n_results': 2
        },
        {
            'country': ['error'],
            'as_json': False,
            'n_results': 2
        },
        {
            'country': 'andorra',
            'as_json': None,
            'n_results': 2
        },
        {
            'country': 'andorra',
            'as_json': ['error'],
            'n_results': 2
        },
        {
            'country': 'andorra',
            'as_json': False,
            'n_results': None
        },
        {
            'country': 'spain',
            'as_json': False,
            'n_results': 1001
        },
    ]

    for param in params:
        try:
            investpy.get_funds_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass


    params = [
        {
            'by': None,
            'value': 'bbva',
        },
        {
            'by': ['error'],
            'value': 'bbva',
        },
        {
            'by': 'error',
            'value': 'bbva',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'isin',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_funds(by=param['by'], value=param['value'])
        except:
            pass
    

def test_etfs_errors():
    """
    This function raises errors on etf retrieval functions.
    """

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_etfs(country=param['country'])
        except:
            pass

        try:
            investpy.get_etfs_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': 'spain',
            'columns': 0,
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_etfs_dict(country=param['country'],
                                   columns=param['columns'],
                                   as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'etf': None,
            'country': 'spain',
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': ['error'],
            'country': 'spain',
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': None,
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'error',
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'netherlands',
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': ['error'],
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'etf': 'error',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': ['error'],
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': True,
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': 'error',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbvae',
            'country': 'spain',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
    ]

    for param in params:
        try:
            investpy.get_etf_recent_data(etf=param['etf'],
                                         country=param['country'],
                                         is_symbol=param['is_symbol'],
                                         as_json=param['as_json'],
                                         order=param['order'],
                                         interval=param['interval'])
        except:
            pass

    params = [
        {
            'etf': None,
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'error',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'netherlands',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': None,
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': ['error'],
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'error',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': ['error'],
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': '01/01/1998',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': True,
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbvae',
            'country': 'spain',
            'is_symbol': False,
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': 'error',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
    ]

    for param in params:
        try:
            investpy.get_etf_historical_data(etf=param['etf'],
                                             country=param['country'],
                                             is_symbol=param['is_symbol'],
                                             from_date=param['from_date'],
                                             to_date=param['to_date'],
                                             as_json=param['as_json'],
                                             order=param['order'],
                                             interval=param['interval'])
        except:
            pass

    params = [
        {
            'etf': None,
            'country': 'spain',
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': ['error'],
            'country': 'spain',
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': None,
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': ['error'],
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': False,
            'as_json': None
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'error',
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'country': 'spain',
            'is_symbol': True,
            'as_json': False
        },
        {
            'etf': 'bbvae',
            'country': 'spain',
            'is_symbol': False,
            'as_json': False
        },
        {
            'etf': 'bbvae',
            'country': 'spain',
            'is_symbol': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_etf_information(etf=param['etf'], country=param['country'], is_symbol=param['is_symbol'], as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'country': 'error',
            'as_json': False,
            'n_results': 2
        },
        {
            'country': None,
            'as_json': False,
            'n_results': 2
        },
        {
            'country': ['error'],
            'as_json': False,
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': None,
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': ['error'],
            'n_results': 2
        },
        {
            'country': 'spain',
            'as_json': False,
            'n_results': None
        },
        {
            'country': 'spain',
            'as_json': False,
            'n_results': 1001
        },
    ]

    for param in params:
        try:
            investpy.get_etfs_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'bbva',
        },
        {
            'by': ['error'],
            'value': 'bbva',
        },
        {
            'by': 'error',
            'value': 'bbva',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'isin',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_etfs(by=param['by'], value=param['value'])
        except:
            pass


def test_indices_errors():
    """
    This function raises errors on index retrieval functions.
    """

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_indices(country=param['country'])
        except:
            pass

        try:
            investpy.get_indices_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': 'spain',
            'columns': 0,
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_indices_dict(country=param['country'],
                                      columns=param['columns'],
                                      as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'index': None,
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': ['error'],
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'netherlands',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': True,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'index': 'error',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': ['error'],
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_index_recent_data(index=param['index'],
                                           country=param['country'],
                                           as_json=param['as_json'],
                                           order=param['order'],
                                           interval=param['interval'])
        except:
            pass

    params = [
        {
            'index': None,
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'netherlands',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'error',
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': ['error'],
            'country': 'spain',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/1998',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/01/1998',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_index_historical_data(index=param['index'],
                                               country=param['country'],
                                               from_date=param['from_date'],
                                               to_date=param['to_date'],
                                               as_json=param['as_json'],
                                               order=param['order'],
                                               interval=param['interval'])
        except:
            pass

    params = [
        {
            'index': None,
            'country': 'spain',
            'as_json': False
        },
        {
            'index': ['error'],
            'country': 'spain',
            'as_json': False
        },
        {
            'index': 'ibex 35',
            'country': None,
            'as_json': False
        },
        {
            'index': 'ibex 35',
            'country': ['error'],
            'as_json': False
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': None
        },
        {
            'index': 'error',
            'country': 'spain',
            'as_json': False
        },
        {
            'index': 'ibex 35',
            'country': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_index_information(index=param['index'], country=param['country'], as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'country': None, 
            'as_json': False,
            'n_results': 10
        },
        {
            'country': ['error'], 
            'as_json': False,
            'n_results': 10
        },
        {
            'country': 'spain', 
            'as_json': None,
            'n_results': 10
        },
        {
            'country': 'spain', 
            'as_json': False,
            'n_results': 'error'
        },
        {
            'country': 'spain', 
            'as_json': False,
            'n_results': 0
        },
        {
            'country': 'error', 
            'as_json': False,
            'n_results': 10
        },
    ]

    for param in params:
        try:
            investpy.get_indices_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'ibex',
        },
        {
            'by': ['error'],
            'value': 'ibex',
        },
        {
            'by': 'error',
            'value': 'ibex',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'name',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_indices(by=param['by'], value=param['value'])
        except:
            pass


def test_currency_crosses_errors():
    """
    This function raises errors on currency cross retrieval functions.
    """

    params = [
        {
            'base': ['error'],
            'second': None
        },
        {
            'base': None,
            'second': ['error']
        },
        {
            'base': 'error',
            'second': None
        },
        {
            'base': 'EUR',
            'second': 'error'
        },
        {
            'base': None,
            'second': 'error'
        },
        {
            'base': 'EUR',
            'second': 'EUR',
        }
    ]

    for param in params:
        try:
            investpy.get_currency_crosses(base=param['base'],
                                          second=param['second'])
        except:
            pass

        try:
            investpy.get_currency_crosses_list(base=param['base'],
                                               second=param['second'])
        except:
            pass

    params = [
        {
            'base': ['error'],
            'second': None,
            'columns': None,
            'as_json': False
        },
        {
            'base': None,
            'second': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'base': None,
            'second': None,
            'columns': None,
            'as_json': 'error'
        },
        {
            'base': None,
            'second': None,
            'columns': 'error',
            'as_json': False
        },
        {
            'base': None,
            'second': None,
            'columns': ['error'],
            'as_json': False
        },
        {
            'base': 'error',
            'second': None,
            'columns': None,
            'as_json': False
        },
        {
            'base': 'EUR',
            'second': 'error',
            'columns': None,
            'as_json': False
        },
        {
            'base': None,
            'second': 'error',
            'columns': None,
            'as_json': False
        },
        {
            'base': 'EUR',
            'second': 'Eur',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_currency_crosses_dict(base=param['base'],
                                               second=param['second'],
                                               columns=param['columns'],
                                               as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'currency_cross': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'error/error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_currency_cross_recent_data(currency_cross=param['currency_cross'],
                                                    as_json=param['as_json'],
                                                    order=param['order'],
                                                    interval=param['interval'])
        except:
            pass

    params = [
        {
            'currency_cross': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2017',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'error/error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_currency_cross_historical_data(currency_cross=param['currency_cross'],
                                                        from_date=param['from_date'],
                                                        to_date=param['to_date'],
                                                        as_json=param['as_json'],
                                                        order=param['order'],
                                                        interval=param['interval'])
        except:
            pass

    params = [
        {
            'currency': None,
            'as_json': False,
            'n_results': 100
        },
        {
            'currency': ['error'],
            'as_json': True,
            'n_results': 100
        },
        {
            'currency': 'eur',
            'as_json': 'error',
            'n_results': 100
        },
        {
            'currency': 'eur',
            'as_json': True,
            'n_results': 'error'
        },
        {
            'currency': 'eur',
            'as_json': True,
            'n_results': 0
        },
        {
            'currency': 'error',
            'as_json': True,
            'n_results': 10
        }
    ]
    
    for param in params:
        try:
            investpy.get_currency_crosses_overview(currency=param['currency'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'currency_cross': None,
            'as_json': False
        },
        {
            'currency_cross': ['error'],
            'as_json': False
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': None
        },
        {
            'currency_cross': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_currency_cross_information(currency_cross=param['currency_cross'], as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'EUR',
        },
        {
            'by': ['error'],
            'value': 'EUR',
        },
        {
            'by': 'error',
            'value': 'EUR',
        },
        {
            'by': 'base',
            'value': None,
        },
        {
            'by': 'base',
            'value': ['error'],
        },
        {
            'by': 'base',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_currency_crosses(by=param['by'], value=param['value'])
        except:
            pass


def test_bonds_errors():
    """
    This function raises errors on bond retrieval functions.
    """

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_bonds(country=param['country'])
        except:
            pass

        try:
            investpy.get_bonds_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': 'error'
        },
        {
            'country': 'spain',
            'columns': 0,
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_bonds_dict(country=param['country'],
                                    columns=param['columns'],
                                    as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'bond': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'as_json': True,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'bond': 'error',
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': ['error'],
            'as_json': True,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'as_json': True,
            'order': 'ascending',
            'interval': None
        },
        {
            'bond': 'Argentina 3Y',
            'as_json': True,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'bond': 'Argentina 3Y',
            'as_json': True,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_bond_recent_data(bond=param['bond'],
                                          as_json=param['as_json'],
                                          order=param['order'],
                                          interval=param['interval'])
        except:
            pass

    params = [
        {
            'bond': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2019',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/1999',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/1950',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2019',
            'to_date': '01/01/1999',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'bond': 'Argentina 3Y',
            'from_date': '01/01/2019',
            'to_date': '01/03/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_bond_historical_data(bond=param['bond'],
                                              from_date=param['from_date'],
                                              to_date=param['to_date'],
                                              as_json=param['as_json'],
                                              order=param['order'],
                                              interval=param['interval'])
        except:
            pass

    params = [
        {
            'bond': None,
            'as_json': False
        },
        {
            'bond': ['error'],
            'as_json': False
        },
        {
            'bond': 'argentina 3y',
            'as_json': None
        },
        {
            'bond': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_bond_information(bond=param['bond'], as_json=param['as_json'])
        except:
            pass
    
    params = [
        {
            'country': None,
            'as_json': False,
        },
        {
            'country': ['error'],
            'as_json': False,
        },
        {
            'country': 'spain',
            'as_json': None,
        },
        {
            'country': 'error',
            'as_json': False,
        }
    ]

    for param in params:
        try:
            investpy.get_bonds_overview(country=param['country'], as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'Argentina',
        },
        {
            'by': ['error'],
            'value': 'Argentina',
        },
        {
            'by': 'error',
            'value': 'Argentina',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'name',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_bonds(by=param['by'], value=param['value'])
        except:
            pass


def test_commodities_errors():
    """
    This function raises errors on commodity retrieval functions.
    """

    params = [
        {
            'group': ['error']
        },
        {
            'group': 'error'
        },
    ]

    for param in params:
        try:
            investpy.get_commodities(group=param['group'])
        except:
            pass

        try:
            investpy.get_commodities_list(group=param['group'])
        except:
            pass

    params = [
        {
            'group': ['error'],
            'columns': None,
            'as_json': False
        },
        {
            'group': 'error',
            'columns': None,
            'as_json': False
        },
        {
            'group': 'metals',
            'columns': None,
            'as_json': 'error'
        },
        {
            'group': 'metals',
            'columns': 0,
            'as_json': True
        },
        {
            'group': 'metals',
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_commodities_dict(group=param['group'],
                                          columns=param['columns'],
                                          as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'commodity': None,
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': ['error'],
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': False,
            'order': 'error',
            'interval': 'Daily',
        },
        {
            'commodity': 'chocolate',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': None,
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': ['error'],
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'error',
        },
        {
            'commodity': 'copper',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'country': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        }
    ]

    for param in params:
        try:
            investpy.get_commodity_recent_data(commodity=param['commodity'],
                                               country=param['country'],
                                               as_json=param['as_json'],
                                               order=param['order'],
                                               interval=param['interval'])
        except:
            pass

    params = [
        {
            'commodity': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'error',
            'interval': 'Daily',
        },
        {
            'commodity': 'chocolate',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': 'error',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/1999',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/1900',
            'to_date': '01/01/1950',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/1950',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2019',
            'to_date': '01/01/1999',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': None,
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': ['error'],
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'error',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'commodity': 'copper',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'country': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        }
    ]

    for param in params:
        try:
            investpy.get_commodity_historical_data(commodity=param['commodity'],
                                                   from_date=param['from_date'],
                                                   to_date=param['to_date'],
                                                   country=param['country'],
                                                   as_json=param['as_json'],
                                                   order=param['order'],
                                                   interval=param['interval'])
        except:
            pass

    params = [
        {
            'commodity': None,
            'country': None,
            'as_json': False
        },
        {
            'commodity': ['error'],
            'country': None,
            'as_json': False
        },
        {
            'commodity': 'copper',
            'country': ['error'],
            'as_json': False
        },
        {
            'commodity': 'copper',
            'country': None,
            'as_json': None
        },
        {
            'commodity': 'error',
            'country': None,
            'as_json': False
        },
        {
            'commodity': 'copper',
            'country': 'error',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_commodity_information(commodity=param['commodity'], country=param['country'], as_json=param['as_json'])
        except:
            pass
    
    params = [
        {
            'group': None,
            'as_json': True,
            'n_results': 100
        },
        {
            'group': ['error'],
            'as_json': True,
            'n_results': 100
        },
        {
            'group': 'metals',
            'as_json': None,
            'n_results': 100
        },
        {
            'group': 'metals',
            'as_json': True,
            'n_results': 'error'
        },
        {
            'group': 'metals',
            'as_json': True,
            'n_results': 0
        },
        {
            'group': 'error',
            'as_json': True,
            'n_results': 10
        },
    ]

    for param in params:
        try:
            investpy.get_commodities_overview(group=param['group'], as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'silver',
        },
        {
            'by': ['error'],
            'value': 'silver',
        },
        {
            'by': 'error',
            'value': 'silver',
        },
        {
            'by': 'name',
            'value': None,
        },
        {
            'by': 'name',
            'value': ['error'],
        },
        {
            'by': 'name',
            'value': 'error',
        },
    ]

    for param in params:
        try:
            investpy.search_commodities(by=param['by'], value=param['value'])
        except:
            pass


def test_crypto_errors():
    """
    This function raises errors on crypto retrieval functions.
    """

    params = [
        {
            'columns': None,
            'as_json': None
        },
        {
            'columns': 'error',
            'as_json': False
        },
        {
            'columns': ['error'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_cryptos_dict(columns=param['columns'],
                                      as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'crypto': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'crypto': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'crypto': 'bitcoin',
            'as_json': None,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'crypto': 'bitcoin',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'crypto': 'bitcoin',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'crypto': 'bitcoin',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'crypto': 'bitcoin',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
        {
            'crypto': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'crypto': 'Single Collateral DAI',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
    ]

    for param in params:
        try:
            investpy.get_crypto_recent_data(crypto=param['crypto'],
                                            as_json=param['as_json'],
                                            order=param['order'],
                                            interval=param['interval'])
        except:
            pass

    params = [
        {
            'crypto': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': None,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily',
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None,
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error'],
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error',
        },
        {
            'crypto': 'bitcoin',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2018',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'bitcoin',
            'from_date': '01/01/2019',
            'to_date': '01/01/2018',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
        {
            'crypto': 'Single Collateral DAI',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily',
        },
    ]

    for param in params:
        try:
            investpy.get_crypto_historical_data(crypto=param['crypto'],
                                                from_date=param['from_date'],
                                                to_date=param['to_date'],
                                                as_json=param['as_json'],
                                                order=param['order'],
                                                interval=param['interval'])
        except:
            pass

    params = [
        {
            'crypto': None,
            'as_json': False
        },
        {
            'crypto': ['error'],
            'as_json': False
        },
        {
            'crypto': 'bitcoin',
            'as_json': None
        },
        {
            'crypto': 'error',
            'as_json': False
        },
        {
            'crypto': 'single collateral dai',
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_crypto_information(crypto=param['crypto'], as_json=param['as_json'])
        except:
            pass
    
    params = [
        {
            'as_json': None,
            'n_results': 10
        },
        {
            'as_json': False,
            'n_results': 'error'
        },
        {
            'as_json': False,
            'n_results': 0
        },
    ]

    for param in params:
        try:
            investpy.get_cryptos_overview(as_json=param['as_json'], n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'bitcoin'
        },
        {
            'by': 'error',
            'value': 'bitcoin'
        },
        {
            'by': ['error'],
            'value': 'bitcoin'
        },
        {
            'by': 'name',
            'value': None
        },
        {
            'by': 'name',
            'value': ['error']
        },
        {
            'by': 'symbol',
            'value': 'error'
        },
    ]

    for param in params:
        try:
            investpy.search_cryptos(by=param['by'], value=param['value'])
        except:
            pass


def test_certificate_errors():
    """
    This function raises errors on certificate retrieval functions.
    """

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        }
    ]

    for param in params:
        try:
            investpy.get_certificates(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error']
        },
        {
            'country': 'error'
        }
    ]

    for param in params:
        try:
            investpy.get_certificates_list(country=param['country'])
        except:
            pass

    params = [
        {
            'country': ['error'],
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'france',
            'columns': ['full_name', 'name'],
            'as_json': 'error'
        },
        {
            'country': 'france',
            'columns': 'error',
            'as_json': False
        },
        {
            'country': 'france',
            'columns': ['error'],
            'as_json': False
        },
        {
            'country': 'error',
            'columns': ['full_name', 'name'],
            'as_json': False
        },
    ]

    for param in params:
        try:
            investpy.get_certificates_dict(country=param['country'],
                                           columns=param['columns'],
                                           as_json=param['as_json'])
        except:
            pass

    params = [
        {
            'certificate': None,
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': ['error'],
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': None,
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': ['error'],
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': 'error',
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'spain',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'error',
            'country': 'france',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        }
    ]

    for param in params:
        try:
            investpy.get_certificate_recent_data(certificate=param['certificate'],
                                                 country=param['country'],
                                                 as_json=param['as_json'],
                                                 order=param['order'],
                                                 interval=param['interval'])
        except:
            pass
        
    params = [
        {
            'certificate': None,
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': ['error'],
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': None,
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': ['error'],
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': None,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'error',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': None
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': ['error']
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'error'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': 'error',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': 'error',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/2019',
            'to_date': '01/01/2018',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'from_date': '01/01/1990',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'error',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        },
        {
            'certificate': 'error',
            'country': 'france',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'ascending',
            'interval': 'Daily'
        }
    ]

    for param in params:
        try:
            investpy.get_certificate_historical_data(certificate=param['certificate'],
                                                     country=param['country'],
                                                     from_date=param['from_date'],
                                                     to_date=param['to_date'],
                                                     as_json=param['as_json'],
                                                     order=param['order'],
                                                     interval=param['interval'])
        except:
            pass

    params = [
        {
            'certificate': None,
            'country': 'france',
            'as_json': False
        },
        {
            'certificate': ['error'],
            'country': 'france',
            'as_json': False
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': None,
            'as_json': False
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': ['error'],
            'as_json': False
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': None
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'error',
            'as_json': False
        },
        {
            'certificate': 'error',
            'country': 'france',
            'as_json': False
        }
    ]

    for param in params:
        try:
            investpy.get_certificate_information(certificate=param['certificate'],
                                                 country=param['country'],
                                                 as_json=param['as_json'])
        except:
            pass
    
    params = [
        {
            'country': None,
            'as_json': False,
            'n_results': 10
        },
        {
            'country': ['error'],
            'as_json': False,
            'n_results': 10
        },
        {
            'country': 'france',
            'as_json': None,
            'n_results': 10
        },
        {
            'country': 'france',
            'as_json': False,
            'n_results': 'error'
        },
        {
            'country': 'france',
            'as_json': False,
            'n_results': 0
        },
        {
            'country': 'error',
            'as_json': False,
            'n_results': 10
        }
    ]

    for param in params:
        try:
            investpy.get_certificates_overview(country=param['country'],
                                               as_json=param['as_json'],
                                               n_results=param['n_results'])
        except:
            pass

    params = [
        {
            'by': None,
            'value': 'BNP'
        },
        {
            'by': ['error'],
            'value': 'BNP'
        },
        {
            'by': 'error',
            'value': 'BNP'
        },
        {
            'by': 'name',
            'value': None
        },
        {
            'by': 'name',
            'value': ['error']
        },
        {
            'by': 'symbol',
            'value': 'error'
        },
    ]

    for param in params:
        try:
            investpy.search_certificates(by=param['by'], value=param['value'])
        except:
            pass


def test_search_errors():
    """
    This function raises errors on search functions.
    """

    params = [
        {
            'text': None,
            'products': None,
            'countries': None,
            'n_results': None
        },
        {
            'text': ['error'],
            'products': None,
            'countries': None,
            'n_results': None
        },
        {
            'text': 'error',
            'products': None,
            'countries': None,
            'n_results': None
        },
        {
            'text': 'bbva',
            'products': None,
            'countries': None,
            'n_results': ['error']
        },
        {
            'text': 'bbva',
            'products': None,
            'countries': None,
            'n_results': 0
        },
        {
            'text': 'bbva',
            'products': 'error',
            'countries': None,
            'n_results': 10
        },
        {
            'text': 'bbva',
            'products': ['error'],
            'countries': None,
            'n_results': 10
        },
        {
            'text': 'bbva',
            'products': None,
            'countries': 'error',
            'n_results': 10
        },
        {
            'text': 'bbva',
            'products': None,
            'countries': ['error'],
            'n_results': 10
        },
        {
            'text': 'bbva',
            'products': None,
            'countries': None,
            'n_results': 10
        }
    ]

    for param in params:
        try:
            results = investpy.search_quotes(text=param['text'],
                                             countries=param['countries'],
                                             products=param['products'],
                                             n_results=param['n_results'])

            dates = [
                {
                    'from_date': 'error',
                    'to_date': '01/01/2019'
                },
                {
                    'from_date': '01/01/2019',
                    'to_date': 'error'
                },
                {
                    'from_date': '01/01/2019',
                    'to_date': '01/01/2018'
                },
            ]

            for result in results[:1]:
                for date in dates:
                    try:
                        result.retrieve_historical_data(from_date=date['from_date'], to_date=date['to_date'])
                    except:
                        continue
            
            intervals = ['non_existing', '1min']
            for interval in intervals:
                try:
                    result.pair_type = 'funds'
                    result.retrieve_technical_indicators(interval=interval)
                except:
                    continue
        except:
            pass


def test_news_errors():
    """
    This function raises errors on news functions.
    """

    params = [
        {
            'time_zone': ['error'],
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': 'error',
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': None,
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': ['error'],
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': 'error',
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': 'error',
            'categories': None,
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': 'error',
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': ['error'],
            'to_date': None
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': None,
            'to_date': ['error']
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/02/2020'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': 'error',
            'to_date': '01/02/2020'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': 'error'
        },
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/01/2019'
        }
    ]

    for param in params:
        try:
            investpy.economic_calendar(time_zone=param['time_zone'],
                                  time_filter=param['time_filter'],
                                  countries=param['countries'],
                                  importances=param['importances'],
                                  categories=param['categories'],
                                  from_date=param['from_date'],
                                  to_date=param['to_date'])
        except:
            pass


def test_technical_errors():
    """
    This function raises errors on technical functions.
    """

    params = [
        {
            'name': None,
            'country': 'spain',
            'product_type': 'stock',
            'interval': 'weekly',
        },
        {
            'name': ['error'],
            'country': 'spain',
            'product_type': 'stock',
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': ['error'],
            'product_type': 'stock',
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': None,
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': ['error'],
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': 'stock',
            'interval': None,
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': 'stock',
            'interval': ['error'],
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': 'error',
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': 'spain',
            'product_type': 'stock',
            'interval': 'error',
        },
        {
            'name': 'bbva',
            'country': None,
            'product_type': 'stock',
            'interval': 'weekly',
        },
        {
            'name': 'bbva',
            'country': 'error',
            'product_type': 'stock',
            'interval': 'weekly',
        },
        {
            'name': 'error',
            'country': 'spain',
            'product_type': 'stock',
            'interval': 'weekly',
        }
    ]

    for param in params:
        try:
            investpy.technical_indicators(name=param['name'],
                                          country=param['country'],
                                          product_type=param['product_type'],
                                          interval=param['interval'])
        except:
            pass

        try:
            investpy.moving_averages(name=param['name'],
                                     country=param['country'],
                                     product_type=param['product_type'],
                                     interval=param['interval'])
        except:
            pass

        try:
            investpy.pivot_points(name=param['name'],
                                  country=param['country'],
                                  product_type=param['product_type'],
                                  interval=param['interval'])
        except:
            pass

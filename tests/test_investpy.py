# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import pytest

import investpy


def test_investpy():
    """
    This function checks that both the investpy's author and version are the correct ones.
    """

    print(investpy.__author__)
    print(investpy.__version__)


def test_investpy_stocks():
    """
    This function checks that stock data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'spain',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_stocks(country=param['country'])
        investpy.get_stocks_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_stocks_dict(country=param['country'],
                                 columns=param['columns'],
                                 as_json=param['as_json'])

    investpy.get_stock_countries()

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_stock_recent_data(stock='BBVA',
                                       country='spain',
                                       as_json=param['as_json'],
                                       order=param['order'],
                                       interval='Daily')

        investpy.get_stock_historical_data(stock='BBVA',
                                           country='spain',
                                           from_date='01/01/1990',
                                           to_date='01/01/2019',
                                           as_json=param['as_json'],
                                           order=param['order'],
                                           interval='Daily')

    for value in ['spanish', 'english']:
        investpy.get_stock_company_profile(stock='BBVA',
                                           country='spain',
                                           language=value)

    params = [
        {
            'stock': 'bbva',
            'country': 'spain',
            'as_json': False
        },
        {
            'stock': 'bbva',
            'country': 'spain',
            'as_json': True
        },
        {
            'stock': 'HSBK',
            'country': 'kazakhstan',
            'as_json': False
        }
    ]

    for param in params:
        investpy.get_stock_information(stock=param['stock'], country=param['country'], as_json=param['as_json'])

    params = [
        {
            'country': 'spain',
            'as_json': True,
            'n_results': 50
        },
        {
            'country': 'united states',
            'as_json': False,
            'n_results': 50
        },
        {
            'country': 'bosnia',
            'as_json': False,
            'n_results': 50
        },
        {
            'country': 'palestine',
            'as_json': False,
            'n_results': 50
        },
        {
            'country': 'dubai',
            'as_json': False,
            'n_results': 50
        },
        {
            'country': 'ivory coast',
            'as_json': False,
            'n_results': 50
        },
        {
            'country': 'indonesia',
            'as_json': False,
            'n_results': 362
        }
    ]

    for param in params:
        investpy.get_stocks_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])

    params = [
        {
            'stock': 'bbva',
            'country': 'spain'
        },
        {
            'stock': 'entel',
            'country': 'chile'
        }
    ]

    for param in params:
        investpy.get_stock_dividends(stock=param['stock'], country=param['country'])

    params = [
        {
            'stock': 'bbva',
            'country': 'spain',
            'summary_type': 'balance_sheet',
            'period': 'annual'
        },
        {
            'stock': 'aapl',
            'country': 'united states',
            'summary_type': 'income_statement',
            'period': 'quarterly'
        },
        {
            'stock': 'barc',
            'country': 'united kingdom',
            'summary_type': 'cash_flow_statement',
            'period': 'annual'
        }
    ]

    for param in params:
        investpy.get_stock_financial_summary(stock=param['stock'],
                                             country=param['country'], 
                                             summary_type=param['summary_type'],
                                             period=param['period'])

    investpy.search_stocks(by='name', value='BBVA')


def test_investpy_funds():
    """
    This function checks that fund data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'spain',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_funds(country=param['country'])
        investpy.get_funds_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['name'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': ['name'],
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_funds_dict(country=param['country'],
                                columns=param['columns'],
                                as_json=param['as_json'])

    investpy.get_fund_countries()

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_fund_recent_data(fund='bbva multiactivo conservador pp',
                                      country='spain',
                                      as_json=param['as_json'],
                                      order=param['order'],
                                      interval='Daily')

        investpy.get_fund_historical_data(fund='bbva multiactivo conservador pp',
                                          country='spain',
                                          from_date='01/01/2010',
                                          to_date='01/01/2019',
                                          as_json=param['as_json'],
                                          order=param['order'],
                                          interval='Daily')

    params = [
        {
            'fund': 'bbva multiactivo conservador pp',
            'country': 'spain',
            'as_json': False
        },
        {
            'fund': 'öhman Global Growth',
            'country': 'sweden',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_fund_information(fund=param['fund'],
                                      country=param['country'],
                                      as_json=param['as_json'])

    params = [
        {
            'country': 'andorra',
            'as_json': True,
            'n_results': 2
        },
        {
            'country': 'andorra',
            'as_json': False,
            'n_results': 2
        },
        {
            'country': 'united states',
            'as_json': False,
            'n_results': 2
        },
        {
            'country': 'united kingdom',
            'as_json': False,
            'n_results': 2
        }
    ]

    for param in params:
        investpy.get_funds_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_funds(by='name', value='bbva')


def test_investpy_etfs():
    """
    This function checks that etf data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'spain',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_etfs(country=param['country'])
        investpy.get_etfs_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['name'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': ['name'],
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_etfs_dict(country=param['country'],
                               columns=param['columns'],
                               as_json=param['as_json'])

    investpy.get_etf_countries()

    params = [
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'as_json': True,
            'order': 'ascending',
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'as_json': False,
            'order': 'ascending',
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'as_json': True,
            'order': 'descending',
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'as_json': False,
            'order': 'descending',
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'as_json': True,
            'order': 'ascending',
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'as_json': False,
            'order': 'ascending',
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'as_json': True,
            'order': 'descending',
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_etf_recent_data(etf=param['etf'],
                                     country='spain',
                                     is_symbol=param['is_symbol'],
                                     as_json=param['as_json'],
                                     order=param['order'],
                                     interval='Daily')

        investpy.get_etf_historical_data(etf=param['etf'],
                                         country='spain',
                                         is_symbol=param['is_symbol'],
                                         from_date='01/01/2010',
                                         to_date='01/01/2019',
                                         as_json=param['as_json'],
                                         order=param['order'],
                                         interval='Daily')

    params = [
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'country': 'spain',
            'as_json': False
        },
        {
            'etf': 'bbva accion dj eurostoxx 50',
            'is_symbol': False,
            'country': 'spain',
            'as_json': True
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'country': 'spain',
            'as_json': False
        },
        {
            'etf': 'bbvae',
            'is_symbol': True,
            'country': 'spain',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_etf_information(etf=param['etf'], is_symbol=param['is_symbol'], country=param['country'], as_json=param['as_json'])

    params = [
        {
            'country': 'united states',
            'as_json': True,
            'n_results': 2
        },
        {
            'country': 'united kingdom',
            'as_json': False,
            'n_results': 2
        },
    ]

    for param in params:
        investpy.get_etfs_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_etfs(by='name', value='bbva')


def test_investpy_indices():
    """
    This function checks that index data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'spain',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_indices(country=param['country'])
        investpy.get_indices_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['name', 'currency'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['name', 'currency'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': ['name', 'currency'],
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['name', 'currency'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_indices_dict(country=param['country'],
                                  columns=param['columns'],
                                  as_json=param['as_json'])

    investpy.get_index_countries()

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_index_recent_data(index='ibex 35',
                                       country='spain',
                                       as_json=param['as_json'],
                                       order=param['order'],
                                       interval='Daily')

        investpy.get_index_historical_data(index='ibex 35',
                                           country='spain',
                                           from_date='01/01/2018',
                                           to_date='01/01/2019',
                                           as_json=param['as_json'],
                                           order=param['order'],
                                           interval='Daily')

    params = [
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': False
        },
        {
            'index': 'ibex 35',
            'country': 'spain',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_index_information(index=param['index'], country=param['country'], as_json=param['as_json'])
    
    params = [
        {
            'country': 'united states', 
            'as_json': False,
            'n_results': 10
        },
        {
            'country': 'united kingdom', 
            'as_json': True,
            'n_results': 10
        }
    ]

    for param in params:
        investpy.get_indices_overview(country=param['country'], as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_indices(by='name', value='ibex')


def test_investpy_currency_crosses():
    """
    This function checks that currency cross data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'base': None,
            'second': None,
        },
        {
            'base': 'EUR',
            'second': None,
        },
        {
            'base': None,
            'second': 'EUR',
        },
        {
            'base': 'EUR',
            'second': 'USD',
        },
    ]

    for param in params:
        investpy.get_currency_crosses(base=param['base'], second=param['second'])
        investpy.get_currency_crosses_list(base=param['base'], second=param['second'])

    params = [
        {
            'base': None,
            'second': None,
            'columns': None,
            'as_json': True
        },
        {
            'base': None,
            'second': None,
            'columns': None,
            'as_json': False
        },
        {
            'base': 'EUR',
            'second': None,
            'columns': None,
            'as_json': True
        },
        {
            'base': 'EUR',
            'second': None,
            'columns': None,
            'as_json': False
        },
        {
            'base': None,
            'second': 'USD',
            'columns': None,
            'as_json': True
        },
        {
            'base': None,
            'second': 'USD',
            'columns': None,
            'as_json': False
        },
        {
            'base': 'EUR',
            'second': 'USD',
            'columns': None,
            'as_json': True
        },
        {
            'base': 'EUR',
            'second': 'USD',
            'columns': None,
            'as_json': False
        },
        {
            'base': 'EUR',
            'second': 'USD',
            'columns': ['name', 'full_name'],
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_currency_crosses_dict(base=param['base'],
                                           second=param['second'],
                                           columns=param['columns'],
                                           as_json=param['as_json'])

    investpy.get_available_currencies()

    params = [
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/2018',
            'to_date': '01/01/2019',
            'as_json': True,
            'order': 'ascending',
        },
        {
            'currency_cross': 'EUR/USD',
            'from_date': '01/01/1990',
            'to_date': '01/01/2019',
            'as_json': False,
            'order': 'descending',
        },
        {
            'currency_cross': 'XAG/USD',
            'from_date': '01/01/2010',
            'to_date': '01/01/2015',
            'as_json': False,
            'order': 'descending',
        },
        {
            'currency_cross': 'XAU/USD',
            'from_date': '01/01/2010',
            'to_date': '01/01/2015',
            'as_json': False,
            'order': 'descending',
        }
    ]

    for param in params:
        investpy.get_currency_cross_recent_data(currency_cross=param['currency_cross'],
                                                as_json=param['as_json'],
                                                order=param['order'],
                                                interval='Daily')

        investpy.get_currency_cross_historical_data(currency_cross=param['currency_cross'],
                                                    from_date=param['from_date'],
                                                    to_date=param['to_date'],
                                                    as_json=param['as_json'],
                                                    order=param['order'],
                                                    interval='Daily')

    params = [
        {
            'currency_cross': 'EUR/USD',
            'as_json': False
        },
        {
            'currency_cross': 'EUR/USD',
            'as_json': True
        },
        {
            'currency_cross': 'XAU/USD',
            'as_json': True
        },
        {
            'currency_cross': 'XAG/USD',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_currency_cross_information(currency_cross=param['currency_cross'], as_json=param['as_json'])
    
    params = [
        {
            'currency': 'try',
            'as_json': False,
            'n_results': 100
        },
        {
            'currency': 'amd',
            'as_json': True,
            'n_results': 100
        }
    ]
    
    for param in params:
        investpy.get_currency_crosses_overview(currency=param['currency'], as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_currency_crosses(by='base', value='EUR')


def test_investpy_bonds():
    """
    This function checks that bond data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'spain',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_bonds(country=param['country'])
        investpy.get_bonds_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': 'spain',
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'spain',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_bonds_dict(country=param['country'],
                                columns=param['columns'],
                                as_json=param['as_json'])

    investpy.get_bond_countries()

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_bond_recent_data(bond='Spain 30Y',
                                      as_json=param['as_json'],
                                      order=param['order'],
                                      interval='Daily')

        investpy.get_bond_historical_data(bond='Spain 30Y',
                                          from_date='01/01/1990',
                                          to_date='01/01/2019',
                                          as_json=param['as_json'],
                                          order=param['order'],
                                          interval='Daily')

    params = [
        {
            'bond': 'spain 30y',
            'as_json': False
        },
        {
            'bond': 'argentina 3y',
            'as_json': True
        },
        {
            'bond': 'germany 3m',
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_bond_information(bond=param['bond'], as_json=param['as_json'])
    
    params = [
        {
            'country': 'united states',
            'as_json': True,
        },
        {
            'country': 'united kingdom',
            'as_json': False,
        }
    ]

    for param in params:
        investpy.get_bonds_overview(country=param['country'], as_json=param['as_json'])

    investpy.search_bonds(by='name', value='Spain')


def test_investpy_commodities():
    """
    This function checks that commodity data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'group': 'metals',
        },
        {
            'group': None,
        },
    ]

    for param in params:
        investpy.get_commodities(group=param['group'])
        investpy.get_commodities_list(group=param['group'])

    params = [
        {
            'group': None,
            'columns': ['title', 'full_name', 'name'],
            'as_json': True
        },
        {
            'group': None,
            'columns': ['title', 'full_name', 'name'],
            'as_json': False
        },
        {
            'group': 'metals',
            'columns': ['title', 'full_name', 'name'],
            'as_json': True
        },
        {
            'group': 'metals',
            'columns': ['title', 'full_name', 'name'],
            'as_json': False
        },
        {
            'group': 'metals',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_commodities_dict(group=param['group'],
                                      columns=param['columns'],
                                      as_json=param['as_json'])

    investpy.get_commodity_groups()

    params = [
        {
            'country': None,
            'as_json': True,
            'order': 'ascending',
        },
        {
            'country': 'united states',
            'as_json': False,
            'order': 'ascending',
        },
        {
            'country': 'united states',
            'as_json': True,
            'order': 'descending',
        },
        {
            'country': 'united states',
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_commodity_recent_data(commodity='copper',
                                           country=param['country'],
                                           as_json=param['as_json'],
                                           order=param['order'],
                                           interval='Daily')

        investpy.get_commodity_historical_data(commodity='copper',
                                               from_date='01/01/1990',
                                               to_date='01/01/2019',
                                               country=param['country'],
                                               as_json=param['as_json'],
                                               order=param['order'],
                                               interval='Daily')

    params = [
        {
            'commodity': 'copper',
            'country': None,
            'as_json': False
        },
        {
            'commodity': 'copper',
            'country': 'united states',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_commodity_information(commodity=param['commodity'], country=param['country'], as_json=param['as_json'])
    
    params = [
        {
            'group': 'metals',
            'as_json': True,
            'n_results': 100
        },
        {
            'group': 'metals',
            'as_json': False,
            'n_results': 100
        }
    ]

    for param in params:
        investpy.get_commodities_overview(group=param['group'], as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_commodities(by='name', value='gold')


def test_investpy_cryptos():
    """
    This function checks that crypto currencies data retrieval functions listed in investpy work properly.
    """
    
    investpy.get_cryptos()
    investpy.get_cryptos_list()

    params = [
        {
            'columns': None,
            'as_json': False
        },
        {
            'columns': ['name', 'symbol', 'currency'],
            'as_json': False
        },
        {
            'columns': None,
            'as_json': True
        },    
    ]

    for param in params:
        investpy.get_cryptos_dict(columns=param['columns'],
                                  as_json=param['as_json'])

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_crypto_recent_data(crypto='bitcoin',
                                        as_json=param['as_json'],
                                        order=param['order'],
                                        interval='Daily')

        investpy.get_crypto_historical_data(crypto='bitcoin',
                                            from_date='01/01/1990',
                                            to_date='01/01/2019',
                                            as_json=param['as_json'],
                                            order=param['order'],
                                            interval='Daily')

    params = [
        {
            'crypto': 'bitcoin',
            'as_json': False
        },
        {
            'crypto': 'bitcoin',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_crypto_information(crypto=param['crypto'], as_json=param['as_json'])
    
    params = [
        {
            'as_json': False,
            'n_results': 10
        },
        {
            'as_json': True,
            'n_results': 10
        },
        {
            'as_json': False,
            'n_results': 110
        },
        {
            'as_json': True,
            'n_results': 110
        },
        {
            'as_json': False,
            'n_results': None
        },
        {
            'as_json': True,
            'n_results': None
        },
    ]

    for param in params:
        investpy.get_cryptos_overview(as_json=param['as_json'], n_results=param['n_results'])

    investpy.search_cryptos(by='name', value='bitcoin')


def test_investpy_certificates():
    """
    This function checks that certificate data retrieval functions listed in investpy work properly.
    """

    params = [
        {
            'country': 'france',
        },
        {
            'country': None,
        },
    ]

    for param in params:
        investpy.get_certificates(country=param['country'])
        investpy.get_certificates_list(country=param['country'])

    params = [
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': None,
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'france',
            'columns': ['full_name', 'name'],
            'as_json': True
        },
        {
            'country': 'france',
            'columns': ['full_name', 'name'],
            'as_json': False
        },
        {
            'country': 'france',
            'columns': None,
            'as_json': False
        },
    ]

    for param in params:
        investpy.get_certificates_dict(country=param['country'],
                                       columns=param['columns'],
                                       as_json=param['as_json'])

    investpy.get_certificate_countries()

    params = [
        {
            'as_json': True,
            'order': 'ascending',
        },
        {
            'as_json': False,
            'order': 'ascending',
        },
        {
            'as_json': True,
            'order': 'descending',
        },
        {
            'as_json': False,
            'order': 'descending',
        },
    ]

    for param in params:
        investpy.get_certificate_recent_data(certificate='BNP Gold 31Dec99',
                                             country='france',
                                             as_json=param['as_json'],
                                             order=param['order'],
                                             interval='Daily')

        investpy.get_certificate_historical_data(certificate='BNP Gold 31Dec99',
                                                 country='france',
                                                 from_date='01/01/1990',
                                                 to_date='01/01/2019',
                                                 as_json=param['as_json'],
                                                 order=param['order'],
                                                 interval='Daily')

    params = [
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': False
        },
        {
            'certificate': 'BNP Gold 31Dec99',
            'country': 'france',
            'as_json': True
        }
    ]

    for param in params:
        investpy.get_certificate_information(certificate=param['certificate'],
                                             country=param['country'],
                                             as_json=param['as_json'])
    
    params = [
        {
            'country': 'france',
            'as_json': True,
            'n_results': 10
        },
        {
            'country': 'france',
            'as_json': False,
            'n_results': 10
        }
    ]

    for param in params:
        investpy.get_certificates_overview(country=param['country'],
                                           as_json=param['as_json'],
                                           n_results=param['n_results'])

    investpy.search_certificates(by='name', value='BNP')


def test_investpy_search():
    """
    This function checks that investpy search function works properly.
    """

    params = [
        {
            'text': 'bbva',
            'products': None,
            'countries': None,
            'n_results': 5
        },
        {
            'text': 'spain 3y',
            'products': None,
            'countries': None,
            'n_results': 5
        },
        {
            'text': 'ibex 35',
            'products': None,
            'countries': None,
            'n_results': 5
        },
        {
            'text': 'bnp daxplus',
            'products': None,
            'countries': None,
            'n_results': None
        },
        {
            'text': 'apple',
            'products': ['stocks'],
            'countries': ['united states'],
            'n_results': 1
        },
        {
            'text': 'apple',
            'products': ['stocks'],
            'countries': ['united states'],
            'n_results': 5
        }
    ]

    for param in params:
        results = investpy.search_quotes(text=param['text'],
                                         products=param['products'],
                                         countries=param['countries'],
                                         n_results=param['n_results'])

        dates = [
            {
                'from_date': '01/01/2018',
                'to_date': '01/01/2019'
            },
            {
                'from_date': '01/01/1990',
                'to_date': '01/01/2019'
            },
        ]

        if isinstance(results, list):
            result = results[0]
        else:
            result = results

        print(result)

        assert result.retrieve_recent_data() is not None
        
        for date in dates:
            assert result.retrieve_historical_data(from_date=date['from_date'], to_date=date['to_date']) is not None

        assert result.retrieve_currency() is not None
        assert result.retrieve_technical_indicators() is not None

    financial_products = [
        ('stocks', 'apple'), ('etfs', 'apple'), ('commodities', 'apple'), ('currencies', 'usd'), ('funds', 'apple'), 
        ('bonds', 'apple'), ('cryptos', 'bitcoin'), ('certificates', 'apple'), ('indices', 'apple'), ('fxfutures', 'usd')
    ]

    for product_type, product_name in financial_products:
        search_result = investpy.search_quotes(text=product_name, products=[product_type], n_results=1)

        assert search_result.retrieve_information() is not None


def test_investpy_news():
    """
    This function checks that investpy news retrieval functionality works as expected.
    """

    params = [
        {
            'time_zone': None,
            'time_filter': 'time_only',
            'countries': ['spain', 'france'],
            'importances': ['high', 'low'],
            'categories': ['credit', 'employment'],
            'from_date': None,
            'to_date': None
        },
        {
            'time_zone': 'GMT -3:00',
            'time_filter': 'time_only',
            'countries': None,
            'importances': None,
            'categories': None,
            'from_date': '01/01/2020',
            'to_date': '01/02/2020'
        }
    ]

    for param in params:
        investpy.economic_calendar(time_zone=param['time_zone'],
                                   time_filter=param['time_filter'],
                                   countries=param['countries'],
                                   importances=param['importances'],
                                   categories=param['categories'],
                                   from_date=param['from_date'],
                                   to_date=param['to_date'])


def test_investpy_technical():
    """
    This function checks that investpy news retrieval functionality works as expected.
    """

    params = list()

    for interval in list(investpy.utils.constant.INTERVAL_FILTERS.keys()):
        params.append({
            'name': 'bbva',
            'country': 'spain',
            'product_type': 'stock',
            'interval': interval
        })

    for param in params:
        investpy.technical_indicators(name=param['name'],
                                      country=param['country'],
                                      product_type=param['product_type'],
                                      interval=param['interval'])

        investpy.moving_averages(name=param['name'],
                                 country=param['country'],
                                 product_type=param['product_type'],
                                 interval=param['interval'])

        investpy.pivot_points(name=param['name'],
                              country=param['country'],
                              product_type=param['product_type'],
                              interval=param['interval'])

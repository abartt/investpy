# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, date, timedelta
import pytz

import json
from random import randint

import warnings

import pandas as pd
import pkg_resources
import requests
from unidecode import unidecode
from lxml.html import fromstring

from .utils.extra import random_user_agent
from .utils.data import Data

from .data.etfs_data import etfs_as_df, etfs_as_list, etfs_as_dict
from .data.etfs_data import etf_countries_as_list


def get_etfs(country=None):
    """
    This function retrieves all the available etfs indexed on Investing.com, already stored on `etfs.csv`.
    This function also allows the users to specify which country do they want to retrieve data from or if they
    want to retrieve it from every listed country; so on, all the indexed etfs will be returned.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available etfs from.

    Returns:
        :obj:`pandas.DataFrame` - etfs:
            The resulting :obj:`pandas.DataFrame` contains all the etfs basic information stored on `etfs.csv`, since it
            was previously retrieved by investpy. Unless the country is specified, all the available etfs indexed on 
            Investing.com is returned, but if it is specified, just the etfs from that country are returned.

            In the case that the file reading of `etfs.csv` or the retrieval process from Investing.com was
            successfully completed, the resulting :obj:`pandas.DataFrame` will look like::

                country | name | full_name | symbol | isin | asset_class | currency | stock_exchange | def_stock_exchange 
                --------|------|-----------|--------|------|-------------|----------|----------------|--------------------
                xxxxxxx | xxxx | xxxxxxxxx | xxxxxx | xxxx | xxxxxxxxxxx | xxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxx 

    Raises:
        ValueError: raised when any of the input arguments is not valid.
        FileNotFoundError: raised when `etfs.csv` file was not found.
        IOError: raised when `etfs.csv` file is missing.
    
    """

    return etfs_as_df(country=country)


def get_etfs_list(country=None):
    """
    This function retrieves all the available etfs indexed on Investing.com, already stored on `etfs.csv`.
    This function also allows the users to specify which country do they want to retrieve data from or if they
    want to retrieve it from every listed country; so on, a listing of etfs will be returned. This function
    helps the user to get to know which etfs are available on Investing.com.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available etfs from.

    Returns:
        :obj:`list` - etfs_list:
            The resulting :obj:`list` contains the retrieved data from the `etfs.csv` file, which is
            a listing of the names of the etfs listed on Investing.com, which is the input for data
            retrieval functions as the name of the etf to retrieve data from needs to be specified.

            In case the listing was successfully retrieved, the :obj:`list` will look like::

                etfs_list = [
                    'Betashares U.S. Equities Strong Bear Currency Hedg',
                    'Betashares Active Australian Hybrids',
                    'Australian High Interest Cash', ...
                ]

    Raises:
        ValueError: raised when any of the input arguments is not valid.
        FileNotFoundError: raised when `etfs.csv` file was not found.
        IOError: raised when `etfs.csv` file is missing.
    
    """

    return etfs_as_list(country=country)


def get_etfs_dict(country=None, columns=None, as_json=False):
    """
    This function retrieves all the available etfs indexed on Investing.com, already stored on `etfs.csv`.
    This function also allows the user to specify which country do they want to retrieve data from,
    or from every listed country; the columns which the user wants to be included on the resulting
    :obj:`dict`; and the output of the function will either be a :obj:`dict` or a :obj:`json`.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available etfs from.
        columns (:obj:`list`, optional):
            names of the columns of the etf data to retrieve <country, name, full_name, symbol, isin, asset_class, 
            currency, stock_exchange>
        as_json (:obj:`bool`, optional):
            value to determine the format of the output data which can either be a :obj:`dict` or a :obj:`json`.

    Returns:
        :obj:`dict` or :obj:`json` - etfs_dict:
            The resulting :obj:`dict` contains the retrieved data if found, if not, the corresponding
            fields are filled with `None` values.

            In case the information was successfully retrieved, the :obj:`dict` will look like::

                etfs_dict = {
                    "country": country,
                    "name": name,
                    "full_name": full_name,
                    "symbol": symbol,
                    "isin": isin,
                    "asset_class": asset_class,
                    "currency": currency,
                    "stock_exchange": stock_exchange,
                    "def_stock_exchange": def_stock_exchange
                }

    Raises:
        ValueError: raised when any of the input arguments is not valid.
        FileNotFoundError: raised when `etfs.csv` file was not found.
        IOError: raised when `etfs.csv` file is missing.
    
    """

    return etfs_as_dict(country=country, columns=columns, as_json=as_json)


def get_etf_countries():
    """
    This function retrieves all the available countries to retrieve etfs from, as the listed
    countries are the ones indexed on Investing.com. The purpose of this function is to list
    the countries which have available etfs according to Investing.com data, so to ease the
    etf retrieval process of a particular country.

    Returns:
        :obj:`list` - countries:
            The resulting :obj:`list` contains all the countries listed on Investing.com with
            etfs available to retrieve data from.

            In the case that the file reading of `etf_countries.csv` which contains the names and codes of the countries
            with etfs was successfully completed, the resulting :obj:`list` will look like::

                countries = ['australia', 'austria', 'belgium', 'brazil', ...]

    Raises:
        FileNotFoundError: raised when `etf_countries.csv` file was not found.
    
    """

    return etf_countries_as_list()


def get_etf_recent_data(etf, country, is_symbol=False, stock_exchange=None, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves recent historical data from the introduced `etf` from Investing
    via Web Scraping. The resulting data can it either be stored in a :obj:`pandas.DataFrame` or in a
    :obj:`json` file, with `ascending` or `descending` order.

    Args:
        etf (:obj:`str`): name or symbol of the etf to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the etf is.
        is_symbol (:obj:`bool`, optional):
            determine wether the etf is searched by its name or by its symbol.
        stock_exchange (:obj:`str`, optional):
            optional argument to filter the results by the stock exchange field.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        order (:obj:`str`, optional):
            optional argument to define the order of the retrieved data (`ascending`, `asc` or `descending`, `desc`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            recent data from the specified etf via argument. The dataset contains the open, high, low and close
            values for the selected etf on market days.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency | Exchange
                -----||------|------|-----|-------|--------|----------|---------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx | xxxxxxxx

            but if we define `as_json=True`, then the output will be::

                {
                    name: name,
                    recent: [
                        {
                            date: dd/mm/yyyy,
                            open: x,
                            high: x,
                            low: x,
                            close: x,
                            volume: x,
                            currency: x,
                            exchange: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised whenever any of the arguments is not valid or errored.
        IOError: raised if etfs object/file not found or unable to retrieve.
        RuntimeError:raised if the introduced etf does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if etf information was unavailable or not found.

    Examples:
        >>> data = investpy.get_etf_recent_data(etf='bbva accion dj eurostoxx 50', country='spain')
        >>> data.head()
                      Open    High    Low   Close  Volume Currency Exchange
        Date                                                               
        2020-04-09  28.890  29.155  28.40  28.945   20651      EUR   Madrid
        2020-04-14  29.345  30.235  28.94  29.280   14709      EUR   Madrid
        2020-04-15  29.125  29.125  28.11  28.130   14344      EUR   Madrid
        2020-04-16  28.505  28.590  28.08  28.225   17662      EUR   Madrid
        2020-04-17  29.000  29.325  28.80  28.895   19578      EUR   Madrid

    """

    if not etf:
        raise ValueError("ERR#0031: etf parameter is mandatory and must be a valid etf name.")

    if not isinstance(etf, str):
        raise ValueError("ERR#0030: etf argument needs to be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(is_symbol, bool):
        raise ValueError("ERR#0139: is_symbol argument can just be True or False (default), bool type.")

    if stock_exchange is not None and not isinstance(stock_exchange, str):
        raise ValueError("ERR#0125: specified stock_exchange value is not valid, it should be a str.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    interval = interval.lower()

    if interval not in ['daily', 'weekly', 'monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0058: etfs file not found or errored.")

    if etfs is None:
        raise IOError("ERR#0009: etfs object not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_etf_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    etfs = etfs[etfs['country'].str.lower() == country]
    
    etf = unidecode(etf.strip().lower())

    search_field = 'symbol' if is_symbol else 'name'

    def_exchange = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['def_stock_exchange'] == True)).idxmax()]

    if etf not in list(etfs[search_field].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0019: etf " + etf + " not found, check if it is correct.")

    etfs = etfs[etfs[search_field].apply(unidecode).str.lower() == etf]

    if def_exchange['country'] != country:
        warnings.warn(
            'Selected country does not contain the default stock exchange of the introduced ETF. ' + \
            'Default country is: \"' + def_exchange['country'] + '\" and default stock_exchange: \"' + \
            def_exchange['stock_exchange'] + '\".', 
            Warning
        )
        
        if stock_exchange:
            if stock_exchange.lower() not in etfs['stock_exchange'].str.lower():
                raise ValueError("ERR#0126: introduced stock_exchange value does not exists, leave this parameter to None to use default stock_exchange.")
            
            etf_exchange = etfs.loc[(etfs['stock_exchange'].str.lower() == stock_exchange.lower()).idxmax(), 'stock_exchange']
        else:
            found_etfs = etfs[etfs[search_field].apply(unidecode).str.lower() == etf]
    
            if len(found_etfs) > 1:
                warnings.warn(
                    'Note that the displayed information can differ depending on the stock exchange. Available stock_exchange' + \
                    ' values for \"' + country + '\" are: \"' + '\", \"'.join(found_etfs['stock_exchange']) + '\".',
                    Warning
                )

            del found_etfs

            etf_exchange = etfs.loc[(etfs[search_field].apply(unidecode).str.lower() == etf).idxmax(), 'stock_exchange']
    else:
        if stock_exchange:
            if stock_exchange.lower() not in etfs['stock_exchange'].str.lower():
                raise ValueError("ERR#0126: introduced stock_exchange value does not exists, leave this parameter to None to use default stock_exchange.")

            if def_exchange['stock_exchange'].lower() != stock_exchange.lower():
                warnings.warn(
                    'Selected stock_exchange is not the default one of the introduced ETF. ' + \
                    'Default country is: \"' + def_exchange['country'] + '\" and default stock_exchange: \"' + \
                    def_exchange['stock_exchange'].lower() + '\".', 
                    Warning
                )

            etf_exchange = etfs.loc[(etfs['stock_exchange'].str.lower() == stock_exchange.lower()).idxmax(), 'stock_exchange']
        else:
            etf_exchange = def_exchange['stock_exchange']

    symbol = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'symbol']
    id_ = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'id']
    name = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), search_field]

    etf_currency = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'currency']

    header = symbol + ' Historical Data'

    head = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    params = {
        "curr_id": id_,
        "smlID": str(randint(1000000, 99999999)),
        "header": header,
        "interval_sec": interval.capitalize(),
        "sort_col": "date",
        "sort_ord": "DESC",
        "action": "historical_data"
    }

    url = "https://www.investing.com/instruments/HistoricalDataAjax"

    req = requests.post(url, headers=head, data=params)

    if req.status_code != 200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

    root_ = fromstring(req.text)
    path_ = root_.xpath(".//table[@id='curr_table']/tbody/tr")
    
    result = list()

    if path_:
        for elements_ in path_:
            if elements_.xpath(".//td")[0].text_content() == 'No results found':
                raise IndexError("ERR#0010: etf information unavailable or not found.")
            
            info = []
        
            for nested_ in elements_.xpath(".//td"):
                info.append(nested_.get('data-real-value'))

            etf_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0]), tz=pytz.timezone('GMT')).date()), '%Y-%m-%d')

            etf_close = float(info[1].replace(',', ''))
            etf_open = float(info[2].replace(',', ''))
            etf_high = float(info[3].replace(',', ''))
            etf_low = float(info[4].replace(',', ''))

            etf_volume = int(info[5])

            result.insert(len(result),
                          Data(etf_date, etf_open, etf_high, etf_low, etf_close, etf_volume, etf_currency, etf_exchange))

        if order in ['ascending', 'asc']:
            result = result[::-1]
        elif order in ['descending', 'desc']:
            result = result

        if as_json is True:
            json_ = {
                'name': name,
                'recent':
                    [value.etf_as_json() for value in result]
            }

            return json.dumps(json_, sort_keys=False)
        elif as_json is False:
            df = pd.DataFrame.from_records([value.etf_to_dict() for value in result])
            df.set_index('Date', inplace=True)

            return df
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")


def get_etf_historical_data(etf, country, from_date, to_date, is_symbol=False, stock_exchange=None, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves historical data from the introduced `etf` from Investing.com via Web Scraping on the 
    introduced date range. The resulting data can it either be stored in a :obj:`pandas.DataFrame` or in a 
    :obj:`json` object with `ascending` or `descending` order.

    Args:
        etf (:obj:`str`): name or symbol of the etf to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the etf is.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        is_symbol (:obj:`bool`, optional):
            determine wether the etf is searched by its name or by its symbol.
        stock_exchange (:obj:`str`, optional):
            optional argument to filter the results by the stock exchange field.
        as_json (:obj:`bool`, optional):
            to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        order (:obj:`str`, optional):
            optional argument to define the order of the retrieved data (`ascending`, `asc` or `descending`, `desc`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            recent data from the specified etf via argument. The dataset contains the open, high, low and close
            values for the selected etf on market days.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency | Exchange
                -----||------|------|-----|-------|--------|----------|---------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx | xxxxxxxx

            but if we define `as_json=True`, then the output will be::

                {
                    name: name,
                    historical: [
                        {
                            date: dd/mm/yyyy,
                            open: x,
                            high: x,
                            low: x,
                            close: x,
                            volume: x,
                            currency: x,
                            exchange: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised whenever any of the arguments is not valid or errored.
        IOError: raised if etfs object/file not found or unable to retrieve.
        RuntimeError:raised if the introduced etf does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if etf information was unavailable or not found.

    Examples:
        >>> data = investpy.get_etf_historical_data(etf='bbva accion dj eurostoxx 50', country='spain', from_date='01/01/2010', to_date='01/01/2019')
        >>> data.head()
                     Open   High    Low  Close  Volume Currency Exchange
        Date                                                            
        2011-12-07  23.70  23.70  23.70  23.62    2000      EUR   Madrid
        2011-12-08  23.53  23.60  23.15  23.04     599      EUR   Madrid
        2011-12-09  23.36  23.60  23.36  23.62    2379      EUR   Madrid
        2011-12-12  23.15  23.26  23.00  22.88   10695      EUR   Madrid
        2011-12-13  22.88  22.88  22.88  22.80      15      EUR   Madrid

    """

    if not etf:
        raise ValueError("ERR#0031: etf parameter is mandatory and must be a valid etf name.")

    if not isinstance(etf, str):
        raise ValueError("ERR#0030: etf argument needs to be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(is_symbol, bool):
        raise ValueError("ERR#0139: is_symbol argument can just be True or False (default), bool type.")

    if stock_exchange is not None and not isinstance(stock_exchange, str):
        raise ValueError("ERR#0125: specified stock_exchange value is not valid, it should be a str.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    interval = interval.lower()

    if interval not in ['daily', 'weekly', 'monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    try:
        datetime.strptime(from_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0011: incorrect data format, it should be 'dd/mm/yyyy'.")

    try:
        datetime.strptime(to_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0011: incorrect data format, it should be 'dd/mm/yyyy'.")

    start_date = datetime.strptime(from_date, '%d/%m/%Y')
    end_date = datetime.strptime(to_date, '%d/%m/%Y')

    if start_date >= end_date:
        raise ValueError("ERR#0032: to_date should be greater than from_date, both formatted as 'dd/mm/yyyy'.")

    date_interval = {
        'intervals': [],
    }

    flag = True

    while flag is True:
        diff = end_date.year - start_date.year

        if diff > 19:
            obj = {
                'start': start_date.strftime('%m/%d/%Y'),
                'end': start_date.replace(year=start_date.year + 19).strftime('%m/%d/%Y'),
            }

            date_interval['intervals'].append(obj)

            start_date = start_date.replace(year=start_date.year + 19) + timedelta(days=1)
        else:
            obj = {
                'start': start_date.strftime('%m/%d/%Y'),
                'end': end_date.strftime('%m/%d/%Y'),
            }

            date_interval['intervals'].append(obj)

            flag = False

    interval_limit = len(date_interval['intervals'])
    interval_counter = 0

    data_flag = False

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0058: etfs file not found or errored.")

    if etfs is None:
        raise IOError("ERR#0009: etfs object not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_etf_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    etf = unidecode(etf.strip().lower())

    search_field = 'symbol' if is_symbol else 'name'

    def_exchange = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['def_stock_exchange'] == True)).idxmax()]
    
    etfs = etfs[etfs['country'].str.lower() == country]

    if etf not in list(etfs[search_field].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0019: etf " + etf + " not found, check if it is correct.")

    etfs = etfs[etfs[search_field].apply(unidecode).str.lower() == etf]

    if def_exchange['country'] != country:
        warnings.warn(
            'Selected country does not contain the default stock exchange of the introduced ETF. ' + \
            'Default country is: \"' + def_exchange['country'] + '\" and default stock_exchange: \"' + \
            def_exchange['stock_exchange'] + '\".', 
            Warning
        )
        
        if stock_exchange:
            if stock_exchange.lower() not in etfs['stock_exchange'].str.lower():
                raise ValueError("ERR#0126: introduced stock_exchange value does not exists, leave this parameter to None to use default stock_exchange.")
            
            etf_exchange = etfs.loc[(etfs['stock_exchange'].str.lower() == stock_exchange.lower()).idxmax(), 'stock_exchange']
        else:
            found_etfs = etfs[etfs[search_field].apply(unidecode).str.lower() == etf]
    
            if len(found_etfs) > 1:
                warnings.warn(
                    'Note that the displayed information can differ depending on the stock exchange. Available stock_exchange' + \
                    ' values for \"' + country + '\" are: \"' + '\", \"'.join(found_etfs['stock_exchange']) + '\".',
                    Warning
                )

            del found_etfs

            etf_exchange = etfs.loc[(etfs[search_field].apply(unidecode).str.lower() == etf).idxmax(), 'stock_exchange']
    else:
        if stock_exchange:
            if stock_exchange.lower() not in etfs['stock_exchange'].str.lower():
                raise ValueError("ERR#0126: introduced stock_exchange value does not exists, leave this parameter to None to use default stock_exchange.")

            if def_exchange['stock_exchange'].lower() != stock_exchange.lower():
                warnings.warn(
                    'Selected stock_exchange is not the default one of the introduced ETF. ' + \
                    'Default country is: \"' + def_exchange['country'] + '\" and default stock_exchange: \"' + \
                    def_exchange['stock_exchange'].lower() + '\".', 
                    Warning
                )

            etf_exchange = etfs.loc[(etfs['stock_exchange'].str.lower() == stock_exchange.lower()).idxmax(), 'stock_exchange']
        else:
            etf_exchange = def_exchange['stock_exchange']

    symbol = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'symbol']
    id_ = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'id']
    name = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), search_field]

    etf_currency = etfs.loc[((etfs[search_field].apply(unidecode).str.lower() == etf) & (etfs['stock_exchange'].str.lower() == etf_exchange.lower())).idxmax(), 'currency']

    final = list()

    header = symbol + ' Historical Data'

    for index in range(len(date_interval['intervals'])):
        interval_counter += 1

        params = {
            "curr_id": id_,
            "smlID": str(randint(1000000, 99999999)),
            "header": header,
            "st_date": date_interval['intervals'][index]['start'],
            "end_date": date_interval['intervals'][index]['end'],
            "interval_sec": interval.capitalize(),
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }

        head = {
            "User-Agent": random_user_agent(),
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }

        url = "https://www.investing.com/instruments/HistoricalDataAjax"

        req = requests.post(url, headers=head, data=params)

        if req.status_code != 200:
            raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

        if not req.text:
            continue

        root_ = fromstring(req.text)
        path_ = root_.xpath(".//table[@id='curr_table']/tbody/tr")
        
        result = list()

        if path_:
            for elements_ in path_:
                if elements_.xpath(".//td")[0].text_content() == 'No results found':
                    if interval_counter < interval_limit:
                        data_flag = False
                    else:
                        raise IndexError("ERR#0010: etf information unavailable or not found.")
                else:
                    data_flag = True
                
                info = []

                for nested_ in elements_.xpath(".//td"):
                    info.append(nested_.get('data-real-value'))

                if data_flag is True:
                    etf_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0]), tz=pytz.timezone('GMT')).date()), '%Y-%m-%d')
                    
                    etf_close = float(info[1].replace(',', ''))
                    etf_open = float(info[2].replace(',', ''))
                    etf_high = float(info[3].replace(',', ''))
                    etf_low = float(info[4].replace(',', ''))

                    etf_volume = int(info[5])

                    result.insert(len(result),
                                  Data(etf_date, etf_open, etf_high, etf_low, etf_close, etf_volume, etf_currency, etf_exchange))

            if data_flag is True:
                if order in ['ascending', 'asc']:
                    result = result[::-1]
                elif order in ['descending', 'desc']:
                    result = result

                if as_json is True:
                    json_list = [value.etf_as_json() for value in result]

                    final.append(json_list)
                elif as_json is False:
                    df = pd.DataFrame.from_records([value.etf_to_dict() for value in result])
                    df.set_index('Date', inplace=True)

                    final.append(df)
        else:
            raise RuntimeError("ERR#0004: data retrieval error while scraping.")

    if order in ['descending', 'desc']:
        final.reverse()

    if as_json is True:
        json_ = {
            'name': name,
            'historical': [value for json_list in final for value in json_list]
        }
        return json.dumps(json_, sort_keys=False)
    elif as_json is False:
        return pd.concat(final)


def get_etf_information(etf, country, is_symbol=False, as_json=False):
    """
    This function retrieves fundamental financial information from the specified ETF. The retrieved 
    information from the ETF can be valuable as it is additional information that can be used combined 
    with OHLC values, so to determine financial insights from the company which holds the specified ETF.

    Args:
        etf (:obj:`str`): name or symbol of the ETF to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the ETF is.
        is_symbol (:obj:`bool`, optional):
            determine wether the etf is searched by its name or by its symbol.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`dict` or :obj:`json`).

    Returns:
        :obj:`pandas.DataFrame` or :obj:`dict`- etf_information:
            The resulting :obj:`pandas.DataFrame` contains the information fields retrieved from Investing.com
            from the specified ETF; it can also be returned as a :obj:`dict`, if argument `as_json=True`.

            If any of the information fields could not be retrieved, that field/s will be filled with
            None values. If the retrieval process succeeded, the resulting :obj:`dict` will look like::

                etf_information = {
                    "1-Year Change": "21.83%",
                    "52 wk Range": "233.76 - 320.06",
                    "Asset Class": "Equity",
                    "Average Vol. (3m)": 59658771.0,
                    "Beta": 1.01,
                    "Dividend Yield": "1.73%",
                    "Dividends (TTM)": 4.03,
                    "ETF Name": "SPDR S&P 500",
                    "Market Cap": 296440000000.0,
                    "Open": 319.25,
                    "Prev. Close": 317.27,
                    "ROI (TTM)": "- 0.46%",
                    "Shares Outstanding": 934132116.0,
                    "Todays Range": "319.18 - 320.06",
                    "Total Assets": 167650000000.0,
                    "Volume": 27928710.0
                }

    Raises:
        ValueError: raised if any of the introduced arguments is not valid or errored.
        FileNotFoundError: raised if `etfs.csv` file was not found or errored.
        IOError: raised if `etfs.csv` file is empty or errored.
        RuntimeError: raised if scraping process failed while running.
        ConnectionError: raised if the connection to Investing.com errored (did not return HTTP 200)

    """

    if not etf:
        raise ValueError("ERR#0031: etf parameter is mandatory and must be a valid etf name.")

    if not isinstance(etf, str):
        raise ValueError("ERR#0030: etf argument needs to be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(is_symbol, bool):
        raise ValueError("ERR#0139: is_symbol argument can just be True or False (default), bool type.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0058: etfs file not found or errored.")

    if etfs is None:
        raise IOError("ERR#0009: etfs object not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_etf_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    etfs = etfs[etfs['country'] == country]

    etf = unidecode(etf.strip().lower())

    search_field = 'symbol' if is_symbol else 'name'

    if etf not in list(etfs[search_field].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0019: etf " + etf + " not found, check if it is correct.")

    name = etfs.loc[(etfs[search_field].apply(unidecode).str.lower() == etf).idxmax(), search_field]
    tag = etfs.loc[(etfs[search_field].apply(unidecode).str.lower() == etf).idxmax(), 'tag']

    url = "https://www.investing.com/etfs/" + tag

    head = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    req = requests.get(url, headers=head)

    if req.status_code != 200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

    root_ = fromstring(req.text)
    path_ = root_.xpath("//div[contains(@class, 'overviewDataTable')]/div")

    result = pd.DataFrame(columns=['ETF Name', 'Prev. Close', 'Todays Range', 'ROI (TTM)',
                                   'Open', '52 wk Range', 'Dividends (TTM)', 'Volume',
                                   'Market Cap', 'Dividend Yield', 'Average Vol. (3m)',
                                   'Total Assets', 'Beta', '1-Year Change', 'Shares Outstanding',
                                   'Asset Class'])
    result.at[0, 'ETF Name'] = name

    if path_:
        for elements_ in path_:
            element = elements_.xpath(".//span[@class='float_lang_base_1']")[0]
            title_ = element.text_content()
            if title_ == "Day's Range":
                title_ = 'Todays Range'
            if title_ in result.columns.tolist():
                try:
                    result.at[0, title_] = float(element.getnext().text_content().replace(',', ''))
                    continue
                except:
                    pass
                try:
                    text = element.getnext().text_content().strip()
                    result.at[0, title_] = datetime.strptime(text, "%b %d, %Y").strftime("%d/%m/%Y")
                    continue
                except:
                    pass
                try:
                    value = element.getnext().text_content().strip()
                    if value.__contains__('K'):
                        value = float(value.replace('K', '').replace(',', '')) * 1e3
                    elif value.__contains__('M'):
                        value = float(value.replace('M', '').replace(',', '')) * 1e6
                    elif value.__contains__('B'):
                        value = float(value.replace('B', '').replace(',', '')) * 1e9
                    elif value.__contains__('T'):
                        value = float(value.replace('T', '').replace(',', '')) * 1e12
                    result.at[0, title_] = value
                    continue
                except:
                    pass

        result.replace({'N/A': None}, inplace=True)

        if as_json is True:
            json_ = result.iloc[0].to_dict()
            return json_
        elif as_json is False:
            return result
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")


def get_etfs_overview(country, as_json=False, n_results=100):
    """
    This function retrieves an overview containing all the real time data available for the main ETFs from a country,
    such as the ETF names, symbols, current value, etc. as indexed in Investing.com. So on, the main usage of this
    function is to get an overview on the main ETFs from a country, so to get a general view. Note that since 
    this function is retrieving a lot of information at once, by default just the overview of the Top 100 ETFs 
    is being retrieved, but an additional parameter called n_results can be specified so to retrieve N results.

    Args:
        country (:obj:`str`): name of the country to retrieve the ETFs overview from.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        n_results (:obj:`int`, optional): number of results to be displayed on the overview table (0-1000).

    Returns:
        :obj:`pandas.DataFrame` - etfs_overview:
            The resulting :obj:`pandas.DataFrame` contains all the data available in Investing.com of the main ETFs
            from a country in order to get an overview of it.

            If the retrieval process succeeded, the resulting :obj:`pandas.DataFrame` should look like::

                country | name | full_name | symbol | last | change | turnover
                --------|------|-----------|--------|------|--------|----------
                xxxxxxx | xxxx | xxxxxxxxx | xxxxxx | xxxx | xxxxxx | xxxxxxxx
    
    Raises:
        ValueError: raised if there was any argument error.
        FileNotFoundError: raised when `etfs.csv` file is missing.
        IOError: raised if data could not be retrieved due to file error.
        RuntimeError: 
            raised either if the introduced country does not match any of the listed ones or if no overview results could be 
            retrieved from Investing.com.
        ConnectionError: raised if GET requests does not return 200 status code.
    
    """

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if not isinstance(n_results, int):
        raise ValueError("ERR#0089: n_results argument should be an integer between 1 and 1000.")

    if 1 > n_results or n_results > 1000:
        raise ValueError("ERR#0089: n_results argument should be an integer between 1 and 1000.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0058: etfs file not found or errored.")

    if etfs is None:
        raise IOError("ERR#0009: etfs object not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_etf_countries():
        raise RuntimeError('ERR#0025: specified country value is not valid.')

    etfs = etfs[etfs['country'] == country]

    if country.lower() == 'united states':
        country= 'usa'
    elif country.lower() == 'united kingdom':
        country = 'uk'

    head = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    url = "https://www.investing.com/etfs/" + country.replace(' ', '-') + "-etfs?&issuer_filter=0"

    req = requests.get(url, headers=head)

    if req.status_code != 200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

    root_ = fromstring(req.text)
    table = root_.xpath(".//table[@id='etfs']/tbody/tr")

    results = list()

    if len(table) > 0:
        for row in table[:n_results]:
            id_ = row.get('id').replace('pair_', '')
            symbol = row.xpath(".//td[contains(@class, 'symbol')]")[0].get('title')

            nested = row.xpath(".//a")[0]
            name = nested.text.strip()
            full_name = nested.get('title').rstrip()

            # In Euro Zone the ETFs are from different countries so the country is specified
            country_flag = row.xpath(".//td[@class='flag']/span")[0].get('title')
            country_flag = unidecode(country_flag.lower())

            last_path = ".//td[@class='" + 'pid-' + str(id_) + '-last' + "']"
            last = row.xpath(last_path)[0].text_content()

            change_path = ".//td[contains(@class, '" + 'pid-' + str(id_) + '-pcp' + "')]"
            change = row.xpath(change_path)[0].text_content()

            turnover_path = ".//td[contains(@class, '" + 'pid-' + str(id_) + '-turnover' + "')]"
            turnover = row.xpath(turnover_path)[0].text_content()

            if turnover == '':
                continue

            if turnover.__contains__('K'):
                turnover = float(turnover.replace('K', '').replace(',', '')) * 1e3
            elif turnover.__contains__('M'):
                turnover = float(turnover.replace('M', '').replace(',', '')) * 1e6
            elif turnover.__contains__('B'):
                turnover = float(turnover.replace('B', '').replace(',', '')) * 1e9
            else:
                turnover = float(turnover.replace(',', ''))

            data = {
                "country": country_flag,
                "name": name,
                "full_name": full_name,
                "symbol": symbol,
                "last": float(last.replace(',', '')),
                "change": change,
                "turnover": int(turnover),
                "currency": etfs.loc[(etfs['name'] == name).idxmax(), 'currency']
            }

            results.append(data)
    else:
        raise RuntimeError("ERR#0092: no data found while retrieving the overview from Investing.com")

    df = pd.DataFrame(results)

    if as_json:
        return json.loads(df.to_json(orient='records'))
    else:
        return df


def search_etfs(by, value):
    """
    This function searches etfs by the introduced value for the specified field. This means that this function
    is going to search if there is a value that matches the introduced value for the specified field which is the
    `etfs.csv` column name to search in. Available fields to search etfs are 'name', 'full_name' and 'symbol'.

    Args:
        by (:obj:`str`): name of the field to search for, which is the column name ('name', 'full_name' or 'symbol').
        value (:obj:`str`): value of the field to search for, which is the str that is going to be searched.

    Returns:
        :obj:`pandas.DataFrame` - search_result:
            The resulting `pandas.DataFrame` contains the search results from the given query (the specified value
            in the specified field). If there are no results and error will be raised, but otherwise this
            `pandas.DataFrame` will contain all the available field values that match the introduced query.

    Raises:
        ValueError: raised if any of the introduced params is not valid or errored.
        FileNotFoundError: raised if `etfs.csv` file is missing.
        IOError: raised if data could not be retrieved due to file error.
        RuntimeError: raised if no results were found for the introduced value in the introduced field.
    
    """

    if not by:
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if not isinstance(by, str):
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if not value:
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    if not isinstance(value, str):
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0058: etfs file not found or errored.")

    if etfs is None:
        raise IOError("ERR#0009: etfs object not found or unable to retrieve.")

    etfs.drop(columns=['tag', 'id'], inplace=True)

    available_search_fields = etfs.columns.tolist()

    if isinstance(by, str) and by not in available_search_fields:
        raise ValueError('ERR#0026: the introduced field to search can either just be '
                         + ' or '.join(available_search_fields))

    etfs['matches'] = etfs[by].str.contains(value, case=False)

    search_result = etfs.loc[etfs['matches'] == True].copy()

    if len(search_result) == 0:
        raise RuntimeError('ERR#0043: no results were found for the introduced ' + str(by) + '.')

    search_result.drop(columns=['matches'], inplace=True)
    search_result.reset_index(drop=True, inplace=True)

    return search_result

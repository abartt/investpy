# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime, date, timedelta
import pytz

import json
from random import randint

import pandas as pd
import pkg_resources
import requests
from unidecode import unidecode
from lxml.html import fromstring

from .utils.extra import random_user_agent
from .utils.data import Data

from .data.indices_data import indices_as_df, indices_as_list, indices_as_dict
from .data.indices_data import index_countries_as_list


def get_indices(country=None):
    """
    This function retrieves all the available `indices` from Investing.com as previously listed in investpy, and
    returns them as a :obj:`pandas.DataFrame` with all the information of every available index. If the country
    filtering is applied, just the indices from the introduced country are going to be returned.
    All the available indices can be found at: https://www.investing.com/indices/world-indices and at
    https://www.investing.com/indices/world-indices, since both world and global indices are retrieved.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available indices from.

    Returns:
        :obj:`pandas.DataFrame` - indices_df:
            The resulting :obj:`pandas.DataFrame` contains all the indices information retrieved from Investing.com,
            as previously listed by investpy.

            In case the information was successfully retrieved, the :obj:`pandas.DataFrame` will look like::

                country | name | full_name | symbol | currency | class | market
                --------|------|-----------|--------|----------|-------|--------
                xxxxxxx | xxxx | xxxxxxxxx | xxxxxx | xxxxxxxx | xxxxx | xxxxxx

    Raises:
        ValueError: raised if any of the introduced parameters is missing or errored.
        FileNotFoundError: raised if the `indices.csv` file was not found.
        IOError: raised if the `indices.csv` file from `investpy` is missing or errored.
    
    """

    return indices_as_df(country=country)


def get_indices_list(country=None):
    """
    This function retrieves all the available `indices` from Investing.com as previously listed in investpy, and
    returns them as a :obj:`list` with the names of every available index. If the country filtering is applied, just
    the indices from the introduced country are going to be returned.
    All the available indices can be found at: https://www.investing.com/indices/world-indices and at
    https://www.investing.com/indices/world-indices, since both world and global indices are retrieved.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available indices from.

    Returns:
        :obj:`list` - indices_list:
            The resulting :obj:`list` contains the retrieved data, which corresponds to the index names of
            every index listed in Investing.com.

            In case the information was successfully retrieved, the :obj:`list` will look like::

                indices = ['S&P Merval', 'S&P Merval Argentina', 'S&P/BYMA Argentina General', ...]

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid or errored.
        FileNotFoundError: raised if the `indices.csv` file was not found.
        IOError: raised if the `indices.csv` file is missing or errored.
    
    """

    return indices_as_list(country=country)


def get_indices_dict(country=None, columns=None, as_json=False):
    """
    This function retrieves all the available `indices` from Investing.com as previously listed in investpy, and
    returns them as a :obj:`dict` with all the information of every available index. If the country
    filtering is applied, just the indices from the introduced country are going to be returned. Additionally, the
    columns to retrieve data from can be specified as a parameter formatted as a :obj:`list`.
    All the available indices can be found at: https://www.investing.com/indices/world-indices and at
    https://www.investing.com/indices/world-indices, since both world and global indices are retrieved.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available indices from.
        columns (:obj:`list` of :obj:`str`, optional): description
            a :obj:`list` containing the column names from which the data is going to be retrieved.
        as_json (:obj:`bool`, optional): description
            value to determine the format of the output data (:obj:`dict` or :obj:`json`).

    Returns:
        :obj:`dict` or :obj:`json` - indices_dict:
            The resulting :obj:`dict` contains the retrieved data if found, if not, the corresponding
            fields are filled with `None` values.

            In case the information was successfully retrieved, the :obj:`dict` will look like::

                indices_dict = {
                    'country': country,
                    'name': name,
                    'full_name': full_name,
                    'symbol': symbol,
                    'currency': currency,
                    'class': class,
                    'market': market
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid or errored.
        FileNotFoundError: raised if the `indices.csv` file was not found.
        IOError: raised if the `indices.csv` file is missing or errored.
    
    """

    return indices_as_dict(country=country, columns=columns, as_json=as_json)


def get_index_countries():
    """
    This function retrieves all the country names indexed in Investing.com with available indices to retrieve data
    from, via reading the `indices.csv` file from the resources directory. So on, this function will display a listing
    containing a set of countries, in order to let the user know which countries are available for indices data retrieval.

    Returns:
        :obj:`list` - countries:
            The resulting :obj:`list` contains all the available countries with indices as indexed in Investing.com

    Raises:
        FileNotFoundError: raised if the `indices.csv` file was not found.
        IOError: raised if the `indices.csv` file is missing or errored.
    
    """

    return index_countries_as_list()


def get_index_recent_data(index, country, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves recent historical data from the introduced `index` from Investing
    via Web Scraping. The resulting data can it either be stored in a :obj:`pandas.DataFrame` or in a
    :obj:`json` file, with `ascending` or `descending` order.

    Args:
        index (:obj:`str`): name of the index to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the index is.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        order (:obj:`str`, optional):
            optional argument to define the order of the retrieved data (`ascending`, `asc` or `descending`, `desc`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            recent data from the specified index via argument. The dataset contains the open, high, low, close and volume
            values for the selected index on market days, additionally the currency value is returned.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx

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
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised if there was an argument error.
        IOError: raised if indices object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced index does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if index information was unavailable or not found.

    Examples:
        >>> data = investpy.get_index_recent_data(index='ibex 35', country='spain')
        >>> data.head()
                       Open     High      Low    Close   Volume Currency
        Date
        2019-08-26  12604.7  12646.3  12510.4  12621.3  4770000      EUR
        2019-08-27  12618.3  12723.3  12593.6  12683.8  8230000      EUR
        2019-08-28  12657.2  12697.2  12585.1  12642.5  7300000      EUR
        2019-08-29  12637.2  12806.6  12633.8  12806.6  5650000      EUR
        2019-08-30  12767.6  12905.9  12756.9  12821.6  6040000      EUR

    """

    if not index:
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if not isinstance(index, str):
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

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
    resource_path = '/'.join(('resources', 'indices.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_index_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    indices = indices[indices['country'] == country]

    index = unidecode(index.strip().lower())

    if index not in list(indices['name'].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0045: index " + index + " not found, check if it is correct.")

    full_name = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'full_name']
    id_ = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'id']
    name = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'name']

    index_currency = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'currency']

    header = full_name + ' Historical Data'

    params = {
        "curr_id": id_,
        "smlID": str(randint(1000000, 99999999)),
        "header": header,
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

    root_ = fromstring(req.text)
    path_ = root_.xpath(".//table[@id='curr_table']/tbody/tr")
    
    result = list()

    if path_:
        for elements_ in path_:
            if elements_.xpath(".//td")[0].text_content() == 'No results found':
                raise IndexError("ERR#0046: index information unavailable or not found.")

            info = []
        
            for nested_ in elements_.xpath(".//td"):
                info.append(nested_.get('data-real-value'))

            index_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0]), tz=pytz.timezone('GMT')).date()), '%Y-%m-%d')
            
            index_close = float(info[1].replace(',', ''))
            index_open = float(info[2].replace(',', ''))
            index_high = float(info[3].replace(',', ''))
            index_low = float(info[4].replace(',', ''))

            index_volume = int(info[5])

            result.insert(len(result), Data(index_date, index_open, index_high, index_low,
                                            index_close, index_volume, index_currency, None))

        if order in ['ascending', 'asc']:
            result = result[::-1]
        elif order in ['descending', 'desc']:
            result = result

        if as_json is True:
            json_ = {
                'name': name,
                'recent':
                    [value.index_as_json() for value in result]
            }

            return json.dumps(json_, sort_keys=False)
        elif as_json is False:
            df = pd.DataFrame.from_records([value.index_to_dict() for value in result])
            df.set_index('Date', inplace=True)

            return df
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")

def get_index_futures_recent_data(index, country, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves recent historical data from the introduced `index futures` from Investing
    via Web Scraping. The resulting data can it either be stored in a :obj:`pandas.DataFrame` or in a
    :obj:`json` file, with `ascending` or `descending` order.

    Args:
        index (:obj:`str`): name of the index to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the index is.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        order (:obj:`str`, optional):
            optional argument to define the order of the retrieved data (`ascending`, `asc` or `descending`, `desc`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            recent data from the specified index via argument. The dataset contains the open, high, low, close and volume
            values for the selected index on market days, additionally the currency value is returned.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx

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
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised if there was an argument error.
        IOError: raised if indices object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced index does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if index information was unavailable or not found.

    Examples:
        >>> investpy.get_index_recent_data(index='ibex 35', country='spain')
                           Open     High      Low    Close   Volume Currency
            Date
            2019-08-26  12604.7  12646.3  12510.4  12621.3  4770000      EUR
            2019-08-27  12618.3  12723.3  12593.6  12683.8  8230000      EUR
            2019-08-28  12657.2  12697.2  12585.1  12642.5  7300000      EUR
            2019-08-29  12637.2  12806.6  12633.8  12806.6  5650000      EUR
            2019-08-30  12767.6  12905.9  12756.9  12821.6  6040000      EUR

    """

    if not index:
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if not isinstance(index, str):
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if interval not in ['Daily', 'Weekly', 'Monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'indices', 'indices_f.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    if unidecode.unidecode(country.lower()) not in get_index_countries():
        raise RuntimeError("ERR#0034: country " + country.lower() + " not found, check if it is correct.")

    indices = indices[indices['country'] == unidecode.unidecode(country.lower())]

    index = index.strip()
    index = index.lower()

    if unidecode.unidecode(index) not in [unidecode.unidecode(value.lower()) for value in indices['name'].tolist()]:
        raise RuntimeError("ERR#0045: index " + index + " not found, check if it is correct.")

    full_name = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'full_name']
    id_ = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'id']
    name = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'name']

    index_currency = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'currency']

    header = full_name + ' Historical Data'

    params = {
        "curr_id": id_,
        "smlID": str(randint(1000000, 99999999)),
        "header": header,
        "interval_sec": interval,
        "sort_col": "date",
        "sort_ord": "DESC",
        "action": "historical_data"
    }

    head = {
        "User-Agent": get_random(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
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
                raise IndexError("ERR#0046: index information unavailable or not found.")

            info = []
        
            for nested_ in elements_.xpath(".//td"):
                info.append(nested_.get('data-real-value'))

            index_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
            
            index_close = float(info[1].replace(',', ''))
            index_open = float(info[2].replace(',', ''))
            index_high = float(info[3].replace(',', ''))
            index_low = float(info[4].replace(',', ''))

            index_volume = int(info[5])

            result.insert(len(result), Data(index_date, index_open, index_high, index_low,
                                            index_close, index_volume, index_currency, None))

        if order in ['ascending', 'asc']:
            result = result[::-1]
        elif order in ['descending', 'desc']:
            result = result

        if as_json is True:
            json_ = {'name': name,
                     'recent':
                         [value.index_as_json() for value in result]
                     }

            return json.dumps(json_, sort_keys=False)
        elif as_json is False:
            df = pd.DataFrame.from_records([value.index_to_dict() for value in result])
            df.set_index('Date', inplace=True)

            return df
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")

def get_futures_symbols():
    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'indices', 'indices_f.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    return indices['name'].tolist()   

def get_index_historical_data(index, country, from_date, to_date, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves historical data of the introduced `index` (from the specified country, note that both
    index and country should match since if the introduced index is not listed in the indices of that country, the
    function will raise an error). The retrieved historical data are the OHLC values plus the Volume and the Currency in
    which those values are specified, from the introduced date range if valid. So on, the resulting data can it either be
    stored in a :obj:`pandas.DataFrame` or in a :obj:`json` file.

    Args:
        index (:obj:`str`): name of the index to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the index is.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            historical data from the specified index via argument. The dataset contains the open, high, low, close and
            volume values for the selected index on market days, additionally the currency in which those values are
            specified is returned.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx

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
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised if there was an argument error.
        IOError: raised if indices object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced index does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if index information was unavailable or not found.

    Examples:
        >>> data = investpy.get_index_historical_data(index='ibex 35', country='spain', from_date='01/01/2018', to_date='01/01/2019')
        >>> data.head()
                       Open     High      Low    Close    Volume Currency
        Date
        2018-01-02  15128.2  15136.7  14996.6  15096.8  10340000      EUR
        2018-01-03  15145.0  15186.9  15091.9  15106.9  12800000      EUR
        2018-01-04  15105.5  15368.7  15103.7  15368.7  17070000      EUR
        2018-01-05  15353.9  15407.5  15348.6  15398.9  11180000      EUR
        2018-01-08  15437.1  15448.7  15344.0  15373.3  12890000      EUR

    """

    if not index:
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if not isinstance(index, str):
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

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
    resource_path = '/'.join(('resources', 'indices.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_index_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    indices = indices[indices['country'] == country]

    index = unidecode(index.strip().lower())

    if index not in list(indices['name'].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0045: index " + index + " not found, check if it is correct.")

    full_name = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'full_name']
    id_ = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'id']
    name = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'name']

    index_currency = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'currency']

    final = list()

    header = full_name + ' Historical Data'

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
                        raise IndexError("ERR#0046: index information unavailable or not found.")
                else:
                    data_flag = True

                info = []
        
                for nested_ in elements_.xpath(".//td"):
                    info.append(nested_.get('data-real-value'))

                if data_flag is True:
                    index_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0]), tz=pytz.timezone('GMT')).date()), '%Y-%m-%d')
                    
                    index_close = float(info[1].replace(',', ''))
                    index_open = float(info[2].replace(',', ''))
                    index_high = float(info[3].replace(',', ''))
                    index_low = float(info[4].replace(',', ''))

                    index_volume = int(info[5])

                    result.insert(len(result), Data(index_date, index_open, index_high, index_low,
                                                    index_close, index_volume, index_currency, None))
            if data_flag is True:
                if order in ['ascending', 'asc']:
                    result = result[::-1]
                elif order in ['descending', 'desc']:
                    result = result

                if as_json is True:
                    json_list = [value.index_as_json() for value in result]
                    
                    final.append(json_list)
                elif as_json is False:
                    df = pd.DataFrame.from_records([value.index_to_dict() for value in result])
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

def get_index_futures_historical_data(index, country, from_date, to_date, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves historical data of the introduced `index futures` (from the specified country, note that both
    index and country should match since if the introduced index is not listed in the indices of that country, the
    function will raise an error). The retrieved historical data are the OHLC values plus the Volume and the Currency in
    which those values are specified, from the introduced date range if valid. So on, the resulting data can it either be
    stored in a :obj:`pandas.DataFrame` or in a :obj:`json` file.

    Args:
        index (:obj:`str`): name of the index to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the index is.
        from_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, from where data is going to be retrieved.
        to_date (:obj:`str`): date as `str` formatted as `dd/mm/yyyy`, until where data is going to be retrieved.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved
            historical data from the specified index via argument. The dataset contains the open, high, low, close and
            volume values for the selected index on market days, additionally the currency in which those values are
            specified is returned.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close | Volume | Currency
                -----||------|------|-----|-------|--------|----------
                xxxx || xxxx | xxxx | xxx | xxxxx | xxxxxx | xxxxxxxx

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
                            currency: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised if there was an argument error.
        IOError: raised if indices object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced index does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if index information was unavailable or not found.

    Examples:
        >>> investpy.get_index_historical_data(index='ibex 35', country='spain', from_date='01/01/2018', to_date='01/01/2019')
                           Open     High      Low    Close    Volume Currency
            Date
            2018-01-02  15128.2  15136.7  14996.6  15096.8  10340000      EUR
            2018-01-03  15145.0  15186.9  15091.9  15106.9  12800000      EUR
            2018-01-04  15105.5  15368.7  15103.7  15368.7  17070000      EUR
            2018-01-05  15353.9  15407.5  15348.6  15398.9  11180000      EUR
            2018-01-08  15437.1  15448.7  15344.0  15373.3  12890000      EUR

    """

    if not index:
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if not isinstance(index, str):
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

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

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    if order not in ['ascending', 'asc', 'descending', 'desc']:
        raise ValueError("ERR#0003: order argument can just be ascending (asc) or descending (desc), str type.")

    if not interval:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if not isinstance(interval, str):
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

    if interval not in ['Daily', 'Weekly', 'Monthly']:
        raise ValueError("ERR#0073: interval value should be a str type and it can just be either 'Daily', 'Weekly' or 'Monthly'.")

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

            start_date = start_date.replace(year=start_date.year + 19, day=start_date.day + 1)
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
    resource_path = '/'.join(('resources', 'indices', 'indices_f.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    if unidecode.unidecode(country.lower()) not in get_index_countries():
        raise RuntimeError("ERR#0034: country " + country.lower() + " not found, check if it is correct.")

    indices = indices[indices['country'] == unidecode.unidecode(country.lower())]

    index = index.strip()
    index = index.lower()

    if unidecode.unidecode(index) not in [unidecode.unidecode(value.lower()) for value in indices['name'].tolist()]:
        raise RuntimeError("ERR#0045: index " + index + " not found, check if it is correct.")

    full_name = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'full_name']
    id_ = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'id']
    name = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'name']

    index_currency = indices.loc[(indices['name'].str.lower() == index).idxmax(), 'currency']

    final = list()

    header = full_name + ' Historical Data'

    for index in range(len(date_interval['intervals'])):
        interval_counter += 1

        params = {
            "curr_id": id_,
            "smlID": str(randint(1000000, 99999999)),
            "header": header,
            "st_date": date_interval['intervals'][index]['start'],
            "end_date": date_interval['intervals'][index]['end'],
            "interval_sec": interval,
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }

        head = {
            "User-Agent": get_random(),
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "text/html",
            "Accept-Encoding": "gzip, deflate, br",
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
                        raise IndexError("ERR#0046: index information unavailable or not found.")
                else:
                    data_flag = True

                info = []
        
                for nested_ in elements_.xpath(".//td"):
                    info.append(nested_.get('data-real-value'))

                if data_flag is True:
                    index_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
                    
                    index_close = float(info[1].replace(',', ''))
                    index_open = float(info[2].replace(',', ''))
                    index_high = float(info[3].replace(',', ''))
                    index_low = float(info[4].replace(',', ''))

                    index_volume = int(info[5])

                    result.insert(len(result), Data(index_date, index_open, index_high, index_low,
                                                    index_close, index_volume, index_currency, None))
            if data_flag is True:
                if order in ['ascending', 'asc']:
                    result = result[::-1]
                elif order in ['descending', 'desc']:
                    result = result

                if as_json is True:
                    json_ = {'name': name,
                             'historical':
                                 [value.index_as_json() for value in result]
                             }

                    final.append(json_)
                elif as_json is False:
                    df = pd.DataFrame.from_records([value.index_to_dict() for value in result])
                    df.set_index('Date', inplace=True)

                    final.append(df)
        else:
            raise RuntimeError("ERR#0004: data retrieval error while scraping.")

    if as_json is True:
        return json.dumps(final[0], sort_keys=False)
    elif as_json is False:
        return pd.concat(final)


def get_index_information(index, country, as_json=False):
    """
    This function retrieves fundamental financial information from the specified index. The retrieved 
    information from the index can be valuable as it is additional information that can be used combined 
    with OHLC values, so to determine financial insights from the company which holds the specified index.

    Args:
        index (:obj:`str`): name of the index to retrieve recent historical data from.
        country (:obj:`str`): name of the country from where the index is.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`dict` or :obj:`json`).

    Returns:
        :obj:`pandas.DataFrame` or :obj:`dict`- index_information:
            The resulting :obj:`pandas.DataFrame` contains the information fields retrieved from Investing.com
            from the specified index; it can also be returned as a :obj:`dict`, if argument `as_json=True`.

            If any of the information fields could not be retrieved, that field/s will be filled with
            None values. If the retrieval process succeeded, the resulting :obj:`dict` will look like::

                index_information = {
                    "Index Name": "S&P Merval",
                    "Prev. Close": 36769.59,
                    "Volume": None,
                    "Todays Range": "36,769.59 - 37,894.32",
                    "Open": 36769.59,
                    "Average Vol. (3m)": None,
                    "52 wk Range": "22,484.4 - 44,470.76",
                    "1-Year Change": "18.19%"
                }

    Raises:
        ValueError: raised if any of the introduced arguments is not valid or errored.
        FileNotFoundError: raised if `indices.csv` file was not found or errored.
        IOError: raised if `indices.csv` file is empty or errored.
        RuntimeError: raised if scraping process failed while running.
        ConnectionError: raised if the connection to Investing.com errored (did not return HTTP 200)

    """

    if not index:
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if not isinstance(index, str):
        raise ValueError("ERR#0047: index param is mandatory and should be a str.")

    if country is None:
        raise ValueError("ERR#0039: country can not be None, it should be a str.")

    if country is not None and not isinstance(country, str):
        raise ValueError("ERR#0025: specified country value not valid.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'indices.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_index_countries():
        raise RuntimeError("ERR#0034: country " + country + " not found, check if it is correct.")

    indices = indices[indices['country'] == country]

    index = unidecode(index.strip().lower())

    if index not in list(indices['name'].apply(unidecode).str.lower()):
        raise RuntimeError("ERR#0045: index " + index + " not found, check if it is correct.")

    name = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'name']
    tag = indices.loc[(indices['name'].apply(unidecode).str.lower() == index).idxmax(), 'tag']

    url = "https://www.investing.com/indices/" + tag

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

    result = pd.DataFrame(columns=['Index Name', 'Prev. Close', 'Volume', 'Todays Range', 'Open',
                                   'Average Vol. (3m)', '52 wk Range', '1-Year Change'])
    result.at[0, 'Index Name'] = name

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


def get_indices_overview(country, as_json=False, n_results=100):
    """
    This function retrieves an overview containing all the real time data available for the main indices from a country,
    such as the names, symbols, current value, etc. as indexed in Investing.com. So on, the main usage of this
    function is to get an overview on the main indices from a country, so to get a general view. Note that since 
    this function is retrieving a lot of information at once, by default just the overview of the Top 100 indices 
    is being retrieved, but an additional parameter called n_results can be specified so to retrieve N results.

    Args:
        country (:obj:`str`): name of the country to retrieve the indices overview from.
        as_json (:obj:`bool`, optional):
            optional argument to determine the format of the output data (:obj:`pandas.DataFrame` or :obj:`json`).
        n_results (:obj:`int`, optional): number of results to be displayed on the overview table (0-1000).

    Returns:
        :obj:`pandas.DataFrame` - indices_overview:
            The resulting :obj:`pandas.DataFrame` contains all the data available in Investing.com of the main indices
            from a country in order to get an overview of it.

            If the retrieval process succeeded, the resulting :obj:`pandas.DataFrame` should look like::

                country | name | last | high | low | change | change_percentage | currency
                --------|------|------|------|-----|--------|-------------------|----------
                xxxxxxx | xxxx | xxxx | xxxx | xxx | xxxxxx | xxxxxxxxxxxxxxxxx | xxxxxxxx
    
    Raises:
        ValueError: raised if any of the introduced arguments is not valid or errored.
        FileNotFoundError: raised when `indices.csv` file is missing.
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
    resource_path = '/'.join(('resources', 'indices.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    country = unidecode(country.strip().lower())

    if country not in get_index_countries():
        raise ValueError("ERR#0034: country " + country + " not found, check if it is correct.")

    indices = indices[indices['country'] == country]

    if country == 'united states':
        country= 'usa'
    elif country == 'united kingdom':
        country = 'uk'

    head = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    url = "https://www.investing.com/indices/" + country.replace(' ', '-') + "-indices?&majorIndices=on&primarySectors=on&additionalIndices=on&otherIndices=on"

    req = requests.get(url, headers=head)

    if req.status_code != 200:
        raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

    root_ = fromstring(req.text)
    table = root_.xpath(".//table[@id='cr1']/tbody/tr")

    results = list()

    if len(table) > 0:
        for row in table[:n_results]:
            id_ = row.get('id').replace('pair_', '')
            country_check = row.xpath(".//td[@class='flag']/span")[0].get('title').lower()

            if country_check == 'bosnia-herzegovina':
                country_check = 'bosnia'
            elif country_check == 'palestinian territory':
                country_check = 'palestine'
            elif country_check == 'united arab emirates':
                country_check = 'dubai'
            elif country_check == "cote d'ivoire":
                country_check = 'ivory coast'

            name = row.xpath(".//td[contains(@class, 'elp')]/a")[0].text_content().strip()

            pid = 'pid-' + id_

            last = row.xpath(".//td[@class='" + pid + "-last']")[0].text_content()
            high = row.xpath(".//td[@class='" + pid + "-high']")[0].text_content()
            low = row.xpath(".//td[@class='" + pid + "-low']")[0].text_content()

            pc = row.xpath(".//td[contains(@class, '" + pid + "-pc')]")[0].text_content()
            pcp = row.xpath(".//td[contains(@class, '" + pid + "-pcp')]")[0].text_content()

            data = {
                "country": country_check,
                "name": name,
                "last": float(last.replace(',', '')),
                "high": float(high.replace(',', '')),
                "low": float(low.replace(',', '')),
                "change": pc,
                "change_percentage": pcp,
                "currency": indices.loc[(indices['name'] == name).idxmax(), 'currency']
            }

            results.append(data)
    else:
        raise RuntimeError("ERR#0092: no data found while retrieving the overview from Investing.com")

    df = pd.DataFrame(results)

    if as_json:
        return json.loads(df.to_json(orient='records'))
    else:
        return df


def search_indices(by, value):
    """
    This function searches indices by the introduced value for the specified field. This means that this function
    is going to search if there is a value that matches the introduced value for the specified field which is the
    `indices.csv` column name to search in. Available fields to search indices are 'name', 'full_name' and 'symbol'.

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
       FileNotFoundError: raised if `indices.csv` file is missing.
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
    resource_path = '/'.join(('resources', 'indices.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        indices = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path), keep_default_na=False)
    else:
        raise FileNotFoundError("ERR#0059: indices file not found or errored.")

    if indices is None:
        raise IOError("ERR#0037: indices not found or unable to retrieve.")

    indices.drop(columns=['tag', 'id'], inplace=True)

    available_search_fields = indices.columns.tolist()

    if isinstance(by, str) and by not in available_search_fields:
        raise ValueError('ERR#0026: the introduced field to search can either just be '
                         + ' or '.join(available_search_fields))

    indices['matches'] = indices[by].str.contains(value, case=False)

    search_result = indices.loc[indices['matches'] == True].copy()

    if len(search_result) == 0:
        raise RuntimeError('ERR#0043: no results were found for the introduced ' + str(by) + '.')

    search_result.drop(columns=['matches'], inplace=True)
    search_result.reset_index(drop=True, inplace=True)

    return search_result

#!/usr/bin/python3

# Copyright 2018-2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

from datetime import datetime, date
import json
import re
from random import randint

import pandas as pd
import pkg_resources
import requests
import unidecode
from lxml.html import fromstring

from investpy.utils.user_agent import get_random
from investpy.utils.data import Data

from investpy.data.certificates_data import certificates_as_df, certificates_as_list, certificates_as_dict
from investpy.data.certificates_data import certificate_countries_as_list


def get_certificates(country=None):
    """
    This function retrieves all the data stored in `certificates.csv` file, which previously was retrieved from 
    Investing.com. Since the resulting object is a matrix of data, the certificate's data is properly structured 
    in rows and columns, where columns are the certificate data attribute names. Additionally, country
    filtering can be specified, which will make this function return not all the stored certificates, but just
    the data of the certificates from the introduced country.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available certificates from.

    Returns:
        :obj:`pandas.DataFrame` - certificates_df:
            The resulting :obj:`pandas.DataFrame` contains all the certificate's data from the introduced country if specified,
            or from every country if None was specified, as indexed in Investing.com from the information previously
            retrieved by investpy and stored on a csv file.

            So on, the resulting :obj:`pandas.DataFrame` will look like::

                country | name | full_name | symbol | issuer | isin | asset_class | underlying
                --------|------|-----------|--------|--------|------|-------------|------------
                xxxxxxx | xxxx | xxxxxxxxx | xxxxxx | xxxxxx | xxxx | xxxxxxxxxxx | xxxxxxxxxx

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
        FileNotFoundError: raised if certificates file was not found.
        IOError: raised when certificates file is missing or empty.

    """

    return certificates_as_df(country)


def get_certificates_list(country=None):
    """
    This function retrieves all the available etfs indexed on Investing.com, already stored on `etfs.csv`.
    This function also allows the users to specify which country do they want to retrieve data from or if they
    want to retrieve it from every listed country; so on, a listing of etfs will be returned. This function
    helps the user to get to know which etfs are available on Investing.com.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available etfs from.

    Returns:
        :obj:`list` - certificates_list:
            The resulting :obj:`list` contains the retrieved data from the `etfs.csv` file, which is
            a listing of the names of the etfs listed on Investing.com, which is the input for data
            retrieval functions as the name of the etf to retrieve data from needs to be specified.

            In case the listing was successfully retrieved, the :obj:`list` will look like::

                certificates_list = ['SOCIETE GENERALE CAC 40 X10 31DEC99', 'COMMERZBANK SG 31Dec99', ...]

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
        FileNotFoundError: raised if certificates file was not found.
        IOError: raised when certificates file is missing or empty.
    
    """

    return certificates_as_list(country)


def get_certificates_dict(country=None, columns=None, as_json=False):
    """
    This function retrieves all the available certificates indexed on Investing.com, stored on `certificates.csv`.
    This function also allows the user to specify which country do they want to retrieve data from, or from every 
    listed country; the columns which the user wants to be included on the resulting :obj:`dict`; and the output 
    of the function will either be a :obj:`dict` or a :obj:`json`.

    Args:
        country (:obj:`str`, optional): name of the country to retrieve all its available certificates from.
        columns (:obj:`list`, optional):
            names of the columns of the etf data to retrieve <country, name, full_name, symbol, issuer, isin, asset_class, underlying>
        as_json (:obj:`bool`, optional):
            value to determine the format of the output data which can either be a :obj:`dict` or a :obj:`json`.

    Returns:
        :obj:`dict` or :obj:`json` - etfs_dict:
            The resulting :obj:`dict` contains the retrieved data if found, if not, the corresponding fields are
            filled with `None` values.

            In case the information was successfully retrieved, the :obj:`dict` will look like::

                {
                    "country": "france",
                    "name": "SOCIETE GENERALE CAC 40 X10 31DEC99",
                    "full_name": "SOCIETE GENERALE EFFEKTEN GMBH ZT CAC 40 X10 LEVERAGE 31DEC99",
                    "symbol": "FR0011214527",
                    "issuer": "Societe Generale Effekten GMBH",
                    "isin": "FR0011214527",
                    "asset_class": "index",
                    "underlying": "CAC 40 Leverage x10 NR"
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid.
        FileNotFoundError: raised if certificates file was not found.
        IOError: raised when certificates file is missing or empty.
    
    """

    return certificates_as_dict(country=country, columns=columns, as_json=as_json)


def get_certificate_countries():
    """
    This function retrieves all the available countries to retrieve certificates from, as the listed countries 
    are the ones indexed on Investing.com. The purpose of this function is to list the countries which 
    have available certificates according to Investing.com data, since the country parameter is needed when
    retrieving data from any certificate available.

    Returns:
        :obj:`list` - countries:
            The resulting :obj:`list` contains all the countries listed on Investing.com with available certificates
            to retrieve data from.

            In the case that the file reading of `certificate_countries.csv` which contains the names of the available
            countries with certificates was successfully completed, the resulting :obj:`list` will look like::

                countries = ['france', 'germany', 'italy', 'netherlands', 'sweden']

    Raises:
        FileNotFoundError: raised when certificate countries file was not found.
    
    """

    return certificate_countries_as_list()


def get_certificate_recent_data(certificate, country, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves recent historical data from the introduced certificate from Investing.com. So on, the recent data
    of the introduced certificate from the specified country will be retrieved and returned as a :obj:`pandas.DataFrame` if
    the parameters are valid and the request to Investing.com succeeds. Note that additionally some optional parameters
    can be specified: as_json and order, which let the user decide if the data is going to be returned as a
    :obj:`json` or not, and if the historical data is going to be ordered ascending or descending (where the index is the 
    date), respectively.

    Args:
        certificate (:obj:`str`): name of the certificate to retrieve recent data from.
        country (:obj:`str`): name of the country from where the certificate is.
        as_json (:obj:`bool`, optional):
            to determine the format of the output data, either a :obj:`pandas.DataFrame` if False and a :obj:`json` if True.
        order (:obj:`str`, optional): to define the order of the retrieved data which can either be ascending or descending.
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function returns either a :obj:`pandas.DataFrame` or a :obj:`json` file containing the retrieved recent 
            data from the specified certificate via argument. The dataset contains the OHLC values of the certificate.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close 
                -----||------|------|-----|-------
                xxxx || xxxx | xxxx | xxx | xxxxx 

            but if we define `as_json=True`, then the output will be::

                {
                    name: name,
                    recent: [
                        {
                            date: dd/mm/yyyy,
                            open: x,
                            high: x,
                            low: x,
                            close: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised if there was an argument error.
        IOError: raised if indices object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced certificate does not match any of the indexed ones.
        ConnectionError: raised if GET requests does not return 200 status code.
        IndexError: raised if certificate information was unavailable or not found.

    Examples:
        >>> investpy.get_certificate_recent_data(certificate='COMMERZBANK Call ALIBABA GROUP', country='france')
                        Open  High   Low  Close
            Date                               
            2019-11-27  5.47  5.47  5.47   5.47
            2019-12-05  5.52  5.52  5.52   5.52
            2019-12-10  5.37  5.37  5.37   5.37
            2019-12-12  6.27  6.27  6.27   6.27
            2019-12-16  6.80  6.80  6.80   6.80
            2019-12-20  7.50  7.50  7.50   7.50

    """

    if not certificate:
        raise ValueError("ERR#0100: certificate param is mandatory and should be a str.")

    if not isinstance(certificate, str):
        raise ValueError("ERR#0100: certificate param is mandatory and should be a str.")

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
    resource_path = '/'.join(('resources', 'certificates', 'certificates.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        certificates = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0096: certificates file not found or errored.")

    if certificates is None:
        raise IOError("ERR#0097: certificates not found or unable to retrieve.")

    if unidecode.unidecode(country.lower()) not in get_certificate_countries():
        raise RuntimeError("ERR#0034: country " + country.lower() + " not found, check if it is correct.")

    certificates = certificates[certificates['country'] == unidecode.unidecode(country.lower())]

    certificate = certificate.strip()
    certificate = certificate.lower()

    if unidecode.unidecode(certificate) not in [unidecode.unidecode(value.lower()) for value in certificates['name'].tolist()]:
        raise RuntimeError("ERR#0101: certificate " + certificate + " not found, check if it is correct.")

    symbol = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'symbol']
    id_ = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'id']
    name = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'name']

    header = symbol + ' Historical Data'

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
                raise IndexError("ERR#0102: certificate information unavailable or not found.")

            info = []
        
            for nested_ in elements_.xpath(".//td"):
                info.append(nested_.get('data-real-value'))

            certificate_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
            
            certificate_close = float(info[1].replace(',', ''))
            certificate_open = float(info[2].replace(',', ''))
            certificate_high = float(info[3].replace(',', ''))
            certificate_low = float(info[4].replace(',', ''))

            result.insert(len(result), Data(certificate_date, certificate_open, certificate_high,
                                            certificate_low, certificate_close, None, None))

        if order in ['ascending', 'asc']:
            result = result[::-1]
        elif order in ['descending', 'desc']:
            result = result

        if as_json is True:
            json_ = {
                'name': name,
                'recent':
                    [value.certificate_as_json() for value in result]
            }

            return json.dumps(json_, sort_keys=False)
        elif as_json is False:
            df = pd.DataFrame.from_records([value.certificate_to_dict() for value in result])
            df.set_index('Date', inplace=True)

            return df
    else:
        raise RuntimeError("ERR#0004: data retrieval error while scraping.")


def get_certificate_historical_data(certificate, country, from_date, to_date, as_json=False, order='ascending', interval='Daily'):
    """
    This function retrieves historical data from the introduced certificate from Investing.com. So on, the historical data
    of the introduced certificate from the specified country in the specified date range will be retrieved and returned as
    a :obj:`pandas.DataFrame` if the parameters are valid and the request to Investing.com succeeds. Note that additionally
    some optional parameters can be specified: as_json and order, which let the user decide if the data is going to
    be returned as a :obj:`json` or not, and if the historical data is going to be ordered ascending or descending (where the
    index is the date), respectively.

    Args:
        certificate (:obj:`str`): name of the certificate to retrieve historical data from.
        country (:obj:`str`): name of the country from where the certificate is.
        from_date (:obj:`str`): date formatted as `dd/mm/yyyy`, since when data is going to be retrieved.
        to_date (:obj:`str`): date formatted as `dd/mm/yyyy`, until when data is going to be retrieved.
        as_json (:obj:`bool`, optional):
            to determine the format of the output data, either a :obj:`pandas.DataFrame` if False and a :obj:`json` if True.
        order (:obj:`str`, optional): to define the order of the retrieved data which can either be ascending or descending.
        interval (:obj:`str`, optional):
            value to define the historical data interval to retrieve, by default `Daily`, but it can also be `Weekly` or `Monthly`.

    Returns:
        :obj:`pandas.DataFrame` or :obj:`json`:
            The function can return either a :obj:`pandas.DataFrame` or a :obj:`json` object, containing the retrieved
            historical data of the specified certificate from the specified country. So on, the resulting dataframe contains the
            OHLC values for the selected certificate on market days.

            The returned data is case we use default arguments will look like::

                Date || Open | High | Low | Close 
                -----||------|------|-----|-------
                xxxx || xxxx | xxxx | xxx | xxxxx 

            but if we define `as_json=True`, then the output will be::

                {
                    name: name,
                    historical: [
                        {
                            date: 'dd/mm/yyyy',
                            open: x,
                            high: x,
                            low: x,
                            close: x
                        },
                        ...
                    ]
                }

    Raises:
        ValueError: raised whenever any of the introduced arguments is not valid or errored.
        IOError: raised if certificates object/file was not found or unable to retrieve.
        RuntimeError: raised if the introduced certificate/country was not found or did not match any of the existing ones.
        ConnectionError: raised if connection to Investing.com could not be established.
        IndexError: raised if certificate historical data was unavailable or not found in Investing.com.

    Examples:
        >>> investpy.get_certificate_historical_data(certificate='COMMERZBANK Call ALIBABA GROUP', country='france', from_date='01/01/2010', to_date='01/01/2019')
                         Open   High    Low  Close
            Date                                  
            2018-03-14  39.77  39.77  39.77  39.77
            2018-03-15  48.18  48.18  48.18  46.48
            2018-03-16  46.48  46.48  46.48  46.48
            2018-03-19  40.73  40.73  40.73  40.73
            2018-03-20  44.61  44.61  44.61  44.61

    """

    if not certificate:
        raise ValueError("ERR#0100: certificate param is mandatory and should be a str.")

    if not isinstance(certificate, str):
        raise ValueError("ERR#0100: certificate param is mandatory and should be a str.")

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

    try:
        datetime.strptime(from_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0011: incorrect from_date date format, it should be 'dd/mm/yyyy'.")

    try:
        datetime.strptime(to_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("ERR#0012: incorrect to_date format, it should be 'dd/mm/yyyy'.")

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

        if diff > 20:
            obj = {
                'start': start_date.strftime('%m/%d/%Y'),
                'end': start_date.replace(year=start_date.year + 20).strftime('%m/%d/%Y'),
            }

            date_interval['intervals'].append(obj)

            start_date = start_date.replace(year=start_date.year + 20)
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
    resource_path = '/'.join(('resources', 'certificates', 'certificates.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        certificates = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0096: certificates file not found or errored.")

    if certificates is None:
        raise IOError("ERR#0097: certificates not found or unable to retrieve.")

    if unidecode.unidecode(country.lower()) not in get_certificate_countries():
        raise RuntimeError("ERR#0034: country " + country.lower() + " not found, check if it is correct.")

    certificates = certificates[certificates['country'] == unidecode.unidecode(country.lower())]

    certificate = certificate.strip()
    certificate = certificate.lower()

    if unidecode.unidecode(certificate) not in [unidecode.unidecode(value.lower()) for value in certificates['name'].tolist()]:
        raise RuntimeError("ERR#0101: certificate " + certificate + " not found, check if it is correct.")

    symbol = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'symbol']
    id_ = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'id']
    name = certificates.loc[(certificates['name'].str.lower() == certificate).idxmax(), 'name']

    header = symbol + ' Historical Data'

    final = list()

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
                        raise IndexError("ERR#0102: certificate information unavailable or not found.")
                else:
                    data_flag = True
                
                info = []
            
                for nested_ in elements_.xpath(".//td"):
                    info.append(nested_.get('data-real-value'))

                if data_flag is True:
                    certificate_date = datetime.strptime(str(datetime.fromtimestamp(int(info[0])).date()), '%Y-%m-%d')
            
                    certificate_close = float(info[1].replace(',', ''))
                    certificate_open = float(info[2].replace(',', ''))
                    certificate_high = float(info[3].replace(',', ''))
                    certificate_low = float(info[4].replace(',', ''))

                    result.insert(len(result), Data(certificate_date, certificate_open, certificate_high,
                                                    certificate_low, certificate_close, None, None))

            if data_flag is True:
                if order in ['ascending', 'asc']:
                    result = result[::-1]
                elif order in ['descending', 'desc']:
                    result = result

                if as_json is True:
                    json_ = {
                        'name': name,
                        'historical':
                            [value.certificate_as_json() for value in result]
                    }
                    
                    final.append(json_)
                elif as_json is False:
                    df = pd.DataFrame.from_records([value.certificate_to_dict() for value in result])
                    df.set_index('Date', inplace=True)

                    final.append(df)

        else:
            raise RuntimeError("ERR#0004: data retrieval error while scraping.")

    if as_json is True:
        return json.dumps(final[0], sort_keys=False)
    elif as_json is False:
        return pd.concat(final)


def get_certificate_information():
    return None


def get_certificates_overview():
    return None


def search_certificates(by, value):
    """
    This function searches certificates by the introduced value for the specified field. This means that this function
    is going to search if there is a value that matches the introduced one for the specified field which is the
    `certificates.csv` column name to search in. Available fields to search certificates are `country`, `name`, 
    `full_name`, `symbol`, `issuer`, `isin`, `asset_class`, `underlying`.

    Args:
        by (:obj:`str`):
            name of the field to search for, which is the column name which can be: country, name, full_name, symbol,
            issuer, isin, asset_class or underlying.
        value (:obj:`str`): value of the field to search for, which is the value that is going to be searched.

    Returns:
        :obj:`pandas.DataFrame` - search_result:
            The resulting :obj:`pandas.DataFrame` contains the search results from the given query, which is
            any match of the specified value in the specified field. If there are no results for the given query,
            an error will be raised, but otherwise the resulting :obj:`pandas.DataFrame` will contain all the
            available certificates that match the introduced query.

    Raises:
        ValueError: raised if any of the introduced parameters is not valid or errored.
        IOError: raised if data could not be retrieved due to file error.
        RuntimeError: raised if no results were found for the introduced value in the introduced field.

    """

    resource_package = 'investpy'
    resource_path = '/'.join(('resources', 'certificates', 'certificates.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        certificates = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0096: certificates file not found or errored.")

    if certificates is None:
        raise IOError("ERR#0097: certificates not found or unable to retrieve.")

    certificates.drop(columns=['tag', 'id'], inplace=True)

    available_search_fields = certificates.columns.tolist()

    if not by:
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if not isinstance(by, str):
        raise ValueError('ERR#0006: the introduced field to search is mandatory and should be a str.')

    if isinstance(by, str) and by not in available_search_fields:
        raise ValueError('ERR#0026: the introduced field to search can either just be '
                         + ' or '.join(available_search_fields))

    if not value:
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    if not isinstance(value, str):
        raise ValueError('ERR#0017: the introduced value to search is mandatory and should be a str.')

    certificates['matches'] = certificates[by].str.contains(value, case=False)

    search_result = certificates.loc[certificates['matches'] == True].copy()

    if len(search_result) == 0:
        raise RuntimeError('ERR#0043: no results were found for the introduced ' + str(by) + '.')

    search_result.drop(columns=['matches'], inplace=True)
    search_result.reset_index(drop=True, inplace=True)

    return search_result

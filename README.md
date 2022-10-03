<p align="center">
  <img src="https://raw.githubusercontent.com/alvarobartt/investpy/master/docs/source/_static/logo.png" hspace="20">
</p>

## :warning: `investpy` is not working fine currently due to some Investing.com changes in their APIs, so please use [`investiny`](https://github.com/alvarobartt/investiny) in the meantime as I'm actively updating it and adding more and more features of some temporary solutions while we fix `investpy`. Thanks!

<h2 align="center">Financial Data Extraction from Investing.com with Python</h2>

investpy is a Python package to retrieve data from [Investing.com](https://www.investing.com/), which provides data retrieval 
from up to 39952 stocks, 82221 funds, 11403 ETFs, 2029 currency crosses, 7797 indices, 688 bonds, 66 commodities, 250 certificates, 
and 4697 cryptocurrencies.

investpy allows the user to download both recent and historical data from all the financial products indexed at Investing.com. 
**It includes data from all over the world**, from countries such as United States, France, India, Spain, Russia, or Germany, 
amongst many others.

investpy seeks to be one of the most complete Python packages when it comes to financial data extraction to stop relying 
on public/private APIs since investpy is **FREE** and has **NO LIMITATIONS**. These are some of the features that currently lead 
investpy to be one of the most consistent packages when it comes to financial data retrieval.

[![Python Version](https://img.shields.io/pypi/pyversions/investpy.svg)](https://pypi.org/project/investpy/)
[![PyPI Version](https://img.shields.io/pypi/v/investpy.svg)](https://pypi.org/project/investpy/)
[![Package Status](https://img.shields.io/pypi/status/investpy.svg)](https://pypi.org/project/investpy/)
[![Build Status](https://github.com/alvarobartt/investpy/workflows/run_tests/badge.svg)](https://github.com/alvarobartt/investpy/actions?query=workflow%3Arun_tests)
[![Documentation Status](https://readthedocs.org/projects/investpy/badge/?version=latest)](https://investpy.readthedocs.io/)

**If you want to support the project, you can buy the developer a coffee. More information at: [buy-me-a-coffee](https://github.com/alvarobartt/buy-me-a-coffee)**

<p align="center"><a href="https://www.buymeacoffee.com/alvarobartt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></p>

---

## :hammer_and_wrench: Installation

To get this package working you will need to **install it via pip** (with a Python 3.6 version or higher) on the terminal by typing:

``$ pip install investpy``

Additionally, **if you want to use the latest investpy version instead of the stable one, you can install it from source** with the following command:

``$ pip install git+https://github.com/alvarobartt/investpy.git@master``

**The master branch ensures the user that the most updated version will always be working and fully operative** so as not to wait until the 
the stable release comes out (which eventually may take some time depending on the number of issues to solve).

---

## :computer: Usage

Even though some investpy usage examples are presented on the [docs](https://investpy.readthedocs.io/usage.html), 
some basic functionality will be sorted out with sample Python code blocks. Additionally, more usage examples 
can be found under [examples/](https://github.com/alvarobartt/investpy/tree/master/examples) directory, which 
contains a collection of Jupyter Notebooks on how to use investpy and handle its data.

:pushpin: __Note that `investpy.search_quotes` is the only function that ensures that the data is updated and aligned 1:1 with
the data provided by Investing.com!__

### :chart_with_upwards_trend: Recent/Historical Data Retrieval

investpy allows the user to **download both recent and historical data from any financial product indexed** 
(stocks, funds, ETFs, currency crosses, certificates, bonds, commodities, indices, and cryptos). In 
the example presented below, the historical data from the past years of a stock is retrieved. 

```python
import investpy

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
print(df.head())
```
```{r, engine='python', count_lines}
             Open   High    Low  Close     Volume Currency
Date                                                      
2010-01-04  30.49  30.64  30.34  30.57  123432176      USD
2010-01-05  30.66  30.80  30.46  30.63  150476160      USD
2010-01-06  30.63  30.75  30.11  30.14  138039728      USD
2010-01-07  30.25  30.29  29.86  30.08  119282440      USD
2010-01-08  30.04  30.29  29.87  30.28  111969192      USD
```

To get to know all the available recent and historical data extraction functions provided by 
investpy, and also, parameter tuning, please read the docs.

### :mag: Search Live Data

**Investing.com search engine is completely integrated** with investpy, which means that any available 
financial product (quote) can be easily found. The search function allows the user to tune the parameters 
to adjust the search results to their needs, where both product types and countries from where the 
products are, can be specified. **All the search functionality can be easily used**, for example, as 
presented in the following piece of code:

```python
import investpy

search_result = investpy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)
print(search_result)
```
```json
{"id_": 6408, "name": "Apple Inc", "symbol": "AAPL", "country": "united states", "tag": "/equities/apple-computer-inc", "pair_type": "stocks", "exchange": "NASDAQ"}
```

Retrieved search results will be a `list` of `investpy.utils.search_obj.SearchObj` class instances, unless
`n_results` is set to 1, when just a single `investpy.utils.search_obj.SearchObj` class instance will be returned.
To get to know which are the available functions and attributes of the returned search results, please read the related 
documentation at [Search Engine Documentation](https://investpy.readthedocs.io/search_api.html). So on, those 
search results let the user retrieve both recent and historical data, its information, the technical indicators,
the default currency, etc., as presented in the piece of code below:

```python
recent_data = search_result.retrieve_recent_data()
historical_data = search_result.retrieve_historical_data(from_date='01/01/2019', to_date='01/01/2020')
information = search_result.retrieve_information()
default_currency = search_result.retrieve_currency()
technical_indicators = search_result.retrieve_technical_indicators(interval='daily')
```

### :money_with_wings: Crypto Currencies Data Retrieval

Cryptocurrencies support has recently been included, to let the user retrieve data and information from any 
available crypto at Investing.com. Please note that some cryptocurrencies do not have available data indexed 
at Investing.com so that it can not be retrieved using investpy either, even though they are just a few, 
consider it.

As already presented previously, **historical data retrieval using investpy is really easy**. The piece of code 
presented below shows how to retrieve the past years of historical data from Bitcoin (BTC).

```python
import investpy

data = investpy.get_crypto_historical_data(crypto='bitcoin',
                                           from_date='01/01/2014',
                                           to_date='01/01/2019')

print(data.head())
```
```{r, engine='python', count_lines}
             Open    High    Low   Close  Volume Currency
Date                                                     
2014-01-01  805.9   829.9  771.0   815.9   10757      USD
2014-01-02  815.9   886.2  810.5   856.9   12812      USD
2014-01-03  856.9   888.2  839.4   884.3    9709      USD
2014-01-04  884.3   932.2  848.3   924.7   14239      USD
2014-01-05  924.7  1029.9  911.4  1014.7   21374      USD
```

---

## :open_book: Documentation

You can find the **complete investpy documentation** at [Documentation](https://investpy.readthedocs.io/).

---

## :sparkles: Contribute

As this is an open-source project it is **open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements, and ideas**. There is an open tab of [issues](https://github.com/alvarobartt/investpy/issues) where 
anyone can open new issues if needed or navigate through them to solve them or contribute to its solving. 
Remember that issues are not threads to describe multiple problems, this does not mean that issues can not 
be discussed, but so to keep structured project management, the same issue should not describe different 
problems, just the main one and some nested/related errors that may be found.

---

## :question: Discussions (Q&A, AMA)

GitHub recently released a new feature named __GitHub Discussions__ (still in beta). GitHub Discussions is a 
collaborative communication forum for the community around an open source project.

Check the investpy GitHub Discussions page at [Discussions](https://github.com/alvarobartt/investpy/discussions), 
and feel free to ask me (ar any developer) anything, share updates, have open-ended conversations, and follow along 
on decisions affecting the community's way of working.

:pushpin: __Note__. Usually I don't answer emails asking me questions about investpy, as we currently have the
GitHub Discussions tab, and I encourage you to use it. GitHub Discussions is the easiest way to contact me about 
investpy, so that I don't answer the same stuff more than once via email, as anyone can see the opened/answered
discussions.

---

## :card_index_dividers: Related projects

Since investpy is intended to retrieve data from different financial products as indexed in Investing.com, 
the **development of some support modules which implement an additional functionality based on investpy data**, 
is presented. Note that **anyone can contribute to this section** by creating any package, module, or utility that 
uses investpy. So on, the ones already created are going to be presented, since they are intended to be used 
combined with investpy:

- [pyrtfolio](https://github.com/alvarobartt/pyrtfolio/): is a Python package to generate stock portfolios.
- [trendet](https://github.com/alvarobartt/trendet/): is a Python package for trend detection on stock time-series data.
- [pypme](https://github.com/ymyke/pypme): is a Python package for PME (Public Market Equivalent) calculation

If you developed an interesting/useful project based on investpy data, please open an issue to let me know to 
include it in this section.

---

## :memo: Citation

When citing this repository on your scientific publications please use the following **BibTeX** citation:

```bibtex
@misc{investpy,
    author = {Alvaro Bartolome del Canto},
    title = {investpy - Financial Data Extraction from Investing.com with Python},
    year = {2018-2021},
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/alvarobartt/investpy}},
}
```

When citing this repository on any other social media, please use the following citation:

```
investpy - Financial Data Extraction from Investing.com with Python developed by Alvaro Bartolome del Canto
```

You should also mention the source from where the data is retrieved, Investing.com; even though it's already
included in the package short description title.

---

## :man_technologist: Contact Information

You can contact me at any of my social network profiles:

- :briefcase: LinkedIn: https://linkedin.com/in/alvarobartt
- :bird: Twitter: https://twitter.com/alvarobartt
- :octocat: GitHub: https://github.com/alvarobartt

Or via email at alvarobartt@yahoo.com.

---

## :warning: Disclaimer

This Python package has been made for **research purposes** to fit the needs that Investing.com does not cover, 
so this package works like an Application Programming Interface (API) of Investing.com developed in an **altruistic way**.

Conclude that **investpy is not affiliated in any way to Investing.com or any dependant company**, the only 
requirement specified by Investing.com to develop this package was to "mention the source where data is 
retrieved from".

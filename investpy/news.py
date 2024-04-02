# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

from datetime import datetime
from random import choice
from time import gmtime, localtime, strftime

import pandas as pd
import pytz
import requests
from lxml.html import fromstring
from unidecode import unidecode

from .utils import constant as cst
from .utils.extra import random_user_agent


def economic_calendar(
    time_zone=None,
    time_filter="time_only",
    countries=None,
    importances=None,
    categories=None,
    from_date=None,
    to_date=None,
    lang=None,
):
    """
    This function retrieves the economic calendar, which covers financial events and indicators from all over the world
    updated in real-time. By default, the economic calendar of the currrent day from you local timezone will be retrieved, but
    note that some parameters can be specified so that the economic calendar to retrieve can be filtered.

    Args:
        time_zone (:obj:`str`, optional):
            time zone in GMT +/- hours:minutes format, which will be the reference time, if None, the local GMT time zone will be used.
        time_filter (:obj:`str`, optional):
            it can be `time_only` or `time_remain`, so that the calendar will display the time when the event will occurr according to
            the time zone or the remaining time until an event occurs.
        countries (:obj:`list` of :obj:`str`, optional):
            list of countries from where the events of the economic calendar will be retrieved, all contries will be taken into consideration
            if this parameter is None.
        importances (:obj:`list` of :obj:`str`, optional):
            list of importances of the events to be taken into consideration, can contain: high, medium and low; if None all the importance
            ratings will be taken into consideration including holidays.
        categories (:obj:`list` of :obj:`str`, optional):
            list of categories to which the events will be related to, if None all the available categories will be taken into consideration.
        from_date (:obj:`str`, optional):
            date from when the economic calendar will be retrieved in dd/mm/yyyy format, if None just current day's economic calendar will be retrieved.
        to_date (:obj:`str`, optional):
            date until when the economic calendar will be retrieved in dd/mm/yyyy format, if None just current day's economic calendar will be retrieved.

    Returns:
        :obj:`pandas.DataFrame` - economic_calendar:
            The resulting :obj:`pandas.DataFrame` will contain the retrieved information from the economic calendar with the specified parameters
            which will include information such as: date, time, zone or country of the event, event's title, etc. Note that some of the retrieved fields
            may be None since Investing.com does not provides that information.

    Raises:
        ValueError: raised if any of the introduced parameters is not valid or errored.

    Examples:
        >>> data = investpy.economic_calendar()
        >>> data.head()
            id        date     time         zone currency importance                         event actual forecast previous
        0  323  27/01/2020  All Day    singapore     None       None  Singapore - Chinese New Year   None     None     None
        1    9  27/01/2020  All Day    hong kong     None       None    Hong Kong - New Year's Day   None     None     None
        2   71  27/01/2020  All Day    australia     None       None     Australia - Australia Day   None     None     None
        3  750  27/01/2020  All Day        china     None       None       China - Spring Festival   None     None     None
        4  304  27/01/2020  All Day  south korea     None       None  South Korea - Market Holiday   None     None     None

    """

    if time_zone is not None and not isinstance(time_zone, str):
        raise ValueError(
            "ERR#0107: the introduced time_zone must be a string unless it is None."
        )

    if time_zone is None:
        time_zone = "GMT"

        diff = datetime.strptime(
            strftime("%d/%m/%Y %H:%M", localtime()), "%d/%m/%Y %H:%M"
        ) - datetime.strptime(strftime("%d/%m/%Y %H:%M", gmtime()), "%d/%m/%Y %H:%M")

        hour_diff = int(diff.total_seconds() / 3600)
        min_diff = int(diff.total_seconds() % 3600) * 60

        if hour_diff != 0:
            time_zone = (
                "GMT "
                + ("+" if hour_diff > 0 else "")
                + str(hour_diff)
                + ":"
                + ("00" if min_diff < 30 else "30")
            )
    else:
        if time_zone not in cst.TIMEZONES.keys():
            raise ValueError(
                "ERR#0108: the introduced time_zone does not exist, please consider"
                " passing time_zone as None."
            )

    if not isinstance(time_filter, str):
        raise ValueError(
            "ERR#0109: the introduced time_filter is not valid since it must be a"
            " string."
        )

    if time_filter not in cst.TIME_FILTERS.keys():
        raise ValueError(
            "ERR#0110: the introduced time_filter does not exist, available ones are:"
            " time_remaining and time_only."
        )

    if countries is not None and not isinstance(countries, list):
        raise ValueError(
            "ERR#0111: the introduced countries value is not valid since it must be a"
            " list of strings unless it is None."
        )

    if importances is not None and not isinstance(importances, list):
        raise ValueError(
            "ERR#0112: the introduced importances value is not valid since it must be a"
            " list of strings unless it is None."
        )

    if categories is not None and not isinstance(categories, list):
        raise ValueError(
            "ERR#0113: the introduced categories value is not valid since it must be a"
            " list of strings unless it is None."
        )

    if from_date is not None and not isinstance(from_date, str):
        raise ValueError(
            "ERR#0114: the introduced date value must be a string unless it is None."
        )

    if to_date is not None and not isinstance(to_date, str):
        raise ValueError(
            "ERR#0114: the introduced date value must be a string unless it is None."
        )

    if lang is not None and not isinstance(lang, str):
        raise ValueError(
            "ERR#0139: the introduced lang value must be a string unless it is None."
        )

    host = "www.investing.com"
    if lang == "korean":
        host = "kr.investing.com"

    url = f"https://{host}/economic-calendar/Service/getCalendarFilteredData"

    headers = {
        "User-Agent": random_user_agent(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    dates = [from_date, to_date]

    if any(date is None for date in dates) is True:
        data = {
            "timeZone": choice(cst.TIMEZONES[time_zone]),
            "timeFilter": cst.TIME_FILTERS[time_filter],
            "currentTab": "today",
            "submitFilters": 1,
            "limit_from": 0,
        }
    else:
        try:
            datetime.strptime(from_date, "%d/%m/%Y")
        except ValueError:
            raise ValueError(
                "ERR#0011: incorrect from_date date format, it should be 'dd/mm/yyyy'."
            )

        start_date = datetime.strptime(from_date, "%d/%m/%Y")

        try:
            datetime.strptime(to_date, "%d/%m/%Y")
        except ValueError:
            raise ValueError(
                "ERR#0012: incorrect to_date format, it should be 'dd/mm/yyyy'."
            )

        end_date = datetime.strptime(to_date, "%d/%m/%Y")

        if start_date > end_date:
            raise ValueError(
                "ERR#0032: to_date should be equal to from_date or greater than from_date, both formatted as"
                " 'dd/mm/yyyy'."
            )

        data = {
            "dateFrom": datetime.strptime(from_date, "%d/%m/%Y").strftime("%Y-%m-%d"),
            "dateTo": datetime.strptime(to_date, "%d/%m/%Y").strftime("%Y-%m-%d"),
            "timeZone": choice(cst.TIMEZONES[time_zone]),
            "timeFilter": cst.TIME_FILTERS[time_filter],
            "currentTab": "custom",
            "submitFilters": 1,
            "limit_from": 0,
        }

    if countries is not None:
        def_countries = list()

        available_countries = list(cst.COUNTRY_ID_FILTERS.keys())

        # TODO: improve loop using lambda
        for country in countries:
            country = unidecode(country.strip().lower())

            if country in available_countries:
                def_countries.append(cst.COUNTRY_ID_FILTERS[country])

        if len(def_countries) > 0:
            data["country[]"] = def_countries

    if categories is not None:
        def_categories = list()

        available_categories = list(cst.CATEGORY_FILTERS.keys())

        # TODO: improve loop using lambda
        for category in categories:
            category = unidecode(category.lower())
            category = category.strip()

            if category in available_categories:
                def_categories.append(cst.CATEGORY_FILTERS[category])

        if len(def_categories) > 0:
            data["category[]"] = def_categories

    if importances is not None:
        def_importances = list()

        # TODO: improve loop using lambda
        for importance in importances:
            importance = unidecode(importance.lower())
            importance = importance.strip()

            for key, value in cst.IMPORTANCE_RATINGS.items():
                if value == importance:
                    if key not in def_importances:
                        def_importances.append(key)
                    break

        if len(def_importances) > 0:
            data["importance[]"] = def_importances

    id_, last_id = 0, 0
    results = list()

    while True:
        req = requests.post(url, headers=headers, data=data)

        root = fromstring(req.json()["data"])
        table = root.xpath(".//tr")

        for reversed_row in table[::-1]:
            id_ = reversed_row.get("id")
            if id_ is not None:
                id_ = id_.replace("eventRowId_", "")
                break

        if id_ == last_id:
            break

        for row in table:
            id_ = row.get("id")
            if id_ == None:
                curr_timescope = int(row.xpath("td")[0].get("id").replace("theDay", ""))
                curr_date = datetime.fromtimestamp(
                    curr_timescope, tz=pytz.timezone("GMT")
                ).strftime("%d/%m/%Y")
            else:
                id_ = id_.replace("eventRowId_", "")

                time = (
                    zone
                ) = currency = sentiment = event = actual = forecast = previous = None

                if row.get("id").__contains__("eventRowId_"):
                    for value in row.xpath("td"):
                        if value.get("class").__contains__("first left"):
                            time = value.text_content()
                        elif value.get("class").__contains__("flagCur"):
                            zone = value.xpath("span")[0].get("title").lower()
                            currency = value.text_content().strip()
                        elif value.get("class").__contains__("sentiment"):
                            if value.get("data-img_key") == None:
                                importance_rating = None
                            else:
                                importance_rating = value.get("data-img_key").replace(
                                    "bull", ""
                                )
                        elif value.get("class") == "left event":
                            event = value.text_content().strip()
                        elif value.get("id") == "eventActual_" + id_:
                            actual = value.text_content().strip()
                        elif value.get("id") == "eventForecast_" + id_:
                            forecast = value.text_content().strip()
                        elif value.get("id") == "eventPrevious_" + id_:
                            previous = value.text_content().strip()

                results.append(
                    {
                        "id": id_,
                        "date": curr_date,
                        "time": time,
                        "zone": zone,
                        "currency": None if currency == "" else currency,
                        "importance": None
                        if importance_rating == None
                        else cst.IMPORTANCE_RATINGS[int(importance_rating)],
                        "event": event,
                        "actual": None if actual == "" else actual,
                        "forecast": None if forecast == "" else forecast,
                        "previous": None if previous == "" else previous,
                    }
                )

        last_id = results[-1]["id"]

        data["limit_from"] += 1

    return pd.DataFrame(results)

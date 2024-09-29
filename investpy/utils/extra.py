# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import random

import pandas as pd
import pkg_resources

from . import constant as cst


def resource_to_data(path_to_data):
    """
    This is an auxiliar function to read data from a given path, so as to wrap the load
    process of the static data files from investpy.

    Returns:
        :obj:`pandas.DataFrame` - data:
            This function returns a :obj:`pandas.DataFrame` object with all the static file's data
            retrieved from investpy.

    Raises:
        FileNotFoundError: raised if the static data file was not found.
        IOError: raised if the data file is empty or errored.

    """

    resource_package = "investpy"
    resource_path = "/".join(("resources", path_to_data))
    if pkg_resources.resource_exists(resource_package, resource_path):
        data = pd.read_csv(
            pkg_resources.resource_filename(resource_package, resource_path),
            keep_default_na=False,
        )
    else:
        raise FileNotFoundError("ERR#0115: data file not found or errored.")

    if data is None:
        raise IOError("ERR#0115: data file was empty or errored.")

    return data


def random_user_agent():
    """
    This function selects a random User-Agent from the User-Agent list, which is a constant
    variable that can be found at `investpy.utils.constant.USER_AGENTS`. User-Agents are used in
    order to avoid the limitations of the requests to Investing.com. The User-Agent is
    specified on the headers of the requests and is different for every request.

    Note that Investing.com, via changing the User-Agent on the headers of every request, allows
    a lot of requests, since it has been tested with over 10k consecutive requests without getting
    any HTTP error code from Investing.com.

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the
            headers of a request so to avoid restrictions due to the use of multiple requests from the
            same User-Agent.

    """

    return random.choice(cst.USER_AGENTS)


def convert_abbreviations_to_number(value):
    """Converts abbreviated numbers to float format, e.g. 3.5M -> 3500000.0"""
    if value[-1] in cst.MULTIPLIERS:
        return float(value[:-1]) * 10 ** cst.MULTIPLIERS[value[-1]]
    else:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"The value '{value}' format is not supported")


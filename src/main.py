#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
Author: Arran Dinsmore
Updated: 17/12/2020
Description: Main file for running fpl EA
"""

import pandas as pd

from data import FplData

fpl_data: pd.DataFrame = FplData()

fpl_data.set_history()

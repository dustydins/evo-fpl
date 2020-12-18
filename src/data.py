#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data.py
Author: Arran Dinsmore
Updated: 17/12/2020
Description: Fetches and maintains data for current team and fpl website
"""

import json
from datetime import datetime
import requests
import pandas as pd

SEASON = '2020-21'
FPL_URL: str = 'https://fantasy.premierleague.com/api/bootstrap-static/'


class FplData:
    """
    Keep track of FPL API data
    """
    gameweek_id: int
    next_gameweek_id: int
    history: pd.DataFrame

    def __init__(self):
        self._set_gameweek_id()
        if self.gameweek_id < 38:
            self.next_gameweek_id = self.gameweek_id + 1
        else:
            self.next_gameweek_id = -1

    def _set_gameweek_id(self):
        """
        Sets the current gameweek id
        """
        data = requests.get(FPL_URL)
        data = json.loads(data.content)
        gameweeks = data['events']
        now = datetime.utcnow()
        for gameweek in gameweeks:
            next_deadline = datetime.strptime(gameweek['deadline_time'],
                                              '%Y-%m-%dT%H:%M:%SZ')
            if next_deadline > now:
                self.gameweek_id = gameweek['id'] - 1
                break

    def set_history(self):
        """
        Update history
        """
        vastaav_url = f"https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/\
master/data/{SEASON}/gws/gw{self.gameweek_id}"
        print(vastaav_url)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:23:50 2018

@author: Ben
"""

import pandas as pd

#read in data for stations and riders
station_df = pd.read_csv('NYC_Transit_Subway_Entrance_And_Exit_Data.csv')
rider_df = pd.read_csv('datMTA20180922.csv')

#find out whether 'station' variables in the dfs have any values in common
station_common_values = [station for station in rider_df.STATION if station in station_df['Station Name']]
#station_common_values = [], so the datasets don't have values for the Station variable in common


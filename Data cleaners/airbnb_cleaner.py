#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 2018

@author: Kamil Toraman
"""
import numpy as np
import pandas as pd


def main():
    df = pd.read_csv("../airbnb_data/listings_5cols.csv")
    print df.head()
    df = df[pd.to_numeric(df['latitude'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['longitude'], errors='coerce').notnull()]
    df.to_csv("../airbnb_data/listings_5cols_cleaned.csv")

if __name__ == '__main__':
    main()

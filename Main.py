#  Main file for application
# Import required functions

from GetData import GetFinancials
from GetData import statistics
from Ratios import calculate_ratio
import pandas as pd
from functools import reduce

import matplotlib.pyplot as plt


def compare_ratio(ticker1, ticker2, ticker3):

    financials_t1 = GetFinancials(ticker1)
    financials_t2 = GetFinancials(ticker2)
    financials_t3 = GetFinancials(ticker3)

    key_stats_t1 = statistics(ticker1)
    key_stats_t2 = statistics(ticker2)
    key_stats_t3 = statistics(ticker3)

    ratio_t1 = calculate_ratio(financials_t1, key_stats_t1)
    ratio_t2 = calculate_ratio(financials_t2, key_stats_t2)
    ratio_t3 = calculate_ratio(financials_t3, key_stats_t3)



    return df_merged

# Test case :

# We ask the user to select a few compagnie

Northland = "NPI.TO"  # Northland Power Corp.
Innergex = "INE.TO"   # Innergex
Fortis = "FTS.TO"  # Fortis Inc.

compare = compare_ratio(Northland, Innergex, Fortis)


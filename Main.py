#  Main file for application
# Import required functions

from GetData import GetFinancials
from GetData import statistics
from Ratios import calculate_ratio

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
    df_merged = ratio_t1.merge(ratio_t2, left_index=True, right_index=True).set_index(ratio_t1.index)
    df_merged_all = df_merged.merge(ratio_t3, left_index=True, right_index=True).set_index(ratio_t1.index)
    df = df_merged_all.rename(columns={"Ratio_x": ticker1, "Ratio_y": ticker2, "Ratio": ticker3})
    return df


def compare_chart(df, ratio):
    """:return bar chart from selectede Ratio"""

    objects = []
    for col_name in df.columns:
        objects.append(col_name)

    y_pos = np.arange(len(objects))
    performance = df.loc[ ratio, : ]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.title(ratio)

    bar_chart = plt.show()
    return bar_chart


# Test case :
# We ask the user to select a few compagnie
Northland = "NPI.TO"  # Northland Power Corp.
Innergex = "INE.TO"   # Innergex
Fortis = "FTS.TO"  # Fortis Inc.
compare = compare_ratio(Northland, Innergex, Fortis)

# Test Case Bar chart :
Beta_Chart = compare_chart(compare, "Beta 5Y")

#!/usr/bin/env python3

from df_utils import ImprovedDataFrame

lists = [[1,2,3],[4,5,6]]


idf = ImprovedDataFrame(lists)

idf.columns = ['col 1','Col 2','Col 3']



idf = idf.add_col('new col',[7,8])

idf = idf.correctify().simplify_cols()

print(idf)

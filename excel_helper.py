#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-07-27 00:33

__author__ = 'Ted'
import pandas as pd

group = pd.read_excel("group.xls",header=None)
group.columns=["分组","角色"]
group.dropna(how="all")
print(group)

source = pd.read_csv("source.csv")
filter_merge = source.iloc[:,[0,2,4,5,6,13]]
print(source)
print(filter_merge)

combine = pd.merge(group,filter_merge,on="角色")
combine.insert(1,"数据K/60",round(filter_merge["数据K"]/60,2))
print(combine)

combine.to_excel(excel_writer="result.xlsx",index=False)

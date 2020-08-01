# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:36:38 2020

@author: ZhuangWenjia
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#定义函数用于独热编码
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
    
#导入订单表，选取订单日期，客户ID,产品名称3个字段
data = pd.read_csv('C:/Users/wing007/Videos/Captures/数据分析训练营-结营考试/ProjectB/订单表.csv',  usecols=['订单日期','客户ID', '产品名称'], encoding='GBK')

#将订单日期和客户ID两个字段作为订单分类依据和索引，对产品名称进行独热编码
hot_encoded_product=data.groupby(['订单日期','客户ID','产品名称'])['产品名称'].count().unstack().reset_index().fillna(0).set_index(['订单日期','客户ID'])
print(hot_encoded_product)
hot_encoded_product =hot_encoded_product.applymap(encode_units)

#给出频繁项集和关联规则并排序打印
frequent_itemsets = apriori(hot_encoded_product, min_support=0.03, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("频繁项集：", frequent_itemsets.sort_values('support',ascending=False))
print("关联规则：", rules.sort_values('lift',ascending=False))


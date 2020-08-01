# -*- coding: utf-8 -*-;x.
"""
Created on Tue Jul 28 20:34:20 2020

@author: wing007
"""


#通过八爪鱼工具采集到SVW品牌的SUV车辆信息，包括品牌，价格，产品图片链接3列。其中价格列是区间范围，需要将其进行拆分。

import pandas as pd

#读入通过八爪鱼采集的文件
SVW_SUV = pd.read_csv('D:/d/Zhuangwenjia D/试验报告/学习/python视频/数据分析训练营-结营考试/1.csv', encoding='UTF-8')

pd.options.display.max_columns=100

#通过连接符'-'将价格区间进行拆分，一列拆成两列
SVW_SUV = SVW_SUV.drop('价格', axis=1).join(SVW_SUV['价格'].str.split('-',expand=True))
print(SVW_SUV)

#对拆分的两列进行重命名为最低价格，最高价格
SVW_SUV.rename(columns={0:'最低价格',1:'最高价格'}, inplace=True)
#填充空项
SVW_SUV = SVW_SUV.fillna("暂无")
#文件输出成csv格式
SVW_SUV.to_csv('D:/d/Zhuangwenjia D/试验报告/学习/python视频/数据分析训练营-结营考试/test1.csv', index=None, encoding='GBK')


'''
Developer: liziyuan
Other Contributor: none
Version: V1.0.0
Development Environment: Python 3.7
Copyright © CRRC ZHUZHOU INSTITUTE CO.,LTD. WindPower Business Unit
Date: 2022-05-24 19:30:40
'''

import numpy as np
import pandas as pd

data = pd.read_csv(r"D:\CRRC_WorkDocument\pythonsupport\task4\hxmj_tag.csv")

### 由于数字后混搭空格与非空格 先统一去掉空格
li = []
for f in list(data["wec_tag"]):
    f = f.replace(" ", "")
    li.append(f)
data["wec_tag"] = li
### 在"_001"~"_200"后加上空格
wt = 1
lis = list(data["wec_tag"])
while wt<201:
    for f in lis:
        if "_"+str(wt).zfill(3) in str(f):
            lis_index = lis.index(f)
            f=f.replace("_"+str(wt).zfill(3),"_"+str(wt).zfill(3)+" ")
            lis[lis_index] = f
    wt = wt+1
data["wec_tag"] = lis

data.to_csv(r"D:\CRRC_WorkDocument\pythonsupport\task4\hxmj_tag_result.csv")

print("test")
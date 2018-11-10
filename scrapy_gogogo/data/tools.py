import pandas as pd
import numpy as np
df = pd.read_csv("./科技公司名单.csv")
df['公司名称']+="财务指标"
# 为了应对
df.to_csv("name.csv",encoding="utf-8-sig")

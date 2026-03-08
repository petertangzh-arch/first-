#!/usr/bin/env python3
"""财经数据接口测试"""

import tushare as ts
import akshare as ak
import pandas as pd
from datetime import datetime, timedelta

TOKEN = "88c357c1a1dbdca5417e60533831f987f92f5d0118f6594825b23d42"

print("=" * 50)
print("财经数据接口测试")
print("=" * 50)

# ===== Tushare 测试 =====
print("\n【1. Tushare 测试】")
try:
    pro = ts.pro_api(TOKEN)
    # 获取上证指数日线
    df = pro.daily(ts_code='000001.SH', start_date='20250301', end_date='20250308')
    print(f"✅ Tushare 连接成功! 获取到 {len(df)} 条数据")
    print(df.head(3))
except Exception as e:
    print(f"❌ Tushare 失败: {e}")

# ===== AKShare 测试 =====
print("\n【2. AKShare 测试】")
try:
    # A股实时行情
    df_ak = ak.stock_zh_a_spot_em()
    print(f"✅ AKShare 连接成功! 获取到 {len(df_ak)} 只股票")
    print(df_ak.head(3))
except Exception as e:
    print(f"❌ AKShare 失败: {e}")

# ===== 额外测试：个股行情 =====
print("\n【3. 个股历史数据测试 (AKShare)】")
try:
    df_hist = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20250301", end_date="20250308")
    print(f"✅ 个股历史数据获取成功! {len(df_hist)} 条")
    print(df_hist)
except Exception as e:
    print(f"❌ 个股历史数据失败: {e}")

print("\n" + "=" * 50)
print("测试完成")
print("=" * 50)

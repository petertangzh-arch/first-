#!/usr/bin/env python3
"""
财经数据自动抓取脚本
优先使用稳定的免费接口
"""

import akshare as ak
import pandas as pd
import os
from datetime import datetime
import json
import time
import warnings
warnings.filterwarnings('ignore')

# 配置
DATA_DIR = "/Users/henryt/.openclaw/workspace/data"
os.makedirs(DATA_DIR, exist_ok=True)

# 重试次数
MAX_RETRIES = 3
RETRY_DELAY = 5

def retry_request(func, *args, **kwargs):
    """带重试的请求"""
    for i in range(MAX_RETRIES):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if i < MAX_RETRIES - 1:
                print(f"⚠️ {func.__name__} 失败，{RETRY_DELAY}秒后重试... ({i+1}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            else:
                raise e

def save_data(df, name):
    """保存数据"""
    if df is None or len(df) == 0:
        print(f"⚠️ {name} 无数据")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{DATA_DIR}/{name}_{timestamp}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"✅ 已保存: {filename} ({len(df)} 条)")
    return filename

# ===== 可用的接口 =====

def get_macro_cpi():
    """宏观CPI数据"""
    print("📊 获取宏观CPI...")
    df = retry_request(ak.macro_china_cpi)
    return df

def get_macro_m2():
    """广义货币M2"""
    print("💵 获取M2数据...")
    df = retry_request(ak.macro_china_m2)
    return df

def get_stock_ipo():
    """新股上市信息"""
    print("🆕 获取新股信息...")
    df = retry_request(ak.stock_ipo_info)
    return df

def get_stock_ipo_cal():
    """IPO日历"""
    print("📅 获取IPO日历...")
    df = retry_request(ak.stock_ipo_calendar)
    return df

def get_futures_daily():
    """期货日线"""
    print("🌾 获取期货日线...")
    df = retry_request(ak.futures_zh_daily_sina, symbol="RU")
    return df

def get_fund_etf_hist():
    """ETF历史"""
    print("💰 获取ETF历史...")
    df = retry_request(ak.fund_etf_hist_em, symbol="510300", period="daily",
                       start_date="20250101", end_date="20250308")
    return df

def get_stock_zh_a_hist():
    """A股历史（平安银行测试通过）"""
    print("📈 获取A股历史...")
    df = retry_request(ak.stock_zh_a_hist, symbol="000001", period="daily",
                       start_date="20250101", end_date="20250308")
    return df

def main():
    print("=" * 50)
    print("财经数据抓取", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 50)
    
    results = {}
    
    # 宏观数据
    try:
        df = get_macro_cpi()
        results['macro_cpi'] = save_data(df, "macro_cpi")
    except Exception as e:
        print(f"❌ CPI失败: {e}")
    
    try:
        df = get_macro_m2()
        results['macro_m2'] = save_data(df, "macro_m2")
    except Exception as e:
        print(f"❌ M2失败: {e}")
    
    # 新股
    try:
        df = get_stock_ipo()
        results['stock_ipo'] = save_data(df, "stock_ipo")
    except Exception as e:
        print(f"❌ IPO失败: {e}")
    
    # ETF历史
    try:
        df = get_fund_etf_hist()
        results['etf_hist'] = save_data(df, "etf_hist_510300")
    except Exception as e:
        print(f"❌ ETF失败: {e}")
    
    # A股历史
    try:
        df = get_stock_zh_a_hist()
        results['stock_hist'] = save_data(df, "stock_hist_000001")
    except Exception as e:
        print(f"❌ A股历史失败: {e}")
    
    # 保存索引
    with open(f"{DATA_DIR}/latest.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "=" * 50)
    print("抓取完成!")
    print("=" * 50)
    return results

if __name__ == "__main__":
    main()

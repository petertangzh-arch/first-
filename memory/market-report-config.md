# 每日市场早报 - 配置说明

**日期**: 2026年2月18日 星期三

## ⚠️ 数据源配置问题

当前早报任务无法获取实时市场数据，需要配置数据源。

### 需要配置的数据源

1. **Yahoo Finance (yfinance Python库)**
   - 已安装但被rate limit限制
   - 解决方案：添加代理或使用其他数据源

2. **Alpha Vantage (推荐)**
   - 注册: https://www.alphavantage.co/
   - 免费tier: 25请求/天
   - 配置方式: 设置环境变量 `ALPHA_VANTAGE_API_KEY`

3. **Twelve Data**
   - 注册: https://twelvedata.com/
   - 免费tier: 800请求/天
   - 配置方式: 设置环境变量 `TWELVE_DATA_API_KEY`

4. **Financial Modeling Prep**
   - 注册: https://site.financialmodelingprep.com/
   - 免费tier: 250请求/天

### 推荐的解决方案

请运行以下命令配置 Brave Search API (用于网络搜索):
```bash
openclaw configure --section web
```

或者配置市场数据API:
```bash
# Alpha Vantage
export ALPHA_VANTAGE_API_KEY="your_key_here"

# Twelve Data  
export TWELVE_DATA_API_KEY="your_key_here"
```

---

## 📊 早报模板结构

一旦数据源配置完成，早报将包含以下内容:

### 1. 宏观分析师观点和市场前瞻
- 全球宏观经济形势分析
- 主要央行政策动向
- 市场风险情绪评估

### 2. 大宗商品数据
| 商品 | 价格 | 涨跌幅 |
|------|------|--------|
| 黄金 (COMEX Gold) | $XXX.XX | +X.XX% |
| 原油 (WTI Crude) | $XX.XX | +X.XX% |
| 铜 (COMEX Copper) | $X.XXXX | +X.XX% |

### 3. 全球股市数据
| 市场 | 指数 | 点位 | 涨跌幅 |
|------|------|------|--------|
| 🇺🇸 美国 | S&P 500 | XXXX.XX | +X.XX% |
| 🇺🇸 美国 | Dow Jones | XXXXX.XX | +X.XX% |
| 🇺🇸 美国 | NASDAQ | XXXXX.XX | +X.XX% |
| 🇨🇳 中国 | 上证指数 | XXXX.XX | +X.XX% |
| 🇨🇳 中国 | 深证成指 | XXXX.XX | +X.XX% |
| 🇯🇵 日本 | 日经225 | XXXXX.XX | +X.XX% |
| 🇰🇷 韩国 | KOSPI | XXXX.XX | +X.XX% |

### 4. 今日AI/科技要闻
- 主要AI/科技公司动态
- 重大技术突破或产品发布
- 科技行业政策动向

### 5. 中国股市政策/国家队动向
- 证监会最新政策
- 国家队（社保、险资）持仓变化
- 北向资金流向

---

**数据来源**: Yahoo Finance, Alpha Vantage, Bloomberg, 东方财富, 新浪财经

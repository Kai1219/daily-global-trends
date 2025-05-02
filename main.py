from trendspy import Trends
from datetime import datetime
import pygsheets
import json
import os
import base64

# 從 GitHub Secrets 讀取並寫入暫存的憑證檔案
key_base64 = os.environ.get("GCP_KEY_BASE64")
key_path = "gcp_key.json"

if not key_base64:
    raise ValueError("❌ 沒有找到 GCP_KEY_BASE64 secret，請先在 GitHub Secrets 設定")

with open(key_path, "w") as f:
    f.write(base64.b64decode(key_base64).decode("utf-8"))

# 初始化 Trends 物件
tr = Trends()

# 獲取現在趨勢(24小時)
df = tr.trending_now(geo='TW')

data = []

current_date_time = datetime.now()
current_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

for item in df:
    region=item.geo
    keyword=item.keyword
    volume=item.volume
    trend_keywords = ', '.join(item.trend_keywords) if isinstance(item.trend_keywords, list) else item.trend_keywords
    topic_names = ', '.join(item.topic_names) if isinstance(item.topic_names, list) else item.topic_names
    volume_growth_pct=str(item.volume_growth_pct)+"%"
    data.append([current_time,region,keyword,volume,trend_keywords,topic_names,volume_growth_pct])

# 授權 Google Sheets
gc = pygsheets.authorize(service_file=key_path)
spreadsheet = gc.open("Google-trends-python")
worksheet = spreadsheet.sheet1

#找到空白列
next_empty_row = len(worksheet.get_col(1, include_empty=False)) + 1
start_cell = f"A{next_empty_row}"

# 寫入資料
worksheet.update_values(start_cell, data)

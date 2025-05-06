# 🌍 Google 全球搜尋趨勢（每日自動更新）

📅 專案時間 2025/05  
📈 即時掌握各國聲量成長最快的議題，協助制定在地化的行銷方向。
---
## 📌 專案簡介

本專案透過 Python 腳本每日自動擷取 Google Trends 上的熱門關鍵字，追蹤台灣、新加坡、日本、香港等地每日熱搜變化，並將資料整合進 Google Sheets 與 Looker Studio，作為市場分析與行銷策略的依據。

---

## 🎯 目標與動機

- 快速掌握亞洲市場每日的熱門關鍵字趨勢  
- 協助團隊擬定更即時且在地化的行銷策略  
- 建立自動化流程，節省人工彙整時間

---

## ⚙️ 做法與流程

1. 使用 [`trendspy`](https://pypi.org/project/trendspy/) 套件，抓取台灣、新加坡、日本、香港每日熱門關鍵字與成長趨勢資料
2. 使用 `pygsheets` 將資料寫入 Google Sheets
3. 設定 GitHub Actions，於每日凌晨 1 點（台灣時間）自動執行 Python 腳本
4. 串接 Looker Studio 將資料視覺化，快速提供趨勢洞察給相關團隊

---

## 🛠 使用技術

- Python
  - trendspy
  - pygsheets
- GitHub Actions（自動化排程）
- Google Sheets（儲存資料）
- Looker Studio（視覺化展示）

---

## 🗂 範例截圖

![image](https://github.com/user-attachments/assets/c49dfc32-df0b-40d3-bf93-7bec60b396d1)

## 🔍 線上儀表板

[👉 查看 Looker Studio 報表]([https://lookerstudio.google.com/s/your-dashboard-id](https://lookerstudio.google.com/reporting/52358280-7b0e-4da4-b5ea-f97c90f261b2))

---

## 📄 License

本專案僅供學習與非商業用途。如需商業使用，請先聯繫作者取得授權。

---

## ✉️ 聯絡方式

如有建議或問題，歡迎提出 Issue 或聯繫作者。


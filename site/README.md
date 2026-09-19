# Website source

本目錄保存公開病例指南的靜態網站來源。

- `build_site.py`：以 Python 產生所有 HTML 頁面。
- `dist/`：可直接部署的 static output。

重新產生網站：

```bash
python3 build_site.py
python3 -m http.server 4173 --directory dist
```

正式網站：<https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/>

網站內容與 repo 一樣只使用去識別化 relative-day data。Hosting project metadata、deployment credentials 與私有設定不納入公開 repo。

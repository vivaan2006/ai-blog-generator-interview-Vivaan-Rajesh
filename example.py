import requests, json

resp = requests.get("http://127.0.0.1:5000/generate?keyword=smart%20watches")
data = resp.json()
md_text = data["content"]
with open("example_smart_watches.md", "w", encoding="utf-8") as f:
    f.write(md_text)

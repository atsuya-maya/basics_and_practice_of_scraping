import requests
from urllib.parse import quote, quote_plus

def _2_3(url):
    res = requests.get(url)
    params={"status_code": res.status_code, "status_message": res.reason,
            "header": res.headers, "request": res.request, "request_header": res.headers,
            "contents": res.text}
    return params

def _2_4(url, string):
    res = requests.get(url)
    params = {"url": res.request.url, "text": res.text, "quote": url+quote(string, safe=''), "quote_plus": url+quote_plus(string)}
    return params
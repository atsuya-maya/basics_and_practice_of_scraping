import requests

def _2_3(url):
    res = requests.get(url)
    params={"status_code": res.status_code, "status_message": res.reason,
            "header": res.headers, "request": res.request, "request_header": res.headers,
            "contents": res.text}
    return params

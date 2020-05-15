import requests

url = 'http://127.0.0.1:5000/statistics'


def save_result(name, mode, cpm, wpm, time):
    stat = {
        "name": name,
        "mode": mode,
        "cpm": cpm,
        "wpm": wpm,
        "time": time
    }
    print(requests.post(url, json=stat).status_code)

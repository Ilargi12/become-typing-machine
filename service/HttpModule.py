import requests
from tkinter import messagebox

url = 'http://127.0.0.1:5000/statistics'


def save_result(name, mode, cpm, wpm, time):
    stat = {
        "name": name,
        "mode": mode,
        "cpm": cpm,
        "wpm": wpm,
        "time": time
    }
    try:
        print(requests.post(url, json=stat).status_code)
    except Exception:
        messagebox.showerror("Connection Error", "Cannot send data to server!")


def get_all_stats():
    # zwraca listę słowników
    try:
        return requests.get(url=url).json()
    except Exception:
        messagebox.showerror("Connection Error", "Cannot get data from server!")
        return []




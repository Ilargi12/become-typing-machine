import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import requests

url = 'http://127.0.0.1:5000/statistics'


class GlobalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f9f8fd")
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Comic Sans MS", 20, "bold"))
        self.dict_of_players = requests.get(url=url).json()
        self.table = None
        self.graph = None
        self.menu_photo = tk.PhotoImage(file=r"img/menu.png")
        self.top_ten_players_photo = tk.PhotoImage(file=r"img/top_ten_players.png")
        self.wpm_stats_photo = tk.PhotoImage(file=r"img/wpm_stats.png")

        top_ten_players_label = tk.Label(self, bg="#f9f8fd", image=self.top_ten_players_photo).pack(pady=(10, 0))
        self.show_table()

        wpm_stats_label = tk.Label(self, bg="#f9f8fd", image=self.wpm_stats_photo).pack()
        self.show_donut_graph()

        tk.Button(self, image=self.menu_photo, bg="#f9f8fd", borderwidth=0,
                  command=lambda: controller.show_frame("MainMenu")).pack()

    def show_table(self):
        player_list = self.get_top_ten_players()
        cols = ['Position', 'Name', 'WPM', 'CPM']
        self.table = ttk.Treeview(self, columns=cols, show='headings')
        for col in cols:
            self.table.heading(col, text=col)

        for i, player in enumerate(player_list, start=1):
            if i > 10:
                break

            if i % 2 == 1:
                self.table.insert("", "end", values=(i, player['name'], '%.3f'%player['wpm'], '%.3f'%player['cpm']),
                                  tags=('odd_row', ))
            else:
                self.table.insert("", "end", values=(i, player['name'], '%.3f'%player['wpm'], '%.3f'%player['cpm']),
                                  tags=('even_row', ))

        self.table.tag_configure('odd_row', background='#ffba08')
        self.table.tag_configure('even_row', background='#f48c06')

        self.table.pack()

    def get_top_ten_players(self):
        list_of_players = list(self.dict_of_players)
        list_of_players.sort(key=lambda e: e['wpm'])
        list_of_players = list(dict((v['name'], v) for v in list_of_players).values())
        return list_of_players

    def show_donut_graph(self):
        names = ['1-30', '31-60', '61-90', '91-120', '121-150', '151-180', '>180']
        sizes = self.get_wpm_stats()
        my_circle = plt.Circle((0, 0), 0.6, color='white')
        plt.pie(sizes, labels=names, colors=['red', 'green', 'blue', 'skyblue', 'magenta', 'cyan', 'yellow'],
                wedgeprops={'linewidth': 5, 'edgecolor': 'white'})
        p = plt.gcf()
        p.set_size_inches(2.7, 2.7)
        p.gca().add_artist(my_circle)
        self.graph = FigureCanvasTkAgg(p, self)
        self.graph.get_tk_widget().pack(fill='x')

    def get_wpm_stats(self):
        wpm_stats = [0, 0, 0, 0, 0, 0, 0]
        list_of_players = list(self.dict_of_players)
        for player in list_of_players:
            if player['wpm'] <= 30:
                wpm_stats[0] += 1
            elif player['wpm'] <= 60:
                wpm_stats[1] += 1
            elif player['wpm'] <= 90:
                wpm_stats[2] += 1
            elif player['wpm'] <= 120:
                wpm_stats[3] += 1
            elif player['wpm'] <= 150:
                wpm_stats[4] += 1
            elif player['wpm'] <= 180:
                wpm_stats[5] += 1
            else:
                wpm_stats[6] += 1

        return wpm_stats





import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from service.GlobalStatsService import GlobalStatsService


class GlobalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = GlobalStatsService()
        self.configure(bg="#f9f8fd")
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Comic Sans MS", 20, "bold"))
        self.menu_photo = tk.PhotoImage(file=r"img/menu.png")
        self.top_ten_players_photo = tk.PhotoImage(file=r"img/top_ten_players.png")
        self.wpm_stats_photo = tk.PhotoImage(file=r"img/wpm_stats.png")

        self.table = None
        self.graph = None

        top_ten_players_label = tk.Label(self, bg="#f9f8fd", image=self.top_ten_players_photo).pack(pady=(10, 0))
        self.show_table()

        wpm_stats_label = tk.Label(self, bg="#f9f8fd", image=self.wpm_stats_photo).pack()
        self.show_donut_graph()

        tk.Button(self, image=self.menu_photo, bg="#f9f8fd", borderwidth=0,
                  command=lambda: controller.show_frame("MainMenu")).pack()

    def show_table(self):
        player_list = self.service.get_top_ten_players()
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

        self.table.tag_configure('odd_row', background='#c77dff')
        self.table.tag_configure('even_row', background='#9d4edd')

        self.table.pack()

    def show_donut_graph(self):
        names = ['1-30', '31-60', '61-90', '91-120', '121-150', '151-180']
        sizes = self.service.get_wpm_stats()
        my_circle = plt.Circle((0, 0), 0.6, color='#f9f8fd')
        plt.pie(sizes, labels=names, colors=['red', 'green', 'blue', 'skyblue', 'yellow', '#9d4edd'],
                wedgeprops={'linewidth': 5, 'edgecolor': '#f9f8fd'})
        p = plt.gcf()
        p.patch.set_facecolor('#f9f8fd')
        p.set_size_inches(2.7, 2.7)
        p.gca().add_artist(my_circle)
        self.graph = FigureCanvasTkAgg(p, self)
        self.graph.get_tk_widget().pack(fill='x')








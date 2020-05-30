import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from service.GlobalStatsService import GlobalStatsService


class GlobalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service = None
        self.configure(bg="#f9f8fd")
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Comic Sans MS", 20, "bold"))
        self.menu_photo = tk.PhotoImage(file=r"img/menu.png")
        self.top_ten_players_photo = tk.PhotoImage(file=r"img/top_ten_players.png")
        self.wpm_stats_photo = tk.PhotoImage(file=r"img/wpm_stats.png")
        self.refresh_photo = tk.PhotoImage(file=r"img/refresh.png")

        self.top_ten_players = None
        self.table = None
        self.graph = None
        self.wpm_stats = None
        self.menu_button = None
        self.refresh_button = None
        self.display_visualization()

    def show_table(self):
        player_list = self.service.get_top_ten_players()
        cols = ['Position', 'Name', 'WPM', 'CPM']
        self.table = ttk.Treeview(self, columns=cols, show='headings', selectmode='none')
        for col in cols:
            self.table.heading(col, text=col)

        for i, player in enumerate(player_list, start=1):
            if i > 10:
                break

            if i % 2 == 1:
                self.table.insert("", "end", values=(i, player['name'], '%.3f'%player['wpm'], '%.3f'%player['cpm']),
                                  tags=('odd_row', ))
            else:
                self.table.insert("", "end", values=(i, player['name'], '%.3f' % player['wpm'], '%.3f' % player['cpm']),
                                  tags=('even_row', ))

        self.table.tag_configure('odd_row', background='#c1c3e8')
        self.table.tag_configure('even_row', background='#666ccd')
        self.table.pack()

    def show_donut_graph(self):
        names = ['1-30', '31-60', '61-90', '91-120', '121-150', '151-180']
        sizes = self.service.get_wpm_stats()
        if sizes is None:
            return
        my_circle = plt.Circle((0, 0), 0.6, color='#f9f8fd')
        plt.pie(sizes, labels=names, colors=['red', 'green', 'blue', 'skyblue', 'yellow', '#9d4edd'],
                wedgeprops={'linewidth': 5, 'edgecolor': '#f9f8fd'})
        p = plt.gcf()
        p.patch.set_facecolor('#f9f8fd')
        p.set_size_inches(2.7, 2.7)
        p.gca().add_artist(my_circle)
        self.graph = FigureCanvasTkAgg(p, self)
        self.graph.get_tk_widget().pack(fill='x')

    def display_visualization(self):
        self.service = GlobalStatsService()
        self.top_ten_players = tk.Label(self, bg="#f9f8fd", image=self.top_ten_players_photo)
        self.top_ten_players.pack()

        self.show_table()

        self.wpm_stats = tk.Label(self, bg="#f9f8fd", image=self.wpm_stats_photo)
        self.wpm_stats.pack()

        self.show_donut_graph()

        self.menu_button = tk.Button(self, image=self.menu_photo, bg="#f9f8fd", borderwidth=0,
                                     command=lambda: self.controller.show_frame("MainMenu"))
        self.menu_button.place(x=200, y=620)

        self.refresh_button = tk.Button(self, image=self.refresh_photo, bg="#f9f8fd", borderwidth=0,
                                        command=lambda: self.refresh())
        self.refresh_button.place(x=600, y=620)

    def delete_visualization(self):
        self.top_ten_players.destroy()
        self.table.destroy()
        self.graph.get_tk_widget().destroy()
        self.wpm_stats.destroy()
        self.menu_button.destroy()
        self.refresh_button.destroy()

    def refresh(self):
        self.delete_visualization()
        self.display_visualization()








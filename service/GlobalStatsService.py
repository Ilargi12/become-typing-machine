import service.HttpModule


class GlobalStatsService:
    def __init__(self):
        self.dict_of_players = service.HttpModule.get_all_stats()

    def get_dict_of_players(self):
        return self.dict_of_players

    def get_top_ten_players(self):
        list_of_players = list(self.dict_of_players)
        list_of_players = list(dict((v['name'], v) for v in list_of_players).values())
        list_of_players.sort(key=lambda e: e['wpm'], reverse=True)
        return list_of_players

    def get_wpm_stats(self):
        wpm_stats = [0, 0, 0, 0, 0, 0]
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
        if wpm_stats == [0, 0, 0, 0, 0, 0]:
            return None
        return wpm_stats

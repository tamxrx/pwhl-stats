import player_info
# Montreal 2024

def get_game_info(home, away, date):

def get_game_list(fname, lname):
    game_list = []
    game1 = player_info.get_player_home(fname, lname, "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=85&key=446521baf8c38984&site_id=0&client_code=pwhl&lang=en&league_id=&callback=angular.callbacks._5")
    game2 = player_info.get_player_home(fname, lname, "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=87&key=446521baf8c38984&site_id=0&client_code=pwhl&lang=en&league_id=&callback=angular.callbacks._5")
    game3 = player_info.get_player_home(fname, lname, "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=85&key=446521baf8c38984&site_id=0&client_code=pwhl&lang=en&league_id=&callback=angular.callbacks._5")
    




import requests
import json
import re

#gets the dictionary of a specific game
def game_data_to_dict(url):
    api_url = url
    response = requests.get(api_url);

    if response.status_code == 200: # successful
        jsonp_data = response.text # data extraction

        match = re.search(r'angular.callbacks._\d+\((.*)\)', jsonp_data)

        if match: 
            json_data = match.group(1)
            data = json.loads(json_data)
            return data
   
    else:
        print("Error, status code:", response.status_code)

# gets visiting team player dicitonary
def get_data_visiting(data_dict):
    visiting_team = data_dict["visitingTeam"]
    skaters= visiting_team["skaters"]
    return skaters;
    
# gets visiting home player dicitonary
def get_data_home(data_dict):
    home_team = data_dict["homeTeam"]
    skaters= home_team["skaters"]
    return skaters;
    

# gets player specific stat from a specifc game
def get_player(lname, fname, data_dict, away_or_home):
    found = False;
    if away_or_home == "home":
        skaters_home = get_data_home(data_dict) #dictionary of skaters
        for skater in skaters_home:
            info = skater["info"]
            name_info = info["firstName"]
            lname_info = info["lastName"]
            if name_info == fname and lname_info == lname:
                stats = skater["stats"]
                found = True
                return stats
            
    elif away_or_home == "away":
        skater_visit = get_data_visiting(data_dict)
        for skater in skater_visit:
            info = skater["info"]
            name_info = info["firstName"]
            lname_info = info["lastName"]
            if name_info == fname and lname_info == lname:
                stats = skater["stats"]
                found = True
                return stats
            
    else:
        if found == False:
            return "No player found"
        else:
            return "wrong stat"

# data = game_data_to_dict("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=104&key=446521baf8c38984&site_id=0&client_code=pwhl&lang=en&league_id=&callback=angular.callbacks._5")
# player = get_player("Watts", "Daryl", data, "home")
# print(player["assists"])

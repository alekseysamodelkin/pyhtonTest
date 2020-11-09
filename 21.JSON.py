# -----------------------------
# Program by Samodelkin
# -----------------------------
import json
filename = "user_settings.txt"
myfile = open(filename, mode="w")

player1 = {
    "PlayerName": "Trump",
    "Score": 345,
    "Awards": ["OR", "NY", "NW"]
}

player2 = {
    "PlayerName": "Bayden",
    "Score": 280,
    "Awards": ["WT", "NM", "LA"]
}

myplayers=[]
myplayers.append(player1)
myplayers.append(player2)

#_______SAVE BY JSON___________

json.dump(myplayers, myfile)
myfile.close()

#______LOAD BY JSON__________

myfile = open(filename, mode="r")
json_data = json.load(myfile)

for user in json_data:
    print("player name is " +str(user["PlayerName"]))
    print("Player score is " +str(user["Score"]))
    print("Player award N1 is " +str(user["Awards"][0]))
    print("Player award N2 is " + str(user["Awards"][1]))
    print("Player award N3 is " + str(user["Awards"][2]))
    print("-----------------------------------------------")
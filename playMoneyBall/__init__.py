import os

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

players_data = {}


def reader():
    folder = "../../playMoneyBall_data/all_csv"
    """
    players = {"MSD":{"testID":24,"TestId2":43},""Crickter" :{"testId":34,"TestId3":65}}
    """
    players = {}
    for file in os.listdir(folder):
        testId = file.rstrip(".csv")
        filepath = folder + "/" + file
        if file != ".DS_Store":
            with open(filepath, 'r') as fileReader:
                line = fileReader.read()
                data = line.split("\n")
                for i, value in enumerate(data):
                    value_length = len(value.split(','))
                    if value_length == 11:
                        over_wise_data = value.split(',')
                        batsman = over_wise_data[4]
                        if batsman in players:
                            if testId in players.get(batsman):
                                players[batsman][testId] = players.get(batsman).get(testId) + int(over_wise_data[7])
                            else:
                                players[batsman][testId] = int(over_wise_data[7])
                        else:
                            players[batsman] = {testId: int(over_wise_data[7])}
    return players


players_data = reader()


def plotbar():
    batsman = list(players_data.keys())[0]
    objects = tuple(players_data.get(batsman).keys())
    y_pos = np.arange(len(objects))
    performance = players_data.get(batsman).values()

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Runs")
    plt.title("Plot for " + batsman)

    plt.show()


if __name__ == "__main__":
    plotbar()

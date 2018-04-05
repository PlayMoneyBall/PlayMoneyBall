import os


def reader():
    folder = "/Users/shirishakodimala/projects/NMG/playMoneyBall_data/all_csv"
    """
    players = {"MSD":{"testID":24,"TestId2":43},""Crickter" :{"testId":34,"TestId3":65}}
    """
    players = {}
    for file in os.listdir(folder):
        testId = file.rstrip(".csv")
        print(testId)
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
    # print(players)


if __name__ == "__main__":
    reader()

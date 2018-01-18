def reader():
    with open("./data/211028.csv", 'r') as file:
        line = file.read()
        data = line.split("\n")
        players={}
        for i, value in enumerate(data):
            value_length = len(value.split(','))
            if value_length == 11:
                over_wise_data = value.split(',');
                batsman=over_wise_data[4];
                if batsman in players:
                    players[batsman]= players.get(batsman) + int(over_wise_data[7])
                else:
                    players[batsman]= int(over_wise_data[7];
        print(players)

if __name__ == "__main__":
    reader()

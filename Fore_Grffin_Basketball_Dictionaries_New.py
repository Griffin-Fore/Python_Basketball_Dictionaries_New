kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }

jason = {
    "name": "Jason Tatum",
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    }

kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    }

damian = {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    }

joel = {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    }



class Player:
    all_players = []

    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
        Player.all_players.append(self)

    @classmethod
    def get_team(cls, team):
        new_team = []
        for player in Player.all_players:
            if player.team == team:
                new_team.append(player)
        for i in new_team:
            print(i.name)

Kevin = Player(kevin)
Jason = Player(jason)
Kyrie = Player(kyrie)
Damian = Player(damian)
Joel = Player(joel)
print(Kevin.name)
print(Jason.name)
print(Kyrie.name)
print(Damian.name)
print(Joel.name)

players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "Griffin Fore", 
        "age":16, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    }
]

player_list = []

for i in players:
    player = Player(i)
    player_list.append(player)

for player in player_list:
    print(player.name)

Player.get_team("Brooklyn Nets")
# TODO: LINE 1043
import os, pyfiglet
import json
from datetime import datetime
import pathlib # for handling directories
from termcolor import colored

team1_players = ['1a', '2a', '3a', '4a', '5a', '6a']
team2_players = ['1b', '2b', '3b', '4b', '5b', '6b']

index_serves = 0
index_serves_failed = 1
index_serves_aces = 2
index_receives = 3
index_receives_failed = 4
index_sets = 5
index_sets_failed = 6
index_attacks = 7
index_attacks_kills = 8
index_attacks_failed = 9
index_blocks = 10
index_blocks_we_have_ball = 11
index_block_opponent_has_ball = 12
index_blocks_failed = 13
index_blocks_kills = 14
index_tips = 15
index_tips_failed = 16
index_tips_kills = 17
index_freeballs = 18
index_freeballs_fails = 19
index_freeballs_kills = 20

SET_POINTS = 25
LAST_SET_POINTS = 15

class Game: # data
    # keeps sets, teams
    # game has max 5 sets
    # game includes two teams playing
    # each set is played until 25 poitns are scored or more, with 2 points difference between teams
    # game ends in BO5 fashion

    MAX_SETS = 5

    def __init__(self, team1, team2):
        self.sets = []
        self.current_set = -1
        self.teams = [team1, team2]
        self.teams_order = [team1, team2]
        self.sets_team1 = 0
        self.sets_team2 = 0
    
    def startNewSet(self):
        self.current_set += 1
        set = Set(self.current_set)
        self.sets.append(set)
    

    def playSet(self, team_with_ball, set):
        print("Set has started. Confirm every prompt by inputing number and pressing ENTER.\n")
        event_list = []
        while not set.isFinished(Stats(), set):
            pointScored = False # reset point scoring check
            pointIsCanceled = False
            event_list.clear() # reset event list every new point
            event = None
            self.displayScore()
            # serve -> [receive -> set -> attack] <- LOOP
            # serve
            print(f"{team_with_ball.name} serves.") # get player name TO DO
            print('\t1. Success\n\t2. Fail\n\t3. Ace')
            while True:
                uinput = input("Outcome: ")
                match uinput:
                    case '1': # success
                        event = Event(team_with_ball, 'serve')
                        Stats().evaluateEvent(event, self, set)
                        team_with_ball = Stats().ballOver(self, team_with_ball)
                        break
                    case '2': # fail
                        event = Event(team_with_ball, 'serve_fail')
                        Stats().evaluateEvent(event, self, set)
                        team_with_ball = Stats().ballOver(self, team_with_ball)
                        Stats().updateScore(event, self, set)
                        pointScored = True
                        break
                    case '3': # ace
                        event = Event(team_with_ball, 'ace')
                        Stats().evaluateEvent(event, self, set)
                        Stats().updateScore(event, self, set)
                        pointScored = True
                        break
                    case 'x': # cancel point
                        pointIsCanceled = True
                        revertPoint(self, set, event_list)
                        break
                    case _:
                        pass
            if pointIsCanceled: break
            if event is not None:
                event_list.append(event) 
            while not pointScored:
                # receive
                print(f"\n\t{team_with_ball.name} receives\n\t\t1.Success\n\t\t2. Fail")
                while True:
                    uinput = input('\tOutcome: ')
                    match uinput:
                        case '1': # success
                            event = Event(team_with_ball, 'receive')
                            Stats().evaluateEvent(event, self, set)
                            break
                        case '2': # fail
                            event = Event(team_with_ball, 'receive_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '4': # freeball, where ball goes over
                            event = Event(team_with_ball, 'freeball')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '5': # freeball fail
                            event = Event(team_with_ball, 'freeball_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '6': # freeball point (sometimes happens)
                            event = Event(team_with_ball, 'freeball_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case 'x': # cancel point
                            pointIsCanceled = True
                            revertPoint(self, set, event_list)
                            break
                        case _:
                            pass
                if pointIsCanceled: break
                event_list.append(event)
                if pointScored: break

                # set
                print(f"\n\t\t{team_with_ball.name} sets:\n\t\t\t1.Success\n\t\t\t2. Fail")
                while True:
                    uinput = input('\t\tOutcome: ')
                    match uinput:
                        case '1': # success
                            event = Event(team_with_ball, 'set')
                            Stats().evaluateEvent(event, self, set)
                            break
                        case '2': # fail
                            event = Event(team_with_ball, 'set_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '4': # freeball, where ball goes over
                            event = Event(team_with_ball, 'freeball')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '5': # freeball fail
                            event = Event(team_with_ball, 'freeball_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '6': # freeball point (sometimes happens)
                            event = Event(team_with_ball, 'freeball_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '7': # tip
                            event = Event(team_with_ball, 'tip')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '8': # tip fail
                            event = Event(team_with_ball, 'tip_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '9': # tip point
                            event = Event(team_with_ball, 'tip_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case 'x': # cancel point
                            pointIsCanceled = True
                            revertPoint(self, set, event_list)
                            break
                        case _:
                            pass

                if pointIsCanceled: break
                event_list.append(event)
                if pointScored: break

                # attack
                print(f"\n\t\t\t{team_with_ball.name} attacks:\n\t\t\t\t1.Success\n\t\t\t\t2. Fail\n\t\t\t\t3. Kill")
                while True:
                    uinput = input('\t\t\tOutcome: ')
                    match uinput:
                        case '1': # success
                            event = Event(team_with_ball, 'attack')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '2': # fail
                            event = Event(team_with_ball, 'attack_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '3': # kill
                            event = Event(team_with_ball, 'attack_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '4': # freeball, where ball goes over
                            event = Event(team_with_ball, 'freeball')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '5': # freeball fail
                            event = Event(team_with_ball, 'freeball_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '6': # freeball point (sometimes happens)
                            event = Event(team_with_ball, 'freeball_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '7': # tip
                            event = Event(team_with_ball, 'tip')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case '8': # tip fail
                            event = Event(team_with_ball, 'tip_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '9': # tip point
                            event = Event(team_with_ball, 'tip_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case 'x': # cancel point
                            pointIsCanceled = True
                            revertPoint(self, set, event_list)
                            break
                        case _:
                            pass
                
                if pointIsCanceled: break
                event_list.append(event)

                # block
                print(f"\n\t\t\t{team_with_ball.name} blocks?\n\t\t\t\tEnter. No block\n1.Monster block\n\t\t\t\t2. Fail\n\t\t\t\t3. Touch, ball ours\n\t\t\t\t4. Blok, opponent has ball")
                while True:
                    uinput = input('\t\t\tOutcome: ')
                    match uinput:
                        case '': # no block
                            break
                        case '1': # monster block
                            event = Event(team_with_ball, 'block_kill')
                            Stats().evaluateEvent(event, self, set)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '2': # fail
                            event = Event(team_with_ball, 'block_fail')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            Stats().updateScore(event, self, set)
                            pointScored = True
                            break
                        case '3': # touch, ball ours
                            event = Event(team_with_ball, 'block_we_have_ball')
                            Stats().evaluateEvent(event, self, set)
                            break
                        case '4': # touch, opponent has ball
                            event = Event(team_with_ball, 'block_opponent_has_ball')
                            Stats().evaluateEvent(event, self, set)
                            team_with_ball = Stats().ballOver(self, team_with_ball)
                            break
                        case 'x': # cancel point
                            pointIsCanceled = True
                            revertPoint(self, set, event_list)
                            break
                        case _:
                            pass
                
                if pointIsCanceled: break
                event_list.append(event)

        # assign +1 set to winning team
        # determine who won maybe?
        winning_team = Stats().getSetWinningTeam(self, set)
        if self.teams[0].name == winning_team.name:
            self.sets_team1 += 1
            set.setWinner(self.teams[0].name)
        else:
            self.sets_team2 += 1
            set.setWinner(self.teams[1].name)


    def displayScore(self):
        current_set = self.sets[self.current_set]
        print(f'\t\t\tCurrent set: {self.current_set+1}')
        print(f'\t\t\t{self.teams[0].name} {self.sets_team1}\t{current_set.score_team1}:{current_set.score_team2}\t{self.sets_team2} {self.teams[1].name}') # change formatting
        print("\n\n")

    def getCurrentSet(self):
        return self.sets[self.current_set]
    
    def getTeamName(self, team):
        return team.name
    
    def isOver(self):
        # check if the game just started
        if len(self.sets) == 0: return False
        # check if either team has 3 won sets
        winners = []
        for set in self.sets:
            winners.append(set.getWinner())
        for i in range(0,2):
            set_count = winners.count(self.teams[i].name)
            if set_count == 3:
                self.setWinner(self.teams[i])
                return True
        return False
    
    def changeServeStartingTeam(self, previous_team):
        if previous_team.name == self.teams[0].name: team = self.teams[1]
        else: team = self.teams[0]    
        return team
    
    def setWinner(self, winner): # sets string name of winner team
        self.winner = winner.name

    def getWinner(self): # returns string name of winner team
        return self.winner

class Set: # data
    # points, rotations, substitutions, scoring history, and events
    def __init__(self, current_set):
        self.set_number = current_set+1
        self.score_team1 = 0
        self.score_team2 = 0
        self.statistics_team1 = [0 for x in range(21)]
        self.statistics_team2 = [0 for x in range(21)]
        self.events = []
        self.winner = "NA"

    def recordEvent(self, event):
        self.events.append(event)

    def isFinished(self, stats, set):
        return stats.isSetFinished(set)
       
    def setWinner(self, winner_team): # sets string name of winner team
        self.winner = winner_team
    
    def getWinner(self): # returns string name of winner team
        return self.winner

class Team:
    # players
    # team level stats in object TeamStats
    def __init__(self, name, players):
        self.name = name
        self.players = players

class Player:
    # name
    # Team
    # number
    # role/position
    # has PlayerStats object
    def __init__(self, name, team, number, position):
        self.name = name
        self.team = team
        self.number = number
        self.position = position
    
    def getName(self):
        return self.name
    
    def getTeam(self):
        return self.team

    def getNumber(self):
        return self.number
    
    def getPosition(self):
        return self.position
    
    # Convert Player object to dictionary for JSON serialization
    def to_dict(self):
        return {
            'name': self.name,
            'team': self.team,
            'number': self.number,
            'position': self.position
        }
    
    # Create Player object from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            team=data['team'],
            number=data['number'],
            position=data['position']
        )
    
class PlayerStats:
    # holds all player-level metrics: attacks, kills, attack errors, receptions, digs, blocks, serves, service errors, etc.
    def __init__(self):
        pass

class TeamStats:
    # games played
    # games won
    # games lost
    def __init__(self):
        pass

class Stats: # calculations
    # engine for processing and calculating stats from events
    # assign outcomes to PlayerStats and ClubStats
    def __init__(self):
        pass
    
    def evaluateEvent(self, event, game, set):
        if game.teams[0].name == event.team.name:
            statistics = set.statistics_team1
        else:
            statistics = set.statistics_team2

        match event.action_type:
            # Serves
            case 'serve':
                set.recordEvent(event)
                statistics[index_serves] += 1
            case 'serve_fail':
                set.recordEvent(event)
                statistics[index_serves] += 1
                statistics[index_serves_failed] += 1
            case 'ace':
                set.recordEvent(event)
                statistics[index_serves] += 1
                statistics[index_serves_aces] += 1

            # Receives
            case 'receive':
                set.recordEvent(event)
                statistics[index_receives] += 1
            case 'receive_fail':
                set.recordEvent(event)
                statistics[index_receives] += 1
                statistics[index_receives_failed] += 1

            # Sets
            case 'set':
                set.recordEvent(event)
                statistics[index_sets] += 1
            case 'set_fail':
                set.recordEvent(event)
                statistics[index_sets] += 1
                statistics[index_sets_failed] += 1

            # Attacks
            case 'attack':
                set.recordEvent(event)
                statistics[index_attacks] += 1
            case 'attack_kill':
                set.recordEvent(event)
                statistics[index_attacks_kills] += 1
            case 'attack_fail':
                set.recordEvent(event)
                statistics[index_attacks] += 1
                statistics[index_attacks_failed] += 1

            # Blocks
            case 'block_we_have_ball':
                set.recordEvent(event)
                statistics[index_blocks] += 1
                statistics[index_blocks_we_have_ball] += 1
            case 'block_opponent_has_ball':
                set.recordEvent(event)
                statistics[index_blocks] += 1
                statistics[index_block_opponent_has_ball] += 1
            case 'block_fail':
                set.recordEvent(event)
                statistics[index_blocks] += 1
                statistics[index_blocks_failed] += 1
            case 'block_kill':
                set.recordEvent(event)
                statistics[index_blocks] += 1
                statistics[index_blocks_kills] += 1

            # Tips
            case 'tip':
                set.recordEvent(event)
                statistics[index_tips] += 1
            case 'tip_fail':
                set.recordEvent(event)
                statistics[index_tips] += 1
                statistics[index_tips_failed] += 1
            case 'tip_kill':
                set.recordEvent(event)
                statistics[index_tips] += 1
                statistics[index_tips_kills] += 1

            # Freeballs
            case "freeball":
                set.recordEvent(event)
                statistics[index_freeballs] += 1
            case "freeball_fail":
                set.recordEvent(event)
                statistics[index_freeballs] += 1
                statistics[index_freeballs_fails] += 1
            case "freeball_kill":
                set.recordEvent(event)
                statistics[index_freeballs] += 1
                statistics[index_freeballs_kills] += 1

            case _:
                print("Unknown event happened.")

    def updateScore(self, event, game, set):
        # im getting event data from OLD OBJECT YOU DUMMY
        # I need to update score based on succes/fail

        fails = ['serve_fail', 'receive_fail', 'set_fail', 'attack_fail', 'block_fail']

        if event.action_type in fails: # for fails, award the other team
            if game.teams[0].name == event.team.name:
                set.score_team2 += 1
                #statistics = set.statistics_team2
            else:
                set.score_team1 += 1
                #statistics = set.statistics_team1 
        else:
            if game.teams[0].name == event.team.name:
                set.score_team1 += 1
                #statistics = set.statistics_team1
            else:
                set.score_team2 += 1
                #statistics = set.statistics_team2

    def isSetFinished(self, set):
        if set.set_number == 5:
            if (set.score_team1 >= LAST_SET_POINTS) or (set.score_team2 >= LAST_SET_POINTS):
                if ((set.score_team1 - set.score_team2) >= 2) or ((set.score_team1 - set.score_team2) <= -2):
                    return True
            return False 
        else: 
            if (set.score_team1 >= SET_POINTS) or (set.score_team2 >= SET_POINTS):
                if ((set.score_team1 - set.score_team2) >= 2) or ((set.score_team1 - set.score_team2) <= -2):
                    return True
            return False
    
    def getSetWinningTeam(self, game, set):
        if (set.score_team1 - set.score_team2) >= 2:
            return game.teams[0]
        else: return game.teams[1]
    
    def startingTeam(self, game):
        print(f'Who serves first?\n1. {game.teams[0].name}\n2. {game.teams[1].name}')
        uinput = input("Choose team: ")
        while True:
            match uinput:
                case '1':
                    team_name = game.teams[0]
                    break
                case '2':
                    team_name = game.teams[1]
                    break
                case _:
                    pass     
        return team_name
        
    def chooseSides(self, game):
        print(f'Who is on left side?\n1. {game.teams[0].name}\n2. {game.teams[1].name}')
        while True:
            uinput = input('Choose team: ')
            if uinput == '1':
                game.teams_order = [game.teams[0], game.teams[1]]
                return game.teams_order
            elif uinput == '2':
                game.teams_order = [game.teams[1], game.teams[0]]
                return game.teams_order
            else: pass


    def ballOver(self, game, current_team): # return team that currently has ball in-play
        if current_team.name == game.teams[0].name: team_with_ball = game.teams[1]
        else: team_with_ball = game.teams[0]
        return team_with_ball

    def revertPoint(self, game, set, event_list): # go back 1 point and remove all events from that point
        # event list has all events that we need to revert
        # Im getting set.statistics_team1 or 2 objects with different indexes


        # check if there is anything to revert
        if not event_list: return

        '''
        example:

        I got one event - serve success, meaning that:
            event_list = [Event(team_with_ball, 'serve')], which is
            event_list = [
                [index.team = team_with_ball, index.action_type = 'serve']
            ]

        So I have two values - team name and what happened
        To revert the event I need to locate which team is team_with_ball.
        I will group events by team name:
        '''

        # group events by team
        team1_events = []
        team2_events = []

        for event in reversed(event_list):
            # now I need to remove all events from set.events log
            for i in range(len(set.events) - 1, -1, -1):
                if set.events[i] == event:
                    del set.events[i]
                    break
            if event.team.name == game.teams[0].name:
                team1_events.append(event)
            else:
                team2_events.append(event)

        '''
        Then going through each team events, I will find corresponding event.action_type and substract 1 from it
        '''
        team_event_list = [team1_events, team2_events]
        for team_events in team_event_list:
            if not team_events: pass
            else:
                if team_events[0].team.name == game.teams[0].name:
                    statistics = set.statistics_team1
                else:
                    statistics = set.statistics_team2
                for event in team_events:
                    match event.action_type:
                        # Serves
                        case 'serve':
                            statistics[index_serves] -= 1
                        case 'serve_fail':
                            statistics[index_serves] -= 1
                            statistics[index_serves_failed] -= 1
                        case 'ace':
                            statistics[index_serves] -= 1
                            statistics[index_serves_aces] -= 1

                        # Receives
                        case 'receive':
                            statistics[index_receives] -= 1
                        case 'receive_fail':
                            statistics[index_receives] -= 1
                            statistics[index_receives_failed] -= 1

                        # Sets
                        case 'set':
                            statistics[index_sets] -= 1
                        case 'set_fail':
                            statistics[index_sets] -= 1
                            statistics[index_sets_failed] -= 1

                        # Attacks
                        case 'attack':
                            statistics[index_attacks] -= 1
                        case 'attack_kill':
                            statistics[index_attacks_kills] -= 1
                        case 'attack_fail':
                            statistics[index_attacks] -= 1
                            statistics[index_attacks_failed] -= 1

                        # Blocks
                        case 'block_we_have_ball':
                            statistics[index_blocks] -= 1
                            statistics[index_blocks_we_have_ball] -= 1
                        case 'block_opponent_has_ball':
                            statistics[index_blocks] -= 1
                            statistics[index_block_opponent_has_ball] -= 1
                        case 'block_fail':
                            statistics[index_blocks] -= 1
                            statistics[index_blocks_failed] -= 1
                        case 'block_kill':
                            statistics[index_blocks] -= 1
                            statistics[index_blocks_kills] -= 1

                        # Tips
                        case 'tip':
                            statistics[index_tips] -= 1
                        case 'tip_fail':
                            statistics[index_tips] -= 1
                            statistics[index_tips_failed] -= 1
                        case 'tip_kill':
                            statistics[index_tips] -= 1
                            statistics[index_tips_kills] -= 1

                        # Freeballs
                        case "freeball":
                            statistics[index_freeballs] -= 1
                        case "freeball_fail":
                            statistics[index_freeballs] -= 1
                            statistics[index_freeballs_fails] -= 1
                        case "freeball_kill":
                            statistics[index_freeballs] -= 1
                            statistics[index_freeballs_kills] -= 1

class Event: # data
    # all kinds of events/actions during the game
    # add event logger? 
    action_types = [ # update this based on Stats().evaluateEvent()
        'serve',
        'serve_fail',
        'ace',
        'receive',
        'receive_fail',
        'set',
        'set_fail'
        'attack',
        'attack_kill',
        'attack_fail',
        'block_we_have_ball',
        'block_opponent_has_ball'
        'block_fail',
        'block_kill',
        'tip'
        'tip_fail',
        'tip_kill'
    ]

    def __init__(self, team, action_type):
        self.team = team
        self.action_type = action_type   

def save_game_to_file(game, filename='games.json'):
    """
    Save a Game object to JSON file
    """
    try:
        # Check if file exists and load existing games
        games_data = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                games_data = json.load(file)
        
        # Convert Game object to dictionary
        game_data = {
            'timestamp': datetime.now().isoformat(),
            'team_names': [game.teams[0].name, game.teams[1].name],
            'teams': [game.teams[0], game.teams[1]],
            'winner': game.getWinner() if hasattr(game, 'winner') else "Not finished",
            'sets_team1': game.sets_team1,
            'sets_team2': game.sets_team2,
            'sets': []
        }
        
        # Add set data
        for set_obj in game.sets:
            set_data = {
                'set_number': set_obj.set_number,
                'score_team1': set_obj.score_team1,
                'score_team2': set_obj.score_team2,
                'winner': set_obj.getWinner(),
                'statistics_team1': set_obj.statistics_team1,
                'statistics_team2': set_obj.statistics_team2
            }
            game_data['sets'].append(set_data)
        
        # Add to existing games and save
        games_data.append(game_data)
        
        with open(filename, 'w') as file:
            json.dump(games_data, file, indent=2)
        
        print(f"Game saved to {filename}")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_games_from_file(filename='games.json'):
    """
    Load games from JSON file
    """
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []
    except Exception as e:
        print(f"Error loading games: {e}")
        return []

def clear_screen():
    os.system('cls')

def start_match():
    clear_screen()
    print("=== START NEW MATCH ===")

    # Create team objects and assign players
    team1_name = input("Name of first team: ")
    team2_name = input("Name of second team: ")
    print()

    team1 = Team(team1_name, team1_players)
    team2 = Team(team2_name, team2_players)

    # Initialize stats object
    stats = Stats()

    # Create game object
    game = Game(team1, team2)

    # Decide which team starts serving
    serve_starting_team = stats.startingTeam(game)
    print()
    
    # check if game is done with isGameOver()
    while not game.isOver():
        game.startNewSet()
        current_set = game.getCurrentSet()
        if game.current_set > 0: serve_starting_team = game.changeServeStartingTeam(serve_starting_team)

        # Change on which side a team is playing - qol for user, not relevant for stats
        teams_order = stats.chooseSides(game)

        clear_screen()
        game.playSet(serve_starting_team, current_set)
        game.displayScore()
        input(f'{current_set.getWinner()} won the set! Press ENTER to continue...')
    
    input(f"\n{game.getWinner()} won! Press ENTER to return to menu...")

    # Save the game data after match is complete
    save_game_to_file(game)

def view_stats():
    clear_screen()
    print("=== VIEW STATISTICS ===")

     # Load all games
    games = load_games_from_file()
    
    if not games:
        print("No game data found. Play some matches first!")
        input("\nPress ENTER to return to menu...")
        return
    
    while True:
        print("\n1. View All Games Summary")
        print("2. View Detailed Game Statistics - TO DO")
        print("3. View Team Statistics - TO DO")
        print("4. Back to Main Menu")
        
        choice = input("\nChoose option: ")
        
        if choice == '1':
            view_all_games_summary(games)
        elif choice == '2':
            pass
            #view_detailed_game_stats(games)
        elif choice == '3':
            pass
            #view_team_statistics(games)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    input("\nPress ENTER to return to menu...")

def view_all_games_summary(games_file):
    clear_screen()
    print("=== ALL GAMES SUMMARY ===")
    print()
    
    for i, game in enumerate(games_file, 1):
        print(f"Game {i}:")
        print(f"  Teams: {game['team_names'][0]} vs {game['team_names'][1]}")
        print(f"  Winner: {game['winner']}")
        print(f"  Final Score: {game['sets_team1']}-{game['sets_team2']}")
        print(f"  Date: {game['timestamp'][:10]}")
        print(f"  Sets:")
        for set_data in game['sets']:
            print(f"    Set {set_data['set_number']}: {set_data['score_team1']}-{set_data['score_team2']} (Winner: {set_data['winner']})")
            
            # figure out later how to do it with zip(), for now let it work
            serve_total = set_data['statistics_team1'][index_serves]
            serve_fails = set_data['statistics_team1'][index_serves_failed]
            serve_aces = set_data['statistics_team1'][index_serves_aces]
            receive_total = set_data['statistics_team1'][index_receives]
            receive_fails = set_data['statistics_team1'][index_receives_failed]
            receive_success = receive_total - receive_fails
            set_total = set_data['statistics_team1'][index_sets]
            set_fails = set_data['statistics_team1'][index_sets_failed]
            set_successes = set_total - set_fails
            attack_total = set_data['statistics_team1'][index_attacks]
            attack_kills = set_data['statistics_team1'][index_attacks_kills]
            attack_fails = set_data['statistics_team1'][index_attacks_failed]
            block_total = set_data['statistics_team1'][index_blocks]
            block_us = set_data['statistics_team1'][index_blocks_we_have_ball]
            block_them = set_data['statistics_team1'][index_block_opponent_has_ball]
            block_fails = set_data['statistics_team1'][index_blocks_failed]
            block_kills = set_data['statistics_team1'][index_blocks_kills]
            tip_total = set_data['statistics_team1'][index_tips]
            tip_fails = set_data['statistics_team1'][index_tips_failed]
            tip_kills = set_data['statistics_team1'][index_tips_kills]
            freeball_total = set_data['statistics_team1'][index_freeballs]
            freeball_fails = set_data['statistics_team1'][index_freeballs_fails]
            freeball_kills = set_data['statistics_team1'][index_freeballs_kills]

            # opps
            opp_serve_total = set_data['statistics_team2'][index_serves]
            opp_serve_fails = set_data['statistics_team2'][index_serves_failed]
            opp_serve_aces = set_data['statistics_team2'][index_serves_aces]
            opp_receive_total = set_data['statistics_team2'][index_receives]
            opp_receive_fails = set_data['statistics_team2'][index_receives_failed]
            opp_receive_success = opp_receive_total - opp_receive_fails
            opp_set_total = set_data['statistics_team2'][index_sets]
            opp_set_fails = set_data['statistics_team2'][index_sets_failed]
            opp_set_successes = opp_set_total - opp_set_fails
            opp_attack_total = set_data['statistics_team2'][index_attacks]
            opp_attack_kills = set_data['statistics_team2'][index_attacks_kills]
            opp_attack_fails = set_data['statistics_team2'][index_attacks_failed]
            opp_block_total = set_data['statistics_team2'][index_blocks]
            opp_block_us = set_data['statistics_team2'][index_blocks_we_have_ball]
            opp_block_them = set_data['statistics_team2'][index_block_opponent_has_ball]
            opp_block_fails = set_data['statistics_team2'][index_blocks_failed]
            opp_block_kills = set_data['statistics_team2'][index_blocks_kills]
            opp_tip_total = set_data['statistics_team2'][index_tips]
            opp_tip_fails = set_data['statistics_team2'][index_tips_failed]
            opp_tip_kills = set_data['statistics_team2'][index_tips_kills]
            opp_freeball_total = set_data['statistics_team2'][index_freeballs]
            opp_freeball_fails = set_data['statistics_team2'][index_freeballs_fails]
            opp_freeball_kills = set_data['statistics_team2'][index_freeballs_kills]

            serve_fails_p = serve_fails/serve_total
            serve_aces_p = serve_aces/serve_total

            print(f'Detailed Data for team {team}:')
            print('Serves:')
            print(f'\tTotal: {serve_total}')
            print(f'\tFailed: {serve_fails}, which is {serve_fails_p:.0%} total')
            print(f'\tAces: {serve_aces}, which is {serve_aces_p:.0%} total')

            receive_fails_p = receive_fails/receive_total
            receive_success_p = receive_success/receive_total

            print('Receives:')
            print(f'\tTotal: {receive_total}')
            print(f'\tFailed: {receive_fails}, which is {receive_fails_p:.0%} total')
            print(f'\tSuccessful: {receive_success}, which is {receive_success_p:.0%} total')

            set_fails_p = set_fails/set_total
            set_successes_p = set_successes/set_total

            print('Sets:')
            print(f'\tTotal: {set_total}')
            print(f'\tFailed: {set_fails}, which is {set_fails_p:.0%} total')
            print(f'\tSuccessful: {set_successes}, which is {set_successes_p:.0%} total')

            attack_fails_p = attack_fails/attack_total
            attack_kills_p = attack_kills/attack_total
        
            print('Attacks:')
            print(f'\tTotal: {attack_total}')
            print(f'\tFailed: {attack_fails}, which is {attack_fails_p:.0%} total')
            print(f'\tKills: {attack_kills}, which is {attack_kills_p:.0%} total')

            tip_fails_p = tip_fails/tip_total
            tip_kills_p = tip_kills/tip_total

            print('Tips:')
            print(f'\tTotal: {tip_total}')
            print(f'\tFailed: {tip_fails}, which is {tip_fails_p:.0%} total')
            print(f'\tKills: {tip_kills}, which is {tip_kills_p:.0%} total')

            block_fails_p = block_fails/block_total
            block_kills_p = block_kills/block_total
            block_us_p = block_us/block_total
            block_them_p = block_them/block_total

            print('Blocks:')
            print(f'\tTotal: {block_total}')
            print(f'\tFailed: {block_fails}, which is {block_fails_p:.0%} total')
            print(f'\tKills: {block_kills}, which is {block_kills_p:.0%} total')
            print(f'\tTouches, we got ball: {block_us}, which is {block_us_p:.0%} total')
            print(f'\tTouches, they got ball: {block_them}, which is {block_them_p:.0%} total')

            freeball_fails_p = freeball_fails/freeball_total
            freeball_kills_p = freeball_kills/freeball_total

            print('Freeballs:')
            print(f'\tTotal: {freeball_total}')
            print(f'\tFailed: {freeball_fails}, which is {freeball_fails_p:.0%} total')
            print(f'\tKills: {freeball_kills}, which is {freeball_kills_p:.0%} total')

            print("-" * 50)

            # now total stats
            main_scored = serve_aces + attack_kills + block_kills + tip_kills + freeball_kills
            #main_gave = serve_fails + receive_fails + set_fails + attack_fails + block_fails + tip_fails + freeball_fails
            opp_scored = opp_serve_aces + opp_attack_kills + opp_block_kills + opp_tip_kills + opp_freeball_kills
            opp_gave = opp_serve_fails + opp_receive_fails + opp_set_fails + opp_attack_fails + opp_block_fails + opp_tip_fails + opp_freeball_fails
            
            print(f'Points won: {set_data['score_team1']}')
            print(f'We scored: {main_scored} ({main_scored/set_data['score_team1']:.0%})\tThey gave us: {opp_gave} ({opp_scored/set_data['score_team2']:.0%})')
            print(f'From points we scored: \tAces: {serve_aces/main_scored:.0%}\tKills: {attack_kills/main_scored:.0%}\tBlocks: {block_kills/main_scored:.0%}\tTips: {tip_kills/main_scored:.0%}\tFreeball kills: {freeball_kills/main_scored:.0%}')
            print(f'From points they gave us: \tServe fails: {opp_serve_fails/opp_gave:.0%}\tAttack fails: {attack_fails/opp_gave:.0%}\tBlock fails: {block_fails/opp_gave:.0%}\tTip fails: {tip_fails/opp_gave:.0%}\tFreeball fails: {freeball_fails/opp_gave:.0%}')
            # make a list of all % of getting points/total points and get max and min
            scoring_dict_main = {
                'Aces' : serve_aces,
                'Spikes' : attack_kills,
                'Blocks' : block_kills,
                'Tips' : tip_kills,
                'Freeballs' : freeball_kills
            }
            giving_dict_main = {
                'Serves' : serve_fails,
                'Spikes' : attack_fails,
                'Blocks' : block_fails,
                'Tips' : tip_fails,
                'Freebalss' : freeball_fails
            }
            scoring_dict_opp = {
                'Aces' : opp_serve_aces,
                'Spikes' : opp_attack_kills,
                'Blocks' : opp_block_kills,
                'Tips' : opp_tip_kills,
                'Freeballs' : opp_freeball_kills
            }
            giving_dict_opp = {
                'Serves' : opp_serve_fails,
                'Spikes' : opp_attack_fails,
                'Blocks' : opp_block_fails,
                'Tips' : opp_tip_fails,
                'Freebalss' : opp_freeball_fails
            }

            max([serve_aces, attack_kills, block_kills, tip_kills, freeball_kills])
            print(f'Our most effective scoring way: {max(scoring_dict_main, key=scoring_dict_main.get)} ({scoring_dict_main[max(scoring_dict_main, key=scoring_dict_main.get)]})')
            print(f'We gave them most points on: {max(giving_dict_main, key=giving_dict_main.get)} ({giving_dict_main[max(giving_dict_main, key=giving_dict_main.get)]}')
            print(f'Their most effective scoring way: {max(scoring_dict_opp, key=scoring_dict_opp.get)} ({scoring_dict_opp[max(scoring_dict_opp, key=scoring_dict_opp.get)]}')
            print(f'They gave us most points on: {max(giving_dict_opp, key=giving_dict_opp.get)} ({giving_dict_opp[max(giving_dict_opp, key=giving_dict_opp.get)]}')
    
    input("\nPress ENTER to continue...")

def manage_players():
    clear_screen()
    print("=== PLAYER MANAGEMENT ===")
    print("1. Add player")
    print("2. Remove player")
    print("3. Show all players")
    uinput = input("\nChoose option ('e' to exit): ")
    match uinput:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case 'e':
            pass
        case _:
            clear_screen()
            input('Invalid input! Press ENTER to try again...')
            manage_players()

def display_menu():
    ascii_art = pyfiglet.figlet_format("Volleyball Tracker", font='fender', width = 133, justify = 'center')
    c_ascii_art = colored(ascii_art, 'red')
    print(colored('=' * 133, 'red'))
    print("\n\n\n")
    print(c_ascii_art)
    print()
    print(colored('=' * 133, 'red'))

    print("1. Start New Match")
    print("2. View Statistics") 
    print("3. Player Management")
    print()

def menu_choice(uinput):
    match uinput:
        case '1':
            start_match()
        case '2':
            view_stats()
        case '3':
            manage_players()
        case 'e':
            quit()
        case _:
            clear_screen()
            input('Invalid input! Press ENTER to try again...')

def main():
    while True:
        display_menu()
        uinput = input("Choose option ('e' to exit): ")
        if uinput == 'e':
            break
        else:
            menu_choice(uinput)

main()
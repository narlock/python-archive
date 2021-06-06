#This assignment will allow you to practice writing classes in Python

#Title: OOP Assignment: Games
#Author: Anthony Narlock
#Prof: Lisa Minogue
#Class: CSCI 2061
#Date: Nov 2, 2020

class Game:
    #Class constructor
    def __init__(self,name,desc):
         self._name = name
         self._desc = desc

    #Getters for name and description
         
    #name getter
    def get_name(self):
        return self._name
    
    #description getter
    def get_desc(self):
        return self._desc

    #name.setter
    def set_name(self, new_name):
        self._name = new_name

    #desc.setter
    def set_desc(self, new_desc):
        self._desc = new_desc

    #__str__ method
    def __str__(self):
        return "Game name: " + self._name + " Description: " + self._desc + "\n"
    

class PCGame(Game):
    #Constructor to make PC Game
    def __init__(self, name, desc, min_RAM, min_CPU, recommended_RAM, recommended_CPU):
        Game.__init__(self, name, desc)
        self._min_RAM = min_RAM
        self._min_CPU = min_CPU
        self._recommended_RAM = recommended_RAM
        self._recommended_CPU = recommended_CPU

    #min_RAM getter
    def get_min_RAM(self):
        return self._min_RAM

    #min_CPU getter
    def get_min_CPU(self):
        return self._min_CPU
    
    #recommended RAM getter
    def get_recommended_RAM(self):
        return self._recommended_RAM

    #recommended CPU getter
    def get_recommended_CPU(self):
        return self._recommended_CPU

    #min_RAM.setter
    def set_min_RAM(self, new_min_RAM):
        self._min_RAM = new_min_RAM

    #min_CPU.setter
    def set_min_CPU(self, new_min_CPU):
        self.min_CPU = new_min_CPU

    #recommended_RAM.setter
    def set_recommended_RAM(self, new_recommended_RAM):
        self.recommended_RAM = new_recommended_RAM

    #recommended_CPU.setter
    def set_recommended_CPU(self, new_recommended_CPU):
        self.recommended_CPU = new_recommended_CPU

    #__str__ method
    def __str__(self):
        return Game.__str__(self) + "Min RAM: " + self._min_RAM + " Min CPU: " + self._min_CPU + " Recommended RAM: " + self._recommended_RAM + " Recommended CPU: " + self._recommended_CPU + "\n\n"

class BoardGame(Game):
    #Constructor to make Board Game
    def __init__(self, name, desc, min_players, max_players):
        Game.__init__(self, name, desc)
        self._min_players = min_players
        self._max_players = max_players

    #property
    def get_min_players(self):
        return self._min_players

    #property
    def get_max_players(self):
        return self._max_players

    #min_players.setter
    def set_min_players(self, new_min_players):
        self._min_players = new_min_players

    #max_players.setter
    def set_max_players(self, new_max_players):
        self._max_players = new_max_players

    #__str__ method
    def __str__(self):
        return Game.__str__(self) + "Min players: " + self._min_players + " Max players: " + self._max_players + "\n\n"

#Driver
def main():
    #Create empty list for reference, create options
    game_list = []
    options = ['G','P','B','D','Q']
    print("Choose the type of Game to create \nG: Generic Game, P: PC Game, B: Board Game\n or D: Display all Games, Q: Quit")
    select = input("Enter your choice: ")

    #Input validation, the choice must be in the options
    while(select.upper() not in options):
        print("Invalid choice, please re-enter. You entered: " + select)
        select = input("Enter your choice: ")


    #Under the condition that the user does not want to quit
    while(select.upper() != 'Q'):
        #Option to make Generic Game
        if(select.upper() == 'G'):
            game_name = input("Enter the name of the game:")
            game_desc = input("Enter the description:")
            generic_game = Game(game_name, game_desc)
            #Add game to list
            game_list.append(generic_game)

        #Option to make PC Game
        elif(select.upper() == 'P'):
            game_name = input("Enter the name of the game:")
            game_desc = input("Enter the description:")
            min_RAM = input("Enter the minimum RAM needed to run the game (in MB):")
            min_CPU = input("Enter the minimum CPU needed to run the game (in GHz):")
            rec_RAM = input("Enter the recommended RAM needed to run the game (in MB):")
            rec_CPU = input("Enter the recommended CPU needed to run the game (in GHz):")
            pc_game = PCGame(game_name, game_desc, min_RAM, min_CPU, rec_RAM, rec_CPU)

            #add game to list
            game_list.append(pc_game)
                            
        #Option to make Board Game
        elif(select.upper() == 'B'):
            game_name = input("Enter the name of the game:")
            game_desc = input("Enter the description:")
            min_players = input("Enter the minimum number of players:")
            max_players = input("Enter the maximum number of players:")
            board_game = BoardGame(game_name, game_desc, min_players, max_players)

            #Add game to the list
            game_list.append(board_game)

        #Option to display the list
        elif(select.upper() == 'D'):
            for i in range(len(game_list)):
                print(game_list[i])

        #Reprompt user
        select = input("Enter your choice: ")
        

if __name__ == '__main__':
    main()

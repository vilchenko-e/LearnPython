import os

class Choice:
    def __init__(self, name):
        self.name = name
    
    def beats(self, other):
        return False


class Rock(Choice):
    def __init__(self):
        super().__init__("камень")
    
    def beats(self, other):
        return isinstance(other, Scissors)


class Scissors(Choice):
    def __init__(self):
        super().__init__("ножницы")
    
    def beats(self, other):
        return isinstance(other, Paper)


class Paper(Choice):
    def __init__(self):
        super().__init__("бумага")
    
    def beats(self, other):
        return isinstance(other, Rock)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def make_choice(self, choice_name):
        if choice_name == "камень":
            return Rock()
        elif choice_name == "ножницы":
            return Scissors()
        elif choice_name == "бумага":
            return Paper()
        return None


class Game:
    def __init__(self):
        self.players = []
        self.rounds = 0
    
    def clear_screen(self):
        os.system('clear')
    
    def wait_for_enter(self, msg="Нажмите Enter для продолжения..."):
        input(msg)
    
    def setup_players(self):
        self.clear_screen()
        num_players = int(input("Введите количество игроков: "))
        
        for i in range(num_players):
            name = input(f"Введите имя игрока {i+1}: ")
            self.players.append(Player(name))
    
    def setup_rounds(self):
        while True:
            try:
                self.rounds = int(input("\nСколько раундов будете играть? "))
                if self.rounds > 0:
                    break
                print("Введите положительное число!")
            except ValueError:
                print("Введите целое число!")
    
    def get_player_choice(self, player):
        self.clear_screen()
        print(f"Ход игрока: {player.name}")
        print()
        
        while True:
            choice_name = input(f"{player.name}, ваш выбор (камень/ножницы/бумага): ").lower()
            choice = player.make_choice(choice_name)
            if choice:
                self.clear_screen()
                print(f"{player.name}, ваш выбор принят!")
                self.wait_for_enter()
                self.clear_screen()
                return choice
            print("Неверный выбор! Используйте: камень, ножницы или бумага")
    
    def determine_winner(self, choices):
        rock_players = []
        scissors_players = []
        paper_players = []
        
        for player, choice in choices:
            if choice.name == "камень":
                rock_players.append(player)
            elif choice.name == "ножницы":
                scissors_players.append(player)
            elif choice.name == "бумага":
                paper_players.append(player)
        if len(rock_players) == len(self.players) or \
           len(scissors_players) == len(self.players) or \
           len(paper_players) == len(self.players) or \
           (paper_players and rock_players and scissors_players):
            return None
        
        winners = []
        
        if rock_players and scissors_players:
            winners.extend(rock_players)
        if scissors_players and paper_players:
            winners.extend(scissors_players)
        if paper_players and rock_players:
            winners.extend(paper_players)
        
        return winners if winners else None
    
    def play_round(self, round_num):
        choices = []
        
        for player in self.players:
            choice = self.get_player_choice(player)
            choices.append((player, choice))
        
        self.clear_screen()
        for player, choice in choices:
            print(f"{player.name} выбрал: {choice.name}")
        print()
        
        winners = self.determine_winner(choices)
        
        if winners is None:
            print("ничья")
        else:
            for winner in winners:
                winner.score += 1
            print(f"Победители:")
            for winner in winners:
                print(f"  {winner.name}")
        
        self.show_score()
    
    def show_score(self):
        print(f"\nТекущий счёт")
        for player in self.players:
            print(f"{player.name}: {player.score}")
    
    def show_final_result(self):
        print("Финальный результат")
        
        self.show_score()
        
        max_score = max(player.score for player in self.players)
        winners = [player for player in self.players if player.score == max_score]
        
        if len(winners) == 1:
            print(f"\n{winners[0].name} Победил в игре!")
        else:
            print(f"\nНичья между:")
            for winner in winners:
                print(f"  {winner.name}")
    
    def start(self):
        self.clear_screen()
        print("Игра Камень-Ножницы-Бумага")
        self.wait_for_enter("Нажмите Enter для начала...")
        
        self.setup_players()
        self.clear_screen()
        self.setup_rounds()
        
        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)
            
            if round_num < self.rounds:
                self.wait_for_enter("\nНажмите Enter для следующего раунда...")
        
        self.show_final_result()
        print("\nСпасибо за игру!")

game = Game()
game.start()


import random
import os
from typing import List, Tuple, Dict

class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.coordinates = []
        self.hits = 0

    def is_sunk(self) -> bool:
        return self.hits >= self.size

class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships: List[Ship] = []
        self.shots = set()

    def place_ship(self, ship: Ship, start: Tuple[int, int], orientation: str) -> bool:
        x, y = start
        coords = []
        
        for i in range(ship.size):
            if orientation == 'H':
                if y + i >= self.size or self.board[x][y + i] != '~':
                    return False
                coords.append((x, y + i))
            else:  # vertical
                if x + i >= self.size or self.board[x + i][y] != '~':
                    return False
                coords.append((x + i, y))
        
        ship.coordinates = coords
        for x, y in coords:
            self.board[x][y] = 'O'
        self.ships.append(ship)
        return True

    def receive_shot(self, coord: Tuple[int, int]) -> str:
        x, y = coord
        if coord in self.shots:
            return 'Already shot here!'
        
        self.shots.add(coord)
        
        for ship in self.ships:
            if coord in ship.coordinates:
                ship.hits += 1
                self.board[x][y] = 'X'
                if ship.is_sunk():
                    return f'Sunk {ship.name}!'
                return 'Hit!'
        
        self.board[x][y] = 'M'
        return 'Miss!'

    def display(self, hide_ships: bool = False):
        print('   ' + ' '.join([chr(65 + i) for i in range(self.size)]))
        for i in range(self.size):
            row = [str(i).rjust(2), '']
            for j in range(self.size):
                cell = self.board[i][j]
                if hide_ships and cell == 'O':
                    row.append('~')
                else:
                    row.append(cell)
            print(' '.join(row))

class Game:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()
        self.ships = [
            Ship('Carrier', 5),
            Ship('Battleship', 4),
            Ship('Cruiser', 3),
            Ship('Submarine', 3),
            Ship('Destroyer', 2)
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_player_move(self) -> Tuple[int, int]:
        while True:
            try:
                move = input("Enter your move (e.g., A5): ").upper()
                if len(move) < 2:
                    raise ValueError
                col = ord(move[0]) - 65
                row = int(''.join(move[1:]))
                if 0 <= row < self.player_board.size and 0 <= col < self.player_board.size:
                    return row, col
            except ValueError:
                pass
            print("Invalid move! Please enter a letter followed by a number (e.g., A5)")

    def place_computer_ships(self):
        for ship in self.ships:
            while True:
                x = random.randint(0, self.computer_board.size - 1)
                y = random.randint(0, self.computer_board.size - 1)
                orientation = random.choice(['H', 'V'])
                if self.computer_board.place_ship(ship, (x, y), orientation):
                    break

    def place_player_ships(self):
        print("\nPlace your ships!")
        for ship in self.ships:
            self.player_board.display()
            while True:
                try:
                    print(f"\nPlacing {ship.name} (size: {ship.size})")
                    pos = input("Enter starting position (e.g., A5): ").upper()
                    orientation = input("Enter orientation (H/V): ").upper()
                    
                    if len(pos) < 2 or orientation not in ['H', 'V']:
                        raise ValueError
                    
                    col = ord(pos[0]) - 65
                    row = int(''.join(pos[1:]))
                    
                    if self.player_board.place_ship(ship, (row, col), orientation):
                        break
                    print("Invalid placement! Try again.")
                except ValueError:
                    print("Invalid input! Please enter a letter followed by a number and H/V for orientation")
            self.clear_screen()

    def play(self):
        self.clear_screen()
        print("Welcome to Battleship!")
        self.place_player_ships()
        self.place_computer_ships()
        
        computer_shots = set()
        
        while True:
            self.clear_screen()
            print("\nComputer's board (your shots):")
            self.computer_board.display(hide_ships=True)
            print("\nYour board:")
            self.player_board.display()
            
            # Player's turn
            move = self.get_player_move()
            result = self.computer_board.receive_shot(move)
            print(f"\nYour shot: {result}")
            
            if all(ship.is_sunk() for ship in self.computer_board.ships):
                print("\nCongratulations! You won!")
                break
            
            # Computer's turn
            while True:
                x = random.randint(0, self.player_board.size - 1)
                y = random.randint(0, self.player_board.size - 1)
                if (x, y) not in computer_shots:
                    computer_shots.add((x, y))
                    break
            
            result = self.player_board.receive_shot((x, y))
            print(f"Computer shot at {chr(65 + y)}{x}: {result}")
            input("\nPress Enter to continue...")
            
            if all(ship.is_sunk() for ship in self.player_board.ships):
                print("\nGame Over! The computer won!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
import random
from typing import List, Tuple
from collections import defaultdict

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = self._get_value()
        
    def _get_value(self) -> int:
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 1
        return int(self.rank)
        
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['♠', '♣', '♥', '♦']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self, num_cards: int) -> List[Card]:
        return [self.cards.pop() for _ in range(num_cards)]

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0
        
    def add_cards(self, cards: List[Card]):
        self.hand.extend(cards)
        
    def remove_cards(self, indices: List[int]) -> List[Card]:
        removed = []
        for index in sorted(indices, reverse=True):
            removed.append(self.hand.pop(index))
        return removed

class Cribbage:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.dealer_index = 0
        self.crib = []
        self.starter_card = None
        
    def play_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.crib = []
        
        # Deal cards
        for player in self.players:
            player.hand = []
            player.add_cards(self.deck.deal(6))
            
        # Players discard to crib
        for player in self.players:
            print(f"\n{player.name}'s hand: {', '.join(str(card) for card in player.hand)}")
            indices = self._get_discard_input(player)
            self.crib.extend(player.remove_cards(indices))
            
        # Cut for starter
        self.starter_card = self.deck.deal(1)[0]
        print(f"\nStarter card: {self.starter_card}")
        
        # If starter is Jack, dealer gets 2 points
        if self.starter_card.rank == 'J':
            self.players[self.dealer_index].score += 2
            print(f"Nibs! {self.players[self.dealer_index].name} gets 2 points")
            
        # Count hands
        for i, player in enumerate(self.players):
            points = self._count_hand(player.hand, self.starter_card)
            player.score += points
            print(f"{player.name}'s hand scores {points} points")
            
        # Count crib
        crib_points = self._count_hand(self.crib, self.starter_card)
        self.players[self.dealer_index].score += crib_points
        print(f"Crib scores {crib_points} points")
        
        # Switch dealer
        self.dealer_index = (self.dealer_index + 1) % 2
        
    def _get_discard_input(self, player: Player) -> List[int]:
        while True:
            try:
                input_str = input(f"{player.name}, choose 2 cards to discard (0-5): ")
                indices = [int(x) for x in input_str.split()]
                if len(indices) == 2 and all(0 <= i <= 5 for i in indices):
                    return indices
            except ValueError:
                pass
            print("Please enter two valid card indices")
            
    def _count_hand(self, cards: List[Card], starter: Card) -> int:
        all_cards = cards + [starter]
        points = 0
        
        # Fifteens
        points += self._count_fifteens(all_cards)
        
        # Pairs
        points += self._count_pairs(all_cards)
        
        # Runs
        points += self._count_runs(all_cards)
        
        # Flush
        if len(set(card.suit for card in cards)) == 1:
            points += 4
            if starter.suit == cards[0].suit:
                points += 1
                
        return points
        
    def _count_fifteens(self, cards: List[Card]) -> int:
        def find_fifteens(remaining: List[Card], current_sum: int) -> int:
            if current_sum == 15:
                return 1
            if current_sum > 15 or not remaining:
                return 0
            return (find_fifteens(remaining[1:], current_sum + remaining[0].value) +
                   find_fifteens(remaining[1:], current_sum))
                   
        return find_fifteens(cards, 0) * 2
        
    def _count_pairs(self, cards: List[Card]) -> int:
        pairs = 0
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                if cards[i].rank == cards[j].rank:
                    pairs += 1
        return pairs * 2
        
    def _count_runs(self, cards: List[Card]) -> int:
        ranks = [card.rank for card in cards]
        rank_values = []
        for rank in ranks:
            if rank == 'A':
                rank_values.append(1)
            elif rank in ['J', 'Q', 'K']:
                rank_values.append(10 + ['J', 'Q', 'K'].index(rank))
            else:
                rank_values.append(int(rank))
                
        rank_values.sort()
        max_run = 0
        current_run = 1
        
        for i in range(1, len(rank_values)):
            if rank_values[i] == rank_values[i-1] + 1:
                current_run += 1
            else:
                max_run = max(max_run, current_run)
                current_run = 1
                
        max_run = max(max_run, current_run)
        return max_run if max_run >= 3 else 0

if __name__ == "__main__":
    game = Cribbage()
    while max(player.score for player in game.players) < 121:
        game.play_round()
        print("\nScores:")
        for player in game.players:
            print(f"{player.name}: {player.score}")
    
    winner = max(game.players, key=lambda p: p.score)
    print(f"\n{winner.name} wins with {winner.score} points!")
    
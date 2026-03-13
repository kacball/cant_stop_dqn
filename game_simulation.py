import random

MAX_EP_LEN = 1_000_000

class GameState:
    columns_taken: dict
    player1_won_columns: int
    player2_won_columns: int
    player1_column_position: list[int]
    player2_column_position: list[int]
    position_with_current_columns_climbed: list[int]
    dice_thrown: list[int]

    def __init__(self):
        self.columns_taken = {}
        self.player1_won_columns = 0
        self.player2_won_columns = 0
        self.player1_column_position = 11 * [0]
        self.player2_column_position = 11 * [0]
        self.position_with_current_columns_climbed = 11 * [0]
        self.dice_thrown = None

    def did_finish(self):
        return self.player1_won_columns >= 3 or self.player2_won_columns >= 3

    def player_finishes_move_with_passing(self, player_id: int):
        if player_id == 1:
            for i in range(11):
                self.player1_column_position[i] = max(self.player1_column_position[i], self.position_with_current_columns_climbed[i])
                self.player1_won_columns += int(self.player1_won_columns[i] == 13 - 2 * abs(i - 7))
            self.position_with_current_columns_climbed = 11 * [0]
        else:
            for i in range(11):
                self.player2_column_position[i] = max(self.player2_column_position[i], self.position_with_current_columns_climbed[i])
                self.player2_won_columns += int(self.player2_won_columns[i] >= 13 - 2 * abs(i - 7))

        self.position_with_current_columns_climbed = 11 * [0]

    def player_finishes_move_with_no_moves_possible(self):
        self.position_with_current_columns_climbed = 11 * [0]
    
    def current_climbed_columns(self) -> set:
        current_climbed_columns = []
        for i in range(11):
            if self.position_with_current_columns_climbed[i] > 0:
                current_climbed_columns.append(i)
        return set(current_climbed_columns)

    def climb_column(self, column_id):
        self.current_climbed_columns[column_id] += 1




def simulate_move_and_check_if_player_ends_move(game_state: GameState, player_strategy, player_id: int) -> bool:
    is_throwing, index_of_pair_of_first_dice, choose_the_first_pair_if_necessary =  player_strategy(game_state)

    if game_state.dice_thrown is None:
        if is_throwing:
            game_state.dice_thrown = sorted([random.randint(1, 7) for _ in range(4)])
        else:
            game_state.player_finishes_move(player_id)
            return True
    
    else:
        first_pair_sum = game_state.dice_thrown[0] + game_state.dice_thrown[index_of_pair_of_first_dice]
        second_pair_sum = sum(game_state.dice_thrown) - first_pair_sum

        current_columns_climbed = game_state.current_climbed_columns()

        
        if len(current_columns_climbed) == 3:
            if len(current_columns_climbed & set(first_pair_sum, second_pair_sum)) == 0:
                game_state.player_finishes_move_with_no_moves_possible()
                return True
            else:
                for sum in [first_pair_sum, second_pair_sum]:
                    if sum in current_columns_climbed:
                        game_state.climb_column(sum)

        elif len(current_columns_climbed) == 2 and len(current_columns_climbed & set(first_pair_sum, second_pair_sum)) == 0:
            if choose_the_first_pair_if_necessary == 1:
                game_state.climb_column(first_pair_sum)
            else:
                game_state.climb_column(second_pair_sum)
        
        else:
            for sum in [first_pair_sum, second_pair_sum]:
                game_state.climb_column(sum)

        game_state.dice_thrown == None

    return False


def simulate_game_and_return_winning_player(player1_strategy, player2_strategy):
    game = GameState()
    current_player = 1
    winning_player = None

    for i in range(MAX_EP_LEN):
        if current_player == 1:
            does_player_ends = simulate_move_and_check_if_player_ends_move(game, player1_strategy)
        else:
            does_player_ends = simulate_move_and_check_if_player_ends_move(game, player2_strategy)
        
        if game.did_finish():
            winning_player = current_player
        
        if does_player_ends: # Swap player
            current_player = 3 - current_player


    return winning_player
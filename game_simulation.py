from random import randint


def simulate_game(player1_choose_to_throw_strategy, player1_choose_to_pair_strategy, player2_choose_to_throw_strategy, player2_choose_to_pair_stategy):
    columns_taken = []
    player1_won_columns = 0
    player2_won_columns = 0
    player1_column_position = 11 * [0]
    player2_column_position = 11 * [0]
    while(true):
        if max(player1_won_columns, player2_won_columns) >= 3:
            return player1_won_columns >= 3
        while(true):
            wants_to_throw = player1_choose_to_

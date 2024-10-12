from random import randint


def simulate_game(player1_choose_to_throw_strategy, player1_choose_to_pair_strategy, player2_choose_to_throw_strategy, player2_choose_to_pair_stategy):
    columns_taken = []
    player1_won_columns = 0
    player2_won_columns = 0
    player1_column_position = 11 * [0]
    player2_column_position = 11 * [0]
    position_with_current_columns_climbed = 11 * [0]
    while(true):
        if max(player1_won_columns, player2_won_columns) >= 3:
            return player1_won_columns >= 3

        while(true):
            if player1_choose_to_throw_strategy(player1_column_position, player2_column_position, position_with_current_columns_climbed) == False:
                break
            throws = [random.randint(1, 7) for i in range(4)]
            throw_pairs = {}
            throw_pairs.add((throws[0] + throws[1], throws[2] + throws[3]))
            throw_pairs.add((throws[0] + throws[2], throws[1] + throws[3]))
            throw_pairs.add((throws[0] + throws[3], throws[2] + throws[1]))

            a, b = player1_choose_to_pair_strategy(player1_column_position, player2_column_position, position_with_current_columns_climbed, throw_pairs) 

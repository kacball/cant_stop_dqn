from random import randint


def simulate_game(player1_choose_to_throw_strategy, player1_choose_to_pair_strategy, player2_choose_to_throw_strategy, player2_choose_to_pair_stategy):
    def current_columns_climbed():
        columns = {}
        for i in len(position_with_current_columns_climbed):
            if position_with_current_columns_climbed[i] > 0:
                columns.add(i)
        return columns

    columns_taken = {}
    player1_won_columns = 0
    player2_won_columns = 0
    player1_column_position = 11 * [0]
    player2_column_position = 11 * [0]
    position_with_current_columns_climbed = 11 * [0]

    while(true):
        if max(player1_won_columns, player2_won_columns) >= 3:
            return player1_won_columns >= 3

        position_with_current_columns_climbed
        while(true):
            if player1_choose_to_throw_strategy(player1_column_position, player2_column_position, position_with_current_columns_climbed) == False:
                for i in len(position_with_current_columns_climbed):
                    if position_with_current_columns_climbed[i] > 0:
                        player1_column_position[i] = position_with_current_columns_climbed[i]
                        if player1_column_position[i] == 12 - abs(i - 7):
                            player1_won_columns += 1
                            columns_taken.add(i)
                break

            throws = [random.randint(1, 7) for i in range(4)]
            throw_pairs = {}
            throw_pairs.add((throws[0] + throws[1], throws[2] + throws[3]))
            throw_pairs.add((throws[0] + throws[2], throws[1] + throws[3]))
            throw_pairs.add((throws[0] + throws[3], throws[2] + throws[1]))
            current_columns_climbed = current_columns_climbed()
            possible_columns = {}
            for a, b in throw_pairs:
                possible_columns.add(a).add(b)

            if len(current_columns_climbed) < 3 and size(possible_columns - columns_taken) or any(element in (possible_columns - columns_taken) for element in current_columns_climbed):
                pair_of_first_dice = player1_choose_to_pair_strategy(player1_column_position, player2_column_position, position_with_current_columns_climbed, throw_pairs) 
                position_with_current_columns_climbed[throws[0] + throws[pair_of_first_dice]] += 1
                if pair_of_first_dice == 1:
                    position_with_current_columns_climbed[throws[2] + throws[3]] += 1
                elif pair_of_first_dice == 2:
                    position_with_current_columns_climbed[throws[1] + throws[3]] += 1
                else:
                    position_with_current_columns_climbed[throws[1] + throws[2]] += 1

            else:
                # Player can't move up
                position_with_current_columns_climbed = 11 * [0]

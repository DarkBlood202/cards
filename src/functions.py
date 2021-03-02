def get_adjacent_cards(slots, card):
    card_index = slots.index(card)
    adj_list = []
    for index, element in enumerate(slots):
        if index == 0:
            adj_list.append((None, slots[index + 1]))
        elif index == len(slots) - 1:
            adj_list.append((slots[index - 1], None))
        else:
            adj_list.append((slots[index - 1], slots[index + 1]))
    return adj_list[card_index]


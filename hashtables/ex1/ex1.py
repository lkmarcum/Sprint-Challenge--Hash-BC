#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        search_index = hash_table_retrieve(ht, limit - weights[i])
        if search_index is not None:
            if i > search_index:
                return [i, search_index]
            return [search_index, i]

    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

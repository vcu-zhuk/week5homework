"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    largest_value = max(incoming_list)
    return largest_value



def find_least_number(incoming_list):
    smallest_value = min(incoming_list)
    return smallest_value



def add_list_numbers(incoming_list):
    if incoming_list is None:
        return 0
    total_value = sum(incoming_list)
    return total_value



def longest_value_key(incoming_dict):
    if incoming_dict is not None:
        if len(incoming_dict) == 0:
            return None
        final_key = max(incoming_dict, key=lambda k: len(incoming_dict[k]))
        return final_key
    return None

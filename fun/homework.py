"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    return max(incoming_list)
    


def find_least_number(incoming_list):
     return min(incoming_list)
  


def add_list_numbers(incoming_list):
    if incoming_list is None:
        return 0
    return sum(incoming_list)
   


def longest_value_key(incoming_dict):
    if incoming_dict is None:
        return None
    highest_length_key = max(incoming_dict, key=lambda k: len(incoming_dict[k]))
    return highest_length_key

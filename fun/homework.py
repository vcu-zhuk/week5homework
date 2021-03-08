"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    largest_value = max(incoming_list)
    return largest_value
    


def find_least_number(incoming_list):
     smallest_value = min(incoming_list)
     return smallest_value
  


def add_list_numbers(incoming_list):
    total_value = sum(incoming_list)
    if incoming_list is not None:
        return total_value
    else:
        return 0
   


def longest_value_key(incoming_dict):
    highest_length_key = max(incoming_dict, key=lambda k=len(incoming_dict[k]))
    if len(incoming_dict) == 0:
        return None
    else:
        return highest_length_key
    

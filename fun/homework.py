"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    largest_value = max(incoming_list)
    return largest_value



def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    smallest_value = min(incoming_list)
    return smallest_value



def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list is None:
        return 0
    total_value = sum(incoming_list)
    return total_value



def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if incoming_dict is None:
        return None
    highest_length_key = max(len(x) for x in incoming_dict)
    return highest_length_key

#!/usr/bin/python
import re

# Filter to check a string against a list for matches
def fuzzy_bidirectional_search(check_list, check_string):
    # Check for any string matches on the list item, or vice versa
    for list_item in check_list:
        if re.search(check_string,list_item):
            return True
        if re.search(list_item,check_string):
            return True
    return False

class FilterModule(object):
    '''
    custom jinja2 filter
    '''
    def filters(self):
        return {
            'fuzzy_bidirectional_search': fuzzy_bidirectional_search,
        }

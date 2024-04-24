def return_list(path, banned_elements=[]):
    returned_list= []
    with open(path) as file:
        for line in file:
            element = line.strip()
            if element not in banned_elements:
                returned_list.append(element)
    return returned_list


import os

def dir_lister(path, banned_elements=[]):
    listing = []
    for element in os.listdir(path):
        if element in banned_elements:
            continue
        else:
            listing.append(element)
    return listing



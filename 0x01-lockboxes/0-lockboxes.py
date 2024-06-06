#!/usr/bin/python3
"""
Module 0-lockboxes
Contains function canUnlockAll that determines if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): A list where each element is a list of keys for
    other boxes

    Returns:
    bool: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked = set()
    keys = set()

    unlocked.add(0)
    keys.update(boxes[0])

    queue = [0]

    while queue:
        box_index = queue.pop(0)

        for key in boxes[box_index]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                queue.append(key)
                keys.update(boxes[key])

    return len(unlocked) == n

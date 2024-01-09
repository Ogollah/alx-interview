#!/usr/bin/python3
"""
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    opened_boxes = set([0])

    # Helper function to perform DFS

    def dfs(box):
        for key in boxes[box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                dfs(key)

    # Start DFS from the first box
    dfs(0)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)

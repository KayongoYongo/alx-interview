#!/usr/bin/pyhon3
"""Lockboxes question"""


def canUnlockAll(boxes):
    """Lockbox question"""

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

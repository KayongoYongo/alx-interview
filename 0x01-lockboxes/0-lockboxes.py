#!/usr/bin/pyhon3
"""Lockbox question"""


def canUnlockAll(boxes):
    """Lockbox question"""
    n = len(boxes)  # Number of boxes
    visited = [False] * n  # Track visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Stack to store boxes to visit

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

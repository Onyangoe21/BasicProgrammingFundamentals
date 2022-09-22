# Purpose: This is a basic implementation of trees and graphs for practice
# Author: Edwin
# Date: September 2022

# Why might trees be useful? Things like binary search trees make work a lot easier so I like trees

class Trees_P:
    def __init__(self) -> None:
        # generate tree with two branches and a parent: We could work without remembering parent
        self.left = None
        self.right = None
        self.parent = None
    
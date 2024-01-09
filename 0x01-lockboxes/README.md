# 0x01-lockboxes

## A method that determines if all the boxes can be opened.

```
Using the depth-first search (DFS) algorithm to traverse through the boxes and determine if all of them can be opened.

open_boxes set keeps track of the boxes that have been opened. 

If, after the DFS traversal, the size of open_boxes is equal to the total number of boxes, then all boxes can be opened Hence return True, else return false.
```

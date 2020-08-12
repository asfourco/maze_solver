# TODO

My collection of some ideas for improvements or fixes that need addressing.

## Issues

1. [Issue] - Write unit tests for `solver.vertex`, `solver.pattern`, and find neighbours in `solver.main.Maze`
1. [Issue] - `Maze.find_entry_points()` fails to find all entry/exit points. For example, in line `AAABAAAAB` would represent and entry and exit on the same side of the maze. The routine will not pickup the second entry. The same when the entry and exit are at the same row on opposite sides of the maze.
1. [Issue] - `Maze.find_path()` returns a path of entry and exit vertex without a valid path in between
1. [Issue] - `Maze.find_path()` should swap the entry/exit points if it didn't find a path the first time around b/c the path is in "reverse"

## Enhancements

1. [Enhancement] - Consume maps with multiple entry points and exit points and report the shortest path between each pair of entry and exit point

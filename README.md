# Maze Solver

## Description

Python maze solver using Dikstra's algorithm to find the shortest and viable path through a maze. Where the maze is defined by a matrix of letters or characters, where one character is a wall, the other the start and end of the maze, and the rest are possible paths. The solver then searches for the shortest viable path based on a desired path pattern and generates a file representing the path through the maze.

For example, given the following maze:

```shell
A B A A A A A A A A A A
A C A D D E A C C C D A
A C C D A E A D A D A A
A A A A A E D D A D E A
A C C D D D A A A A E A
A C A A A A A D D D E A
A D D D E E A C A A A A
A A A E A E A C C D D A
A D E E A D A A A A A A
A A D A A D A C D D A A
A D D D A D C C A D E B
A A A A A A A A A A A A
```

Find a path using the following pattern `CCC-DDD-EEE-DDD`.

## Requirements

1. Python 3.8 or greater
1. Pipenv

## Install

1. Clone this repo: `git clone git@github.com:asfourco/maze_solver.git` or unpack the tarball/archive in a project directory
2. Navigate to the project directory `cd /path/to/maze_solver`
3. Initiate a python virtual environment: `pipenv shell`
4. Install dependencies: `pipenv install`

## Usage

## Contributing

Development tools we use are:

* `flake8` - code linting
* `bandit` - vulnerability scanner
* `black` - code formatter
* `mypy` - data typing library
* `pre-commit` - pre commit task runner, runs the other three tools prior to committing code to catch any issues *a priori*

To install `pre-commit` run the following in at the root of the project directory: `pre-commit install`. You can then use this tool independently of committing your changes: `pre-commit run -a` (runs all tools) or a specific tool: `pre-commit run flake8`.

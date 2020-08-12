# Maze Solver

## Description

Python maze solver using Dikstra's algorithm to find a viable path through a maze. Where the maze is defined by a matrix of letters or characters, where one character represents a wall, the other the entry/exit points of the maze, and the rest are possible paths. The solver then searches for the shortest viable path based on a desired path pattern and generates a file representing the path through the maze.

For example, given the following maze:

```shell
ABAAAAAAAAAA
ACADDEACCCDA
ACCDAEADADAA
AAAAAEDDADEA
ACCDDDAAAAEA
ACAAAAADDDEA
ADDDEEACAAAA
AAAEAEACCDDA
ADEEADAAAAAA
AADAADACDDAA
ADDDADCCADEB
AAAAAAAAAAAA
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

Basic usage is:

```console
# Basic command will print output to stdout
$ python solve.py path/to/input_file

# To write the output as well
$ python solve.py path/to/input_file --output path/to/output_file

# Help on usage
$ python solve.py --help
```

### Input file format

The following is the input format of the maze:

1. The first line is the character representing the Entry and Exit of the maze.
1. The second line is the character representing the Wall within the maze
1. The third line is the character path pattern the solver should use
1. The rest of the lines represent the maze itself

For example, to represent the above maze, the input file `input.txt` would be:

```txt
B
A
CCCDDDEEEDDD
ABAAAAAAAAAA
ACADDEACCCDA
ACCDAEADADAA
AAAAAEDDADEA
ACCDDDAAAAEA
ACAAAAADDDEA
ADDDEEACAAAA
AAAEAEACCDDA
ADEEADAAAAAA
AADAADACDDAA
ADDDADCCADEB
AAAAAAAAAAAA
```

### Input Requirements

There a number of constraints on the structure of the maze:

1. The maze cannot have the entry/exit points on the same row, i.e., neither on the same edge (e.g., `AAABAABAAA`)  or on opposites lateral sides of the maze (e.g., `BAAAAAAB`)
1. There is only one pair of entry/exit points to the maze
1. The start of the path pattern should begin at the top of the maze.

### Example usage

The above maze is saved as `input_examples/input_1.txt`. Running the solver will give you the following result:

```console
$ python solve.py input_examples/input_1.txt

# output =>
Finding path in maze shape of (rows, cols):(12, 12), using path pattern: 'CCCDDDEEEDDD'
...
Path Found of length: 32
_B__________
_C_DDE______
_CCD_E______
_____E______
_CCDDD______
_C__________
_DDDEE______
_____E______
_____D______
_____D_CDD__
_____DCC_DEB
____________
```

If the solver did not find a path it will print out `No Path Found!`

## Contributing

Development tools we use are:

* `flake8` - code linting
* `bandit` - vulnerability scanner
* `black` - code formatter
* `mypy` - data typing library
* `pre-commit` - pre commit task runner, runs the other three tools prior to committing code to catch any issues *a priori*

To install `pre-commit` run the following in at the root of the project directory: `pre-commit install`. You can then use this tool independently of committing your changes: `pre-commit run -a` (runs all tools) or a specific tool: `pre-commit run flake8`.

## Testing

There are example input files in the subfolder `input_examples`:

1. `input_1.txt` is the above mentioned maze
1. `input_2.txt` is a smaller maze to test path patterns
1. `input_3.txt` is to test a maze with no solution; should output `No path found`

#!/usr/bin/env python

import click
from solver import Maze
from solver.pattern import Pattern


def read_input(path: str) -> list:
    with open(path, "r") as file:
        data = file.read()
    return data.split("\n")


def write_output(data: list, path: str) -> None:
    with open(path, "w") as file:
        for line in data:
            file.write(f"{''.join(line)}\n")


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
@click.option(
    "-o", "--output", "output_path", type=click.STRING, help="Path to output file"
)
def main(file_name, output_path: str = None) -> None:
    lines = read_input(file_name)
    entry_char = lines[0]
    wall_char = lines[1]
    pattern = Pattern(lines[2])
    map_data = lines[3:]
    maze = Maze(
        entry_char=entry_char, wall_char=wall_char, data=map_data, pattern=pattern
    )

    try:
        source, destination = maze.find_entry_points()
    except ValueError:
        print("Maze has no entry/exit points")
        return

    print(
        f"Finding path in maze shape of (rows, cols):{maze.shape}, using path pattern: '{pattern}'\n..."
    )
    success, msg = maze.find_path(source=source, destination=destination)
    print(msg)

    if success:
        map_data = maze.generate_output()

        for line in map_data:
            print(f"{''.join(line)}")

        if output_path:
            write_output(data=map_data, path=output_path)
            print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()

class Vertex:
    def __init__(self, row: int, col: int, data: str) -> None:
        self.row = row
        self.col = col
        self.d = float("inf")  # distance from source
        self.processed = False
        self.data = data
        self.parent: Vertex = None

    def __str__(self):
        return f"{self.data} @{self.row},{self.col}"

    def __repr__(self):
        return str(self.__dict__)

    def items(self):
        return self.__dict__.items()

class Pattern:
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
        self.index = 0
        self.len = len(pattern)

    def __str__(self) -> str:
        return self.pattern

    def __repr__(self):
        return self.pattern

    def __iter__(self):
        for char in self.pattern:
            yield char

    @property
    def expected_step(self) -> str:
        return self.pattern[self.index]

    def next_step(self) -> None:
        if self.index + 1 >= self.len:
            self.index = 0
        else:
            self.index += 1

    def previous_step(self) -> None:
        if self.index - 1 >= 0:
            self.index -= 1
        else:
            self.index = self.len - 1

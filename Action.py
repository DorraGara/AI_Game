from State import State

class Action:
    def __init__(self, state, index, partition, remainder) -> None:
        self.state = state
        self.index = index
        self.partition = partition
        self.remainder = remainder

    def to_string(self):
        return(f"devide {self.state.array[self.index]} into {self.partition}, {self.remainder}" )

    def verify(self):
        if (len(self.state.array) <= self.index):
            return False
        if (self.partition == 0):
            return False
        if (self.remainder == 0):
            return False
        if (self.partition == self.remainder):
            return False
        if (self.partition + self.remainder != self.state.array[self.index]):
            return False
        return True

    def execute(self):
        array = self.state.array[:]
        array[self.index] = self.partition
        array.append(self.remainder)
        return State(array, self.state.depth + 1)
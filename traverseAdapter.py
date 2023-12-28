from gpParser import GpParser


class TraverseAdapter(GpParser):
    def __init__(self, data, start_index):
        data = data[start_index:]
        super().__init__(data)
        self.start_index = start_index

    def shallow_traverse(self):
        super().traverse()
        return self.start_index, self.start_index + self.iterator + 1
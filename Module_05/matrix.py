class Matrix:
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        elif isinstance(data, list) and all(isinstance(row, list) for row in data) and all(len(row) == len(data[0]) for row in data):
            self.data = data
            self.shape = (len(data), len(data[0]) if data else 0)
        elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(dim, int) for dim in data):
            self.data = [[0] * data[1] for _ in range(data[0])]
            self.shape = data
        else:
            raise TypeError("Data must be a list of lists or a tuple of two integers")
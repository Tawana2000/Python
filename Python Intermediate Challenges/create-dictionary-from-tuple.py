# Write a function that uses a loop to take 3 key-value tuples and create a dictionary using these keys and values

def make_dict(*tuples):

    return dict(tuples)

tuple1 = ("name", "John")
tuple2 = ("age", 25)
tuple3 = ("City", "New York")
print(make_dict(tuple1, tuple2, tuple3))
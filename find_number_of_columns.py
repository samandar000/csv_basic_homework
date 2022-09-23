def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data = data.split('\n')
    l= []
    for i in data:
        a = i.split(',')
        l.append(a)
    return len(l[0])
data = open('data.csv').read()

print(find_number_of_columns(data))
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data = data.split('\n')
    l= []
    for i in data:
        a = i.split(',')
        l.append(a[0])
       
    return (l)
data = open('data.csv').read()

print(get_first_column(data))

# Read the csv file
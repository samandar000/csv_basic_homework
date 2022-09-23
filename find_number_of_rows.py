def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    data = data.split('\n')
    l= []
    for i in data:
        a = i.split(',')
        l.append(a)
       
    return len(data)-1
data = open('data.csv').read()

print(find_number_of_rows(data))


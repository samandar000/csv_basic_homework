def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    list1 = data.split(',')
    list1 = data.split('\n')
    return (list1[0])

data = open('data.csv').read()
#data = data.split('\n')
# data = data.split(',')


print(get_first_column((data)))
    
# Read the csv file
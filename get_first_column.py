def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    column_name = data.split(',')
    column_name = data.split('\n')
    return list((column_name[0]).split(','))

data = open('data.csv').read()
#data = data.split('\n')
# data = data.split(',')


print(get_first_column((data)))
    
# Read the csv file
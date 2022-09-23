#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data = data.split('\n')
    column_name = [data]
    data = data.split(',')
    return column_name

data = open('data.csv').read()
data = data.split('\n')
print((data[0]))
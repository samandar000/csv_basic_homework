#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
   
    column_name = data.split('\n')
    column_name = data.split(',')
    
    return column_name[0:4]

data = open('data.csv').read()
print(get_column_names(data))
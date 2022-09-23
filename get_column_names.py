#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
      
    
    column_name = data.split(',')
    column_name = data.split('\n')
    return list((column_name[0]).split(','))

data = open('data.csv').read()
#data = data.split('\n')
# data = data.split(',')


print(get_column_names((data)))
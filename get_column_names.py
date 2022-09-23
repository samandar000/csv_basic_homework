#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
   
    column_name = [data]
    
    return column_name
l = []
data = open('data.csv').read()
data = data.split('\n')
l.append(data[0])
print((l))
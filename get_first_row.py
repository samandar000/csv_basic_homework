def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data = data.split('\n')
   l = []
   for i in data:
        a = i.split(',')
        l.append(a[0])   
   return l

data = open('data.csv').read()

print(get_first_row(data))

# Read the csv file
def display_distribution(data):
... values, counts = np.unique(data, return_counts=True)
... for value, count in zip(values, counts):
... print(f'Number of rating {int(value)}: {count}')
display_distribution(data)
import pandas as pd


# Example data
def example():
    pos_off = ['p', 'p', 'p', 'p', 'p', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    id = ['position1', 'position2', 'position3', 'position4', 'position5',
          'employee1', 'employee2', 'employee3', 'employee4', 'employee5',
          'employee6', 'employee7', 'employee8', 'employee9', 'employee10',
          'employee11', 'employee12', 'employee13', 'employee14', 'employee15',
          'employee16', 'employee17', 'employee18', 'employee19', 'employee20']
    pref_1 = [2, 2, 2, 2, 12, 5, 4, 5, 1, 1, 2, 5, 4, 2, 2, 4, 2, 5, 4, 4, 4, 1, 2, 3, 4]
    pref_2 = [19, 12, 14, 7, 3, 1, 1, 2, 3, 5, 1, 2, 1, 3, 4, 1, 1, 3, 2, 1, 3, 2, 3, 1, 5]
    pref_3 = [5, 1, 11, 18, 19, 2, 3, 3, 2, 2, 4, 3, 5, 1, 3, 2, 3, 1, 1, 5, 5, 3, 1, 4, 2]
    data = {'position_or_employee': pos_off, 'id': id, 'pref_1': pref_1,
            'pref_2': pref_2, 'pref_3': pref_3}

    df = pd.DataFrame(data)

    return df


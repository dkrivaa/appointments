import pandas as pd


# Example data
def example():
    pos_off = ['p', 'p', 'p', 'p', 'p', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    id = ['position1', 'position2', 'position3', 'position4', 'position5',
          'officer1', 'officer2', 'officer3', 'officer4', 'officer5',
          'officer6', 'officer7', 'officer8', 'officer9', 'officer10',
          'officer11', 'officer12', 'officer13', 'officer14', 'officer15',
          'officer16', 'officer17', 'officer18', 'officer19', 'officer20']
    pref_1 = [2, 2, 2, 2, 12, 5, 4, 5, 1, 1, 2, 5, 4, 2, 2, 4, 2, 5, 4, 4, 4, 1, 2, 3, 4]
    pref_2 = [19, 12, 14, 7, 3, 1, 1, 2, 3, 5, 1, 2, 1, 3, 4, 1, 1, 3, 2, 1, 3, 2, 3, 1, 5]
    pref_3 = [5, 1, 11, 18, 19, 2, 3, 3, 2, 2, 4, 3, 5, 1, 3, 2, 3, 1, 1, 5, 5, 3, 1, 4, 2]
    data = {'position_or_officer': pos_off, 'id': id, 'pref_1': pref_1,
            'pref_2': pref_2, 'pref_3': pref_3}

    df = pd.DataFrame(data)

    return df


import pandas as pd


# Example data
def example():
    pos_emp = ['p', 'p', 'p', 'p', 'p', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    id = ['position1', 'position2', 'position3', 'position4', 'position5',
          'candidate1', 'candidate2', 'candidate3', 'candidate4', 'candidate5',
          'candidate6', 'candidate7', 'candidate8', 'candidate9', 'candidate10',
          'candidate11', 'candidate12', 'candidate13', 'candidate14', 'candidate15',
          'candidate16', 'candidate17', 'candidate18', 'candidate19', 'candidate20']
    pref_1 = [2, 2, 2, 2, 12, 5, 4, 5, 1, 1, 2, 5, 4, 2, 2, 4, 2, 5, 4, 4, 4, 1, 2, 3, 4]
    pref_2 = [19, 12, 14, 7, 3, 1, 1, 2, 3, 5, 1, 2, 1, 3, 4, 1, 1, 3, 2, 1, 3, 2, 3, 1, 5]
    pref_3 = [5, 1, 11, 18, 19, 2, 3, 3, 2, 2, 4, 3, 5, 1, 3, 2, 3, 1, 1, 5, 5, 3, 1, 4, 2]
    data = {'position_or_employee': pos_emp, 'id': id, 'pref_1': pref_1,
            'pref_2': pref_2, 'pref_3': pref_3}

    df = pd.DataFrame(data)

    return df


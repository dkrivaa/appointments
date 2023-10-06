import pandas as pd


# Example data
def example():
    types = ['type1', 'type1', 'type1', 'type1', 'type1', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2', 'type2']
    id = ['משרה1', 'משרה2', 'משרה3', 'משרה4', 'משרה5',
          'מועמד1', 'מועמד2', 'מועמד3', 'מועמד4', 'מועמד5',
          'מועמד6', 'מועמד7', 'מועמד8', 'מועמד9', 'מועמד10',
          'מועמד11', 'מועמד12', 'מועמד13', 'מועמד14', 'מועמד15',
          'מועמד16', 'מועמד17', 'מועמד18', 'מועמד19', 'מועמד20']
    pref_1 = [2, 2, 2, 2, 12, 5, 4, 5, 1, 1, 2, 5, 4, 2, 2, 4, 2, 5, 4, 4, 4, 1, 2, 3, 4]
    pref_2 = [19, 12, 14, 7, 3, 1, 1, 2, 3, 5, 1, 2, 1, 3, 4, 1, 1, 3, 2, 1, 3, 2, 3, 1, 5]
    pref_3 = [5, 1, 11, 18, 19, 2, 3, 3, 2, 2, 4, 3, 5, 1, 3, 2, 3, 1, 1, 5, 5, 3, 1, 4, 2]
    data = {'position_or_employee': types, 'id': id, 'pref_1': pref_1,
            'pref_2': pref_2, 'pref_3': pref_3}

    df = pd.DataFrame(data)

    return df


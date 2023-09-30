import random

import streamlit as st
import pandas as pd


def read_data():
    start_container = st.container()
    with start_container:
        st.header('Upload your data file here')
        file = st.file_uploader('Choose CSV file', 'csv')
        if file is not None:
            df = pd.read_csv(file)
            if df not in st.session_state:
                st.session_state.df = df

            st.write('Your file has been uploaded successfully')
            continue_button = st.button('press to continue', type='primary')

            if continue_button:
                organize()


def organize():
    df = st.session_state.df

    # Adding 'o' or 'p' to preference to imply if referring to officer or position
    df['pref_1'] = df.apply(lambda row: 'officer' + str(row['pref_1']) if row['position_or_officer'] == 'p'
                            else 'position' + str(row['pref_1']), axis=1)
    df['pref_2'] = df.apply(lambda row: 'officer' + str(row['pref_2']) if row['position_or_officer'] == 'p'
                            else 'position' + str(row['pref_2']), axis=1)
    df['pref_3'] = df.apply(lambda row: 'officer' + str(row['pref_3']) if row['position_or_officer'] == 'p'
                            else 'position' + str(row['pref_3']), axis=1)

    # making preferences into list and dropping the individual columns
    def make_list(row):
        pref_list = list(row[['pref_1', 'pref_2', 'pref_3']])
        if len(pref_list) == len(set(pref_list)):
            return pref_list
        else:
            st.write('Your file is not intact (identical preference by position/employee).'
                     'Please check and submit file after correction')
            exit()


    df['prefs'] = df.apply(make_list, axis=1)

    df = df.drop(['pref_1', 'pref_2', 'pref_3'], axis=1)

    # breaking dataframe into two parts for positions and officers
    df_position = df.loc[df['position_or_officer'] == 'p']
    position_list = df_position['id'].tolist()
    position_pref_list = df_position['prefs'].tolist()
    position_dict = dict(zip(position_list, position_pref_list))

    df_officer = df.loc[df['position_or_officer'] == 'o']
    officer_list = df_officer['id'].tolist()
    officer_pref_list = df_officer['prefs'].tolist()
    officer_dict = dict(zip(officer_list, officer_pref_list))

    # The stable matching algorithm

    tentative_appoint = []
    free_positions = []
    free_officers = []

    special_list = []

    def init_free_positions():
        for position in position_dict.keys():
            free_positions.append(position)

    def init_free_officers():
        for officer in officer_dict.keys():
            free_officers.append(officer)
    def stable_matching():
        while len(free_positions) > 0:
            for position in free_positions:
                special_list.append(position)
                if special_list.count(position) < 5:
                    begin_matching(position)
                elif 5 <= special_list.count(position) < 10:
                    special_matching(position)
                else:
                    st.write('Quitting due to inability to find solution for all positions')
                    quit()

    def begin_matching(position):
        print(f'Dealing with position {position}')
        for officer in position_dict[position]:

            taken_match = [couple for couple in tentative_appoint if officer in couple]

            if len(taken_match) == 0:
                tentative_appoint.append([position, officer])
                free_positions.remove(position)
                free_officers.remove(officer)
                print(f'{officer} is tentatively appointed to {position}')
                break

            elif len(taken_match) > 0:
                print(f'{officer} is tentatively appointed already')
                try:
                    current_position = officer_dict[officer].index(taken_match[0][0])
                except:
                    current_position = len(df_position) - 1
                try:
                    potential_position = officer_dict[officer].index(position)
                except:
                    potential_position = len(df_position)

                if current_position < potential_position:
                    print('the officer is happy with his present tentative position')

                else:
                    print('the officer is happier with the new position')
                    free_positions.remove(position)
                    free_positions.append(taken_match[0][0])
                    taken_match[0][0] = position
                    break


    def special_matching(position):

        chosen_officer = [chosen for chosen in free_officers if position in officer_dict[chosen]]
        if len(chosen_officer) != 0:
            tentative_appoint.append([position, chosen_officer[0]])
            free_positions.remove(position)
            free_officers.remove(chosen_officer[0])
            print(f'{chosen_officer} is tentatively appointed to {position}')

        else:
            chosen_officer = random.choice(free_officers)
            tentative_appoint.append([position, chosen_officer])
            free_positions.remove(position)

    init_free_positions()
    init_free_officers()
    stable_matching()

    # Showing results
    st.subheader('The optimal appointments:')
    st.write(tentative_appoint[0])
    st.write(type(tentative_appoint[0]))
    for i in range(0, len(df_position)):
        st.write(f'Appoint **{tentative_appoint[i][1]}** to **{tentative_appoint[i][0]}**')



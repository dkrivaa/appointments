import random

import streamlit as st
import pandas as pd

def start():
    st.header('The MATCH-BOX')
    st.write('Making the best match')

    # What to match?
    mission = st.radio('What would you like to match?', (
        'open positions and candidates',
        ), disabled=True)
    if mission == 'open positions and candidates':
        upperhand = 'position'
        lowerhand = 'candidate'

    if mission == 'other':
        upperhand = st.text_input('who/what to match:')
        lowerhand = st.text_input('with whom/what?:')

    if upperhand not in st.session_state:
        st.session_state.upperhand = upperhand
    if lowerhand not in st.session_state:
        st.session_state.lowerhand = lowerhand

    st.markdown('___')
    read_data()


def read_data():
    start_container = st.container()
    with start_container:
        st.subheader('Upload your data file here')
        file = st.file_uploader('Choose CSV file', 'csv')
        if file is not None:
            df = pd.read_csv(file)
            df = df.fillna(int(0))

            if df not in st.session_state:
                st.session_state.df = df

            st.write('Your file has been uploaded successfully')
            continue_button = st.button('press to continue', type='primary')

            if continue_button:
                organize()


def organize():
    df = st.session_state.df

    upperhand = st.session_state.upperhand
    lowerhand = st.session_state.lowerhand

    # Renaming columns
    first_column = f'{upperhand}_or_{lowerhand}'
    df.rename(columns={df.columns[0]: first_column}, inplace=True)
    df.rename(columns={df.columns[1]: 'id'}, inplace=True)

    #################
    st.write(df)

    x = df[first_column]
    df['work_id'] = df.apply(lambda x: f'{upperhand}' + df.index.astype(str) if x == 'p'
                             else f'{lowerhand}' + df.index.astype(str))



    st.write(df)

    #################


    for i in range(2, len(df.columns)):
        df.rename(columns={df.columns[i]: f'pref_{i-1}'}, inplace=True)

    # Adding the matchee's to preferences to imply if referring to position or employee
        column_name = f'pref_{i-1}'
        df[column_name] = df.apply(lambda row: f'{lowerhand}' + str(int(row[column_name])) if row[first_column] == 'p'
                                   else f'{upperhand}' + str(int(row[column_name])), axis=1)

    # making preferences into list and dropping the individual columns
    def make_list(row):
        col_list = []
        for i in range(2, len(df.columns)):
            col_list.append(f'pref_{i-1}')
        pref_list = list(row[col_list])
        pref_list = [x for x in pref_list if x != f'{upperhand}0' and x != f'{lowerhand}0']
        if len(pref_list) == len(set(pref_list)):
            return pref_list
        else:
            st.write('Your file is not intact (identical preference by position/employee).'
                     'Please check and submit corrected file')
            exit()

    df['prefs'] = df.apply(make_list, axis=1)

    # breaking dataframe into two parts for positions and officers
    df_position = df.loc[df[first_column] == 'p']
    position_list = df_position['id'].tolist()
    position_pref_list = df_position['prefs'].tolist()
    position_dict = dict(zip(position_list, position_pref_list))

    df_employee = df.loc[df[first_column] == 'e']
    employee_list = df_employee['id'].tolist()
    employee_pref_list = df_employee['prefs'].tolist()
    employee_dict = dict(zip(employee_list, employee_pref_list))

    # Getting the number of max preferences for upperhand (positions) and lowerhand (employees)
    num_of_prefs_upperhand = len(max(position_pref_list, key=len))
    num_of_prefs_lowerhand = len(max(employee_pref_list, key=len))

    if num_of_prefs_upperhand not in st.session_state:
        st.session_state.num_of_prefs_upperhand = num_of_prefs_upperhand

    if num_of_prefs_lowerhand not in st.session_state:
        st.session_state.num_of_prefs_lowerhand = num_of_prefs_lowerhand

    # Calculating how many employees have matching preferences with positions
    possible = 0
    for employee in employee_list:
        for position in employee_dict[employee]:
            try:
                if employee in position_dict[position]:
                    possible += 1
                    break
            except KeyError:
                pass

    # The stable matching algorithm

    tentative_appoint = []
    free_positions = []
    free_employees = []

    special_list = []

    def init_free_positions():
        for position in position_dict.keys():
            free_positions.append(position)

    def init_free_employees():
        for employee in employee_dict.keys():
            free_employees.append(employee)

    def stable_matching():
        if len(free_positions) > len(free_employees):
            st.write('Not enough employees to fill all positions!')
            quit()

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

        # Function for calculating combined preferences
        def points(position, employee):
            num_of_prefs_upperhand = st.session_state.num_of_prefs_upperhand
            num_of_prefs_lowerhand = st.session_state.num_of_prefs_lowerhand

            if (employee not in position_dict[position]) or (employee == f'{lowerhand}0'):
                position_points = 0
            else:
                position_points = 10 + num_of_prefs_upperhand - position_dict[position].index(employee)

            if (position not in employee_dict[employee]) or (position == f'{upperhand}0'):
                employee_points = 0
            else:
                employee_points = 5.1 + num_of_prefs_lowerhand - employee_dict[employee].index(position)
            points = position_points + employee_points

            return points

        # st.write(f'Dealing with {position}')

        # Sorting position pref list by combined points of prefs
        best_list = []
        for employee in position_dict[position]:
            point = points(position, employee)
            best_list.append((employee, point))
        best_list = sorted(best_list, key=lambda x: x[1], reverse=True)
        temp_list = [x[0] for x in best_list]
        position_dict[position] = temp_list

        # Going through employees to find best match
        for employee in position_dict[position]:

            if employee == 'employee0':
               break

            taken_match = [couple for couple in tentative_appoint if employee in couple]

            if len(taken_match) == 0:
                tentative_appoint.append([position, employee])
                free_positions.remove(position)
                free_employees.remove(employee)
                # st.write(f'{employee} is tentatively appointed to {position}')
                break

            elif len(taken_match) > 0:
                # st.write(f'{employee} is tentatively appointed already')

                current_position_points = points(taken_match[0][0], employee)
                potential_position_points = points(position, employee)

                if current_position_points >= potential_position_points:
                    pass
                    # st.write('the previous tentative position is a better match')

                else:
                    # st.write('the new position is a better match')
                    free_positions.remove(position)
                    free_positions.append(taken_match[0][0])
                    taken_match[0][0] = position
                    break

    def special_matching(position):

        chosen_employee = [chosen for chosen in free_employees if position in employee_dict[chosen]]
        if len(chosen_employee) != 0:
            tentative_appoint.append([position, chosen_employee[0]])
            free_positions.remove(position)
            free_employees.remove(chosen_employee[0])
            # st.write(f'{chosen_employee} is tentatively appointed to {position}')

        else:
            chosen_employee = random.choice(free_employees)
            tentative_appoint.append([position, chosen_employee])
            free_positions.remove(position)

    # The following statements are initializing the matching process
    init_free_positions()
    init_free_employees()
    stable_matching()

    # Showing results
    st.subheader('The optimal appointments:')
    pos_count = 0
    emp_count = 0
    for i in range(0, len(df_position)):
        st.write(f'Appoint **{tentative_appoint[i][1]}** to **{tentative_appoint[i][0]}**')

        # Calculating how many got one of top wishes
        if tentative_appoint[i][1] in position_dict[tentative_appoint[i][0]]:
            pos_count += 1

        if tentative_appoint[i][0] in employee_dict[tentative_appoint[i][1]]:
            emp_count += 1

    # Making csv file of results to download
    pos = [sublist[0] for sublist in tentative_appoint]
    emp = [sublist[1] for sublist in tentative_appoint]
    df_results = pd.DataFrame({'position': pos, 'employee': emp})

    def convert_df(df_any):
        return df_any.to_csv(index=False).encode('utf-8')

    down_result = convert_df(df_results)

    st.download_button('Download results',
                       data=down_result,
                       file_name='results.csv',
                       mime='text/csv',
                       type='primary')

    # Summary data
    st.markdown('___')

    st.subheader('Summary')
    st.write(f'Number of **{upperhand}s** that got one of top wishes: **{pos_count}** '
             f'(out of **{len(tentative_appoint)}** open positions)')
    st.write(f'Number of **{lowerhand}s** that got one of top wishes: **{emp_count}** '
             f'(out of **{possible}** that have corresponding wishes with positions)')

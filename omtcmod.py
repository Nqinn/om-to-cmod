import streamlit as st
#welcome screen
print('Hi, this program will convert your osu!mania scroll speed to etterna scroll speed')

#asking for your data
osu_mania_sp = st.number_input('\nPlease input your osu!mania Scroll Speed: ',
                               min_value=1, max_value=40, step=1)
etterna_recep = st.number_input('\nPlease input your Etterna Receptor Size: ',
                               min_value=1, max_value=10000, step=10)

#calculating and printing the results
CMod = osu_mania_sp * 3200 / etterna_recep
st.text(f'Your Etterna CMod is {CMod}')

# next_calculation = input ('Type Enter to Close the Program: ')

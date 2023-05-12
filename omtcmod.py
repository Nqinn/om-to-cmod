#welcome screen
print('Hi, this program will convert your osu!mania scroll speed to etterna scroll speed')

#asking for your data
osu_mania_sp = int(input('\nPlease input your osu!mania scroll speed: '))
etterna_recep = int(input('\nPlease input your Etterna Receptor Size: '))

#calculating and printing the results
CMod = osu_mania_sp * 3200 / etterna_recep
print('Your Etterna CMod is', CMod)

next_calculation = input ('Press Enter to Close the Program: ')

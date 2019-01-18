import ast


def settingsWrite(temp_zad1, temp_zad2, histereza, time_sleep, run):

    d = {'temp_zad1': temp_zad1,
         'temp_zad2': temp_zad2,
         'histereza': histereza,
         'time_sleep': time_sleep,
         'z_run': run}
    setfile = open('settings.txt', 'w')
    setfile.write(str(d))
    return d


def settingsRead():

    F = open('settings.txt', 'r')
    tab = F.readline()
    tab = ast.literal_eval(tab)
    return tab


seti = 1
set2 = 2
set3 = 3
set4 = 4
set5 = 5

for i in range(10):
    int(seti[i]) += i
    set2 += i
    set3 += i
    set4 += i
    set5 += i

    start = settingsWrite(set1, set2, set3, set4, set5)

    nastawy = settingsRead()
# print(nastawy['temp_zad1'])

    print('{} , {}, {}, {}, {}'.format(nastawy['temp_zad1'],
                                       nastawy['temp_zad2'],
                                       nastawy['histereza'],
                                       nastawy['time_sleep'],
                                       nastawy['z_run']))

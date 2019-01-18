import path


def settingsWrite(temp_zad1,temp_zad2,histereza, time_sleep, run):
    setfile = open(path.setPath, 'w')
    setfile.write('{0}, {1}, {2}, {3}, {4} '.format(temp_zad1,temp_zad2, histereza,time_sleep, run))
    setfile.close()


def settingsRead():

    F = open(path.setPath, 'r')
    line = F.readline()
    parts = line.split(',')
    numbers = [float(P) for P in parts]
    temp_zad1_F = numbers[0]
    temp_zad2_F = numbers[1]
    histereza_F=numbers[2]
    time_sleep_F = numbers[3]
    run = numbers[4]
    return temp_zad1_F, temp_zad2_F, histereza_F ,time_sleep_F, run

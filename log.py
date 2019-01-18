import path
import sys


def logWrite(data, godzina, temperatura,
             temp_zad, pracaPrzekaznika, log_no):
    '''Trzy metody przekierownia strumienia'''
    log_no += 1
    if log_no > 10:
        logfile = open(path.logPath, 'a')
        print(('{0}, {1}, {2:.2f}, {3:.2f}, {4}'
               .format(data, godzina, temperatura, temp_zad, pracaPrzekaznika)),file=logfile)
        logfile.close()
        log_no = 0
    return log_no


'''
    logfile = open(path.logPath, 'a')
    logfile.write('{0}, {1}, {2:.2f}, {3:.2f}, {4}\n'.format(data, godzina, temperatura, temp_zad, pracaPrzekaznika))
    logfile.close()
'''

'''
    temp=sys.stdout
    sys.stdout=open(path.logPath,'a')
    print('{0}, {1}, {2:.2f}, {3:.2f}, {4}'.format(data, godzina, temperatura, temp_zad, pracaPrzekaznika))
    #sys.stdout.close()
    sys.stdout=temp
'''

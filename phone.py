import pandas as pd


Viettel = ['86','96','97','98','32','33','34','35','36','37','38','39']

Vinaphone = ['88','91','94','83','84','85','81','82']

Mobiphone = ['89','90','93','70','79','77','76','78']

Vietnamobile = ['92','56','58']

Gmobile = ['99','59']

Itelecom = ['87']

maVung = ['296','254','209','204','291','222','275','256','274','271','252',
          '290','292','206','236','262','261','215','251','277','269','219',
          '226','239','220','225','293','218','221','258','297','260',
          '213','263','205','214','272','228','238','229','259','210','257','232',
          '235','255','203','233','299','212','276','227','208','237','234','273',
          '294','207','270','211','216','24','28']
#maVungDacBiet = ['24','28']
def thuocMaVung(x):
    i = 0
    for i in range(len(maVung)):
        if (x.startswith(maVung[i])):
            return True
    return False

def checkThuocMaVung(x):
    if (thuocMaVung(x)):
        print('Là số cố định hợp lệ')
    else:
        print('Không hợp lệ')





#if (x.startswith('2') and len(x) == 10) or (x.startswith('02') and len(x) == 11) or (x.startswith('842') and len(x) == 12) or (x.startswith('+842') and len(x) == 13):
        
def soDiDong(x):
    if (mangViettel(x)):
        print('Là số di động Viettel')
    elif (mangVinaphone(x)):
        print('Là số di động Vinaphone')
    elif (mangMobifone(x)):
        print('Là số di động Mobifone')
    elif (mangVietnamobile(x)):
        print('Là số di động Vietnamobile')
    elif (mangGmobile(x)):
        print('Là số di động Gmobile')
    elif (mangItelecom(x)):
        print('Là số di động Itelecom')
    else:
        print('Số không hợp lệ')


def mangViettel(number):
    i = 0
    for i in range(len(Viettel)):
        if (number.startswith(Viettel[i])):
            return True
    return False

def mangVinaphone(number):
    i = 0
    for i in range(len(Vinaphone)):
        if (number.startswith(Vinaphone[i])):
            return True
    return False

def mangMobifone(number):
    i = 0
    for i in range(len(Mobiphone)):
        if (number.startswith(Mobiphone[i])):
            return True
    return False

def mangVietnamobile(number):
    i = 0
    for i in range(len(Vietnamobile)):
        if (number.startswith(Vietnamobile[i])):
            return True
    return False

def mangGmobile(number):
    i = 0
    for i in range(len(Gmobile)):
        if (number.startswith(Gmobile[i])):
            return True
    return False

def mangItelecom(number):
    i = 0
    for i in range(len(Itelecom)):
        if (number.startswith(Itelecom[i])):
            return True
    return False
    
def laSoDiDong(x):
    if (len(x) == 9):
        #print("Sđt 9 chữ số")
        soDiDong(x)
        
    elif (len(x) == 10 and x.startswith('0')):
        #print("Sđt 10 chữ số")
        newPhone = x[1:]
        soDiDong(newPhone)

    elif (len(x) == 11 and x.startswith('84')):
        #print('Sđt 11 chữ số')
        newPhone = x[2:]
        soDiDong(newPhone)
    elif (len(x) == 12 and x.startswith('+84')):
        #print('Sđt 12 chữ số')
        newPhone = x[3:]
        soDiDong(newPhone)
    else:
        print('Invalid')

def checkFull(x):
    if (x.startswith('2') and len(x) == 10):
        checkThuocMaVung(x)
    elif (x.startswith('02') and len(x) == 11):
        newPhone = x[1:]
        checkThuocMaVung(newPhone)
    elif (x.startswith('842') and len(x) == 12):
        newPhone = x[2:]
        print(newPhone)
        checkThuocMaVung(newPhone)
    elif (x.startswith('+842') and len(x) == 13):
        newPhone = x[3:]
        checkThuocMaVung(newPhone)
    else:
        laSoDiDong(x)




phone_number = input("Enter phone number: ")
phone_number = phone_number.replace(" ", "").replace("\t", "").replace("\n", "").replace(".","")
checkFull(phone_number)


'''
test case

0919914261 - vina

0335358317 - viettel
'''




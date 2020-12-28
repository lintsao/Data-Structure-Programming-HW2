# -*- coding: utf-8 -*-
import os
import sys

def ASCII_mapping(password):
    convert = 0
    for text in password:
        convert = 100*convert + ord(text)
    return convert

def hash_function(number):
    hash_value = ((243*int(number[:8])) + int(number[8:])) % 85767489
    return hash_value

if __name__ == "__main__":
    # initial
    password_file = sys.argv[1] # password.txt
    list_pa2_file = sys.argv[2] # list_pa2.txt
    path = './'

    # read password.txt
    read_file = open(password_file, 'r').readlines()

    # compute hash value
    password_list = []
    mapping_list = []
    hash_list = []
    for i in range(len(read_file)-1):
        password = read_file[i].replace('\n', '')
        password_list.append(password)
        mapping_list.append(ASCII_mapping(password))
        hash = []
        for j in range(1000):
            number = str(j).zfill(3) + str(ASCII_mapping(password))
            hash_value = hash_function(number)
            hash.append(hash_value)
        hash_list.append(hash)
    print('finish hash value')

    # write Dictionary.txt
    file = open(os.path.join(path, 'Dictionary.txt'), 'w')
    for i in range(len(password_list)):
        for j in range(len(hash_list[0])):
            file.write(password_list[i] + ' ' + str(j).zfill(3) + ' ' + str(hash_list[i][j]))
            file.write('\n')
    file.close()
    print('finish Dictionary.txt')

    # read Dictionary.txt
    Dictionary = open(os.path.join(path, 'Dictionary.txt'), 'r').readlines() 
    # read list_pa2.txt
    list_pa2 = open(list_pa2_file, 'r').readlines()
    # write results_pa2.txt
    file = open(os.path.join(path, 'results_pa2.txt'), 'w')

    for hash in list_pa2:
        initial = False
        hash = hash.replace('\n', '')
        for i in range(len(Dictionary)): # search
            if hash == Dictionary[i][11:-1]:
                initial = True
                break
        if initial == False:
            file.write(hash + ' ' + '******' + ' ' + '***' + ' ' + str(i+1))
            file.write('\n')
        else:
            file.write(hash + ' ' + Dictionary[i][:6] + ' ' + Dictionary[i][7:10] + ' ' + str(i+1))
            file.write('\n')
    file.close()
    print('finish results_pa2.txt')

    # user search
    input_value = input('Please input a hash value：')
    initial = False
    for i in range(len(Dictionary)):
        if input_value == Dictionary[i][11:-1]:
            print('success! The password is {}, salt value is {}, {} entries have been searched'.format(
                Dictionary[i][:6],  Dictionary[i][7:10], str(i+1)))
            initial = True
            break
    if initial == False:
        print('failure!, {} entries have been searched'.format(str(i+1)))
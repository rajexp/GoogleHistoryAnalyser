#-------------------------------------------------------------------------------
# Name      : Google History Analyser
# Purpose   : Program for analysing the google search history
#
# Author    : Rajan Chauhan
# Created   : 7 /Dec/2015
# Copyright : https://plus.google.com/+rajanchauhandiscover
# Licence   : Creative Commons 1.0 Universal
#-------------------------------------------------------------------------------

import json
import datetime
import re
import os
import codecs
from bs4 import BeautifulSoup
def gen_filename(genfile):
    if genfile==False:
        filename=input('provide filename : ')
        genfile=True
    else:
        filename=input('File exists provide another name')
        genfile=True
    if '.' in filename:
        
    return filename,ext
    
def get_text(elementlist):
    return [re.search(r'([a-zA-Z0-9 -.]*)',element.text).group() for element in elementlist]
def save(flist):
    global lst
    for i in flist["event"]:
        for word in i["query"]["query_text"].split():
            lst[word]=get_frequency(word)+1
def get_frequency(word):
    try:
        return lst[word]
    except :
        return 0     
def get_files():
    file='index.html'
    if file in os.listdir():
        index=open(file)
    else:
        print('No file present')
        raise IOError
    soup=BeautifulSoup(index.read(),'html.parser')
    index.close()
    filelist=soup.find_all('div',{'class':'extracted-file-name'})
    return get_text(filelist)
def get_top(n):
    global lst
    if lst is not None:
        sorted_lst=sorted(lst.items(),key=lambda x: x[1],reverse=True)
        return sorted_lst[:n]
    else:
        pass
"""For printing the list of touples in pretty manner"""    
def prettify(_list):
    len_indent= max(len(i[0]) for i in _list)
    for i in _list:
        indent=(len_indent-len(i[0]))*' '
        print(str(i[0])+indent+"   :   "+str(i[1]))
""" Work on function for generating list """
def main():
    global lst
    lst={} #For storing the word search frequency
    genfile= False # Check for file 
    """Specify path to your download folder which contain index.html file"""
    path=str(input('provide path :'))
    while(not len(path)):
        path=str(input('proivde correct path'))     
    try:
        os.chdir(path)
    except:
        os.chdir(path-'\\')
    filenames= get_files()
    for file in filenames:
        try:
            f=codecs.open('Searches\\'+file,encoding='latin-1')
            try:
                flist=json.load(f)
                save(flist)
            except UnicodeDecodeError :
                print(file)    
        except IOError :
            pass
    cache_result=input('Do you want to save file in one y or n :')
    if cache_result=='y':
        while True:
            filename,ext=gen_filename(genfile)
            if filename+ext in  os.listdir():
                genfile=True
                continue
            else:
                genfile=False
                break
        if ext is '':
            file=open(path+filename+'.txt','w')
        else:
            file=open(path+filename,'w')
        file.write(str(lst))
        file.close()
if __name__=="__main__":
    main()



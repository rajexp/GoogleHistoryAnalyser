======================
GoogleHistoryAnalyser
======================
A program to analyse your google history in Python.


==============
 Requirements
==============

1. Python 3.2 +
2. Zip file exractor like  WinZip

Python Libraries Used
======================
1. BeautifulSoup

  For installing listed Libraries use these commands on terminal

     ``python setup.py install``
How to use:
===========
1. Go to www.google.com/history
2. Follow the steps done in images below :
3. Go to your mail and download the attachments sent by google
4. The attachments will be downloaded in a folder name Searches.
5. Extract that folder</li>
6. Run the file google_history_analysor.py and provide path to the <b>Searches</b> folder which contain index.html file and another Searches folder containing json files.

![alt tag](http://imgur.com/cnsUZVJ.jpg)
![alt tag](http://imgur.com/DhSYgpS.jpg)
![alt tag](http://imgur.com/S5yNFGN.jpg)

Usage:
======
  1. Adding Folder where index.html is located
 
    ``>>> provide path :C:\Users\Rajan\Downloads\Searches``
  2. For getting top 10 results with frequency'
 
    ``>>> get_top(10)``

    ``[('in', 631), ('to', 324), ('of', 262), ('for', 197), ('python', 192), ('how', 180), ('google', 122), ('on', 115), ('and', 112),       ('a', 105)]``
  3. For printing the top list in more readable form
 
    ``>>> prettify(get_top(5))``

    ``in       :   631``
    
    ``to       :   324``
    
    ``of       :   262``
    
    ``for      :   197``
    
    ``python   :   192``
  4. For getting the frequency of word searched 
 
    ``>>> get_frequency('india')``

    ``49``
  5. For saving the list of top searched words in file 
 
    ``>>> save(get_top(100))``

    ``>>>provide filename : googlehistoryfile.doc``
    
    ``File created successfully``
  
  



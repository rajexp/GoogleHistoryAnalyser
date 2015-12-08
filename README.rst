# GoogleHistoryAnalyser<br>
A program to analyse your google history in Python <br>
<b>Requirements</b><br>
<ol>
<li>Python 3.2 +</li>
<li>Zip file exractor like <b>WinZip</b></li>
</ol>
<h3>Python Libraries Used</h3>
<ol>
<li><b>BeautifulSoup</b>></li>
</ol>
For installing listed Libraries use these commands on terminal
<br>
<b>pip install BeautifulSoup</b>
<br>
<h3>How to use:</h3></br>
<ol>
<li>Go to www.google.com/history</li>
<li> Follow the steps done in images below :</li>
<li> Go to your mail and download the attachments sent by google</li>
<li> The attachments will be downloaded in a folder name Searches.</li>
<li>Extract that folder</li>
<li><p>Run the file <b>google_history_analysor.py</b> and provide path to the <b>Searches</b> folder which contain <b>index.html</b> file and another Searches folder containing json files.</p></li>
</ol>
![open http://www.google.com/history](http://imgur.com/cnsUZVJ)<br>
![Click on create archive](http://imgur.com/DhSYgpS)<br>
![The history has been sent on your mail](http://imgur.com/S5yNFGN)<br>
Usage
  Adding Folder where index.html is located
  >>> provide path :C:\Users\Rajan\Downloads\Searches
  For getting top 10 results with frequency
  >>> get_top(10)
  [('in', 631), ('to', 324), ('of', 262), ('for', 197), ('python', 192), ('how', 180), ('google', 122), ('on', 115), ('and', 112),       ('a', 105)]
  For printing the top list in more readable form
  >>> prettify(get_top(5))
  in       :   631
  to       :   324
  of       :   262
  for      :   197
  python   :   192
  For getting the frequency of word searched 
  >>> get_frequency('india')
  49
  For saving the list of top searched words in file 
  >>> save(get_top(100))
  provide filename : googlehistoryfile.doc
  File created successfully
  
  
  



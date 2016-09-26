"""This script takes an unlimited amount of youtube links which it them downloads to a specific directory  """

import os

directory = input("\nDirectory: ")

#Change  and/or create directory if it does not exist.
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)
    os.chdir(directory)

urls = []
counter = 1

#deal with blank so it wont continue downloading
url = input(str(counter) + ". url: ")

if url == "":
    os.exit()

while url != "":
    urls.append(str(url))
    counter += 1 
    
    url = input(str(counter) + ". url: ")

for url in urls:
    os.system("youtube-dl %s"%url)




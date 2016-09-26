"""
This script takes a list of youtube URLS and proceds to download them 
It either takes or creates a directory to place the files in them.

This script is more of an add-on to youtube-dl.

Dependencies: 
youtube-dl 
python-pip 

If your new to programming and are using linux, install python-pip
and then install youtube-dl. 

Contac me: gregborrelly@gmail.com 
"""

import os
print("Hint: Type Directory Name to be created.")

directory = input("\nDirectory: ")

#Change  and/or create directory if it does not exist.
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)
    os.chdir(directory)

counter = 1

print("\nHINT: Press ENTER to begin downloading process.")
url = input(str(counter) + ". url: ")

if url == "":
    print("Error Blank URL")
    os.system("exit")

urls= [] 
while url != "":
    urls.append(str(url))
    counter += 1 
    
    url = input(str(counter) + ". url: \n ")

for url in urls:
    os.system("youtube-dl %s"%url)




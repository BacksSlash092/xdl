#!/usr/bin/env
"""
This script is an extension to youtube-dl, the script can be used to download playlist,videos, and podcasts.

Dependencies: 
youtube-dl 
feedparser
python-pip 

If your new to programming and are using linux, install python-pip, youtube-dl and feedparser. 

Contact me: gregborrelly@gmail.com 
"""
import os
import sys
import pickle
import feedparser

def identify_directory():
    """Finds or Creates a directory and changes into it  -_- """
    print("Hint: Type Directory Name to be created.")
    directory = input("\nDirectory: ")
    
    #Makes sure directory exists, if it does not, it proceds to create it. 
    if os.path.exists(directory):
        os.chdir(directory)

    else:
        os.mkdir(directory)
        os.chdir(directory)

def download_playlist():
    """ Utilizes youtube-dl to download an entire playlist."""
    url = input("Url: ")
    os.system("youtube-dl -cit %s"%url)

def get_podcasts(url):
    """Takes in a Feed URL, sorts through the last 10 entries on a given podcast
       and downloads them if the podcasts have not been downloaded already.""" 
    feed = feedparser.parse(url)
    podcasts = {}
    podcast_titles = {} 
    current_path = str(os.getcwd())
    
    for podcast in range(0,10):
        podcasts[podcast] = feed['entries'][podcast]['link']
        
        #This creates the Path to test, wherever files have alredy been downloaded.  
        podcast_titles[podcast] = current_path + feed['entries'][podcast]['title']
    
    for podcast in range(0,10):
        if os.path.isfile(podcast_titles[podcast])
            pass 
        else:
            os.system("youtube-dl %s"%podcasts[podcast])
def add_to_database(podcast_list):
    """Add's podcast to database. """ 
    with open('podcastdatabase.pickle', 'wb') as handle: 
        pickle.dump(podcast,handle)
   
    
#Podcast Database
podcast_list = ['http://feeds.feedburner.com/ALLJupiterVideos']​            

# If no parameters are given. The program quits. 
flag = len(sys.argv)
if flag == 1: 
    print("Please Specify Options.")
    os.system("exit")
    
# Flag -p {playlist url} is used to download an entire youtube playlist.             
if sys.argv[1] == '-p':
    idendify_directory()
    download_playlist()
    
# Flag -up is used to synch podcasts. 
elif sys.argv[1] == '-up':
    idendify_directory()
    for podcast in podcast_list:
        get_podcasts(podcast)
        
# Flag -l is used to provide a list of urls for download. 
elif sys.argv[1] == '-l':
    idendify_directory()
    counter = 1 
    print("\nHINT: Leave Area blank and Press ENTER  to begin downloading process.\n")
    url = input(str(counter) + ". url: ")

    if url == "":
        print("\nError Blank URL")
        os.system("exit")

        urls= [] 

        while url != "":
            urls.append(str(url))
            counter += 1 
            url = input(str(counter) + ". url: ")

        for url in urls:
            os.system("youtube-dl %s"%url)

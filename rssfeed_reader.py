import feedparser
import os

def dem():
	print("-----------------------------------------------------------")

while True:
        flink = input("Please enter the RSS field URL. \n")
        f = open("feedrssURL.txt", "a")
        f.write("this is appending \n")
        f.write(flink)
        f.close

        url = feedparser.parse(flink)


        title = url.feed.title
        description = url.feed.description
        link = url.feed.link

        print(title)
        dem()
        print(description)
        dem()
        print(link + "\n\n")



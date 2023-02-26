import requests
import re
import sys

if __name__ == "__main__":

    file = open("./" + sys.argv[1], 'r')

    print("Opening", file.name)

    file = file.readlines()

    links = []

    url = "https://www.instapaper.com/api/add"

    params = {
            'username': '<YOUR USERNAME/EMAIL>',
            'password': '<YOUR PASSWORD>',
            }

    def parseBookmarks(bookmarks):

        for bookmark in bookmarks:

            query = re.search("(?P<url>http[^\s]+)", bookmark)

            if query is not None:
                query = query.group("url")[:-1]
                links.append(query)

    def sendRequest(links):
        for link in links:
            params['url'] = link
            r = requests.post(url, params)
            print("Response: ", r.status_code)
            if r.status_code == 403:
                print("Failed. Request forbidden, please ensure credentials are correct.")
            elif r.status_code == 201:
                print("Successfully added: ", link)

    parseBookmarks(file)
    sendRequest(links)
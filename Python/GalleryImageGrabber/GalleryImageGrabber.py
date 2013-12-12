import datetime
import getopt
import os
import random
import re
import sys
import time
import urllib.request

class GalleryImageGrabber:
    url = ""
    page = 0
    bound = 3
    numOfChap = 1
    currentChap = 0
    processedChap = 0
    directory = ""
    verbose = False
    websiteMode = 0
    waitTime = 10
    rootSite = ""

    def __init__(self, url, directory):
        self.url = url
        self.directory = directory
        self._setRootSite()
        
    def test(self):
        print("success")

    def process(self):
        self._makeDir(self.directory)
        statement = ("Started on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self._write(self._constructDir([self.directory, "progress"]), statement, "w")
        if (not(self.currentChap)):
            self.currentChap = self._setCurrentChap(self._getHtml(self.url))
        while (self.processedChap < self.numOfChap):
            html = self._getHtml(self.url)
            matched = self._matchPattern(html)
            self._wait()
            if (matched):
                self.url = self._getNextPage(matched)
                self._getImage(self._getImageUrl(matched))
            else:
                matched = self._matchPatternLastPage(html)
                if (matched):
                    self.url = self._getNextPage(matched)
                    self._getImage(self._getImageUrl(matched))
                    self.processedChap += 1
                    self.currentChap += 1
                    self.page = 0
                else:
                    statement = ("Finished with " + str(self.processed) + " chapters obtained, finished at chapter " + str(self.currentChap) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    self._write(self._constructDir([self.directory, "progress"]), statement, "a")
                    self.processedChap = self.numOfChap

    def _constructDir(self, listToJoin):
        return os.path.join(*listToJoin)
        
    def _documentImageError(self):
        statement = ("Issue with chapter " + str(self.currentChap) + ", page " + str(self.page) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self._write(self._constructDir([self.directory, "progress"]), statement, "a")

    def _documentWriteError(self, content, mode):
        statement = (("Issue saving chapter " + str(self.currentChap) + ", page " + str(self.page)), ("Issue writing the following: \"" + content + "\""))[mode != "wb"]
        statement += " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._write(self._constructDir([self.directory, "progress"]), statement, "a")

    def _documentProgress(self):
        if (self.verbose):
            statement = ("Got chapter " + str(self.currentChap) + ", page " + str(self.page) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self._write(self._constructDir([self.directory, "progress"]), statement, "a")

    def _getHtml(self, url):
        return urllib.request.urlopen(url).read().decode('utf-8')

    def _getImage(self, imageUrl):
        directory = self._constructDir([self.directory, self.currentChap])
        if (self.page == 0):
            self._makeDir(directory)
        try:
            self.page += 1
            index = imageUrl.rfind('.')
            fileName = str(self.page).zfill(3) + imageUrl[index:]
            directory = self._constructDir([self.directory, self.currentChap, fileName])
            image = urllib.request.urlopen(imageUrl).read()
            self._write(directory, image, "wb")
            self._documentProgress()
        except:
            self._documentImageError()

    def _getImageUrl(self, matched):
        return matched.group(7)[1:-1]

    def _getNextPage(self, matched):
        self._setRootSite()
        url = matched.group(4)[1:-1]
        if (url[0] != "/" or re.compile('^((http(s?)://)|(www\.))', re.IGNORECASE).match(url)):
            return url
        elif (url[0] == "/"):
            return self.rootSite + url
        else:
            return self.rootSite + '/' + url

    def _makeDir(self, directory):
        os.system("mkdir " + directory)

    def _matchPattern(self, htmlPage):
        pat = re.compile('.*<div.*id\s*=\s*((\"imgholder\")|(\'imgholder\')).*<a.*href\s*=\s*((\"/\S*chapter-' + str(self.currentChap) + '\S*\")|(\'/\S*chapter-' + str(self.currentChap) + '\S*\')).*<img.*\s*src=\s*((\"http(s)*://\S*/' + str(self.currentChap) + '/\S*\")|(\'http(s)*://\S*/' + str(self.currentChap) + '/\S*\'))', re.IGNORECASE | re.DOTALL)
        return pat.match(htmlPage)

    def _matchPatternLastPage(self, htmlPage):
        pat = re.compile('.*<div.*id\s*=\s*((\"imgholder\")|(\'imgholder\')).*<a.*href\s*=\s*((\"/\S*chapter-' + str(self.currentChap + 1) + '\S*\")|(\'/\S*chapter-' + str(self.currentChap + 1) + '\S*\')).*<img.*\s*src=\s*((\"http(s)*://\S*/' + str(self.currentChap) + '/\S*\")|(\'http(s)*://\S*/' + str(self.currentChap) + '/\S*\'))', re.IGNORECASE | re.DOTALL)
        return pat.match(htmlPage)

    def _setCurrentChap(self, htmlPage):
        pat = re.compile('.*<title>.*read.*\s+(\d+)\s+.*online.*</title>', re.IGNORECASE | re.DOTALL)
        return pat.match(htmlPage).group(1)
        
    def _setRootSite(self):
        pat = re.compile('((http(s?)://)?[^/]*)/?.*', re.IGNORECASE)
        self.rootSite = pat.match(self.url).group(1)
        
    def _wait(self):
        if (self.waitTime > 0):
            deviant = random.randrange(self.bound * -100, self.bound * 100)
            length = self.waitTime + deviant
            if (length < 0):
                length *= -1
            time.sleep(length)

    def _write(self, directory, content, mode):
        f = {}
        try:
            f = open(directory, mode)
            f.write(content)
        except:
            self._documentWriteError(content, mode)
        finally:
            if (f):
                f.close()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vt:c:w:")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)
    if (len(args) != 2):
        print("A link and directory are needed for arguments")
        sys.exit(1)
    temp = ImageGrabber(args[0], args[1])
    for (o, a) in opts:
        if (o == '-t' and a.isdigit()):
            temp.waitTime = int(a) * 1.0
        elif (o == '-v'):
            temp.verbose = True
        elif (o == '-w' and a.isdigit()):
            temp.websiteMode = int(a)
        elif (o == '-c' and a.isdigit()):
            temp.numOfChap = int(a)
    temp.process()

if (__name__ == "__main__"):
    main()

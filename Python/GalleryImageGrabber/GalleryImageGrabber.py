import datetime
import getopt
import os
import random
import re
import sys
import time
import urllib.request
import pdb

class GalleryImageGrabber:
    url = ""
    page = 0
    bound = 3
    numOfChap = 1
    currentChap = 0
    processedChap = 0
    path = ""
    verboseLevel = 0
    websiteMode = 0
    waitTime = 10.0
    rootSite = ""
    overwrite = False

    def __init__(self, url, path):
        self.url = url
        self.path = path
        self._setRootSite()
        
    def test(self):
        print("success")

    def process(self):
        self._makeDir(self.path)
        statement = ("Started on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        if (self.verboseLevel > 1):
            print(statement)
        self._write(self._constructPath([self.path, "progress"]), statement, "w")
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
                    self.currentChap = self._getNextChap(matched.group(0))
                    self.page = 0
                else:
                    matched = self._attemptGetLastPage(html)
                    if (matched):
                        self._getImage(self._getLastImageUrl(matched))
                    statement = ("Finished with " + str(self.processedChap) + " chapters obtained, finished at chapter " + str(self.currentChap) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    if (self.verboseLevel > 1):
                        print(statement)
                    self._write(self._constructPath([self.path, "progress"]), statement, "a")
                    self.processedChap = self.numOfChap

    def _attemptGetLastPage(self, htmlPage):
        pat = re.compile('<div.*id\s*=\s*((\"imgholder\")|(\'imgholder\')).*<img.*src\s*=.*((\"http(s)*://\S*/' + str(self.currentChap) + '/\S*\")|(\'http(s)*://\S*/' + str(self.currentChap) + '/\S*\'))+', re.IGNORECASE | re.DOTALL)
        return pat.search(htmlPage)

    def _constructPath(self, listToJoin):
        return os.path.join(*listToJoin)
        
    def _documentImageError(self):
        statement = ("Issue with chapter " + str(self.currentChap) + ", page " + str(self.page) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        if (self.verboseLevel > 1):
            print(statement)
        self._write(self._constructPath([self.path, "progress"]), statement, "a")

    def _documentWriteError(self, content, mode):
        statement = (("Issue saving chapter " + str(self.currentChap) + ", page " + str(self.page)), ("Issue writing the following: \"" + content + "\""))[mode != "wb"]
        statement += " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(statement)

    def _documentProgress(self):
        if (self.verboseLevel):
            statement = ("Got chapter " + str(self.currentChap) + ", page " + str(self.page) + " on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self._write(self._constructPath([self.path, "progress"]), statement, "a")
            if (self.verboseLevel > 2):
                print(statement)

    def _getHtml(self, url):
        return urllib.request.urlopen(url).read().decode('utf-8')

    def _getImage(self, imageUrl):
        path = self._constructPath([self.path, str(self.currentChap)])
        if (self.page == 0):
            self._makeDir(path)
        try:
            self.page += 1
            index = imageUrl.rfind('.')
            fileName = str(self.page).zfill(3) + imageUrl[index:]
            path = self._constructPath([self.path, str(self.currentChap), fileName])
            image = urllib.request.urlopen(imageUrl).read()
            self._write(path, image, "wb")
            self._documentProgress()
        except:
            self._documentImageError()

    def _getImageUrl(self, matched):
        return matched.group(14)[1:-1]
        
    def _getLastImageUrl(self, matched):
        return matched.group(4)[1:-1]

    def _getNextPage(self, matched):
        self._setRootSite()
        url = matched.group(8)[1:-1]
        if (url[0] != "/" or re.compile('^((http(s?)://)|(www\.))', re.IGNORECASE).match(url)):
            return url
        elif (url[0] == "/"):
            return self.rootSite + url
        else:
            return self.rootSite + '/' + url
    
    def _getNextChap(self, url):
        pat = re.compile("chapter-(.*).html", re.IGNORECASE)
        return pat.search(y).group(1)

    def _makeDir(self, path):
        if (not(os.path.exists(path))):
            os.system("mkdir " + path)

    def _matchPattern(self, htmlPage):
        re.compile("document\s*\[\s*((\'chapterno\')|(\"chapterno\"))\s*\]\s*=\s*(.*?)\s*\;.*?document\s*\[\s*((\'nl\')|(\"nl\"))\s*\]\s*=\s*((\'.*?\')|(\".*?\"))*?\s*\;.*?document\s*\[\s*((\'pu\')|(\"pu\"))\s*\]\s*=\s*((\'.*?\')|(\".*?\"))*?\s*\;.*</select>.*?(\d+)\s*</div>", re.IGNORECASE | re.DOTALL).search(y)
        return pat.search(htmlPage)

    def _matchPatternLastPage(self, htmlPage):
        pat = re.compile('<div.*id\s*=\s*((\"imgholder\")|(\'imgholder\')).*<a.*href\s*=\s*((\"/\S*chapter-\w*\.\S*\")|(\'/\S*chapter-\w*\.\S*\')).*<img.*\s*src=\s*((\"http(s)*://\S*/' + str(self.currentChap) + '/\S*\")|(\'http(s)*://\S*/' + str(self.currentChap) + '/\S*\'))', re.IGNORECASE | re.DOTALL)
        return pat.search(htmlPage)

    def _setCurrentChap(self, htmlPage):
        pat = re.compile('.*<title>.*read.*\s+(\d+)\s+.*online.*</title>', re.IGNORECASE | re.DOTALL)
        return int(pat.match(htmlPage).group(1))
        
    def _setRootSite(self):
        pat = re.compile('((http(s?)://)?[^/]*)/?.*', re.IGNORECASE)
        self.rootSite = pat.match(self.url).group(1)
        
    def _wait(self):
        if (self.waitTime > 0):
            deviant = random.randrange(self.bound * -100.0, self.bound * 100.0)
            length = self.waitTime + (deviant / 100.0)
            if (length < 0):
                length *= -1
            time.sleep(length)

    def _write(self, path, content, mode):
        f = {}
        if (not(os.path.exists(path)) or mode != "wb" or self.overwrite):
            try:
                f = open(path, mode)
                f.write(content)
            except:
                self._documentWriteError(content, mode)
                sys.exit(1)
            finally:
                if (f):
                    f.close()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "v:t:c:w:b:o")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)
    if (len(args) != 2):
        print("A link and path are needed for arguments")
        sys.exit(1)
    temp = GalleryImageGrabber(args[0], args[1])
    for (o, a) in opts:
        if (o == '-t' and a.isdigit()):
            temp.waitTime = int(a) * 1.0
        elif (o == '-v'):
            temp.verboseLevel = 1
            if (a and a.isdigit() and int(a) > 0):
                temp.verboseLevel = int(a)
        elif (o == '-w' and a.isdigit()):
            temp.websiteMode = int(a)
        elif (o == '-c' and a.isdigit()):
            temp.numOfChap = int(a)
        elif (o == '-b' and a.isdigit()):
            temp.bound = int(a)
        elif (o == '-o'):
            temp.overwrite = True
    temp.process()

if (__name__ == "__main__"):
    main()

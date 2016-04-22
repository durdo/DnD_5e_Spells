#! /usr/bin/python3.5

import lxml.html as lh
import urllib
from urllib.request import urlopen
from urllib.parse import urljoin

class magClass:
    classSpellList = []
    def __init__(self, className, classUrl):
        self.name = className
        self.url = classUrl
        print("Creating class: %s" % self.name)
    def getName(self):
        return self.name
    def getUrl(self):
        return self.url

class spell:
    def __init__(self, spellName):
        self.name = spellName
        print("Creating spell: %s" % self.name)

class main:
    pageUrl = ""
    tree = None
    classesList = []
    spellLevels = []
    fullSpellList = []
    @staticmethod
    def __init__(page):
        main.pageUrl = page
    @staticmethod
    def getPage():
        return main.pageUrl
    @staticmethod
    def getTree():
        main.tree = lh.parse(urllib.request.urlopen(main.pageUrl)) if main.tree == None else main.tree
        return main.tree
    @staticmethod
    def getClassesList():
        return main.classesList
    @staticmethod
    def getFullSpellList():
        return main.fullSpellList
    @staticmethod
    def getsSpellRanking():
        return main.spellLevels
    @staticmethod
    def listClasses():
        main.getTree()
        cl = main.tree.xpath('//div[@id="menu" and @class="trigger"]/a/text()')
        ur = [urljoin(main.pageUrl,"".join(main.tree.xpath('//a[text()="%s"]/@href' % c))) for c in cl]
        for count, curClass in enumerate(cl):
            main.classesList.append(magClass(curClass, ur[count]))
    @staticmethod
    def listSpellsLevel():
        main.getTree()
        cl = main.tree.xpath('//div[@class="home"]/h2/text()')
        for count, curSpellLevel in enumerate(cl):
            main.spellLevels.append(curSpellLevel)


main("http://ephe.github.io/grimoire")
main.listClasses()
main.listSpellsLevel()
[print("\nClass '%s' can be found at:\n%s" % (c.getName(), c.getUrl())) for c in main.getClassesList()]
print("\nSpells are divided in the following levels:")
[print("%s" % sL) for sL in main.getsSpellRanking()]

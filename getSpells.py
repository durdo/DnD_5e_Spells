#! /usr/bin/python3.5

import lxml.html as lh
from urllib.request import urlopen
from urllib.parse import urljoin

class playerClass:
    def __init__(self, className, classUrl):
        self.name = className
        self.url = classUrl
        classSpellList = []
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
        main.tree = lh.parse(urlopen(main.pageUrl)) if main.tree == None else main.tree
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
    def createClassList():
        main.getTree()
        cl = main.tree.xpath('//div[@id="menu" and @class="trigger"]/a/text()')
        ur = [urljoin(main.pageUrl,"".join(main.tree.xpath('//a[text()="%s"]/@href' % c))) for c in cl]
        for count, curClass in enumerate(cl):
            main.classesList.append(playerClass(curClass, ur[count]))
    @staticmethod
    def createLevelList():
        main.getTree()
        cl = main.tree.xpath('//div[@class="home"]/h2/text()')
        for curSpellLevel in cl:
            main.spellLevels.append(curSpellLevel)
    @staticmethod
    def createSpellListByLevel():
        main.getTree()
        for l in main.spellLevels:
            print("\n* -", l)
            cl = main.tree.xpath('//div[@class="home"]/a[@id="%s"]/../ul/li/a/text()' % l)
            print(cl)

main("http://ephe.github.io/grimoire")
main.createClassList()
main.createLevelList()
main.createSpellListByLevel()
#[print("\nClass '%s' can be found at:\n%s" % (c.getName(), c.getUrl())) for c in main.getClassesList()]
#print("\nSpells are divided in the following levels:")
#[print("%s" % sL) for sL in main.getsSpellRanking()]

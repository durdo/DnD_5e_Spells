#!/usr/bin/python3.5

import lxml.html as lh
from urllib.request import urlopen
from urllib.parse import urljoin

class playerClass:
    def __init__(self, className, classUrl):
        self.name = className
        self.url = classUrl
        self.classSpellList = []
        self.tree = None
        self.createClassSpellList()

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def getClassSpellList(self):
        return self.classSpellList

    def createClassSpellList(self):
        self.getTree()
        self.classSpellList = self.tree.xpath('//div[@class="wrapper"]/ul/li/a/text()')
        print(self.classSpellList)

    def getTree(self):
        self.tree = lh.parse(urlopen(self.url)) if self.tree == None else self.tree
        return self.tree


class spell:
    def __init__(self, spellName, spellUrl):
        self.name = spellName
        self.url = spellUrl
        self.level = ""
        self.tree = None

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def getLevel(self):
        return self.level

    def setLevel(self, spellLevel):
        self.level = spellLevel

    def getTree(self):
        self.tree = lh.parse(urlopen(self.url)) if self.tree == None else self.tree
        return self.tree

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
        main.spellLevels = main.tree.xpath('//div[@class="home"]/h2/text()')

    @staticmethod
    def createSpellList():
        main.getTree()
        cl = main.tree.xpath('//div[@class="home"]/ul/li/a/text()')
        ur = [urljoin(main.pageUrl,"".join(main.tree.xpath('//a[text()="%s"]/@href' % c))) for c in cl]
        for count, curClass in enumerate(cl):
            main.fullSpellList.append(spell(curClass, ur[count]))

    @staticmethod
    def sortFullSpellList():
        main.fullSpellList.sort(key=lambda spell: spell.name)

main("http://ephe.github.io/grimoire")
main.createClassList()
main.createLevelList()
main.createSpellList()
main.sortFullSpellList()

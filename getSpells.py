import lxml.html as lh
from urllib.request import urlopen
from urllib.parse import urljoin

class playerClass:
    def __init__(self, className, classUrl):
        self.name = className
        self.url = classUrl
        classSpellList = []
    def getName(self):
        return str(self.name)
    def getUrl(self):
        return str(self.url)

class spell:
    def __init__(self, spellName, spellUrl):
        self.name = spellName
        self.url = spellUrl
    def getName(self):
        return str(self.name)
    def getUrl(self):
        return str(self.url)

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

main("http://ephe.github.io/grimoire")
main.createClassList()
main.createLevelList()
main.createSpellList()
print(main.spellLevels)
print("Class list:")
print("\n".join(["'" + element.getName() + "' at --> " + element.getUrl() for element in main.classesList]))
print("\n\nSpell list:")
print("\n".join(["'" + element.getName() + "' at --> " + element.getUrl() for element in main.fullSpellList]))
#[print("\nClass '%s' can be found at:\n%s" % (c.getName(), c.getUrl())) for c in main.getClassesList()]
#print("\nSpells are divided in the following levels:")

from django.shortcuts import render
from django.http import HttpResponse
from assignment1.catalogue import *

# Create your views here.
def homepage(request):
    return render(request,'homePageblock.html')
def index(request):
    return render(request,'indexBlock.html')
def catalogue(request):
    return render(request,'catalogueBlock.html')
def datamodel(request):
    return render(request,'datamodelBlock.html')

def indexListView(request):
    catalogueItemList = []
    catalogueItemList = createItems()
    titleList = []
    idList = []
    for item in catalogueItemList:
        titleList.append(item.title)
        idList.append(item.id)
    itemInfo = {'idTitleList':zip(idList,titleList,)
                }
    return render(request,'indexBlock.html',itemInfo)

def createItems():
    catalogueItemList = []
    pathOfExile = catalogueItem(1,'Path of Exile','Grinding Gear Games',
                                'ARPG','23rd of October 2013',
                                """You are an Exile, struggling to survive on the dark continent of Wraeclast, as you fight \n
                                to earn power that will allow you to exact your revenge against those who wronged you.""")
    catalogueItemList.append(pathOfExile)
    rainbow6Siege = catalogueItem(2,'Tom Clancys Rainbow Six Siege','Ubisoft',
                                  'FPS','2nd of December 2015',
                                  """ Master the art of destruction
                                  and gadgetry in Tom Clancy’s Rainbow Six Siege.
                                  Face intense close quarters combat, high lethality, tactical decision making,
                                  team play and explosive action within every moment.
                                  Experience a new era of fierce firefights and expert strategy born from the rich legacy of past
                                  Tom Clancy's Rainbow Six games.""")
    catalogueItemList.append(rainbow6Siege)
    dota2 = catalogueItem(3,'Dota 2','Valve','MOBA','9th of July 2013',
                          """ Dota 2 is a multiplayer online battle arena (MOBA)
                          video game in which two teams of five players compete to collectively destroy a large structure
                          defended by the opposing team known as the "Ancient", whilst defending their own.""")
    catalogueItemList.append(dota2)
    warhammerVermintide2 = catalogueItem(4,'Warhammer Vermintide 2','Fatshark',
                                         'FPS','9th of March 2018',
                                         """Warhammer: Vermintide 2 is the sequel to the critically acclaimed Vermintide.
                                         The time has arrived to revisit the fierce first-person co-op slaughter-fest featuring
                                         visceral and ground breaking melee action,
                                         set in the apocalyptic End Times of the war-ravaged Warhammer Fantasy Battles world .  """)
    catalogueItemList.append(warhammerVermintide2)
    return catalogueItemList

def loadCatalogueItem(request):
    catalogueItemList = []
    catalogueItemList = createItems()
    currentUrl =  request.get_full_path()
    currentUrl = int(currentUrl[-1])
    itemDetails = {}
    for item in catalogueItemList:
        if item.id == currentUrl:
            itemDetails = {
            'itemTitle': item.title,
            'itemDeveloper':item.developer,
            'itemGenre':item.genre,
            'itemRelDate':item.relDate,
            'ItemSetting':item.setting,
            'urll':currentUrl
            }
        else:
            pass
    return render(request,'catalogueBlock.html',itemDetails)

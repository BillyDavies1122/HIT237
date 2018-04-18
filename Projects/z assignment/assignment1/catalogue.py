class catalogueItem:
    def __init__(self,id,title,developer,genre,relDate,setting):
        self.id = id
        self.title = title
        self.developer = developer
        self.genre = genre
        self.relDate = relDate
        self.setting = setting

currentUrl = 'http://127.0.0.1:8000/index/1'
currentUrl = int(currentUrl[-1])



print (currentUrl)

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class PropertiesItem(Item):
    title = Field()
    author = Field()
    description = Field()
    coverImagePath = Field()


    # Primary Fields
    # title = Field()
    # price = Field()
    # description = Field()
    # address = Field()
    # image_urls = Field()

    # # Calculated Fields
    # images = Field()
    # location = Field()
    
    # # Housekeeping Fields
    # url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    # date = Field()


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

__author__ = 'kjb9rk'

from amazon.api import AmazonAPI
from amazonproduct import API

browse_node = "2858778011"
new_browse_node = ""
access_key = 'AKIAJLJSWHEAZKT7CI3A'
secret_key = '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'
associate_tag = 'AKIAJLJSWHEAZKT7CI3A'

api = API(cfg='.amazon-product-api', locale='us')
amazon = AmazonAPI(access_key, secret_key, associate_tag)


def get_amazon_movies():
    movie_db = []
    try:
        products = amazon.search(SearchIndex='Video', BrowseNode=browse_node)
        for product in products:
            if product.price_and_currency[0]:
                movie_db += [AmazonMovie(str(product.title).replace('[HD]', '').strip(), ' ')]
    except Exception, error:
        return str(error)
    return movie_db


# api = API(cfg='.amazon-product-api', locale='us')
# items = api.item_search('Video', BrowseNode=browse_node)
#
# for item in items:
#     print str(item.ItemAttributes.Title).replace("[HD]", "").strip()

class AmazonMovie:

    def __init__(self, title, synopsis):
        self.title = title
        self.synopsis = synopsis

    def __repr__(self):
        report = "<Movie: %s>" % self.title
        return report

    def get_keywords(self):
        return str(self.synopsis).split(" ")


if __name__ == '__main__':
    for mov in get_amazon_movies():
        print mov

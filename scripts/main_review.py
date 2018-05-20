from crawling2 import *
from matchine_best import *



html = (searchDDG("flipkart.com","LG 6.5 kg Semi Automatic Top Load Washing Machine Grey  (P7550R3FA)"))
data = getLinkContent(html,"flipkart.com")
print(data)
data_text=[i[0] for i in data]
data = dict(data)
obj  = Similarity(data_text)
print(data[obj.most_similar(["LG 6.5 kg Semi Automatic Top Load Washing Machine Grey  (P7550R3FA)"])])


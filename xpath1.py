from parsel.selector import Selector  # pip install parsel
import requests

response = requests.get("http://db.auto.sina.com.cn/price/s3136.html")
response = Selector(response.text)

## 删除不需要的节点
response.xpath('//li[@class="hd clearfix"]').remove()

price_list = []

# 获取报价列表
datas = response.xpath('//li[contains(@class, "bd clearfix")]')
for doc in datas:
    title = doc.xpath(".//a/@title").extract_first()
    price = doc.xpath('string(.//div[@class="border lowprice"])').extract_first()
    print(title, "*" * 10, price)

    # 获取车辆价格
    price = doc.xpath(
        'substring-before(.//div[@class="border lowprice"], "万")'
    ).extract_first()
    price_list.append(price)

print("最高车价为：", max(price_list))

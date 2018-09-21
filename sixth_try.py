#一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格

def discount( price ):
    if( price >= 50 and price <= 100 ):
        print("10%的折扣")
        return price * 0.9
    if( price > 100 ):
        print("20%的折扣")
        return price * 0.8
print(discount(100))
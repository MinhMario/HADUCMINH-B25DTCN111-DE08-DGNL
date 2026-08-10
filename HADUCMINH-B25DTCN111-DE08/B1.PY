raw_dishes = [ 
{"name": "Phở Bò Special", "price": 120000, "status": "available"}, 
{"name": " bún chả ", "price": 45000, "status": "available"}, 
{"name": "Lẩu Thái Hải Sản", "price": 250000, "status": "out_of_stock"}, 
{"name": "Gỏi Cuốn Tôm Thịt", "price": 60000, "status": "discontinued"}, 
{"name": "Cơm Tấm Sườn Nướng", "price": 150000, "status": "available"} 
]
def clean_and_validate_dishes(dishes):
    for d in dishes:
        d['name']=d['name'].strip().title()
        if len(d['name'])<2:
            dishes.remove(d)

clean_and_validate_dishes(raw_dishes)
print(raw_dishes)

def search_dishes(dishes, max_price, status=None):
    result=[]
    for d in dishes:
        if d['price']<=max_price and status==None:
                    result.append(d)
        if d['price']<=max_price and d['status']==status:
            result.append(d)
    print(result)

search_dishes(raw_dishes,200000,'available')


                
            
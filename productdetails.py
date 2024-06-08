print("companies : 'AMZ','FLP,'SNP','MYN','AZO'" )
company =input("enter the company:").lower()
print("products : phone,coputer,tv,earphone,tablet,charger,mouse,keypad,bluetooth,pendrive,remote,speaker,hedset,laptop,pc")
products =input("enter the product name:").lower()
if company == 'amz':
    if products == 'laptop':
        data =[{ "produc":"laptop-1","price":2236,"rating":4.7,"discount":63,"availability":"yes"},
               { "produc":"laptop-13","price":1244,"rating":4.5,"discount":45,"availability":"out-of-stock"}
               ,{ "produc":"laptop-3","price":9192,"rating":4.44,"discount":98,"availability":"out-of-stock"},
               {"produc": "laptop-11", "price": 2652, "rating": 4.12, "discount": 70, "availability": "yes"},
               {"produc": "laptop-4", "price": 1258, "rating": 3.8, "discount": 33, "availability": "out-of-stock"},
               {"produc": "laptop-14", "price": 8686, "rating": 3.22, "discount": 24, "availability": "yes"}]
        print(data)
    elif products =='phone':
        data={"produc": "laptop", "price": 1258, "rating": 3.8, "discount": 33, "availability": "out-of-stock"}
        #like that we need write for all produts and companies but present i don't have the time and data.
        print(data)
    else:
        print("will update it in future!!")
else:
    print(" Comming Soon!")





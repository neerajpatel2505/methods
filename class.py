class Mobile:
    fp = "YES"
    @classmethod
    def show_mobile(cls,m,p):
        cls.model = m
        cls.price = p
        print("Mobile Model:",cls.model, " & ","Mobile Price:",cls.price)
        print("Fingure print functionality:",cls.fp)
        
obj = Mobile()
Mobile.show_mobile("Real-me 8",'17000')
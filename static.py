class Mobile:
    fp = "YES"
    @staticmethod
    def show_mobile(m,p):
        model = m
        price = p
        print("Mobile Model:",model, " & ","Mobile Price:",price)
        print("Fingure print functionality:",Mobile.fp)
        print("Hello")
        
obj = Mobile()
Mobile.show_mobile("Real-me 8-pro",'17000')
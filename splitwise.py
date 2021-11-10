# cook your dish here
class splitwise:
    def identify(self,id_name):
        print("enter your id number")
        n=int(input())
        print(n)
        if n in id_name.keys():
            print('Welcome',id_name[n])
            
        else:
            print('Sorry wrong id number')
            
        

n=int(input())  #Number of users
id_name=dict()  #dictionary that stores name and id
for i in range(n):
    id_name[i]=input()
d=splitwise()
d.identify(id_name)
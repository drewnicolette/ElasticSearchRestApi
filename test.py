import requests
import json
import copy
'''
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/user_tweets/Double J Plays", {})
#response = requests.get(BASE + "/count/verified_tweets1", {})
#response = requests.get(BASE + "/all_verified_users/verified_tweets1", {})
print(response.json())
'''














a = "string"
b = a

a += "aaaa"
#print(a)
#print(b)


a = 0
b = a

a += 1

#print(a)
#print(b)



a = [1,2,3]
b = a

a.append(4)
#print(a)
#print(b)


a = [[1,2,3,4],[1,2,3,4]]
b = a

a[0][0] = 100
#print(a)
#print(b)




a = [1,2,3,4,5]
b = [1,2]
c = b.copy()
for i in b:
    if i in a:
        c.remove(i)
print(c)








a = [1,2,3,4]
b = a.copy() #Shallow Copy

a.append(5)
#print(a)
#print(b)

#------------

a = [[1,2,3,4],[1,2,3,4]]
b = a.copy() #Shallow Copy

a[0][3] = 0
#print(a)
#print(b)

#-------

a = [[1,2,3,4],[1,2,3,4]]
b = copy.deepcopy(a)

a[0][0] = 0
#print(a)
#print(b)

# Python program to write JSON 
# to a file 


import json 
import matplotlib.pyplot as plt

plt.style.use('ggplot')
x = ['Wizard', 'Hero', 'Villain', 'Peasant']

# Data to be written 
dictionary ={ 
	"Wizard" : 0, 
	"Hero" : 0, 
	"Villain" : 0, 
	"Peasant" : 0
} 
## use this to reset the dictionary
#with open("sample.json", "w") as outfile: 
	#json.dump(dictionary, outfile) 



with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
json_object["Wizard"]+=1

with open("sample.json", "w") as outfile: 
	json.dump(json_object, outfile) 

print(json_object) 
#print(type(json_object)) 
x_pos = [i for i, _ in enumerate(x)]

energy = [json_object['Wizard'],json_object['Hero'],json_object['Villain'],json_object['Peasant']]

plt.bar(x_pos, energy, color='green')
plt.xlabel("people")
plt.ylabel("numbers")
plt.title("people trying to get treasure")

plt.xticks(x_pos, x)

plt.show()
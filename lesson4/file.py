#ex1
def num_word(file):
    with open(file ,'r') as my_file:
        content= my_file.readlines()
        my_file.seek(0)
        sum = 0
        for line in content:
            sum+= len(line.split())

        return sum


print(num_word('text.txt'))
#ex2

import csv
def writeInformation(info):
    with open('people.csv ','w')as write_file:
        writer=csv.writer(write_file)
        for i in info:
           writer.writerow(i)

arr =[
    ["sara","chohen",12,"mesilat yofef"],["chana","Levi",30,"mesilat yesharim"]]
writeInformation(arr)

#ex3
import  json
def write_and_read_json(dict):
    with open('data.json  ','w')as json_file:
         json.dump(dict,json_file)
    with open('data.json','r')as read_file:
        info=json.load(read_file)
    print(info)


dict={
    "name":"tovi",
    "age":12
}

write_and_read_json(dict)
'''
Created on 31 Jan 2020

@author: rathos
'''
from locust import Locust, TaskSet, task, HttpLocust, TaskSequence
from locust.core import seq_task
from random import randint
import string
import random
 

class MyTaskSet(TaskSequence):    
    @seq_task(1)
    @task
    def homepage(self):
        response = self.client.get("/")    

              
    @seq_task(2) 
    @task
    def reserve(self): 
        response = self.client.post("/reserve.php",{"fromPort": "Paris", "toPort": "Buenos Aires"})
        resp1 = str(response.text)
        #print("resp1: "+resp1)

    @seq_task(3) 
    @task
    def purchase(self):  
        response = self.client.post("/purchase.php",{"flight": "43", "price": "472.56", "airline": "Virgin America", "fromPort": "Paris", "toPort": "Buenos Aires"})
        resp2 = str(response.text)
        #print("resp2: "+resp2)

    @seq_task(4) 
    @task
    def confirm(self): 
        response = self.client.post("/confirmation.php",{"_token": "", "inputName": "Traveler", "address": "123", "city": "Blore", "state": "Ktaka", "zipCode": "1234", "cardType": "visa", "creditCardNumber": "1234567812345678", "creditCardMonth": "11", "creditCardYear": "2017", "nameOnCard": "Travel"})
        resp3 = str(response.text)
        splt1 = resp3.split("<td>Id</td>")
        splt2 = (splt1[1]).split("<td>")
        splt3 = (splt2[1]).split("</")
        print("ID: "+splt3[0])
        
     
class MyLocust(HttpLocust):
    task_set = MyTaskSet
    host = "http://www.blazedemo.com"
    
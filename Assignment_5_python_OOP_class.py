#!/usr/bin/env python
# coding: utf-8

# In[40]:


class Account:
    def __init__(self, cust_num, u_name):
        self.cust_num = cust_num
        self.u_name = u_name

        
class Order(Account):
    def __init__(self, cust_num, u_name, midterm, password, meal_cost, balance):
        super().__init__(cust_num, u_name)
        self.__midterm = midterm
        self.__password = password
        self.meal_cost = meal_cost
        self.balance = balance
    
    def UpdateBalance(self):
        if self.meal_cost >= 15:
            self.balance = self.balance + 10
            number_of_extra_15 = (self.meal_cost-15)//15
            self.balance = self.balance + number_of_extra_15*5
        
        if self.u_name == 'UCLA':
            self.balance = self.balance + 5
        elif self.u_name == 'USC':
            self.balance = self.balance + 3
        
        if self.__midterm > 80:
            self.balance = self.balance + 3
        
        if self.__password == 0:
            self.balance = 0
            
    def getBalance(self):
        return self.balance
        
    def getMidterm(self):
        return self.__midterm
        
    def getPassword(self):
        return self.__password
        
    def updateMidterm(self, midterm):
        self.__midterm = midterm
        


'''
Created on 9 Dec 2019

@author: rathos
'''
from locust import Locust, TaskSet, task, HttpLocust
from locust.core import seq_task, TaskSequence
from random import randint
import string
import random
# from waitress.task import Task
 
 

class MyTaskSet(TaskSequence):
    
    EmpIDs = []
    
    def NameEmp(self):
        m = ""
        for a in range(2):
            z = random.choice(string.ascii_letters)
            m = m + z
        n = "SunilLocust" + m + str(randint(10, 99))
        return n 
    
    def DateDOB(self):
        mnth = str(randint(1, 12))
        DOB = str(randint(1970, 2000)) + "-" + mnth.zfill(2) + "-" + str(randint(1, 28))
        return DOB
    
    def DateDOJ(self):
        mnth = str(randint(1, 12))
        DOJ = str(randint(2015, 2019)) + "-" + mnth.zfill(2) + "-" + str(randint(1, 28))
        return DOJ
    
    def SaveResponse(self,filename,response):
        f=open("C:\Sunil\Python Tutorial\Python_Demo1\Locust\\"+filename, 'w')
        f.write(response)
        f.close()
         
        
      
    @seq_task(1)
    @task
    def login(self):
        res="Create New Employee"
        response = self.client.post("/web/guest/welcome", {'p_p_id':'CustomLogin_WAR_CustomLoginportlet', 'p_p_lifecycle':'1', 'p_p_state':'normal', 'p_p_mode':'view', 'p_p_col_id':'column-1', 'p_p_col_count':'1', '_CustomLogin_WAR_CustomLoginportlet_javax.portlet.action':'customlogin', '_CustomLogin_WAR_CustomLoginportlet_formDate':    '1567169362309', '_CustomLogin_WAR_CustomLoginportlet_saveLastPath': 'false', '_CustomLogin_WAR_CustomLoginportlet_cmd': 'update', '_CustomLogin_WAR_CustomLoginportlet_rememberMe': 'false', '_CustomLogin_WAR_CustomLoginportlet_loginl': '', '_CustomLogin_WAR_CustomLoginportlet_login': 'msghr@msg-global.com', '_CustomLogin_WAR_CustomLoginportlet_password': 'msg@123'}, verify=False)
        content = str(response.text)
        webcontent = response.text
        
        if content.__contains__(res):
            print("Login Successful")
            MyTaskSet.SaveResponse(self, 'Login.html', webcontent)
        else:
            print("Login failed")


    @seq_task(2) 
    @task
    def index(self):   
        res1="Create New Employee"
        response1 = self.client.get("/group/guest/employee-management")
        content1 = str(response1.text)
        if content1.__contains__(res1):
            print("Create EMP form loaded successfully")
        else:
            print("Failed to load EMP form")
        

    @seq_task(3)
    @task 
    def CreateEmp(self):
        #global empid
        EmpID = str(randint(10500, 19999))
        #empid = EmpID
        EmpName = MyTaskSet.NameEmp(self)
        DOB = MyTaskSet.DateDOB(self)
        DOJ = MyTaskSet.DateDOJ(self)
        OffEmail = EmpName + "@msg-global.com"
        PersEmail = EmpName + "@gmail.com"
        ContNum = str(randint(1000000000, 9999999999))

        EmpIDs=self.EmpIDs.append(EmpID)
       
        print("EmpID: " + EmpID)
        print("EmpName: " + EmpName)
        print("DOB: " + DOB)
        print("DOJ: " + DOJ)
        print("OffEmail: " + OffEmail)
        print("PersEmail: " + PersEmail)
        print("ContNum: " + ContNum)
               
        response3 = self.client.post("/group/guest/employee-management", {"p_p_id":"CreateEmpManagementportlet_WAR_CreateEmpManagementportlet", "p_p_lifecycle":"1", "p_p_state":"normal", "p_p_mode":"view", "p_p_col_id":"column-1", "p_p_col_count":"1", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_javax.portlet.action":"CreateEmployee", "employeeDateOfJoining":DOJ, "firstName": EmpName, "middleName": "", "lastName": "A", "employeeDataOfBirth": DOB, "gender": "1", "nationality": "Indian", "bloodGroup": "O+", 'mobileNo': ContNum, 'emergencyNo': '123424354', 'emerNoRelationWithPerson': 'Friend', 'fatherOrHusbandName': 'Freinds', 'relationWithMember': 'Friend', 'employeeId': EmpID, 'employeeSAPNo': EmpID, 'employeeBCSName': EmpName, 'currentLevelId': '2', 'designation': '18', 'employeeType': 'Employee', 'location': 'Bangalore', 'function': '1', 'costCentre': '32', 'depertment': '12', 'managerName': '115', 'userName':EmpID, 'bankAccNo':'78765432128', 'role':'24', 'aadharNo':'', 'nameAsPerAadhar':'', 'panNo':'', 'nameAsPerPassport':'', 'passportNo':'', 'passportDateOfIssue':'', 'passportDateOfExpiry':'', 'issuePlace':'', 'graduation':'', 'graduationSpecialization':'', 'postGraduation':'', 'postGraduationSpecialization':'', 'previousYearsOfExp':'', 'msgGlobalExp':'', 'totalExp':'', 'office':'', 'emailId':OffEmail, 'personalEmailId':PersEmail, 'employeeStatusId':'1'})          
        print("EmpIDs: " + EmpID)
        print("Postres", response3.status_code)
        content3 = str(response3.text)

        res3="Employee Creation process completed successfully!!!"
        if content3.__contains__(res3):
            print("Employee Created successfully")
            MyTaskSet.SearchEmp(self, EmpID)
            
        else:
            print("Failed to create new employee")
        
    @seq_task(4)
    @task
    def SearchEmp(self, empID):
        res4="My Data"
        print("Searchemp:"+empID)
        response4 = self.client.post("/group/guest/employee-management", {"p_p_id": "CreateEmpManagementportlet_WAR_CreateEmpManagementportlet", "p_p_lifecycle": "1", "p_p_state": "normal", "p_p_mode": "view", "p_p_col_id":"column-1", "p_p_col_count": "1", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_action": "getempid", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_formDate": "1568893666555", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_empid": empID})
        content4 = str(response4.text)
        responseFun2 = response4.text
        
        if content4.__contains__(res4):
            print("Emp search is successful")
            MyTaskSet.SaveResponse(self, empID +'.html', responseFun2)
        else:
            print("Emp search failed")
                                                                                  

     
class MyLocust(HttpLocust):
    task_set = MyTaskSet
    EID=MyTaskSet.EmpIDs
    host = "https://10.144.2.132:8443"
    
    
    def teardown(self):
        testId =str(self.EID)
        print("EmpID:" +testId)
    
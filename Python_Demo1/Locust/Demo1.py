'''
Created on 23 Sep 2019

@author: rathos
'''
from locust import Locust, TaskSet, task, HttpLocust, TaskSequence
from locust.core import seq_task
from random import randint
import string
import random
 

class MyTaskSet(TaskSequence):
    
    EmpIDs = []
    
    def nameemp(self):
        m = ""
        for a in range(2):
            z = random.choice(string.ascii_letters)
            m = m + z
        n = "SunilLocust" + m + str(randint(10, 99))
        return n 
    
    def datedob(self):
        mnth = str(randint(1, 12))
        DOB = str(randint(1970, 2000)) + "-" + mnth.zfill(2) + "-" + str(randint(1, 28))
        return DOB
    
    def datedoj(self):
        mnth = str(randint(1, 12))
        DOJ = str(randint(2015, 2019)) + "-" + mnth.zfill(2) + "-" + str(randint(1, 28))
        return DOJ
    
    def savehtml(self, text, name, ext):
        f = open("C:\Sunil\Python Tutorial\Python_Demo1\Locust\\" + name + "." + ext, 'w')
        f.write(text)
        f.close()

    @seq_task(1)
    @task
    def login(self):
        msg1 = "Create New Employee"
        response = self.client.post("/web/guest/welcome", {'p_p_id':'CustomLogin_WAR_CustomLoginportlet', 'p_p_lifecycle':'1', 'p_p_state':'normal', 'p_p_mode':'view', 'p_p_col_id':'column-1', 'p_p_col_count':'1', '_CustomLogin_WAR_CustomLoginportlet_javax.portlet.action':'customlogin', '_CustomLogin_WAR_CustomLoginportlet_formDate':    '1567169362309', '_CustomLogin_WAR_CustomLoginportlet_saveLastPath': 'false', '_CustomLogin_WAR_CustomLoginportlet_cmd': 'update', '_CustomLogin_WAR_CustomLoginportlet_rememberMe': 'false', '_CustomLogin_WAR_CustomLoginportlet_loginl': '', '_CustomLogin_WAR_CustomLoginportlet_login': 'msghr@msg-global.com', '_CustomLogin_WAR_CustomLoginportlet_password': 'msg@123'}, verify=False)
        resp1 = str(response.text)
        if resp1.__contains__(msg1):
            print("Login is successful.")
        else:
            print("Login failed.")
            
    @seq_task(2) 
    @task
    def index(self): 
        msg2 = "Create New Employee"  
        response = self.client.get("/group/guest/employee-management")
        resp1 = str(response.text)
        if resp1.__contains__(msg2):
            print("Home page loaded successfully.")
        else:
            print("Home page was not loaded.")
        
    @seq_task(3) 
    @task
    def creatempform(self):
        msg3 = "Personal Data"
        response = self.client.get("/group/guest/employee-management?p_p_id=CreateEmpManagementportlet_WAR_CreateEmpManagementportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_render=hrView")
        response = response.decode('ascii', 'ignore')
        resp1 = str(response.text)
        if resp1.__contains__(msg3):
            print("Create employee form loaded successfully.")
        else:
            print("Create employee form failed.")

    @seq_task(4)
    @task 
    def createemp(self):
        msg3 = "Employee Creation process completed successfully"
        EmpID = str(randint(10500, 19999))
        EmpName = MyTaskSet.nameemp(self)
        DOB = MyTaskSet.datedob(self)
        DOJ = MyTaskSet.datedoj(self)
        OffEmail = EmpName + "@msg-global.com"
        PersEmail = EmpName + "@gmail.com"
        ContNum = str(randint(1000000000, 9999999999))
            
        response = self.client.post("/group/guest/employee-management", {"p_p_id":"CreateEmpManagementportlet_WAR_CreateEmpManagementportlet", "p_p_lifecycle":"1", "p_p_state":"normal", "p_p_mode":"view", "p_p_col_id":"column-1", "p_p_col_count":"1", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_javax.portlet.action":"CreateEmployee", "employeeDateOfJoining":DOJ, "firstName": EmpName, "middleName": "", "lastName": "A", "employeeDataOfBirth": DOB, "gender": "1", "nationality": "Indian", "bloodGroup": "O+", 'mobileNo': ContNum, 'emergencyNo': '123424354', 'emerNoRelationWithPerson': 'Friend', 'fatherOrHusbandName': 'Freinds', 'relationWithMember': 'Friend', 'employeeId': EmpID, 'employeeSAPNo': EmpID, 'employeeBCSName': EmpName, 'currentLevelId': '2', 'designation': '18', 'employeeType': 'Employee', 'location': 'Bangalore', 'function': '1', 'costCentre': '32', 'depertment': '12', 'managerName': '115', 'userName':EmpID, 'bankAccNo':'78765432128', 'role':'24', 'aadharNo':'', 'nameAsPerAadhar':'', 'panNo':'', 'nameAsPerPassport':'', 'passportNo':'', 'passportDateOfIssue':'', 'passportDateOfExpiry':'', 'issuePlace':'', 'graduation':'', 'graduationSpecialization':'', 'postGraduation':'', 'postGraduationSpecialization':'', 'previousYearsOfExp':'', 'msgGlobalExp':'', 'totalExp':'', 'office':'', 'emailId':OffEmail, 'personalEmailId':PersEmail, 'employeeStatusId':'1'})          
        resp1 = response.text
        resp2 = str(resp1)
        
        if (str(resp2)).__contains__(msg3):
            print("Employee created successfully.")
            self.EmpIDs.append(EmpID)
            response1 = self.client.post("/group/guest/employee-management", {"p_p_id": "CreateEmpManagementportlet_WAR_CreateEmpManagementportlet", "p_p_lifecycle": "1", "p_p_state": "normal", "p_p_mode": "view", "p_p_col_id":"column-1", "p_p_col_count": "1", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_action": "getempid", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_formDate": "1568893666555", "_CreateEmpManagementportlet_WAR_CreateEmpManagementportlet_empid": EmpID})
            resp3 = response1.text
            resp4 = str(resp3)
            if resp4.__contains__(EmpID):
                MyTaskSet.savehtml(self, resp3, EmpID, "html")
            else:
                print("Create Employee is success but saving HTML file has failed.")
            
        else:
            print("Employee creation has failed.")

     
class MyLocust(HttpLocust):
    eIDs = MyTaskSet.EmpIDs
    task_set = MyTaskSet
    host = "https://10.144.2.132:8443"
    
    def teardown(self):
        print("IDs:" + str(self.eIDs))

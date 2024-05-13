from guizero import *
from DatabaseCommands import *

def pressNext():
    global index
    
    index += 1
    
    if index == len(picList):
        index = 0
        
    pic.value = picList[index]
    firstNameText.value = fnameList[index]
    lastNameText.value =lnameList[index]
    employeeNumText.value =enList[index]
    salaryText.value = salList[index]
    jobText.value = jobList[index]
    yearsText.value = yearsList[index]

def pressSave():
    picList.append("Default.png")
    fnameList.append(firstNameText.value)
    lnameList.append(lastNameText.value)
    enList.append(employeeNumText.value)
    salList.append(salaryText.value)
    jobList.append(jobText.value)
    yearsList.append(yearsText.value)
    
    print("Employee Added to List but not to Database")
    
def pressNew():
    global index
    
    index = 0
    pic.value = "./Default.png"
    firstNameText.value = ""
    lastNameText.value =""
    employeeNumText.value =""
    salaryText.value = ""
    jobText.value = ""
    yearsText.value = ""

def pressLoad():
    global picList, fnameList, lnameList, enList, salList, jobList, yearsList
    
    pass
        
        

app = App(title="Employee Database", width = 450, height = 600, layout="grid")

pic = Picture(app, image="./Default.png", grid=[0,0, 2, 1])

firstNameBox = TitleBox(app, "First Name", grid=[0,1])
firstNameText = TextBox(firstNameBox, width=20)

lastNameBox = TitleBox(app, "Last Name", grid=[1,1])
lastNameText=TextBox(lastNameBox, width=20)

employeeNumBox = TitleBox(app, "Employee Number", grid=[0,2])
employeeNumText =TextBox(employeeNumBox, width=10)

salaryBox=TitleBox(app, "Salary", grid=[1,2])
salaryText=TextBox(salaryBox, width=15)

jobBox=TitleBox(app, "Job Title", grid=[0,3])
jobText=TextBox(jobBox, width=15)

yearsBox= TitleBox(app, "Years Experience", grid=[1,3])
yearsText= TextBox(yearsBox, width=15)

buttonBox = TitleBox(app, "Buttons", layout="grid", grid=[0,4,2,1])
nextButton = PushButton(buttonBox, text="Next", grid=[0,0], command = pressNext)
saveButton = PushButton(buttonBox, text="Save", grid=[1,0], command = pressSave)
newButton = PushButton(buttonBox, text="New", grid=[2,0], command = pressNew)
loadButton = PushButton(buttonBox, text="Load", grid=[3,0], command = pressLoad)

index = 0

picList=["Brewster.png", "Danko.png", "Dzierwa.png", "Ferdig.png", "Krabill.png", "Lambert.png", "Oshea.png", "Roberts.png", "Ruckstuhl.png"]
fnameList=["Mike", "Julie", "Matt", "Tom", "Nick", "Natalie", "Kevin", "Betsy", "Brian"]
lnameList=["Brewster", "Danko", "Dzierwa", "Ferdig", "Krabill", "Lambert", "Oshea", "Roberts", "Ruckstuhl"]
enList = ["3562", "1324", "2049", "3420", "9463", "5603", "3420", "2304", "6707"]
salList = [80000,82475, 74300, 126000, 52600, 65230, 267000, 62000, 54320]
jobList= ["Science Teacher", "Social Studies Teacher", "Math Teacher", "Assistant Principal", "Math Teacher", "Spanish Teacher", "Superintendent", "Secretary", "Deputy"]
yearsList =[23, 33, 26, 18, 2, 9, 15, 16, 6]

app.display()
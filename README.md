# ACME Salary Calculator
## Contents
1. [Exercise](#exercise)
2. [How to run locally?](#howtorun)
3. [Architecture](#architecture)
4. [Approach & Methodology](#methodology)
5. [Testing (PyTest)](#testing)
6. [Developer's final comment](#comment)

## Excercise
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:
```plain
Monday - Friday
00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD

Saturday and Sunday
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD
```
The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:
```plain
MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday
```
**Input:** the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

**Output:** indicate how much the employee has to be paid

For example:
```plain
Case 1:
INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:
The amount to pay RENE is: 215 USD
```
```plain
Case 2:
INPUT
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
The amount to pay ASTRID is: 85 USD
```

## How to run locally?
### Requirements
1. Dowload [Visual Studio Code](https://code.visualstudio.com/)
2. Dowload [Git](https://git-scm.com/)
3. Dowload and install [Python](https://www.python.org/downloads/)
4. Dowload the [repository](https://github.com/rokthar/IOET_Pagos_ACME) or use the command ```git clone https://github.com/rokthar/IOET_Pagos_ACME.git``` in your terminal.
5. Dowload the Python package for Visual Code
![Python package for Visual Code](https://geekytheory.com/uploads/2018/08/configurar-python-visual-studio-vs-code.png)

### Run
1. Open the mail.py file
2. Open the terminal in Visual Code
3. Write the command ```python main.py```
4. The system will ask you to enter the name of the file to be evaluated, you can use the files already created, which are: Rene, Andrea o Juan(Contains errors). You can also create your own file following the structure indicated in both examples above.
5. Once you have entered the name or path of the file you have created, you can press enter and wait for the system response.

## Architecture
The program is structured using the MVC architecture; it contains the directories for the model, view and controller, as well as the main.py file, which executes the program.
* **Model:** It contains the class to create the object that will be used to present the program response, besides the function getData, which reads the txt file and returns the information inside the file, in case the file does not exist, it returns "Error".
* **View:** Contains the functions necessary to present the response messages to the user.
* **Controler:** t contains the necessary functions to calculate the payment to be made, as well as the functions to check that the file has the indicated structure.

## Approach & Methodology
I used the Python language because of how easy it is to handle strings and arrays. 
The open() function was used, which reads the content of the text file and allows to store it in a variable.
I used this language because I am learning it and I wanted to test myself if I could complete this exercise with a new language and apply the MVC pattern and architecture.

The main code structure is:
* Prompt to enter the file name or path ```name = input()``` 
* Open the file ```data = open()```
* Read the file ```m = data.read()```
* Remove whitespace ```m.replace(" ", "")```
* Separate the name from the schedule
* Separate each schedule by day
* Separate hours and minutes of each hour
* Get the value to be paid per hour, according to the day and time range
* Calculate the payment, multiplying the hourly value by the hours worked.
* Show the result to the user
* 
### The methodology used in the project is detailed below:
I started with setting up the environment, creating the basic project files, creating the repository, creating the README and configuring the GitHub shares.

Then the basic requirements of the exercise were obtained, that is, what was required for the project to be considered functional.

The files ```model.py```, ```controller.py``` and ```view.py``` were created according to the MVC pattern, also the ```main.py``` file was created where the program is executed and the ```constants.py``` file where the constants to be used in the program are placed.

Then we proceeded to write the program logic, in ```model.py``` the ```open``` and ```readLines``` function is used to open and read the .txt document; this information is sent to the controller.

In ```controller.py``` the lines are separated to obtain the necessary information, the name and the working time ranges are obtained, each one with its respective day; then it is validated that the information is correct, that is to say verifying that there are days and that these are part of the days of the week, besides that the hours do not exceed 24 hours and that the minutes do not exceed the value of 59. Subsequently, the value to be paid per hour is obtained, according to the day and the time range in which it was worked and finally the value to be paid is calculated, which increases with each schedule in the information of the txt file.

From ```main.py``` it is sent to execute the functions of the view for the start of the program and after the calculation the result of the amount to be paid is presented through console.

Finally there is the file ```test_calculadoraPagos.py``` in which there are several methods to test different ways in which the information can be written in the txt file, these tests were performed with the framework [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html), which facilitates the generation of unit tests.

## Testing (PyTest)
### Requirements
* Install [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html)
* [Have knowledge in using Pytest](https://docs.pytest.org/en/6.2.x/)

### Steps to Reproduce
* Open the repository in Visual Studio Code
* Open the terminal in Visual Studio Code
* Write the command ```pytest```
* See the results

## Developer's final comment
I had a lot of fun solving this exercise, as it allowed me to learn and reinforce my knowledge with the Python programming language.

Also, for me all this was very important, because thanks to this exercise I realized how the company works and not only that, but also the things that the developers do, and the other people who collaborate in the creation and development of the company's projects. It only remains for me to say thank you very much for this incredible experience and I hope to meet all your expectations.

Thank you,

Esparza Torres Ricardo Javier


# Project Title : Airport Passenger Verfication System using face recognition

### Overview
The Passenger check-in process at airports are time consuming and possess a heavy work load on boarding agents. On an average , a paseenger spends most of the time waiting in queue for check-in at the airport. Also, COVID-19 pandemic has resulted into a need of contactless and fast check-in or boarding process.
Imagine gaining entry to the flight within 15 seconds and without any human intervention.
Yes, this is possible with Face Recognition Technology!

To facilitate this,  Airport Passenger Verfication System will work as follows:
1. When a passenger books a flight online, the system will collect information about passenger like Name, Passport number, Scanned Passport(in JPG format),  Scanned copy of Aadhar Card(in JPG format), a passport-size photo(in JPG format).
2. Based on the images taken while booking the flight, personGroup is created and trained using Microsoft Azure Face API.
3. At the time of the check-in , passenger will capture his photo and the system will verify its details.
4. If the person is not in the database, he is not given the access.

### Features
1. Book flight option : 
   This option enables passenger to book flight online and upload relevant information and documents so that check-in would be faster at      the airport.
2. Flight Check-in option :
   The face recognition system is installed at the airport.
   This option detects and verifies the passenger details and makes check-in process smooth as well as faster.
3. If passenger has not booked the flight prior, it denies the access.

### Requirements to run the project
1. Microsoft Azure Face api subscription.
## Making the Azure Account

In order to run the face dectection and analysis, you must get an API Subscription Key from the Azure Portal. This page by Microsoft provides the features and capabilities of the Face API. You can create a free Azure account that doesn't expire [at this link here](https://azure.microsoft.com/en-us/free/cognitive-services/?api=face-api) by clicking on the "Get API Key" button and choosing the option to create an Azure account.

## Getting the Face API Key from Azure Portal
Once you have created your account, head to the [Azure Portal](https://portal.azure.com/#home). Follow these steps:

1. Click on "Create a resource" on the left side of the portal.
2. Underneath "Azure Marketplace", click on the "AI + Machine Learning" section.
3. Now, under "Featured" you should see "Face". Click on that.
4. You should now be at [this page](https://portal.azure.com/#create/Microsoft.CognitiveServicesFace). Fill in the required information and press "Create" when done.
5. Now, click on "All resources" on the left hand side of the Portal.
6. Click on the name you gave the API.
7. Underneath "Resource Management", click on "Manage Keys".

![image](https://user-images.githubusercontent.com/91329086/170860986-1d42201f-e481-4ea2-bbe7-57cce398f94d.png)

You should now be able to see two different subscription keys that you can use.

## Setup
1. Install PyCharm Community Edition 2020.3.1
2. Install Python Interpreter version : 3.9
3. Create a new project in PyCharm.
4. Add installed python interpreter to the project. You can refer [this](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) for help.
5. Install following libraries: 
    [libraries.txt](https://github.com/Shriya0731/Microsoft-Engage-Face-Recognition-Project/files/8793034/libraries.txt)
6. Download zip of the repository extract all files and paste in the New project folder.
7. Paste your API key and Endpoint in the NewTry.py file and Functions.py file.
8. Open terminal , type streamlit run GUI.py and enter to run the webapp.

Note : Internet connection is required to run the project.

Demo link : 

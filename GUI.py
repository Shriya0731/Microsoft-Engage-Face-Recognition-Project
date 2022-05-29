#importing necessary libraries

# library for GUI
import streamlit as st
# for image processing
import cv2 as cv2
# User-defined function to detect face
from Functions import detectface
# functions to update and get information from database
from Boarding_Info_Update import get_passportno,add_new_booking #
# library to open and save image
from PIL import Image
# To perform operations like create folder, list directories
import os
# For creating sidebar with option menu in GUI
from streamlit_option_menu import option_menu
# User-defined function to create and train personGroup
from NewTry import Train_model

#creating sidebar
with st.sidebar:
    navbar = option_menu("Main Menu", ["Home","Book your flight","Flight Check-in"], icons = ["house","card-checklist","person-bounding-box"],menu_icon="justify", default_index=0)
st.markdown(f'''
          <style>
         section[data-testid="stSidebar"] .css-ho6u4w{{
             background-color : #3c6ce4
         }}
         </style>
            ''',
        unsafe_allow_html=True)
flag = 0

# Home page
if navbar == "Home":
    # Styling sidebar with html code
    st.markdown(f'''
             <style>
            section[data-testid="stSidebar"] .css-ho6u4w{{
                background-color : #FFFFFF
            }}
            </style>
               ''',
                unsafe_allow_html=True)
    # Creating background image for home page using HTML code
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://csmia.adaniairports.com/images/traveller-banner05.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
    # Adding title
    html_temp = """
          <body style="background-color:red;">
         
          <h2 style="color:white;text-align:center;">Welcome To The Mumbai International Airport</h2>
       
          </body>
          """
    st.markdown(html_temp,unsafe_allow_html=True)

# Flight Check-in option to verify passengers at the time of boarding.
if navbar =="Flight Check-in":

    st.title("Passenger Verification")
    st.subheader("Welcome to the Bombay Airport")
    run = st.button("Capture Image")
    if True:
            # Opening camera
            capture = cv2.VideoCapture(0)
            img_display = st.empty()
            name = str
            try :
                while True:

                        ret, img = capture.read()
                        print("ans:",ret)
                        if(run): # When run button is clicked the picture is taken
                            cv2.imwrite(filename='saved_img.jpg', img=img)  # captured image is stored with filename
                            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                            img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)    # converting to RGB
                            temp_add = r"C:\Users\ADMIN\PycharmProjects\Microsoft Engage Project\test.jpg" # Saving converted image
                            cv2.imwrite(temp_add, img_)
                            returned_list = detectface(temp_add) # detectface function returns the list of names of persons recognized
                            if(returned_list is None or len(returned_list)==0): # if person is not identified then detectface functions returns null list
                                st.write("Person not identified!")
                                st.write("Access denied")
                            else:
                                flag=1
                                name = detectface(temp_add)[0] # person detected
                            break
                        img_display.image(img, channels='BGR') # to display video


                # if person is recognized
                if (flag == 1):
                    st.write("Person recognized :", name)
                    st.write("Passport number : ", get_passportno(name)) #calls function to get passportno from database
                    st.write("Successfully verified and boarded!")

                capture.release()
            except Exception as e:
                st.write("Camera not found!")

# this option is chosen when passenger books his flight.
if navbar == "Book your flight":
    st.title("Book Flight")
    backimg = Image.open("flight1.png")
    st.image(backimg,width=800)
    name  = st.text_input("Name")
    if len(name) > 2:
        new_folder = name

    passportno = st.text_input("Passport number")

    photo = st.file_uploader(label = "Upload a passport size photo:",type=['jpg'])
    if photo is not None:
        img1 = Image.open(photo)

    passport = st.file_uploader(label="Upload passport: ", type=['jpg'])
    if passport is not None:
        img2 = Image.open(passport)

    aadhar = st.file_uploader(label="Upload Aadhar card ", type=['jpg'])
    if aadhar is not None:
        img3 = Image.open(aadhar)
    date = st.date_input("Enter departure date:")
    flight = st.text_input("Enter Flight ID:")
    book = st.button("Confirm Booking",key="djfhcmb,n .mdpeariothkjfv")
    if book:
        parent_dir = "C:\\Users\ADMIN\\PycharmProjects\\Microsoft Engage Project\\Images\\"
        path = os.path.join(parent_dir, new_folder)
        os.mkdir(path)
        os.chdir(path)
        img1 = img1.save("img1.jpg")
        img2 = img2.save("img2.jpg")
        img3 = img3.save("img3.jpg")
        st.write("Booked flight successfully!")
        add_new_booking(name,passportno,date,flight)  # adding new data to database
        Train_model()  # Training model with new person

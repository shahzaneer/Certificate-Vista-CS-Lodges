# Imports
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import  pandas as pd
from termcolor import colored
from tqdm import tqdm_gui
import os 
from datetime import datetime
import shutil



# Usually a .csv file but here i've used .xlsx file
# Make sure to have 'Name' column in it
file = pd.read_excel('event.xlsx')

# organization Name
# orgName = input("Enter Organization Name: ")
orgName = "CS Lodges"

# orgAcronym = input("Enter Organization Acronym: ")
orgAcronym = "CSL"

# speaker = input("Enter the name of Speaker: ")
speaker = "Saad Hassan"


eventName = input("Enter Event Name: ")
# leadName = input("Lead Name: ")
leadName = "Shahzaneer Ahmed"

currentDate = datetime.date(datetime.now())

# where certificates will be generated
fname = 'certificates/'
if os.path.exists(fname):
    shutil.rmtree(fname)
os.mkdir(fname)

# Getting 'Name' columns from 'file'
for names in tqdm_gui(file['Name']):
    image = Image.new('RGB',(1920,1080),(255,255,255))


    draw = ImageDraw.Draw(image)
    font_path = './Almondita.ttf'

    # font of ORG
    fontdev = ImageFont.truetype('arial.ttf', size=35)
    # font of Certificate
    fontcert = ImageFont.truetype('arialbd.ttf', size=55)
    # font of participant name
    fontname = ImageFont.truetype('arial.ttf', size=35)
    # font of signature
    signature = ImageFont.truetype(font_path, 150)

    # colors for various writings
    colordev = 'rgb(128, 128, 128)'
    colorcert = 'rgb(89, 89, 89)'
    colorname = 'rgb(77, 148, 255)'
    colorNameLead = 'rgb(229, 57, 53)'


    # org logo
    org_logo = Image.open('logo.png')
    # Resizing the ORG Logo
    org_logo = org_logo.resize((500,100))

    # Left Side style Image
    backgroundImage = Image.open('CertificateBg.png')

    # Putting Logo & Left style Image
    image.paste(backgroundImage, (0,0))
    image.paste(org_logo, (950,125))



    participation_message = f"is hereby awarded this Certificate of Participation on successfully attending \n{eventName} Organized by {orgName} delivered by\n {speaker}."

    # draw.text((1040,143),'CS Lodges',font=fontdev,fill=colordev)
    draw.text((950,250),'Certificate of Participation',font=fontcert,fill=colorcert)
    draw.text((950,350), eventName + ' Participant',font=ImageFont.truetype('arial.ttf', size=32), fill=colordev)
    draw.text((950,450),names,font=fontcert,fill=colorname)
    draw.text((950,550),participation_message,font=ImageFont.truetype('arial.ttf', size=25),fill='rgb(102, 102, 102)')
    draw.text((960,650),leadName,font=signature,fill=colorNameLead)
    draw.line((950,800, 1520,800), fill='rgb(128, 128, 128)', width=3)

    draw.text((950,820),f'CS Lodges,Community Manager',font=ImageFont.truetype('./arialbd.ttf', size=22),fill=colorcert)
    draw.text((950,920), 'Signing Authority', font=ImageFont.truetype('arial.ttf', size=22), fill='rgb(128,128,128)')
    draw.text((950,960), orgAcronym + ' Manager', font=ImageFont.truetype('./arialbd.ttf', size=25), fill='rgb(128,128,128)')
    draw.text((1640,1020),'#CSLodges #CSFoundation',font=ImageFont.truetype('arial_italic.ttf', size=18),fill='rgb(211, 47, 47)')
    draw.text((1640,950),'Certificate ID:',font=ImageFont.truetype('arial.ttf', size=20),fill=colorcert)
    draw.text((1640,980),f'Issue Date: {currentDate}',font=ImageFont.truetype('arial.ttf', size=20),fill=colorcert)
    image.save('certificates/'+names+'.png')

    


import sqlite3
from bottle import Bottle, route, run, template, static_file
import requests #used for making API calls
import xml.etree.ElementTree as ET #search through the API data from Kamar
from datetime import datetime, timedelta #used for getting tomorrow's date
import Todo

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

#calls in kamar API to get timetable and calendar data
#details about API are https://documenter.getpostman.com/view/1593669/S1TU1d8Y
@route('/')
def kamar():
    #from Postman user id and key for kamar API
    kamar_id = '18115'
    kamar_key = 'SdIJkcnrONoOhrcZGOsmO3ncpMDlX92x'     
    #api info
    kamar_api_url = 'https://sacredheart.parents.school.nz/api/api.php'
    #API headers sourced from Postman
    kamar_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'KAMAR API Documentation',
        'Origin': 'file://',
        'X-Requested-With':'nz.co.KAMAR'
    }
    #data needed for the timetable
    kamar_timetable_data = {
        'Command':'GetStudentTimetable',
        'Key':kamar_key,
        'StudentID':kamar_id,        
        'Grid':'2024TT'
    }
    #data needed for the calendar
    kamar_calendar_data = {
        'Command':'GetCalendar',
        'Key': kamar_key,
        'StudentID':kamar_id,        
        'Year':'2024'
    }
   
    #testing if the following commands work and if they don't show the error
    try:
        #get timetable data from kamar API
        response = requests.post(kamar_api_url,headers=kamar_headers,data=kamar_timetable_data)
        response.raise_for_status() #raise any problem
        kamar_timetable_xml = ET.fromstring(response.content)            
        #now get calendar data
        response = requests.post(kamar_api_url,headers=kamar_headers,data=kamar_calendar_data)
        response.raise_for_status() #raise any problem
        kamar_calendar_xml = ET.fromstring(response.content)            

        #get tomorrow's calendar
        tomorrow = datetime.today() + timedelta(days=1) #today plus one day        
        tomorrow_date = tomorrow.strftime('%Y-%m-%d') #giving the full year and month and day for kamar
        tomorrow_day_number = tomorrow.strftime('%w') #Monday=1, Tuesday=2 etc
        
        #get tomorrow's timetable using xpath
        #to get the week number we look through the calendar xml and find recursively the day which has the date from tomorrow variable
        tomorrow_weeknumber = kamar_calendar_xml.find(f".//Day[Date='{tomorrow_date}']/WeekYear").text
        #to get the timetable look through the timetable xml recursively looking for the tomorrow week number and tomorrow day number
        tomorrow_timetable = kamar_timetable_xml.find(f".//W{tomorrow_weeknumber}/D{tomorrow_day_number}").text            
        #separating the whole timetable from the pipes (|)
        tomorrow_timetable_classes = tomorrow_timetable.split('|')
        homeroom = tomorrow_timetable_classes[2]
        period1 = tomorrow_timetable_classes[3]
        period2 = tomorrow_timetable_classes[4]
        period3 = tomorrow_timetable_classes[6]
        period4 = tomorrow_timetable_classes[7]
        period5 = tomorrow_timetable_classes[8]
        period6 = tomorrow_timetable_classes[9]

        #split the class, the teacher and the room from the timetable data for each period
        period1_split = period1.split("-")
        if len(period1_split) < 5:
            period1_subject = "unknown"
            period1_teacher = "unknown"
            period1_room = "unknown"
        else:
            period1_subject = period1_split[2]
            period1_teacher = period1_split[3]
            period1_room = period1_split[4]
        
        period2_split = period2.split("-")
        if len(period2_split) < 5:
            period2_subject = "unknown"
            period2_teacher = "unknown"
            period2_room = "unknown"
        else:
            period2_subject = period2_split[2]
            period2_teacher = period2_split[3]
            period2_room = period2_split[4]

        period3_split = period3.split("-")
        if len(period3_split) < 5:
            period3_subject = "unknown"
            period3_teacher = "unknown"
            period3_room = "unknown"
        else:
            period3_subject = period3_split[2]
            period3_teacher = period3_split[3]
            period3_room = period3_split[4]

        period4_split = period4.split("-")
        if len(period4_split) < 5:
            period4_subject = "unknown"
            period4_teacher = "unknown"
            period4_room = "unknown"
        else:
            period4_subject = period4_split[2]
            period4_teacher = period4_split[3]
            period4_room = period4_split[4]

        period5_split = period5.split("-")
        if len(period5_split) < 5:
            period5_subject = "unknown"
            period5_teacher = "unknown"
            period5_room = "unknown"
        else:
            period5_subject = period5_split[2]
            period5_teacher = period5_split[3]
            period5_room = period5_split[4]

        period6_split = period6.split("-")
        if len(period6_split) < 5:
            period6_subject = "unknown"
            period6_teacher = "unknown"
            period6_room = "unknown"
        else:
            period6_subject = period6_split[2]
            period6_teacher = period6_split[3]
            period6_room = period6_split[4]


        #pass the data back to kamar page from API to display for user
        data = {
            'student_id':kamar_id,
            'period1_subject':period1_subject,
            'period1_teacher':period1_teacher,
            'period1_room':period1_room,
            'inspirational_message':'Do or do not, there is no try - Yoda'
        }        
    #if the try fails then display the error    
    except Exception as e:
        return f"sorry there was an error:{str(e)}"           
    
    #send the data back to homepage and running it as a template to display the data nicely
    #template replaces {{}} with data
    return template('homepage.html',**data)
    
#stattic homepage route
@route('/static')
def index():
    return static_file("homepage.html", root='./')

run(host='localhost', port=8080, reloader = True)

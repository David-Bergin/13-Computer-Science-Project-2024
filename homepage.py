import sqlite3
from bottle import Bottle, route, run, template, static_file, TEMPLATE_PATH
import requests #used for making API calls
import xml.etree.ElementTree as ET #search through the API data from Kamar
from datetime import datetime, timedelta #used for getting tomorrow's date
import Todo
from icalendar import Calendar #to work with ics file
import os

TEMPLATE_PATH.insert(0, 'templates') #putting the templates in their own folder

#from Postman user id and key for kamar API
#kamar_id = '18115' #my ID for testing
kamar_id = '23232' #user ID
#kamar_key = 'SdIJkcnrONoOhrcZGOsmO3ncpMDlX92x' #my key for testing
kamar_key = 'PNcPJcJ7ODYOF793FNRqIMhcPMNkpDlW' #user key
#api info
#kamar_api_url = 'https://sacredheart.parents.school.nz/api/api.php' #my school for testing
kamar_api_url = 'https://portal.baradene.school.nz/api/api.php' #user school
#API headers sourced from Postman
kamar_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'KAMAR API Documentation',
    'Origin': 'file://',
    'X-Requested-With':'nz.co.KAMAR'
}
#kamar_ics_file = 'https://sacredheart.parents.school.nz/ics/school.ics' #my school for testing
kamar_ics_file = 'https://portal.baradene.school.nz/index.php/ics/school.ics' 

#return data from kamar API about timetable in a function so we can access it multiple times
def gettimetable():
    #data needed for the timetable
    kamar_timetable_data = {
        'Command':'GetStudentTimetable',
        'Key':kamar_key,
        'StudentID':kamar_id,        
        'Grid':'2024TT'
    }    
   
    #testing if the following commands work and if they don't show the error
    try:
        #get timetable data from kamar API
        response = requests.post(kamar_api_url,headers=kamar_headers,data=kamar_timetable_data)
        response.raise_for_status() #raise any problem
        kamar_timetable_xml = ET.fromstring(response.content)
        return kamar_timetable_xml
        
    #if the try fails then display the error    
    except Exception as e:
        return f"sorry there was an error:{str(e)}"           

#return data from kamar API about calendar in a function so we can access it multiple times
def getcalendar():
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
        response = requests.post(kamar_api_url,headers=kamar_headers,data=kamar_calendar_data)
        response.raise_for_status() #raise any problem
        kamar_calendar_xml = ET.fromstring(response.content)            
        return kamar_calendar_xml
        
    #if the try fails then display the error    
    except Exception as e:
        return f"sorry there was an error:{str(e)}"           

def gettomorrow():
    #get tomorrow's date
    tomorrow = datetime.today() + timedelta(days=1) #today plus one day        
    return tomorrow

def gettodaydate():
    today = datetime.today()
    today_date = today.strftime('%Y-%m-%d') #giving the full year and month and day for kamar
    return today_date

def gettomorrowdate():
    tomorrow = gettomorrow()
    tomorrow_date = tomorrow.strftime('%Y-%m-%d') #giving the full year and month and day for kamar
    return tomorrow_date

def getdaynum():
    tomorrow = gettomorrow()
    tomorrow_day_number = tomorrow.strftime('%w') #Monday=1, Tuesday=2 etc
    return tomorrow_day_number    

#go and get the reminder data
def getreminder():
    conn = sqlite3.connect('reminders.db')
    c = conn.cursor()
    c.execute("SELECT reminder FROM reminder")
    result_reminders = c.fetchone()
    c.close()
    return result_reminders[0]

#take original API data a period and return the subject and the teacher and the classroom
def translateperiod(original):
    
    if len(original) == 0:
        subject = ''
        teacher = ''
        room = ''
    else:
        try:
            original_split = original.split("-")
            if len(original_split) < 5:
                subject = "unknown"
                teacher = "unknown"
                room = "unknown"
            else:
                subject = original_split[2]
                teacher = original_split[3]
                room = original_split[4]
        except Exception as e:
            return f"sorry there was an error translating:{str(e)}"  

    return subject, teacher, room
       
@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

@route('/timetable')
def timetable():
    try:
        #get timetable data from kamar API
        kamar_timetable_xml = gettimetable()
        #now get calendar data
        kamar_calendar_xml = getcalendar()
        #get today's date
        today_date = gettodaydate()       
        #create an array for the data
        data = {}

        #get current week's timetable using xpath
        #to get the week number we look through the calendar xml and find recursively the day which has the date from today variable
        today_weeknumber = kamar_calendar_xml.find(f".//Day[Date='{today_date}']/WeekYear").text
        #to get the timetable look through the timetable xml recursively looking for the current week number
        currentweek_timetable = kamar_timetable_xml.find(f".//W{today_weeknumber}")
        
        daynumber = 0
        
        #translate day number to weekday
        daynames = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday'
        }

        #go through each day in current week timetable and get the period details
        for day in currentweek_timetable:
            daynumber = daynumber + 1
            
            currentweek_timetable_classes = day.text.split('|')
            homeroom = currentweek_timetable_classes[2]
            period1 = currentweek_timetable_classes[3]
            period2 = currentweek_timetable_classes[4]
            period3 = currentweek_timetable_classes[6]
            period4 = currentweek_timetable_classes[7]
            period5 = currentweek_timetable_classes[9]
            period6 = currentweek_timetable_classes[10]

            #split the class, the teacher and the room from the timetable data for each period
            homeroom_subject, homeroom_teacher, homeroom_room = translateperiod(homeroom)
            period1_subject, period1_teacher, period1_room = translateperiod(period1)        
            period2_subject, period2_teacher, period2_room = translateperiod(period2)        
            period3_subject, period3_teacher, period3_room = translateperiod(period3)        
            period4_subject, period4_teacher, period4_room = translateperiod(period4)        
            period5_subject, period5_teacher, period5_room = translateperiod(period5)        
            period6_subject, period6_teacher, period6_room = translateperiod(period6)        

            #pass the data back to kamar page from API to display for user
            data[daynames[daynumber]] = {
                    'homeroom_subject':homeroom_subject,
                    'homeroom_teacher':homeroom_teacher,
                    'homeroom_room':homeroom_room,
                    'period1_subject':period1_subject,
                    'period1_teacher':period1_teacher,
                    'period1_room':period1_room,
                    'period2_subject':period2_subject,
                    'period2_teacher':period2_teacher,
                    'period2_room':period2_room,
                    'period3_subject':period3_subject,
                    'period3_teacher':period3_teacher,
                    'period3_room':period3_room,
                    'period4_subject':period4_subject,
                    'period4_teacher':period4_teacher,
                    'period4_room':period4_room,
                    'period5_subject':period5_subject,
                    'period5_teacher':period5_teacher,
                    'period5_room':period5_room,
                    'period6_subject':period6_subject,
                    'period6_teacher':period6_teacher,
                    'period6_room':period6_room
                }          
        
    #if the try fails then display the error    
    except Exception as e:
        return f"sorry there was an error:{str(e)}"           
    
    #send the data back to homepage and running it as a template to display the data nicely
    #template replaces {{}} with data    
    return template('layout',title="Timetable",content=template('timetable', timetable_data=data))
    

#calls in kamar API to get timetable and calendar data
#details about API are https://documenter.getpostman.com/view/1593669/S1TU1d8Y
@route('/')
def kamar():    
    #testing if the following commands work and if they don't show the error
    try:
        #get timetable data from kamar API
        kamar_timetable_xml = gettimetable()
        #now get calendar data
        kamar_calendar_xml = getcalendar()

        #get tomorrow's calendar        
        tomorrow_date = gettomorrowdate()
        tomorrow_day_number = getdaynum()
        
        #get tomorrow's timetable using xpath
        #to get the week number we look through the calendar xml and find recursively the day which has the date from tomorrow variable
        tomorrow_weeknumber = kamar_calendar_xml.find(f".//Day[Date='{tomorrow_date}']/WeekYear").text
        #to get the timetable look through the timetable xml recursively looking for the tomorrow week number and tomorrow day number
        tomorrow_timetable = kamar_timetable_xml.find(f".//W{tomorrow_weeknumber}/D{tomorrow_day_number}").text            
        #separating the whole timetable from the pipes (|)
        tomorrow_timetable_classes = tomorrow_timetable.split('|')
        #get tomorrow period 1        
        period1 = tomorrow_timetable_classes[3]
        
        #split the class, the teacher and the room from the timetable data for each period
        period1_subject, period1_teacher, period1_room = translateperiod(period1)        
        
        #get events from the calendar for tomorrow if there are any
        #get ICS file and getting tomorrow events from it        
        try:
            #save the ICS file if not there
            ics_file = 'calendar.ics'
            if not os.path.exists(ics_file):                
                response = requests.post(kamar_ics_file)
                response.raise_for_status() #raise any problem
                if response.status_code == 200:
                    #write the file
                    with open(ics_file, 'wb') as f:
                        f.write(response.content)
            
            #open the ICS file
            with open(ics_file,'r') as f:
                ics_data = f.read()

            #go through the file and add the events into array    
            kamar_events = {}
            kamar_calendar = Calendar.from_ical(ics_data)
            for item in kamar_calendar.walk():
                if item.name == "VEVENT":
                    
                    summary = item.get('summary')                    
                    location = item.get('location')   
                    
                    #decode the details (found via Google)
                    if summary:
                        summary = summary.to_ical().decode('utf-8')
                    if location:
                        location = location.to_ical().decode('utf-8')
                    
                    #get the start date and format it like timetable
                    start_date = item.get('dtstart').dt
                    start_date = start_date.strftime('%Y-%m-%d')                                     
                    
                    #if the location is none don't add it to the array
                    if location is not None:                        
                        event = {                        
                            'start_date': start_date,
                            'summary': summary,
                            'location': location
                        }
                        
                        #in case of multiple events checking if start date is in the array first
                        if start_date not in kamar_events:
                            kamar_events[start_date] = []
                        kamar_events[start_date].append(event)
            
        #if the try fails then display the error            
        except Exception as e:
            return f"sorry there was an error:{str(e)}"        
        
        #get tomorrow's events and if there is no event create a default event saying there are no events
        tomorrow_events = kamar_events.get(tomorrow_date,[{'summary':'nothing on your calendar'}])
        
        #get the reminder data and pass that
        reminder = getreminder()

        #pass the data back to kamar page from API to display for user
        data = {
            'student_id':kamar_id,
            'period1_subject':period1_subject,
            'period1_teacher':period1_teacher,
            'period1_room':period1_room,
            'inspirational_message':'Do or do not, there is no try - Yoda',
            'events':tomorrow_events,
            'reminder':reminder
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

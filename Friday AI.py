from gtts import gTTS
import time
from pygame import mixer
import speech_recognition as sr
import wikipedia
import geocoder
import pycountry
import yt_search
import datetime
import psutil
import smtplib
import webbrowser
import phonenumbers
import cbpy as cb
import bs4 
from bs4 import BeautifulSoup
import requests
import pyowm
from phone_iso3166.country import phone_country
mixer.init()
news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()
soup_page = soup(xml_page, "xml")
client = wolframalpha.Client('GTAT38-RTR7PG4P53')
print("Initializing FRIDAY AI")
news_list=soup_page.findAll("item")
owm = pyowm.OWM('f3852ccaeb3a2b265ccc22185e27367d')
city = 'Bengaluru'
loc = owm.weather_at_place(city)
weather = loc.get_weather()
#temperature
temperature = weather.get_temperature(unit='celsius')
humidity = weather.get_humidity()
wind = weather.get_wind()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.pause_threshold=1
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Searching..")
        query = r.recognize_google(audio,language='en-IN')
        print("User said: "+query)
    except:
        return "None"
    return query
def pauseListen():
    r = sr.Microphone()
    with sr.Microphone as source:
        print(" Listening paused...")
        audio = r.pause_threshold = 1
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Searching..")
        query = r.recognize_google(audio,language = 'en-IN')
        print("User said: "+query)
    except:
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir   ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir  ")   
    else:
        speak("Good Evening Sir   ") 

def speak(text):
    obj = gTTS(text,lang='en-US',slow=False)
    obj.save('/home/pi/welcome.mp3')
    mixer.music.load('/home/pi/welcome.mp3')
    mixer.music.play()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('moderngaming2588@gmail.com' , 'Lohith01')
    server.sendmail('moderngaming2588@gmail.com' ,to ,content)
    server.close()
    
speak("FRIDAY AI bootup  Successful")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'hello' in query.lower() or 'hi ' in query.lower():
            speak("Hello Boss Its so good to see you")
            
        elif 'wikipedia' in query.lower() or "Wikipedia" in query.lower():
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","") or query.replace("Wikipedia","")
            res = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(res)
            speak(res)
                
        elif 'abort' in query.lower() or 'stop' in query.lower() or 'goodbye' in query.lower() or 'deactivate' in query.lower() or 'kill' in query.lower():
            speak("Okay sir") 
            speak("Powering off systems...")
            sor = ['Farewell sir', 'Goodbye sir',]
            speak(random.choice(sor))
            sys.exit()

        elif 'what is the humidity' in query.lower() or 'humid' in query.lower() or 'humidity' in query.lower():
            print(f"Sir,,the humidity is {humidity} percent")
            speak(f"Sir,,the humidity is {humidity} percent")
            if humidity<50:
                speak("Sir,,the humidity is low ,, and so it\'s dry")
            else:
                speak("Sir,,the humidity is high,,so it\'s very humid or wet")

        elif 'where are we' in query.lower() or 'locate ' in query.lower() or 'geolocation ' in query.lower():
            g = geocoder.ip('me')
            geoloc = g.latlng
            speak(f"Our current Latitudes and Longitudes are {geoloc}!!") 
            speak("Location match successful!!")
            geocity = g.city
            speak(f"Sir..we are in {geocity}!!")

        elif 'caller' in query.lower() and 'id' in query.lower() or 'ID' in query.lower() or 'Id' in query.lower():
            speak("Initiating Caller ID Interface")
            time.sleep(1.5)
            speak("Please enter the Phone Number ")
            cell = input("Phone Number :")
            z = phonenumbers.parse(cell,None)
            posble = phonenumbers.is_possible_number(z)
            if posble==True:
                speak("Sir I believe its an Active phone number")
            else:
                speak("Sir I believe this is an Invalid Phone Number")
            phone_country(cell)
            c = pycountry.countries.get(alpha_2=phone_country(cell))
            speak(f"Boss")
            time.sleep(0.50)
            speak(f"Its an {c.name}n number") 
            ro_number = phonenumbers.parse(cell,"RO")
            print(carrier.name_for_number(ro_number, "en"))
            speak(carrier.name_for_number(ro_number, "en"))
            print(geocell.PhoneNumberOfflineGeocoder(cell, "en"))
            speak(geocell.PhoneNumberOfflineGeocoder(cell, "en"))

        elif 'google flights' in query.lower() or 'open flight website' in query.lower():
            speak("Okay Sir ")
            time.sleep(0.50)
            speak("Opening Google Flights")
            webbrowser.open("https://www.google.com/flights?q=flights&sxsrf=ALeKk00WcIRzqVvD5bIrgjbsEvz0OjVgPA:1588514303267&source=lnms&impression_in_search=true&mode_promoted=true&tbm=flm&sa=X&ved=2ahUKEwj985D27JfpAhW-gUsFHfYzDRcQ_AUoAXoECA4QAw#flt=BLR..2020-05-19*.BLR.2020-05-23;c:INR;e:1;sd:1;t:h")

        elif 'tell jokes' in query.lower() or 'tell me some jokes' in query.lower() or 'say jokes' in query.lower() or 'make some jokes' in query.lower() or 'crack some jokes' in query.lower():
            jokeM = ['Why can\'t astronauts eat popsicles........Because in space, no one can hear the ice cream truck','What\'s the first thing a monster eats after he\'s had his teeth checked....the answer is The Dentist','Write an essay on cricket on ......the teacher told the class..,,,,,,,,,Chintu finishes his work in 5 minutes..,,,,,,,,,,,,The teacher is impressed,,,,,,,,,,..she asks Chintu to read his essay out loud for everyone...,,,,,,,Chintu reads...,,,,The cricket match is cancelled due to rain']
            speak(random.choice(jokeM))
            speak("Ha Ha Ha Ha") 
            print("Ha..Ha..Ha..Ha")

        elif 'time' in query.lower() and 'what\'s' in query.lower() or 'what' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            olo = (strTime)[0]
            print(olo)   
            speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query.lower() or 'thanks' in query.lower():
            speak("You're welcome")
            time.sleep(0.25)
            speak("My pleasure Boss")

        elif 'youtube videos' in query.lower() or 'Youtube videos' in query.lower() or 'youtube' in query.lower() or 'Youtube' in query.lower() or 'YouTube' in query.lower():
            speak("Well  what would you like to watch Sir")
            query = takeCommand()
            speak("Excellent Choice Boss")
            te = query
            yt = yt_search.build("AIzaSyCtWMxKG8NA3LGEa5YALIURupE_lAIPa_4")
            search_result = yt.search(te, sMax=1, sType=["video"])
            ytname = search_result.title
            ytchnl = search_result.channelTitle
            ytid = search_result.videoId
            def listToString(s):
                str1 = " "
                return (str1.join(s))
            s = ytid
            ytid = listToString(s)
            speak(f"Playing {ytname} by {ytchnl}")
            ytlink = "https://www.youtube.com/watch?v="
            webbrowser.open(ytlink+ytid)

        elif 'date' in query.lower() or 'today\'s date' in query.lower():
            strTime = datetime.datetime.now().strftime("Today's date is %d %m %y20")
            print(strTime)
            speak(strTime)
        
        elif 'who are you' in query.lower():
            speak("I am Friday , your very own A I assistant")

        elif 'meet' in query.lower():
            query = query.replace("meet"," ")
            nm = query
            speak("Nice to meet you " +nm)

        elif 'news' in query.lower():
            speak("okay sir, here are the latest news from Google News")
            for news in news_list:
                print(news.title.text[5])
                print(news.pubDate.text[5])
                print("-"*60)
                speak(news.title.text[5])

        elif 'quote of the day' in query.lower() or 'quote' in query.lower():
            res=requests.get("https://www.brainyquote.com/quote_of_the_day")
            soup=BeautifulSoup(res.text,'lxml')
            image_quote = soup.find('img', {'class':'p-qotd'})
            print(image_quote['alt'])   
            speak(image_quote['alt'])
        
        elif 'remember' in query.lower() or 'keep in mind' in query.lower():
            query = query.replace("remember", " ") 
            rem = query
            speak("Okay sir..I will that in mind  "+rem)

        elif 'remind' in query.lower():
            speak("You asked me to remember "+rem)

        elif 'how are you' in query.lower() or 'are you ok' in query.lower() or 'are you okay' in query.lower() or 'are you fine' in query.lower() or ' how you doing ' in query.lower():
            slo = ['I\'m fine thank you sir','Oh,,I\'m all well sir']
            speak(random.choice(slo)) 
            
        elif 'images' in query.lower() or 'image' in query.lower() or 'image recognition protocol' in query.lower():
            speak("Initiating Image Recognition Protocol ")
            sp = 'What are you looking for Sir '
            speak(sp)
            query = takeCommand()
            tabUrl = "https://www.google.com/search?q="
            taborl = "+&tbm=isch&ved=2ahUKEwjqmf2J08zpAhX4K7cAHeRPC1UQ2-cCegQIABAA&oq=star+&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQE1CUMli7N2COQGgAcAB4AIABwwSIAccIkgEJMC4yLjEuNS0xmAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=b3zKXqqmKvjX3LUP5J-tqAU&bih=635&biw=1366"
            webbrowser.open(tabUrl+query+taborl)
            
        elif 'online' in query.lower():
            speak("I am indeed Online Boss ")

        elif 'live score' in query.lower():
            p = cb.plivescore(2)
            print(p)
            speak(p)
        
        elif 'upcoming matches' in query.lower():
            y = cb.gmatchlist()
            for x in y:
                print(x)
                speak(x)

        elif 'did it work' in query.lower():
            speak("Oh   I think it worked pretty great sir")

        elif 'you there' in query.lower():
            speak("Yes sir for you      always")
        elif 'find my phone' in query.lower():
            speak("Phone Locater Mode Turned On..Sir!!")
            speak("Searching for your phone!!")
            account_sid = 'AC56c485a3d96c35c6b7710270f2f0660f'
            auth_token = '09099db01cb770a3d4847cb2a2581c6c'
            client = TwilioRestClient(account_sid, auth_token)
            call = client.calls.create(
                        #twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+919480255502',
                        from_='+12513571461',
                        url="http://static.fullstackpython.com/phone-calls-python.xml", method="GET")
        elif 'calculate' in query.lower():
            query = query.lower()
            res = client.query(query)
            speak("Searching for Results ")
            results = next(res.results).text
            speak("Results Found ")
            print(results)
            speak(results) 
        elif 'what can you do' in query.lower():
            speak("I can assist you in the following jobs sir")
            speak("I can search things on Google")
            speak("I can tell you Weather Forecasts")
            speak("I can play Youtube Videos")
            speak("I can open plenty of websites")
            speak("I can toss the coin for you")
            speak("I can open plenty of apps")
            speak("I can set alarms")
            speak("I can send E mails")
            speak("I can play songs")
            speak("I can even make you laugh sir")
            speak("I can also recognize several faces sir")
            speak("I can spell words for you  ")
            speak("I can tell you horoscopes ")
            speak("I can control your TV too sir")
            speak("Well that\'s all I can do right now sir ")

        elif 'good morning' in query.lower():
            speak("Good Morning sir")

        elif 'good evening' in query.lower():
            speak("Good Evening sir")

        elif 'good afternoon' in query.lower():
            speak("Good afternoon sir")

        elif 'good night' in query.lower():
            speak("Good Night sir Sweet Dreams ")

        elif 'i am back' in query.lower() or 'i\'m back' in query.lower() or 'home' in query.lower():
            speak("Welcome Back sir ")
        
        elif 'will it rain' in query.lower() or 'umbrella' in query.lower() or 'raincoat' in query.lower():
            loc = owm.three_hours_forecast(city)
            clouds = str(loc.will_have_clouds())
            rain = str(loc.will_have_rain())  
            print(rain)
            print(clouds) 
            if rain == 'True':
                print("Yes sir...According to the weather reports it looks like it will rain today")
                speak("Yes sir      According to the weather reports it looks like it will rain today")
                print("I suggest you carry an umbrella..in case it rains today")
                speak("I suggest you carry an umbrella in case it rains today")

            elif rain == 'False':
                print("No Sir, according to the weather reports it doesn\'t look like it will rain today")
                speak("No Sir  according to the weather reports it doesnt look like it will rain today ")
                print("............Sir I don\'t think  you should carry an umbrella..because it is clear outside")
                speak("     Sir I don\'t think  you should carry an umbrella..because it is clear outside")

            if clouds == 'True' and rain == 'True':
                print("Moreover sir it is very cloudy today")
                speak("Moreover sir it is very cloudy today")
              
            elif clouds == 'True' and rain == 'False':
                print("But sir even though it won\'t rain today....It is very cloudy outside")
                speak("But sir even though it wont rain today     It is very cloudy outside")    

        elif 'dice ' in query.lower():
            playsound()
            sm = ['One','Two','Three','Four','Five','Six']
            spf = random.choice(sm)
            speak(f"The Dice is rolled and it is {spf}")

        elif 'google ' in query.lower():
            new = 2
            tabUrl = "https://google.com/?#q="
            speak("What are you looking for Sir!!")
            term = takeCommand()
            webbrowser.open(tabUrl+term,new=new)

        elif 'trust ' in query.lower() or 'believe' in query.lower():
            speak("I trust you sir kind of like Trust the Force Luke")

        elif 'quote of the day' in query.lower() or 'quote' in query.lower():
            res=requests.get("https://www.brainyquote.com/quote_of_the_day")
            soup=BeautifulSoup(res.text,'lxml')
            image_quote = soup.find('img', {'class':'p-qotd'})
            print(image_quote['alt'])   
            speak(image_quote['alt'])
            
        elif ' pause 'in query.lower() or ' hold ' in query.lower():
            speak("Okay Boss ")
            speak("SWitching to Auxillary Listening Mode ")
            listen = False
            while listen==False:
                que = pauseListen()
                if 'jarvis' in query.lower() or 'friday' in query.lower() or 'edith' in query.lower():
                    speak("Listening Mode Online")
                    listen = True
                    break
                else:
                    time.sleep(1)
        elif 'send email' in query.lower() or 'email' in query.lower():
            speak("Okay Sir")
            print("OKay Boss")
            time.sleep(0.50)
            speak("Initiating Email Interface")
            time.sleep(1.5)
            speak("What should be the content of E Mail Boss")
            print("Content Boss??")
            content = takeCommand()
            to = "moderngaming2588@gmail.com"
            sendEmail(to,content)
            speak("Email Sent Successfully  boss")
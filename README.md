<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
<h2>Time Server</h2>

<p>A Simple <b><a href="https://flask.palletsprojects.com/" target="_blank">Flask</a></b> Time Server To Get Realtime Time Information Without Any Third Party API</p>

<p>
<h2>Features</h2>

<ul>
  <li>Highly Customizable</li>
  <li>Get Comprehensive List Of Time Data Such As
    <ul>
    <li>Miliseconds</li>
    <li>Seconds</li>
    <li>Minutes</li>
    <li>Hour</li>
    <li>Day</li>
    <li>Month</li>
    <li>Year</li>
    <li>Date & Many More</li>
    </ul>
  </li>
  <li>Can Be Easily Integrated With Android, Web & Any Project With Simple HTTP Request.</li>
</ul>

 <h2>Running</h2>

To Get Started With Time Server On Your Local Machine Follow This Simple Steps One By One To Get Up & Running.

Make Sure You Have <b><a href="https://git-scm.com/" target="_blank">Git</a></b> & <b><a href="https://python.org" target="_blank">Python</a></b> Installed On Your Machine.

```
git --version
```

```
python --version
```

Clone The Repository

```
git clone https://github.com/BirukBelihu/TimeServer.git
```

Go Inside The Project

```
cd TimeServer
```

Install Required Dependencies

```
pip install -r requirements.txt
```

Start The Server

```
python main.py
```

Sample Request Using <b><a href="https://curl.se/" target="_blank">cURL</a></b> Or <b><a href="https://www.postman.com/" target="_blank">Postman</a></b>

```
curl http://IP_ADDRESS:PORT/api/time/current/zone?timeZone=Africa/Addis_Ababa
```

Response

```
{
  "date": "03/04/2025",
  "dateTime": "2025-04-03T19:52:05.599935+03:00",
  "day": 3,
  "dayOfWeek": "Thursday",
  "dstActive": false,
  "hour": 19,
  "milliSeconds": 599,
  "minute": 52,
  "month": 4,
  "seconds": 5,
  "time": "19:52",
  "timeZone": "Africa/Addis_Ababa",
  "year": 2025
}
```

Get All The Available Time Zones

```
curl http://IP_ADDRESS:PORT/api/time/current/zone/timeZones
```

Response

```
[
    "Africa/Abidjan",
    "Africa/Accra",
    "Africa/Addis_Ababa",
    "Africa/Algiers",
    "Africa/Asmara",
    "Africa/Asmera",
    "Africa/Bamako",
    "Africa/Bangui",
    "Africa/Banjul",
    ...
]
```
</p>

<h2>Social Media Pages</h2>

If You Want Android App Development Tutorials & Projects Check My Social Media Pages.

<b>Telegram</b> :- https://t.me/androiddevstutorial

<b>YouTube</b> :- https://youtube.com/@AndroidDevsTutorials

<b>Blogger</b> :- https://androiddevelopersb.blogspot.com

<b>WhatsApp</b> :- https://whatsapp.com/channel/0029VaXEKtjJ3jv1OrvgOA3K

<b>LinkTree</b> :-
https://linktr.ee/androiddeveloperspage

<h2>Support</h2>
<a href="https://www.buymeacoffee.com/birukbelihu" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;"></a>
 </body>
 </html>		



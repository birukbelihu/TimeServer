<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>

![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/TimeServer)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/TimeServer)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/TimeServer)
![GitHub license](https://img.shields.io/github/license/BirukBelihu/TimeServer)

<h2>Time Server</h2>

<p>A Simple <b><a href="https://flask.palletsprojects.com/" target="_blank">Flask</a></b> Time Server To Get Realtime Time Information Without Any Third Party API</p>

<p>
<h2>Features</h2>

<ul>
  <li>Highly Customizable</li>
  <li>Get Comprehensive List Of Time Data Such As
    <ul>
    <li>Milliseconds</li>
    <li>Seconds</li>
    <li>Minutes</li>
    <li>Hour</li>
    <li>Day</li>
    <li>Month</li>
    <li>Year</li>
    <li>Date & Many More</li>
    </ul>
  </li>
  <li>Supports 500+ World Time Zones</li>
  <li>Can Be Easily Integrated With Android, Web & Any Project With A Simple HTTP Request.</li>
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

Start The Time Server

```
python main.py
```

If You're Calling The API From External Clients(Android Or Web) Don't Forget To Expose The Port Using <a href="https://ngrok.com" target="_blank">Ngrok</a>.

```
ngrok http 5000
```

<b>N.B</b> Replace 5000 With Your Own PORT If You're Using Different Port Number. 

Sample Request Using <b><a href="https://curl.se/" target="_blank">cURL</a></b>

```
curl http://IP_ADDRESS:PORT/api/v1/time/current/zone?timeZone=Africa/Addis_Ababa
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
curl http://IP_ADDRESS:PORT/api/v1/time/current/zone/timeZones
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

Get Server Status

```
 http://IP_ADDRESS:PORT/api/v1/status
```

Run Tests Using Pytest

```
pytest test_server.py
```

To Run TimeServer In <a href="https://www.docker.com/" target="_blank">Docker</a> Container Follow This Steps.

Build Docker Image

```
docker build -t timeserver .
```

Run The Server

```
docker run -p 5000:5000 timeserver
```

The Rest Of The Steps Are Same
</p>

<h2>Social Media Pages</h2>

If You Want Python Tutorials Check My Social Media Pages.

<b>Telegram</b> :- 
https://t.me/pythondevstutorials

<b>YouTube</b> :- 
https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.
 </body>
 </html>		



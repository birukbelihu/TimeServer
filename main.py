from datetime import datetime, timedelta

import pytz
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("get_current_time"))


@app.route("/api/time/current/zone", methods=["GET", "POST"])
def get_current_time():
    time_zone = request.args.get("timeZone", "Africa/Addis_Ababa")

    try:
        timezone = pytz.timezone(time_zone)
    except pytz.UnknownTimeZoneError:
        return {"error": "Unknown Time Zone Provided"}

    current_time = datetime.now(timezone)

    response = {
        "year": current_time.year,
        "month": current_time.month,
        "day": current_time.day,
        "hour": current_time.hour,
        "minute": current_time.minute,
        "seconds": current_time.second,
        "milliSeconds": current_time.microsecond // 1000,
        "dateTime": current_time.isoformat(),
        "date": current_time.strftime("%d/%m/%Y"),
        "time": current_time.strftime("%H:%M"),
        "timeZone": str(timezone),
        "dayOfWeek": current_time.strftime("%A"),
        "dstActive": timedelta(0) != current_time.dst()
    }
    return jsonify(response)


@app.route("/api/time/current/zone/timeZones", methods=["GET", "POST"])
def get_available_time_zones():
    return jsonify(pytz.all_timezones)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

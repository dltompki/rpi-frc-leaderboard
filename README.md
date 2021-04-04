# rpi-frc-leaderboard

![](https://i.imgur.com/ae3k7yy.jpg)![](https://i.imgur.com/TmYF2Qw.jpg)

### [Event Data provided by FIRST](https://frc-events.firstinspires.org/services/API)

Using a Raspberry Pi 4B and the FIRST FRC Events API to display live stats for my team on a 16x2 LCD display.

## Materials

- Raspberry Pi 4 Model B and Power Adapter

- Pi Cobbler

- 10K potentiometer

- LCD Display

- some wires and a breadboard

## Dependencies

- [requests](https://docs.python-requests.org/en/master/)

- [base64](https://docs.python.org/3/library/base64.html)

- [adafruit-circuitpython-charlcd](https://github.com/adafruit/Adafruit_CircuitPython_CharLCD)

## Process

1. I used [this Adafruit tutorial](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi) to learn how to interface between python code on the Pi and the LCD display (wiring and LCD python package).

2. I then discovered the [FRC API](https://frc-events.firstinspires.org/services/API) (I had originally planned to web scrape the leader board website), registered, and used [this API documentation page](https://frc-api-docs.firstinspires.org) for reference throughout the project (make sure you change to "Python - Requests" at the top of the page for more useful examples).

3. I used the [`requests` python package](https://docs.python-requests.org/en/master/) to send `GET` requests to the API.

4. The API requires you to encode your authentication information in base 64. For that, I used the [`base64` python package](https://docs.python.org/3/library/base64.html) and [this tutorial](https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/).

5. Since I wanted to publish this project online, I couldn't include my authentication information in my code. Instead, I stored this information in global variables inside a separate file called `creds.py`. I then imported that file where I actually wanted to use that data. When it came time to commit, I added this file to my `.gitgnore`.

6. Once I finally got authentication working, the response was the below. I had to learn a little bit about python data structures in order to parse this (you can see how I did it in `frc_api.py` in the `update()` and `getData()` functions).
   
   ```python
   {"Rankings":[{"rank":6,"teamNumber":1591,"sortOrder1":269.53,"sortOrder2":70.00,"sortOrder3":91.61,"sortOrder4":107.92,"sortOrder5":0.00,"sortOrder6":62.50,"wins":0,"losses":0,"ties":0,"qualAverage":0.00,"dq":0,"matchesPlayed":0}]}
   ```

7. After getting the data in a more workable form, I designed how I wanted to display it on the LCD. Make sure to use a newline character `\n` to display text on the second row of the display. I wanted to use a `switch` statement for this (I have a mainly Java background) but python doesn't have one, so I used [this tutorial](https://jaxenter.com/implement-switch-case-statement-python-138315.html) to emulate a `switch`.

8. I developed this code on my (Arch Linux) desktop, so now I needed to deploy it to the Pi. I started with a brand new installation of Raspberry Pi OS, except that I [enabled `ssh` on my desktop](https://www.raspberrypi.org/documentation/remote-access/ssh/). This allowed me to operate the Pi headless (without a monitor plugged in). I was able to `ssh` into the Pi without knowing its IP address by [using mDNS](https://www.raspberrypi.org/documentation/remote-access/ip-address.md), which allows you to use `hostname.local` instead. My PC did not support mDNS by default, so I had to install it. 

9. I then [used `scp`](https://stackabuse.com/copying-a-directory-with-scp/) to copy my python code to the Pi. I could have used git at this point as well, but I didn't want to have to commit every time I wanted to test on the Pi.

10. In order to leave this running without having to leave the ssh terminal open on my desktop, I learned [how to use `disown`](https://www.cyberciti.biz/faq/unix-linux-disown-command-examples-usage-syntax/).

## Conclusion

This was a fun and relatively useful project that took me one day to actually make and another day to document here (tip: your browser history is a very useful breadcrumb trail if you didn't take notes during the process). I didn't know that vast majority of the knowledge I needed to accomplish this before I started. I have a love-hate relationship with python, but I will certainly use it in the future. It will be a lot of fun to leave this running on my desk up until the FRC 2021 Skills Challenge deadline to have live updates on how my team's scores stack up.

## Want to use this for yourself?

As long as you have the physical materials, there are minimal changes one would need to make to use it for their own team, on their own desk. First, register for the FRC API [here](https://frc-events.firstinspires.org/services/API). Then, fork this repository and create your own `creds.py` file at `rpi-frc-leaderboard/creds.py`. Your file should look something like this:

```python
# get this info from the email you got from FMS Developer when you registered for the API
user = 'your-username'
passwd = 'your-auth-token'
```

Then, you'll need to change the `url` in `frc_api.py`. The format is:

```python
url = 'https://frc-api.firstinspires.org/v2.0/YEAR/rankings/EVENT_CODE?teamNumber=TEAM_NUMBER'
```

Replace what's in CAPS. To find your event code, go to `https://frc-events.firstinspires.org/2021/team/TEAM_NUMBER`.  There are tabs at the bottom which have the event codes on them. There's probably multiple of them, so use this link `https://frc-events.firstinspires.org/2021/EVENT_CODE/rankings` to check them. In my case, I wanted the skills challenge one, which ended up being `IRHKR` for my team.

Then deploy the code to your Pi (if you didn't do the whole process on the Pi already) either like I did in steps 8-10, or just use git. Make sure you have all the dependencies installed using `pip` and then run `lcd_out.py`.

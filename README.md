# project_What
To automate task of sending and receiving messages on whatsapp-web using selenium.

This project was done during my intership at Cleveron Techworks Pvt. Ltd.

Here I tried to make api's through which one can communicate to a headless browser to send and recieve messages on whatsapp web.
Ultimate goal was to utilize these api's and deploy a bot which can hold conversation with the user via whatsapp.

## Installation

selenium for python can be installed using pip

```bash
pip install selenium
```

geckodriver can be found [here](https://github.com/mozilla/geckodriver/releases)

clone this repo to your project
```bash
git clone https://github.com/TubbyStubby/project_What/
```
or download as zip and unzip it

## Usage

```python

import wat0 as wat

#initializing and fetching qr code for scanning
browser = start()
getQr(browser)

#searching and selecting contact
namae = input('Enter contact name: ').lower()
sNS(namae, browser)

#printing last sent, recieved messages
print('last sent: ',lastSent(browser))
print('last recieved: ',lastRcvd(browser))

#sending message
sendMsg('new test',browser)
print('last sent: ',lastSent(browser))

#sending integers after getting an answer. Why not?
i=1
while True:
    l = lastRcvd(browser)
    print('main:',l)
    s = untilNew(browser,l) #stops the execution until new message is received
    sendMsg(str(i),browser)
    i+=1

#closing the browser instance
quit(browser)

```
watbot_fun.py has integration of these functions with a small word matching chatbot.

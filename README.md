# google-dork-script

Inspired by [https://dorks.faisalahmed.me/](https://dorks.faisalahmed.me/) made a dork syntax for bug hunting to some specific hosts on the internet. I created a python script so it would be easier to scan all the dork in one command. The only reason why I did this is because I want to know whether the dork gives a response or not when do googling, then I still checking manualy on the internet but just from works dork so it still make me easier.

You can add your custom query in `query_list` at the source code

The log activity will be stored in `googling_log.txt`

## Installation

```
pip install beautifulsoup4
pip install google
```

## Usage

```
python google_dork_script.py -h
python google_dork_script.py DOMAIN
python google_dork_script.py example.com
```

## PS

If there there is some error like `Error occurred while processing query {number}: HTTP Error 429: Too Many Requests`, it maybe the request get detected as Too Many Requests by google search, just wait for a moment and try again :')

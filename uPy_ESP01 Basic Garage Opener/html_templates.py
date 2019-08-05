


# Ram on the esp8266 is limited, so we remove all formating as spaces take up ram.
# Once I had the html I wanted, I went through and removed all formatting that I did not need.
# Place your html page templates below as a function returning a string
import css_templates

def home(door_state):
  home_page_p1 = """<html><head><title>Garage Door WIFI Remote Opener</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>"""
  home_page_p2= """</style></head><body><div id="main_div"><h1>Garage Door<br>WIFI Opener</h1><p>Door is: """
  home_page_p3 = """</p><p><button id="send_hash" style="width:318px;"class="button" onclick="window.location.href = '/toggle/';">OPEN or CLOSE<br>GARAGE DOOR</button></p></div></body></html>"""
  return home_page_p1 + css_templates.standard() + home_page_p2 + door_state + home_page_p3









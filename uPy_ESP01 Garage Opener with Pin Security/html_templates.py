
# Ram on the esp8266 is limited, so we remove all formating as spaces take up ram.
# Once I had the html I wanted, I went through and removed all formatting that I did not need.

# Place your html page templates below as a function returning a string
import js_templates
import css_templates

def home(door_state, session_pin):
  home_page_p1 = """<html><head><title>Garage Door WIFI Remote Opener</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>"""
  home_page_p2= """</style></head><body><div id="main_div"><h1>Garage Door<br>WIFI Opener</h1><p>Door is: """
  home_page_p3= """</p><p>Session Pin: <b><span id="sessionpin">"""
  home_page_p4 = """</span></b></p><p>Security Pin:<br><input maxlength="4" pattern="\d{4}" required autofocus="autofocus" id="securitypin" type="number" name="securitypin" value=""></p><p><button id="send_hash" style="width:318px;"class="button">OPEN or CLOSE<br>GARAGE DOOR</button></p></div><script>"""  
  home_page_p5 = """</script></body></html>"""
  return home_page_p1 + css_templates.standard() + home_page_p2 + door_state + home_page_p3 + session_pin + home_page_p4 + js_templates.sha256() + home_page_p5






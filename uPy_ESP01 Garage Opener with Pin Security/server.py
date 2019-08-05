

import socket
import html_templates
import utime
import gc
import machine
import uhashlib
import ubinascii
import network
import os



def open_close_door(door_state):
  relay = machine.Pin(0, machine.Pin.OUT)
  relay.on()
  utime.sleep(0.3)
  relay.off()
  print('Door Opened / Closed')
  if door_state == "CLOSED":
    door_state = "OPEN"
  else:
    door_state = "CLOSED"
  gc.collect()
  return door_state


def web_serv():
  # Initial Door state on start / restart / crash recover
  door_state = "CLOSED"
  # 80 is the default http port, however changing this to something more obscure could help security some.
  serv_port = 80 
  # Defaul input field is wide enough for 8 digits, if you need more change the width in css sheet, I don't know the limit.
  security_pin = "0359" # 4 - 8 chars by default

  pin_hash_cache =[]

  door = machine.Pin(0, machine.Pin.OUT)

  wlan = network.WLAN(network.STA_IF)

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(4)
  s.bind(('', serv_port))
  s.listen(2)



  network_check_counter = 0
  while True:
    network_check_counter += 1
    if network_check_counter > 10:
      network_check_counter = 0
      if not wlan.isconnected():
        machine.reset()
      
    try:
      gc.collect()
      while len(pin_hash_cache) > 2:
        pin_hash_cache.pop(0)
      conn, addr = s.accept() 
      request = str(conn.recv(1024))
      # You could change the random function to pull out a longer string of digits for a longer pin.
      # This could be more secure since an attacker wouldn't know the length of the pin used for hashing.
      session_pin = str(int.from_bytes(os.urandom(5), 'big'))[:5]
      new_hash = uhashlib.sha256(session_pin + security_pin)
      # Will grab 8 characters of the hash, which should be good enough security wise. And easier on memory.
      # If you change this, you will have to change it in the javascript as well went sending back.
      pin_hash_cache.append(str(ubinascii.hexlify(new_hash.digest()))[2:11].replace("'", ""))
      
      for hash in pin_hash_cache:
        if hash in request.split('Referer:')[0]:
          door_state = open_close_door(door_state)
        if "tstate" in request.split('Referer:')[0]:
            if door_state == "CLOSED":
              door_state = "OPEN"
            else:
              door_state = "CLOSED"
      response = html_templates.home(door_state, session_pin)
   
      conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
      conn.sendall(response)
      conn.close()
      
    except Exception as e:
      if 'ETIMEDOUT' not in str(e): #Timeouts are normal and seem to resolve buggy connections.
        print("Warning: ", e, '\nfree ram: ', gc.mem_free())

      









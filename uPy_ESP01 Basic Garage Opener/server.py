

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
      conn, addr = s.accept() 
      request = str(conn.recv(1024))
      if "toggle" in request.split('Referer:')[0]:
        door_state = open_close_door(door_state)
      if "tstate" in request.split('Referer:')[0]:
          if door_state == "CLOSED":
            door_state = "OPEN"
          else:
            door_state = "CLOSED"
      response = html_templates.home(door_state)
   
      conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n")
      conn.sendall(response)
      conn.close()
      
    except Exception as e:
      if 'ETIMEDOUT' not in str(e): #Timeouts are normal and seem to resolve buggy connections.
        print("Warning: ", e, '\nfree ram: ', gc.mem_free())

      












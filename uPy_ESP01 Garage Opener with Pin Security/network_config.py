

import network
import utime

#The ESP has the ap enabled by default, disabling it will save a little memory.
def ap_disconnect(): 
  ap_if = network.WLAN(network.AP_IF)
  ap_if.active(False)
  
def sta_connect():
  # Enter your network configuration details below.
  my_network_gateway = '10.0.1.1'
  my_network_subnetmask = '255.255.255.0'
  my_network_dns = '10.0.1.1'
  my_static_ip = '10.0.1.90'
  my_hostname = 'simpleESP-Garage_v2'
  my_wifi_ssid = 'SS-Net-2.4ghz'
  my_wifi_password = 'theundiscoveredcountry'


  wlan = network.WLAN(network.STA_IF)  
  wlan.active(True)
  wlan.config(dhcp_hostname=my_hostname)
  print('Setting Host Name as: {}'.format(my_hostname))

  if not wlan.isconnected():
      print('Connecting to network...')
      wlan.connect(my_wifi_ssid, my_wifi_password)
      while not wlan.isconnected():
          print('Attempting to connect...')
          utime.sleep(1)

  if my_static_ip not in wlan.ifconfig()[0]:
    print('Setting Network Config:')
    wlan.ifconfig((my_static_ip, my_network_subnetmask, my_network_gateway, my_network_dns))
    print(*wlan.ifconfig())
  else:
    print('Current Network Config:')
    print(*wlan.ifconfig())
    
  return my_static_ip










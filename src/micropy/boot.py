#
# <meta:header>
#   <meta:licence>
#     Copyright (C) 2019 by Wizzard Solutions Ltd, ischnura@metagrid.co.uk
#
#     This information is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This information is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   </meta:licence>
# </meta:header>
#
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import uos
import time
import machine
import network
import webrepl

# Reset the Wifi interfaces.
if machine.reset_cause() != machine.SOFT_RESET:
    # Disable the access-point interface.
    network.WLAN(network.AP_IF).active(False)

# Enable the station interface.
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
# Connect to our Wifi network.
if not wifi.isconnected():
    import wifi_cfg
    wifi.connect(
      wifi_cfg.WIFI_SSID,
      wifi_cfg.WIFI_PASS
      )

# save power while waiting
while not wifi.isconnected():
    machine.idle()

# Start the webrepl interface.
webrepl.start()

gc.collect()


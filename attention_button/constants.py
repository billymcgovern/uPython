import secrets
from ucollections import namedtuple

# WIFI
network_wait_time = 10 #time to wait connecting to a network

network_data = namedtuple('network_data', ('id', 'pass'))
wifi_firehouse = network_data('bhvfd-guest', secrets.WIFI_FIREHOUSE)
wifi_tessas = network_data('Snowglobe', secrets.WIFI_TESSAS)
wifi_home = network_data('Willy and Billys Silly Playhouse', secrets.WIFI_HOME)

known_networks = [wifi_tessas, wifi_home, wifi_firehouse]

# END WIFI

# PINS #
LED_GREEN = 2
LED_RED = 17
BUTTON_WAKEUP = 14
BUTTON_WAKEUP_HOLD = 25
# End Pins # 

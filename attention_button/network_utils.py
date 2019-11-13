import network
import constants
import machine
import utime as time

def connect(ssid, password):
    nic = network.WLAN(network.STA_IF)

    if nic.active() and nic.isconnected():
        return True, nic

    network_connect_start_time = time.ticks_ms()

    nic.active(True)
    nic.connect(ssid, password)
    print('Attempting to connect to {}'.format(ssid))

    while True:
        if (network_connect_start_time + constants.network_wait_time*1000) < time.ticks_ms():
            print('Max time waited... Fail')
            return False, nic

        if nic.status() == network.STAT_WRONG_PASSWORD:
            print('Wrong password!')
            break
        elif nic.status() == network.STAT_NO_AP_FOUND:
            print('Wifi point does not exist')
            break
        elif nic.status() == network.STAT_IDLE:
            print('No connection and activity')
            break
        elif nic.status() == network.STAT_ASSOC_FAIL:
            print('Failed to connect')
            break
        elif nic.status() == network.STAT_BEACON_TIMEOUT:
            print('Beacon timeout')
            break
        elif nic.status() == network.STAT_HANDSHAKE_TIMEOUT:
            print('Handshake timeout')
            break
        elif nic.status() == network.STAT_GOT_IP:
            print('Got IP')

        if nic.isconnected():
            return True, nic
        else:
            machine.idle()
            time.sleep_ms(100)

    return False, nic

def connect_any():
    nic = network.WLAN(network.STA_IF)
    if not nic.active():
        nic.active(True)

    available_networks = [ssid for ssid, bssid, channel, RSSI, authmode, hidden in nic.scan()]
    
    for ssid, password in constants.known_networks:
        if not bytes(ssid, 'utf-8') in available_networks:
            continue
        result, nic = connect(ssid, password)
        if result:
            return True, nic
    
    return False, None

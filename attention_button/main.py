import sys
import constants
import network_utils
import utime as time
import urequests
import secrets

from machine import Pin, Timer


def blink_led(led):
    
    def toggle(timer):
        if led.value():
            print('LED on')
            toggle = led.off()
        else:
            print('LED off')
            toggle = led.on()

    timer = Timer(1) 
    timer.init(period=400, callback=toggle) 

    return timer

def send_notification(nic):
    url = secrets.API_URL
    data = {'entity_id': 'script.attention_button'}
    headers= {
        'Authorization': 'Bearer {}'.format(secrets.API_TOKEN), 
        'content-type': 'application/json'}

    print('Attempting to send request...')
    response = urequests.post(url, headers=headers, json=data)
    print('Sent!')

def main():
    led_red = Pin(constants.LED_RED, Pin.OUT)
    led_green = Pin(constants.LED_GREEN, Pin.OUT)

    led_red.on()
    led_green.off()

    result, nic = network_utils.connect_any()
    if result:
        led_green.on()
        led_red.off()

    else:
        return False

    timer = blink_led(led_red) 
    send_notification(nic)
    timer.deinit()

    led_green.off()
    led_red.off()

    return True

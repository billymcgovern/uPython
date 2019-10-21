import sys
import esp32
import machine
import main
import constants
import gc
import micropython

gc.enable()

print('Register wakeup pin')
wake_pin = machine.Pin(constants.BUTTON_WAKEUP, mode=machine.Pin.IN)
esp32.wake_on_ext0(pin=wake_pin, level=esp32.WAKEUP_ANY_HIGH)

print('Register wakeup hold pin')
wake_hold_pin = machine.Pin(constants.BUTTON_WAKEUP_HOLD, mode=machine.Pin.IN)

reset_reason = machine.reset_cause()
print('RESET REASON: {}'.format(reset_reason))
print('HOLD PIN: {}'.format(wake_hold_pin.value()))

wake_reason = machine.wake_reason()
print('WAKE REASON: {}'.format(wake_reason))

if wake_reason == machine.EXT0_WAKE:
    micropython.alloc_emergency_exception_buf(100)
    main.main()
    machine.deepsleep()
elif reset_reason == machine.PWRON_RESET and wake_hold_pin.value() == 1:
    # Holding special button
    print('ENTER HOLD MODE')
    sys.exit(0)
else:
    # Just plain old power on
    print('sleeping')
    machine.deepsleep()

## DONT WRITE ANYTHING UNDER THIS

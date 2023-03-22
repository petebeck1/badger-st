import badger2040
from desktop import desktop

badger2040.system_speed(badger2040.SYSTEM_NORMAL)

display = badger2040.Badger2040()
display.led(128)

desktop(display)
display.update()

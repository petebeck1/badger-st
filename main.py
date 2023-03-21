import badger2040
from desktop import desktop, window, msgbox

badger2040.system_speed(badger2040.SYSTEM_NORMAL)

display = badger2040.Badger2040()
display.led(128)

desktop(display)
window(display, 'Hello', 8, 24, badger2040.WIDTH - 16, badger2040.HEIGHT - 32)
display.update()

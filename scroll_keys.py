from pynput import keyboard
from Quartz.CoreGraphics import (
    CGEventCreateScrollWheelEvent,
    CGEventPost,
    kCGHIDEventTap,
    kCGScrollEventUnitLine
)

def scroll_mac(lines: int):
    event = CGEventCreateScrollWheelEvent(
        None,
        kCGScrollEventUnitLine,
        1,
        lines
    )
    CGEventPost(kCGHIDEventTap, event)

def on_press(key):
    try:
        if key.char == '[':
            scroll_mac(3)
        elif key.char == ']':
            scroll_mac(-3)
    except AttributeError:
        pass  # Ignore special keys

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
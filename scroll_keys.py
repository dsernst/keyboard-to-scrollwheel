from pynput import keyboard
from Quartz.CoreGraphics import (
    CGEventCreateScrollWheelEvent,
    CGEventPost,
    kCGHIDEventTap,
    kCGScrollEventUnitLine
)

scroll_lines = 1

def scroll_mac(lines: int):
    event = CGEventCreateScrollWheelEvent(
        None,
        kCGScrollEventUnitLine,
        1,
        lines
    )
    CGEventPost(kCGHIDEventTap, event)

def on_release(key):
    try:
        if key.char == '[':
            scroll_mac(scroll_lines)
        elif key.char == ']':
            scroll_mac(-scroll_lines)
    except AttributeError:
        pass  # Ignore special keys

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
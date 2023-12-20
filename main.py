import keyboard
import mouse
import time
import random

# Enter the minimum and maximum time for random activation in seconds
min_seconds = 180
max_seconds = 300

print("Press the button you wish to use for anti afk and then press enter")
anti_afk_event = keyboard.record('enter')

# Filter out the 'enter up/down' event from the recorded events
anti_afk_event = [event for event in anti_afk_event if event.name !=
                  'enter']

print(anti_afk_event, "was recorded")
print("Anti afk is now active and will trigger between\n",
      min_seconds, "and", max_seconds, "seconds,\npress ctrl + c to stop")


def loop_play_untill_not_afk():
    counter = 0
    old_mouse_pos = mouse.get_position()
    random_seconds = random.randint(min_seconds, max_seconds)
    while True:
        counter += 1
        if mouse.get_position() != old_mouse_pos:
            break
        time.sleep(1)
        if counter > random_seconds:
            counter = 0
            keyboard.play(anti_afk_event, speed_factor=random.random())


while True:
    loop_play_untill_not_afk()

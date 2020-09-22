import eel
from phue import Bridge
import time

eel.init("Web")

b = Bridge('<Bridge IP Goes Here>')

print("Connecting to bridge")
b.connect()

print("Fetching API dictionary")
b.get_api()

# on html page load
@eel.expose
def get_initial_states():
    states = []
    light = b.get_group('Living Room')
    states.append((light["state"]["all_on"], light["name"]))

    light = b.get_light('Chandelier 1')
    states.append((light["state"]["on"], light["name"], ))
    light = b.get_light('Chandelier 2')
    states.append((light["state"]["on"], light["name"]))
    light = b.get_light('Couch Left')
    states.append((light["state"]["on"], light["name"]))
    light = b.get_light('Couch Right')
    states.append((light["state"]["on"], light["name"]))

    return states

#################### GROUP TOGGLES ####################

@eel.expose
def toggle_all():
    toggle_living_room()
    

@eel.expose
def toggle_living_room():
    light = b.get_group('Living Room')
    print(light)

    if light["state"]['all_on']:
        b.set_group(light['name'], 'on', False)

    if not light["state"]['all_on']:
        b.set_group(light['name'], 'on', True)

    return light["state"]["all_on"], light["name"]

#################### LIGHT TOGGLES ####################

@eel.expose
def toggle_chandelier_1():
    light = b.get_light('Chandelier 1')
    print(light)

    if light["state"]['on']:
        b.set_light(light['name'], 'on', False)

    if not light["state"]['on']:
        b.set_light(light['name'], 'on', True)

    return light["state"]["on"], light["name"]

@eel.expose
def toggle_chandelier_2():
    light = b.get_light('Chandelier 2')
    print(light)

    if light["state"]['on']:
        b.set_light(light['name'], 'on', False)

    if not light["state"]['on']:
        b.set_light(light['name'], 'on', True)

    return light["state"]["on"], light["name"]

@eel.expose
def toggle_couch_left():
    light = b.get_light('Couch Left')
    print(light)

    if light["state"]['on']:
        b.set_light(light['name'], 'on', False)

    if not light["state"]['on']:
        b.set_light(light['name'], 'on', True)

    return light["state"]["on"], light["name"]

@eel.expose
def toggle_couch_right():
    light = b.get_light('Couch Right')
    print(light)

    if light["state"]['on']:
        b.set_light(light['name'], 'on', False)

    if not light["state"]['on']:
        b.set_light(light['name'], 'on', True)

    return light["state"]["on"], light["name"]

#################### CUSTOM ACTIONS ####################

@eel.expose
def strobe_living_room():
    light = b.get_group('Living Room')
    print(light)

    while(True):
        b.set_group(light['name'], 'bri', 254, transitiontime=1)
        break

    return light["state"]["on"], light["name"]

eel.start("index.html")

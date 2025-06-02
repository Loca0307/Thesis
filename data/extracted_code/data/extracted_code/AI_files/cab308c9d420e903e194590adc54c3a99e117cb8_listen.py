    print(hotkeys)
    return hotkeys



# hhh = loadHotkeys()
# hhh["<ctrl>+<alt>+p"]()
# print(hhh)
def addHotkeys(hotkeyDict):

    with keyboard.GlobalHotKeys(
    #     {
    #     "<ctrl>+<alt>+p": lambda: callUserHotkey("python3 /Users/sh/DEV/password-generator/generate-password.py"),
        
    #     "<ctrl>+<alt>+<cmd>+o": lambda: callUserHotkey("python3 /Users/sh/DEV/macroni/scripts/reload.py")
    # }
    hotkeyDict
    ) as h:
        h.join()

addHotkeys(loadHotkeys())
# Attempting to initialise multiple global hotkeys with small dict to fix lamda dict issue
# does not work, only the first executes
def initHotkeys():
    f = open("/Users/sh/DEV/macroni/hotkeys.json", "rt")
    hotkey_string_commands = json.loads(f.read())
    # hotkeys = {}
    for key, value in hotkey_string_commands.items():

        addHotkeys({key: lambda: callUserHotkey(hotkey_string_commands[key])})
    # print(hotkeys)
    f.close()
    # print(hotkeys)
    # return hotkeys
# initHotkeys()
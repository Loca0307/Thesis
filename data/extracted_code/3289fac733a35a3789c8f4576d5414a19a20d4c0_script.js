    // Recall Flag Detection
    // This is used for updating the format when the screen changes, its for responsive design it
    // works by replacing the tabX variable that is given to the function with a backed up version.
    // True: Recall flag passed, replace the value of tabX with tabStored. AKA use the last known value.
    // False: No flag passed, use the current tabX value and update the tabStored value to reflect the current value.
    if(resize == true) {
        console.debug(`Recall flag has been passed, tabStored will not be updated`)
        tabX = tabStored;
    } else {
        tabStored = tabX;
        console.debug(`tabStored update to ${tabStored}`)
    } 

    // Mobile V Desktop format
    // This checks the windows width to detect which format array to use.
    // x > 864: Use the desktopTabs array, AKA use the desktop format.
    // x < 864: Use the mobileTabs array, AKA use the mobile format.
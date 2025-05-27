    
    # Track last update time to periodically check status
    last_update_time = time.time()
    update_interval = 5  # Check for updates every 5 seconds
    
    while not exitRequested:
        current_time = time.time()
        
        # Check button states
        for i, pin in enumerate(button_pins):
            current_state = disp.RPI.digital_read(pin)
            
            # Button press detected (transition from 1 to 0)
            if current_state == 0 and last_button_states[pin] == 1:
                last_button_states[pin] = 0
                
            # Button release detected (transition from 0 to 1)
            elif current_state == 1 and last_button_states[pin] == 0:
                last_button_states[pin] = 1
                
                # Check debounce
                if current_time - last_press_time[pin] > debounce_time:
                    last_press_time[pin] = current_time
                    
                    # Handle button actions
                    if i == 0:  # Mode button
                        print("Changing MODE")
                        switch()
                        updateDisplay(disp)
                    elif i == 1:  # Advanced menu button
                        print("ADVANCED MENU")
                        updateDisplay_Advanced(disp)
                        updateDisplay(disp)
                    elif i == 2:  # OK button
                        print("OK")
                        changeISO_OLED(disp)
                        updateDisplay(disp)
            
            # Update button state
            last_button_states[pin] = current_state
        
        # Handle display updates separately from button presses
        should_update = False
        with update_lock:
            if updateEvent == 1:
                updateEvent = 0
                should_update = True
        
        # Check for periodic updates even if no explicit event
        if current_time - last_update_time > update_interval:
            last_update_time = current_time
            should_update = True
        
        if should_update:
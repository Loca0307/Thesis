        """
        Performs wavelength to angle calibration over a range of temperatures.

        This method calibrates the rotation stage by adjusting the DFB laser temperature,
        measuring the power at different angles, and logging the data.

        Parameters:
        -----------
        dfb : object
            The DFB laser object whose temperature (and therefore wavelength) is controlled.
        powermeter : object
            The powermeter object to measure power.
        temp_list : list of float
            List of temperatures to use for calibration.
        calibration_bounds : tuple
            Bounds for the calibration calculations.
        startangle : float
            The starting angle for the calibration scan.
        endangle : float
            The ending angle for the calibration scan.

        Behavior:
        ---------
        - If `self.ac_begincal` is True:
            - Sets up and moves the stage to the start angle.
            - Waits for the stage to reach the start angle and stops.
            - Sets `self.ac_begincal` to False after initialization.
        - If `self.initcal_bool` is True:
            - Initializes calibration in either low-to-high or high-to-low direction.
            - Scans the stage to the appropriate angle.
            - Emits progress updates.
        - Logs the current time, wavelength, power, and angle to the CSV file while the stage is scanned.
        - Toggles calibration direction and updates progress.
        - When all temperatures are processed, stops the calibration, calculates results, and emits completion signals.

        Example:
        --------
        >>> obj.wavelength_to_angle_calibration(dfb, powermeter, [25.0, 30.0, 35.0], (400, 700), 0, 180)
        """
        def handle_initcal(lowtohi, temp):
            self.init_wavelength_to_angle_calibration(dfb, temp, lowtohi)
            self.stage.scan_to_angle(endangle if lowtohi else startangle, 0.5)
            progress = (self.autocal_iterator + (0.5 if lowtohi else 1)) * 100 / len(temp_list)
            self.autocalibration_progress.emit(int(progress))
            self.initcal_bool = False

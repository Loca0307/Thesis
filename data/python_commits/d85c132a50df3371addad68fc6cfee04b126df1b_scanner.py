    def get_serial_number(self: LeScanner) -> str:
        """Get the serial number of the connected device.

        Returns:
            str: The serial number of the connected device.
        """
        if self._ampcom is None:
            msg = "Scanner not connected"
            raise ScanError(msg)
        return self._ampcom.get_serial_number()

    def get_firmware_version(self: LeScanner) -> str:
        """Get the firmware version of the connected device.

        Returns:
            str: The firmware version of the connected device.
        """
        if self._ampcom is None:
            msg = "Scanner not connected"
            raise ScanError(msg)
        return self._ampcom.get_firmware_version()

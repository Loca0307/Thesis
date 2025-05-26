        if (
            _row["gps_code"] in duplicate_icaos
            and _row["ident"] != _row["gps_code"]
        ):
            logger.info(
                f"ignoring duplicate entry {_row['ident']} for "
                f"{_row['gps_code']} / {_row['iata_code']}."
            )
            continue
        _longitude = float(_row["longitude_deg"])
        _latitude = float(_row["latitude_deg"])
        _timezone = tf.timezone_at(lng=_longitude, lat=_latitude)
        _country = countries[_row["iso_country"]]
        if _timezone is None:
            logger.warning("timezone info unknown: {}".format(_row["gps_code"]))
        _cursor.execute(
            "REPLACE INTO airports(Name, City, Country, IATA, ICAO, Latitude, "
            "Longitude, Altitude, Timezone) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                _row["name"],
                _row["municipality"],
                _country,
                _row["iata_code"],
                _row["gps_code"],
                _latitude,
                _longitude,
                _row["elevation_ft"],
                _timezone,
            ),
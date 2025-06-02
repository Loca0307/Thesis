    public Globals.GenArray<String> getSyncLinkedDevices() {
        Globals.GenArray<String> devicesList = new Globals.GenArray<>();

        // Define the SQL query to retrieve linked devices
        Cursor cursor = db.rawQuery("SELECT linked_devices_id FROM sync WHERE secure_id=?",
                new String[]{
                        secureId
                }
                );

        if (cursor != null) {
            try {
                // Move the cursor to the first row
                if (cursor.moveToFirst()) {
                    do {
                        // Get the linked_devices_id from the cursor
                        String devices_id = cursor.getString(0);

                        // Split the string and add each device to the devicesList
                        String[] devices = devices_id.split(";");
                        for (String device : devices) {
                            devicesList.add(device);
                        }
                    } while (cursor.moveToNext());
                }
            } finally {
                cursor.close(); // Close the cursor when done
            }
        } else {
            Log.e("AccesBdd", "Cursor is null");
        }

        // Remove the last slot (empty space) in the array
        if (!devicesList.isEmpty()) {
            devicesList.popLast();
        }

        return devicesList;
    }


    // GetFileLastVersionId retrieves the last version ID of a file.
    public long GetFileLastVersionId(String path) {
        Cursor cursor = db.rawQuery("SELECT version_id FROM filesystem WHERE path=? AND secure_id=?",
                new String[]{
                        path,
                        secureId
                }
        );

        int version_id = 0;
        if(cursor.moveToFirst()){
            version_id = cursor.getInt(0);
        }

        cursor.close();
        return version_id;
    }


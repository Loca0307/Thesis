    xHWT_log("The plugin has been " + ("enabled" if checked else "disabled"))

# Called every 500ms
def event_loop():
    # Only process items if plugin is enabled
    if not pluginEnabled:
        return

    # get list of items around available for pickup
    items = get_drops()
    # loop through the dictionary items (key-value pairs)
    for item_id, item_data in items.items():
        # check if the item id is in the target item ids list
        current_item_name = item_data['name']
        if current_item_name in target_item_names:
            # pickup the item
            xHWT_log(f"Picking up item: {current_item_name}")
            pickup_item(item_id)
            # Break the loop after picking up the first item
            break

# pickup the item
def pickup_item(item_id):
    # Pack item ID as little-endian unsigned int
    id_bytes = struct.pack('<I', item_id)
    # Create packet: header + first 3 bytes of item_id + trailer
    data = bytearray(b'\x01\x02\x01') + id_bytes[:3] + bytearray(b'\x00')
    inject_joymax(0x7074, data, True)
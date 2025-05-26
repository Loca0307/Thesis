        device = image_rgb.device
        dtype = image_rgb.dtype
        # Move quantization tables to the same device and dtype as input
        # and store it in the local variables created in init
        quantization_table_y = self.quantization_table_y.to(device, dtype)
        quantization_table_c = self.quantization_table_c.to(device, dtype)
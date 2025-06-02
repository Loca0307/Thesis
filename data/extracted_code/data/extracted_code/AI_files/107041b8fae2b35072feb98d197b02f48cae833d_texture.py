    def scale_textures(self) -> None:
        """Resizes all the textures to the map output size."""
        if not self.map.output_size:
            self.logger.debug("No output size defined, skipping scaling.")
            return

        for layer in tqdm(self.layers, desc="Scaling textures", unit="layer"):
            layer_paths = layer.paths(self._weights_dir)
            layer_paths += [layer.path_preview(self._weights_dir)]

            for layer_path in layer_paths:
                if os.path.isfile(layer_path):
                    self.logger.debug("Scaling layer %s.", layer_path)
                    img = cv2.imread(layer_path, cv2.IMREAD_UNCHANGED)
                    img = cv2.resize(
                        img,
                        (self.map.output_size, self.map.output_size),
                        interpolation=cv2.INTER_NEAREST,
                    )
                    cv2.imwrite(layer_path, img)
                else:
                    self.logger.debug("Layer %s not found, skipping scaling.", layer_path)

    waterfall_widget.on_touch_select = [this](int32_t x, int32_t y) {
        if (y > screen_height - screen_height * 0.1) return;  // prevent ghost touch

        frequency_scale.focus();  // focus on frequency scale to show cursor

        if (sampling_rate) {
            // screen x to frequency scale x, NB we need two widgets align
            int32_t cursor_position = x - (screen_width / 2);
            frequency_scale.set_cursor_position(cursor_position);
        }
    };

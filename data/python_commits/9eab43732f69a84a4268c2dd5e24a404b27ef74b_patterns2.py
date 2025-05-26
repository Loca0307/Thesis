
        # add fillet to the corners
        if fillet > 0:            
            left_x_pos = point.x - width / 2
            right_x_pos = point.x + width / 2

            fillet_offset = 1.5
            lower_y_pos = centre_lower_y + lower_trench_height / 2 - fillet * fillet_offset
            top_y_pos = centre_upper_y - upper_trench_height / 2 + fillet * fillet_offset

            lower_left_fillet = FibsemCircleSettings(
                radius=fillet,
                depth=depth/2,
                centre_x=point.x - width / 2,
                centre_y=lower_y_pos,
            )
            lower_right_fillet = FibsemCircleSettings(
                radius=fillet,
                depth=depth/2,
                centre_x=point.x + width / 2,
                centre_y=lower_y_pos,
            )

            # fill the remaining space with rectangles
            lower_left_fill = FibsemRectangleSettings(
                width=fillet,
                height=lower_trench_height - fillet,
                depth=depth,
                centre_x=left_x_pos - fillet / 2,
                centre_y=centre_lower_y - fillet / 2,
                cross_section = cross_section,
                scan_direction="BottomToTop",

            )
            lower_right_fill = FibsemRectangleSettings(
                width=fillet,
                height=lower_trench_height - fillet,
                depth=depth,
                centre_x=right_x_pos + fillet / 2,
                centre_y=centre_lower_y - fillet / 2,
                cross_section = cross_section,
                scan_direction="BottomToTop",
            )

            top_left_fillet = FibsemCircleSettings(
                radius=fillet,
                depth=depth,
                centre_x=point.x - width / 2,
                centre_y=top_y_pos,
            )
            top_right_fillet = FibsemCircleSettings(
                radius=fillet,
                depth=depth,
                centre_x=point.x + width / 2,
                centre_y=top_y_pos,
            )

            top_left_fill = FibsemRectangleSettings(
                width=fillet,
                height=upper_trench_height - fillet,
                depth=depth,
                centre_x=left_x_pos - fillet / 2,
                centre_y=centre_upper_y + fillet / 2,
                cross_section = cross_section,
                scan_direction="TopToBottom",
            )
            top_right_fill = FibsemRectangleSettings(
                width=fillet,
                height=upper_trench_height - fillet,
                depth=depth,
                centre_x=right_x_pos + fillet / 2,
                centre_y=centre_upper_y + fillet / 2,
                cross_section = cross_section,
                scan_direction="TopToBottom",
            )

            self.shapes.extend([lower_left_fill, lower_right_fill, 
                                top_left_fill, top_right_fill, 
                                lower_left_fillet, lower_right_fillet, 
                                top_left_fillet, top_right_fillet])


        # Check row sums (across the x-axis), column sums (y-axis), and pillar sums (z-axis)
        row_sums = values.sum(axis=2)
        col_sums = values.sum(axis=0)
        pillar_sums = values.sum(axis=1)

        # Count conflicts for rows, columns, and pillars
        conflicting += np.sum(row_sums != magic_number)
        conflicting += np.sum(col_sums != magic_number)
        conflicting += np.sum(pillar_sums != magic_number)

        # Space diagonals
        if np.trace(values, axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[::-1], axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, ::-1, :]).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, :, ::-1]).sum() != magic_number:
            conflicting += 1

        # Plane diagonals in xy, yz, and xz planes (forward and reverse)
        for i in range(dim):
            if values[i].diagonal().sum() != magic_number:  # xy-plane
                conflicting += 1
            if values[:, i, :].diagonal().sum() != magic_number:  # yz-plane
                conflicting += 1
            if values[:, :, i].diagonal().sum() != magic_number:  # xz-plane
                conflicting += 1
            if values[i, :, ::-1].diagonal().sum() != magic_number:  # xy-plane, reverse
                conflicting += 1
            if values[:, i, ::-1].diagonal().sum() != magic_number:  # yz-plane, reverse
                conflicting += 1
            if values[::-1, :, i].diagonal().sum() != magic_number:  # xz-plane, reverse
                conflicting += 1

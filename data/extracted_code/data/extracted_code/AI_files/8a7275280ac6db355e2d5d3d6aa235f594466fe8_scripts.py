        if verbose:
            print('%s, %s: %s' % (instanceB.parent_cell, instanceB.parent_cell.parent_cells(), ''))
                        
        def find_parents(layout, target_cell):
            """
            Find all parent cells that instantiate the target cell.
            """
            parents = []
            for cell in layout.each_cell():
                for inst in cell.each_inst():
                    if inst.cell == target_cell:
                        parents.append(cell)
                        break
            return parents

        def trace_hierarchy_up(layout, bottom_cell, path=None):
            """
            Recursively trace the hierarchy upwards from the bottom cell to the top cell.
            """
            if path is None:
                path = [bottom_cell]

            parents = find_parents(layout, bottom_cell)
            if not parents:
                # No parents found, we've reached the top cell
                return [path]

            all_paths = []
            for parent in parents:
                # Recursively trace each parent
                new_path = [parent] + path
                all_paths.extend(trace_hierarchy_up(layout, parent, new_path))

            return all_paths

        def trace_hierarchy_up_single(layout, bottom_cell, path=None):
            """
            Recursively trace the hierarchy upwards from the bottom cell to the top cell.
            Returns a single path as a list of Cell objects.
            """
            if path is None:
                path = [bottom_cell]

            parents = find_parents(layout, bottom_cell)
            if not parents:
                # No parents found, we've reached the top cell
                return path[::-1]  # Reverse the path to start from the top cell

            if len(parents) > 1:
                raise ValueError(f"Cell '{bottom_cell.name}' has multiple parent instances. Use the multi-path version.")

            # If only one parent, continue tracing
            return trace_hierarchy_up_single(layout, parents[0], path + [parents[0]])

        parentsA = trace_hierarchy_up_single(ly, instanceA.parent_cell)
        parentsB = trace_hierarchy_up_single(ly, instanceB.parent_cell)
        if verbose:
            print(" -> ".join(cell.name for cell in parentsA))
            print(" -> ".join(cell.name for cell in parentsB))
    
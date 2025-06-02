            final_data = None

        # Flatten the local data for sending
        sendbuf = local_data.ravel()

        # Determine the MPI datatype corresponding to the numpy dtype.
        # This works for common types (e.g. 'd' for float64, 'i' for int32, etc.).
        mpi_dtype = MPI._typedict[local_data.dtype.char]

        # On root, prepare counts and displacements for Gatherv.
        if rank == 0:
            counts = [r * local_cols for r in all_rows]
            displacements = [sum(counts[:i]) for i in range(len(counts))]
        else:
            counts = None
            displacements = None

        # Use Gatherv to gather the flattened arrays into final_data (also flattened).
        comm.Gatherv(sendbuf, [final_data, counts, displacements, mpi_dtype], root=0)

        comm.Barrier()  # Synchronize processes
        return final_data if rank == 0 else None
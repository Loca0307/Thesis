                interp_data_t = np.linspace(data_t[missing_samples_start_ind], data_t[missing_samples_start_ind+1],
                                            missing_samples)

                # full_data_t = np.linspace(data_t[missing_samples_start_ind], data_t[missing_samples_end_ind],
                #                           missing_samples)
                data_x_interp = cs(interp_data_t)
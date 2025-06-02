
def var_ATE(matching_object, mice_iter=0):
    '''
    This is an EXPERIMENTAL function that implements the variance found in 
    Abadie, Drukker, Herr, and Imbens (The Stata Journal, 2004) assuming
    constant treatment effect and homoscedasticity. Note that the implemented 
    estimator is NOT asymptotically normal and so in particular, 
    asymptotically valid confidence intervals or hypothesis tests cannot be 
    conducted on its basis. In the future, the estimation procedure will be 
    changed.

    Parameters
    ----------
    matching_object : TYPE
        DESCRIPTION.
    mice_iter : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    variance: float
    '''
    validate_matching_obj(matching_object)

    # Compute the sigma^2 estimate from equation 10 in Abadie et al
    # units_per_group is in format [[#,#,#,...], [#,#,#,...],..]
    # Need to double check this, if mice_iter != 0, then possibly need to index
    units_per_group = matching_object.units_per_group
    
    mmgs_dict = all_MGs(matching_object)
    # print(mmgs_dict)
        
    # Compute K_dict, which maps i to KM value
    K_dict = dict.fromkeys(mmgs_dict,0)
    km_temp = 0
    treated_col = matching_object.treatment_column_name
    for i in matching_object.df_units_and_covars_matched.index:        
        # iterate through all matched units of indexes with opposite treatment
        # values. How many of those MMGs am I in, and
        # if I'm in someone's MMG, what is the size of their MMG?

        is_treatment_val = matching_object.input_data.loc[i, treated_col]
        
        ''' # This works for only the without repeats case!
        for group in units_per_group:
            if i in group:
                # find out how many people in this mmg
                # have the opposite treatment status to the treatment_val_mmg
                num_treated = sum(matching_object.input_data.loc[group, 'treated'])
                if is_treatment_val:
                    num_opposite = len(group) - num_treated
                else:
                    num_opposite = num_treated
                    
                K_dict[i] += num_opposite/(len(group)-num_opposite) # is this right???  # (num_opposite/len(group)) # I think this is right per convo w Vittorio
        ''' # This works for both! Technically somewhat slower though!
        for j in matching_object.df_units_and_covars_matched.index:
            if i in mmgs_dict[j] and matching_object.input_data.loc[j, treated_col] != is_treatment_val:
                num_treated = sum(matching_object.input_data.loc[mmgs_dict[j], treated_col])
                if matching_object.input_data.loc[j, treated_col]: # double think -- you have to be opposite of j != opp of i
                    num_opposite = len(mmgs_dict[j]) - num_treated
                else:
                    num_opposite = num_treated
                # print("i", i, "j", j, "num_opp", num_opposite)
                K_dict[i] += 1/num_opposite
        
    # print(K_dict)
    # Compute ATE per simple estimator in paper -- this should be right
    ate = 0
    for i in mmgs_dict:
        treatment_val = matching_object.input_data.loc[i, treated_col]
        outcome_val = matching_object.input_data.loc[
            i, matching_object.outcome_column_name]
        ate += ((2*treatment_val - 1)*(1 + K_dict[i])*outcome_val)
    ate = ate/len(mmgs_dict)
        
    # Compute sigma^2. 
    i_summation = 0
    for i in mmgs_dict:
        group_members = mmgs_dict[i] # these are the l values in Jm(i)
        treatment_val = matching_object.input_data.loc[i, treated_col]
        outcome_val = matching_object.input_data.loc[
            i, matching_object.outcome_column_name]
        opp_group_members = matching_object.input_data.loc[group_members].index[matching_object.input_data.loc[group_members][treated_col] != treatment_val].tolist()
        # iterate through my group members -- only the ones w opp treatment to me!
        temp_l_summation = 0
        for l in opp_group_members:
            Y_l = matching_object.input_data.loc[
            l, matching_object.outcome_column_name]
            if treatment_val:
                temp_l_summation += ((outcome_val - Y_l - ate)**2)
            else:
                temp_l_summation += ((Y_l - outcome_val - ate)**2)         
        i_summation += temp_l_summation/len(opp_group_members)
    sigma_squared = 1/(2*len(mmgs_dict))*i_summation
    
    # Combine the above to compute var_estimator
    dict_summation = 0
    for key, value in K_dict.items():
        dict_summation += (1+value)**2
    var_estimator = sigma_squared*dict_summation/(len(mmgs_dict)**2)
    
    return var_estimator, ate
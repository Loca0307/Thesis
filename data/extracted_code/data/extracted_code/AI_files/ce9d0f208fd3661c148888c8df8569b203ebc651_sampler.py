        try:
            # Expected dict for finetuned checkpoints
            state_dict = {MODEL_STATE_DICT_KEY: get_model_state_dict(model)}
            dcp.load(state_dict=state_dict, checkpoint_id=job_config.checkpoint.init_state_dir)  # type: ignore
            state_dict = state_dict[MODEL_STATE_DICT_KEY]
        except RuntimeError:
            # Expected dict for newly converted checkpoints.
            state_dict = get_model_state_dict(model)
            dcp.load(state_dict=state_dict, checkpoint_id=job_config.checkpoint.init_state_dir)  # type: ignore

        set_model_state_dict(model, model_state_dict=state_dict, options=StateDictOptions(strict=True))
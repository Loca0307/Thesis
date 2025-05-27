    // Frontier
    private void OnMapInit(EntityUid uid, VehicleComponent component, MapInitEvent args)
    {
        bool actionsUpdated = false;
        if (component.HornSound != null)
        {
            _actionContainer.EnsureAction(uid, ref component.HornAction, HornActionId);
            actionsUpdated = true;
        }

        if (component.SirenSound != null)
        {
            _actionContainer.EnsureAction(uid, ref component.SirenAction, SirenActionId);
            actionsUpdated = true;
        }

        if (actionsUpdated)
            Dirty(uid, component);
    }
    // End Frontier

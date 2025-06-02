	err = createResourceIfNotExists(mcmNamespace, types.NamespacedName{Name: mcmNamespace.Name})
	if err != nil {
		log.Error(err, "Failed to create resource", "resource", mcmNamespace.GetObjectKind(), "named", mcmNamespace.Name)
		return ctrl.Result{}, err
	}
	err = createResourceIfNotExists(mcmAgentDeployment, types.NamespacedName{Name: mcmAgentDeployment.Name, Namespace: "mcm"})
	if err != nil {
		log.Error(err, "Failed to create resource", "resource", mcmAgentDeployment.GetObjectKind(), "named", mcmAgentDeployment.Name)
		return ctrl.Result{}, err
	}
	err = createResourceIfNotExists(mcmAgentService, types.NamespacedName{Name: mcmAgentService.Name, Namespace:"mcm"})
	if err != nil {
		log.Error(err, "Failed to create resource", "resource", mcmAgentService.GetObjectKind(), "named", mcmAgentService.Name)
		return ctrl.Result{}, err
	}
	err = createResourceIfNotExists(mcmMediaProxyPv, types.NamespacedName{Name: mcmMediaProxyPv.Name, Namespace: "mcm"})
	if err != nil {	
		log.Error(err, "Failed to create resource", "resource", mcmMediaProxyPv.GetObjectKind(), "named", mcmMediaProxyPv.Name)
		return ctrl.Result{}, err
	}
	err = createResourceIfNotExists(mcmMediaProxyPvc, types.NamespacedName{Name: mcmMediaProxyPvc.Name, Namespace: "mcm"})
	if err != nil {
		log.Error(err, "Failed to create resource", "resource", mcmMediaProxyPvc.GetObjectKind(), "named", mcmMediaProxyPvc.Name)
		return ctrl.Result{}, err
	}
	err = createResourceIfNotExists(mcmMediaProxyDs, types.NamespacedName{Name: mcmMediaProxyDs.Name, Namespace: "mcm"})
    if err != nil {
		log.Error(err, "Failed to create resource", "resource", mcmMediaProxyDs.GetObjectKind(), "named", mcmMediaProxyDs.Name)
		return ctrl.Result{}, err
	}
	
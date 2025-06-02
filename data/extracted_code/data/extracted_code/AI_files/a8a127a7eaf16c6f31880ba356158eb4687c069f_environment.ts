const getEnvironmentByIdMap = (
  environments: Environment[]
): Map<ResourceId, Environment> => {
  return new Map(
    environments.map((environment) => [environment.name, environment])
  );
};

const convertToEnvironments = (
  environments: EnvironmentSetting_Environment[]
): Environment[] => {
  return environments.map<Environment>((env, i) => {
    return {
      name: `${environmentNamePrefix}${env.id}`,
      title: env.title,
      order: i,
      color: env.color,
      tier: env.tags["protected"] === "protected"
        ? EnvironmentTier.PROTECTED
        : EnvironmentTier.UNPROTECTED,
      state: State.ACTIVE,
    };
  });
};

const convertEnvironments = (
  environments: Environment[]
): EnvironmentSetting_Environment[] => {
  return environments.map((env) => {
    const res: EnvironmentSetting_Environment = {
      id: env.name.replace(environmentNamePrefix, ""),
      title: env.title,
      color: env.color,
      tags: {},
    };
    if (env.tier === EnvironmentTier.PROTECTED) {
      res.tags.protected = "protected";
    }
    return res;
  });
};

const getEnvironmentSetting = async (
  silent = false
): Promise<Environment[]> => {
  const setting = await settingServiceClient.getSetting(
    {
      name: "settings/bb.workspace.environment",
    },
    { silent }
  );
  const settingEnvironments =
    setting.value?.environmentSetting?.environments ?? [];
  return convertToEnvironments(settingEnvironments);
};

const updateEnvironmentSetting = async (
  environment: EnvironmentSetting
): Promise<Environment[]> => {
  const setting = await settingServiceClient.updateSetting({
    setting: {
      name: "settings/bb.workspace.environment",
      value: {
        environmentSetting: environment,
      },
    },
    updateMask: ["environment_setting"],
  });
  const settingEnvironments =
    setting.value?.environmentSetting?.environments ?? [];
  return convertToEnvironments(settingEnvironments);
};

		// also check for JPA properties set as environment variables, this is slightly hacky and doesn't cover all
		// the naming conventions Springboot allows
		// but there doesn't seem to be a better/deterministic way to get these properties when they are set as ENV
		// variables and this at least provides
		// a way to set them (in a docker container, for instance)
		Map<String, Object> jpaPropsEnv = getPropertiesStartingWith(environment, "SPRING_JPA_PROPERTIES");
		for (Map.Entry<String, Object> entry : jpaPropsEnv.entrySet()) {
			String strippedKey = entry.getKey().replace("SPRING_JPA_PROPERTIES_", "");
			strippedKey = strippedKey.replaceAll("_", ".");
			strippedKey = strippedKey.toLowerCase();
			properties.put(strippedKey, entry.getValue().toString());
		}

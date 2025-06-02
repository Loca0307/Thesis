
  // This callback is triggered by the hook when a user selects a place
  const handlePlaceSelected = useCallback((place) => {
    console.log('Raw Place Selected:', place);
    const { city, state } = extractCityState(place);
    let locationString = '';

    if (city && state) {
      locationString = `${city}, ${state}`;
    } else {
      locationString = place?.formatted_address || place?.name || '';
      console.warn("Could not extract 'City, ST', using fallback:", locationString);
    }

    console.log('Place Selected -> Calling onChange with:', locationString);
    onChange(locationString);
  }, [onChange]);

  // Initialize the Google Places Widget hook
  const { ref: placesRef } = usePlacesWidget({
    apiKey: GOOGLE_PLACES_API_KEY,
    onPlaceSelected: handlePlaceSelected,
    options: {
      types: ["(regions)"],
      componentRestrictions: { country: "us" },
      fields: ["formatted_address", "address_components", "name", "geometry"],
    },
  });

  useEffect(() => {
    if (placesRef.current && value === '' && placesRef.current.value !== '') {
      placesRef.current.value = '';
    }
  }, [value, placesRef]);

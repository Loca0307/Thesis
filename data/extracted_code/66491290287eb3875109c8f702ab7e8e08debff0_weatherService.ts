  async getWeatherForCity(city: string): Promise<Weather[]> {
    try {
      this.cityName = city;

      console.log(`📍 Fetching weather data for: ${city}`);

      // Step 1: Get coordinates for the city
      const coordinates = await this.fetchAndDestructureLocationData();

      // Step 2: Fetch weather data using coordinates
      const weatherData = await this.fetchWeatherData(coordinates);

      // Step 3: Parse current weather
      const currentWeather = this.parseCurrentWeather(weatherData);

      // Step 4: Build the 5-day forecast
      return this.buildForecastArray(currentWeather, weatherData.list);
    } catch (error: any) {
      console.error(`❌ Error retrieving weather for city (${city}):`, error.message);
      throw error;
    }
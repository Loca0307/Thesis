    console.log("Using OpenAI for analysis");
    
    // [Analysis] Prepare prompt for article analysis with meaningful structure
    const prompt = `
      Analyze this AI news article and provide insights for AI agency professionals:
      
      Title: ${title}
      
      Content: ${content || ""}
      
      Source: ${source || "Unknown"}
      
      Category: ${category || "AI Technology"}
      
      Please respond with JSON containing the following keys:
      - market_impact: A detailed paragraph analyzing market implications for AI agencies
      - technical_predictions: Array of 3-5 bullet points with technical predictions
      - related_technologies: Array of relevant technologies mentioned or implied in the article
      - business_implications: A paragraph explaining strategic business implications for AI agencies
    `;
    
    // [Analysis] Call OpenAI API for enhanced analysis
    const openAIResponse = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${openAIKey}`,
      },
      body: JSON.stringify({
        model: "gpt-4o-mini", // [Analysis] Using an available model from OpenAI
        messages: [
          {
            role: "system",
            content: "You are an AI technology analyst specialized in extracting business insights from news articles for AI agencies. Provide detailed, actionable analysis in JSON format."
          },
          {
            role: "user",
            content: prompt
          }
        ],
        temperature: 0.3, // [Analysis] Lower temperature for more consistent, analytical responses
      }),
    });
    
    if (!openAIResponse.ok) {
      const errorData = await openAIResponse.text();
      console.error("OpenAI API error:", errorData);
      throw new Error(`OpenAI API error: ${errorData}`);
    }
    
    // [Analysis] Process and parse the OpenAI response
    const openAIData = await openAIResponse.json();
    console.log("Received response from OpenAI");
    
    let analysis;
    try {
      // [Analysis] Extract JSON from OpenAI response
      const responseContent = openAIData.choices[0].message.content;
      
      // [Framework] Parse JSON, handling potential formatting issues
      if (responseContent.includes("{") && responseContent.includes("}")) {
        const jsonStart = responseContent.indexOf("{");
        const jsonEnd = responseContent.lastIndexOf("}") + 1;
        const jsonStr = responseContent.substring(jsonStart, jsonEnd);
        analysis = JSON.parse(jsonStr);
      } else {
        // [Analysis] Fallback to text parsing if JSON structure is missing
        analysis = {
          market_impact: "Analysis of market impact unavailable at this time.",
          technical_predictions: ["Prediction data could not be extracted"],
          related_technologies: ["AI"],
          business_implications: "Business implications analysis unavailable at this time."
        };
      }
    } catch (parseError) {
      console.error("Error parsing OpenAI response:", parseError);
      
      // [Analysis] Provide fallback analysis when parsing fails
      analysis = {
        market_impact: "Unable to parse analysis results.",
        technical_predictions: ["Analysis results unavailable"],
        related_technologies: ["AI"],
        business_implications: "Unable to extract business implications at this time."
      };
    }
  try {
    // Prepare the list of products as a comma-separated string
    const productsList = products.join(', ');
    
    // Create the prompt for ChatGPT
    const prompt = `Du bist ein Koch-Experte und sollst Menüvorschläge basierend auf den folgenden Zutaten erstellen:
    
    ${productsList}
    
    Bitte erstelle 6 kreative Menüvorschläge (oder weniger, wenn nicht genug Zutaten vorhanden sind). 
    Jeder Vorschlag sollte kurz sein (maximal 3-4 Wörter) und auf Deutsch.
    Gib nur die Menüvorschläge zurück, einer pro Zeile, ohne Nummerierung oder andere Texte.`;
    
    // Call the OpenAI API
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('openai_api_key') || ''}`
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [
          {
            role: 'system',
            content: 'Du bist ein hilfreicher Assistent, der kreative Menüvorschläge basierend auf vorhandenen Zutaten erstellt.'
          },
          {
            role: 'user',
            content: prompt
          }
        ],
        temperature: 0.7,
        max_tokens: 250
      })
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      console.error('OpenAI API Error:', errorData);
      throw new Error(`OpenAI API Fehler: ${errorData.error?.message || 'Unbekannter Fehler'}`);
    }
    
    const data = await response.json();
    
    // Extract the suggestions from the API response
    const aiResponse = data.choices[0].message.content.trim();
    
    // Split the response by new lines to get individual suggestions
    const suggestions = aiResponse.split('\n')
      .map(line => line.trim())
      .filter(line => line && !line.startsWith('-')) // Remove empty lines and bullet points
      .map(line => {
        // Remove numbers at the beginning if present (e.g. "1. Spaghetti Carbonara" -> "Spaghetti Carbonara")
        return line.replace(/^\d+\.\s*/, '');
      });
    
    // Return up to 6 suggestions
    return suggestions.slice(0, 6);
  } catch (error) {
    console.error('Fehler bei der Generierung von Menüvorschlägen:', error);
    
    // Fall back to the original implementation if the API call fails
    return fallbackMenuSuggestions(products);
  }
};

// Fallback function that uses the original implementation
const fallbackMenuSuggestions = (products: string[]): string[] => {
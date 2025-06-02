  // New endpoint for game design assistance
  app.post("/api/design/chat", async (req, res) => {
    try {
      const { message, sessionId } = req.body;

      // Get or create conversation history
      if (!designConversations.has(sessionId)) {
        designConversations.set(sessionId, []);
      }
      const history = designConversations.get(sessionId)!;

      // Add user message to history
      history.push({ role: 'user', content: message });

      logApi("Design chat request received", { message, sessionId });

      const response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content: DESIGN_ASSISTANT_PROMPT
          },
          ...history
        ],
        temperature: 0.7
      });

      const assistantMessage = response.choices[0].message.content || "";

      // Add assistant response to history
      history.push({ role: 'assistant', content: assistantMessage });

      logApi("Design chat response", { message }, { response: assistantMessage });

      res.json({ 
        message: assistantMessage,
        history: history 
      });
    } catch (error: any) {
      logApi("Error in design chat", req.body, { error: error.message });
      res.status(500).json({ error: error.message });
    }
  });

  // Generate game code based on design conversation
  app.post("/api/design/generate", async (req, res) => {
    try {
      const { sessionId } = req.body;
      const history = designConversations.get(sessionId);

      if (!history) {
        throw new Error("No design conversation found");
      }

      logApi("Game generation request", { sessionId });

      // Compile the conversation into a detailed game specification
      const response = await openai.chat.completions.create({
        model: "gpt-4o",
        messages: [
          {
            role: "system",
            content: SYSTEM_PROMPT
          },
          {
            role: "user",
            content: `Based on the following conversation, create a complete game implementation:\n\n${
              history.map(msg => `${msg.role}: ${msg.content}`).join('\n')
            }`
          }
        ],
        temperature: 0.7,
        max_tokens: 16000
      });

      const content = response.choices[0].message.content || "";
      const code = extractGameCode(content);

      const result = {
        code,
        response: content
      };

      logApi("Game code generated", { sessionId }, result);
      res.json(result);
    } catch (error: any) {
      logApi("Error generating game", req.body, { error: error.message });
      res.status(500).json({ error: error.message });
    }
  });

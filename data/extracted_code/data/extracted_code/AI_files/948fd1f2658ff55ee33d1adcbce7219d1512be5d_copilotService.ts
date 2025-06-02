    
    // Since Copilot updates the source control box, get the message from there
    const { message, repo } = getSourceControlMessage();
    if (message) {
      // Clear the source control box since we're getting the message
      clearSourceControlMessage(repo);
      return message;
    }
    
  // Helper function to generate random filename
  private generateRandomFilename(type: 'input' | 'output'): string {
    const randomId = Math.random().toString(36).substring(2, 8);
    return `${type}-${randomId}.mp4`;
  }

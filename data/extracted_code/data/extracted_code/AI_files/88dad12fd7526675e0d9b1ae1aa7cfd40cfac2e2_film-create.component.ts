
  async generateSummary() {
    this.inProgress = true;
    try {
      const openai = new OpenAI({
        apiKey: environment.apiKey,
        dangerouslyAllowBrowser: true
      });
  
      let completion = await openai.chat.completions.create({
        messages: [{ role: 'user', content: 'Generálj nekem egy maximum 600 karakteres összegzést a: ' + (this.filmForm.get('title')?.value as string) + ' című filmhez'}],
        model: 'gpt-3.5-turbo',
        temperature: 0.95,
        max_tokens: 300,
        top_p: 1.0,
        frequency_penalty: 0.0,
        presence_penalty: 0.0,
      }).then(response => {
        this.summary = response.choices[0].message.content as string;
        this.filmForm.get('summary')?.setValue(this.summary);
        this.canGenerate = false;
        this.isGenerated = true;
        this.inProgress = false;
      }).catch(error => {
        this.isGenerated = false;
        this.inProgress = false;
      });
      
    } catch (error) {
      console.error(error);
      this.isGenerated = false;
      this.inProgress = false;
    }
  }
}
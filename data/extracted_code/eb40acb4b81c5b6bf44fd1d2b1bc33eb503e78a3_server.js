
    let imageUrl;
    if (USE_OPENAI_API) {
      const response = await openai.images.generate({
        model: "dall-e-3",
        prompt: generatedPrompt,
        n: 1,
        size: "1024x1024",
      });
      imageUrl = response.data[0].url;
      const imageId = uuidv4();
      imageUrl = await saveImage(imageUrl, imageId);
    } else {
      imageUrl = generateMockImage(generatedPrompt);
    }

    const metadata = {
      originalPrompt: prompt,
      generatedPrompt: generatedPrompt,
      imageUrl: imageUrl,
      createdAt: new Date().toISOString(),
    };

    // Add to gallery
    galleryItems.push(metadata);

    res.json({ 
      imageUrl: imageUrl, 
      generatedPrompt: generatedPrompt,
      originalPrompt: prompt 
    });
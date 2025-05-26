
def generate_chatgpt_image(japanese_text, english_text):
    """Generate an image using ChatGPT based on the Japanese and English text."""
    api_key = config.get("openai_api_key")
    print("API Key: " + api_key)
    if not api_key:
        return None
    
    prompt_template = config.get("chatgpt_image_prompt_template", 
                               "Create a simple, clear illustration to represent'{japanese}' meaning '{english}'. The image should be minimalist and educational.")
    
    prompt = prompt_template.format(japanese=japanese_text, english=english_text)
    print("ChatGPT Prompt: " + prompt)
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "model": "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        },
        timeout=30
    )

    print("ChatGPT Response: " + str(response.json()))
    
    if response.status_code != 200:
        raise Exception("Failed to generate image with ChatGPT: " + str(response.json()))
    
    data = response.json()
    if "data" not in data or len(data["data"]) < 1:
        return None
    
    return {
        "url": data["data"][0]["url"],
        "thumbnail": load_image_from_url(data["data"][0]["url"]),
        "source": "ChatGPT",
        "title": "AI Generated Image"
    }
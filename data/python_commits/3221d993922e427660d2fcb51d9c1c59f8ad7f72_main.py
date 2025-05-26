dataset = []
for chunk in censored_chunks:
    prompt = f"Assuming both users are gamers talking on Discord, what would one of them have said to get this response?  {chunk}  Give a likely quote in a simple, two-sentence max format that would cause this response, with no other feedback."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    user_content = response.choices[0].message.content
    print("USER:", user_content, "AI:", chunk)
    dataset.append({
        "messages": [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": chunk}
        ]
    })
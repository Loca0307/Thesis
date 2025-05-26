        response = client.chat.completions.create(model=MODEL,
        messages=[{"role": "system", "content": "You are an AI assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=MAX_TOKENS)
        return response.choices[0].message.content
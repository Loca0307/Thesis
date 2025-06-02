        {"role": "system", "content": prompt},
        {
      "role": "user",
      "content": [
        {"type": "text", "text": message},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{img_data}",
          },
        },
      ],
    }
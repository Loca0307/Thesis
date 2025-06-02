        try {
            $response = $this->client->chat()->create([
                'model' => self::config()->get('gpt_model'),
                'messages' => [
                    [
                        'role' => 'system',
                        'content' => $this->getGPTCommand($targetLocale)
                    ],
                    [
                        'role' => 'user',
                        'content' => $text
                    ]
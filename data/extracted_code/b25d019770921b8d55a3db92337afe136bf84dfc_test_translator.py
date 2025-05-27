# def test_japanese():
#     is_english, translated_content = translate_content("これは日本語のメッセージです")
#     assert is_english == False
#     assert translated_content == "This is a Japanese message"

# def test_detect_chinese():
#     is_english, translated_content = translate_content("这是中文")
#     assert is_english == False
#     assert translated_content == "This is Chinese"

# Evaluation dataset
translation_eval_set = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "Here is your first example."
    },
    {
        "post": "¿Dónde está la biblioteca?",
        "expected_answer": "Where is the library?"
    },
    {
        "post": "Je t’aime beaucoup.",
        "expected_answer": "I love you very much."
    },
    {
        "post": "今日は天気がいいですね。",
        "expected_answer": "The weather is nice today, isn't it?"
    },
    {
        "post": "Ciao, come stai?",
        "expected_answer": "Hi, how are you?"
    },
    {
        "post": "나는 한국어를 배우고 있어요.",
        "expected_answer": "I am learning Korean."
    },
    {
        "post": "Спасибо за помощь!",
        "expected_answer": "Thank you for the help!"
    },
    {
        "post": "Buongiorno, signore.",
        "expected_answer": "Good morning, sir."
    },
    {
        "post": "J'ai besoin d'aide.",
        "expected_answer": "I need help."
    },
    {
        "post": "这是什么东西？",
        "expected_answer": "What is this thing?"
    },
]

@pytest.mark.parametrize("test_case", translation_eval_set)
def test_translation(test_case):
    post = test_case["post"]
    expected_answer = test_case["expected_answer"]

    # Call the function to test
    is_english, translated_content = translate_content(post)

    # Assert that the translation matches the expected answer
    assert is_english == False  # Assuming all posts are non-English
    assert translated_content == expected_answer



# Language detection evaluation dataset
language_detection_eval_set = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": "German"
    },
    {
        "post": "¿Dónde está la biblioteca?",
        "expected_answer": "Spanish"
    },
    {
        "post": "Je t’aime beaucoup.",
        "expected_answer": "French"
    },
    {
        "post": "今日は天気がいいですね。",
        "expected_answer": "Japanese"
    },
    {
        "post": "Ciao, come stai?",
        "expected_answer": "Italian"
    },
    {
        "post": "나는 한국어를 배우고 있어요.",
        "expected_answer": "Korean"
    },
    {
        "post": "Спасибо за помощь!",
        "expected_answer": "Russian"
    },
    {
        "post": "Buongiorno, signore.",
        "expected_answer": "Italian"
    },
    {
        "post": "J'ai besoin d'aide.",
        "expected_answer": "French"
    },
    {
        "post": "这是什么东西？",
        "expected_answer": "Chinese"
    },
]

@pytest.mark.parametrize("test_case", language_detection_eval_set)
def test_detect_language(test_case):
    post = test_case["post"]
    expected_answer = test_case["expected_answer"]

    # Call the function to test
    detected_language = detect_language(post)

    # Assert that the detected language matches the expected answer
    assert detected_language == expected_answer
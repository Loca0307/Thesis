async def run(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        url = "https://chatgpt.com"
        await page.goto(url)
        await page.wait_for_selector("textarea#prompt-textarea")
        textarea = await page.locator("textarea#prompt-textarea")
        button = await page.locator("button.absolute.bottom-1\\.5")
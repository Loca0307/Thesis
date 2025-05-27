		this.addChatGPTPromptForGeneratingSummaryToClipboard();
		this.addCommand({
			id: "chatgpt-prompt-for-generating-summary-to-clipboard",
			name: "ChatGPT prompt for generating summary to clipboard",
			icon: `chatgpt-prompt-for-generating-summary-to-clipboard`,
			editorCallback: (editor: Editor, view: MarkdownView) => {
				const prompt = "請將以下的文章節錄縮短成約150字的中文摘要，確保摘要內容精煉且突出重點。你需要注意以下幾點：\n" +
							   "\n" +
							   "1. 將長篇大論縮短，只保留最重要的訊息和主題。\n" +
							   "2. 去除非必要的詳細訊息，並避免使用過於繁複或不必要的語言。\n" +
							   "3. 保留文章中最重要的主題和訊息，並確保這些訊息在摘要中清楚地表達出來。\n" +
							   "4. 使用精煉且直接的語言，以吸引人的方式表達作者將在文章中深入分享這些主題的意圖。\n" +
							   "5. 使用「我」來指稱「作者」，「你」來指稱讀者。\n" +
							   "\n" +
							   "具體來說，你需要確保以下重點訊息被包含其中：\n" +
							   "1. 文章的主要主題或重點討論。\n" +
							   "2. 作者提出的建議、策略或重要觀點。\n" +
							   "3. 這些建議或策略的具體效益或結果。\n" +
							   "\n" +
							   "最後，以吸引並鼓勵讀者進行下一步行動的方式編寫摘要，並表達出文章中更多深入的內容等待讀者去探索。\n" +
							   "請寫出3個版本。\n\n" + editor.getValue();

				navigator.clipboard.writeText(prompt).then(function () {
					new Notice(`Copied prompt for generate summary to clipboard!`);
				}, function (error) {
					new Notice(`error when copy to clipboard!`);
				});
			}
		});

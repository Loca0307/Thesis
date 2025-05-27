const tectalicOpenai = require('@tectalic/openai').default;
const config = require('dotenv').config();

async function cypressTestsGenerator(input) {
  try {
    const res = await tectalicOpenai(process.env.OPENAI_API_KEY)
    .completions.create({
      model: 'text-davinci-003',
      prompt: 'Write Cypress tests for the following JavaScript code: ' + input,
    })

    const cypress_test_recommendations = res.data.choices[0].text.trim();

    console.log(`\n${cypress_test_recommendations}`);

    return `Cypress tests suggestion for this pull request:\n\`\`\`diff\n${cypress_test_recommendations}\n\`\`\``;

  } catch (err) {
    if (err?.response) {
      const { status = null, statusText = '' } = err.response;
      console.error(`${status} - ${statusText}`);
      return err?.response;
    } else {
      console.error(err);
      return err;
    }
  }
}

module.exports = {
  cypressTestsGenerator
};
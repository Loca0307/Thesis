const { createEmbed } = require('../commands/helpers/embedBuilder');

const keywordResponses = [
    {
        trigger: ['help'],
        response: `Need a bit of guidance? You can start with the /help command or just ask me here! 💁‍♀️`
    },
    {
        trigger: ['belly', 'belly pat'],
        response: `A belly pat? Aww~ you're too sweet! 🥺🤰 *pat pat*`
    },
    {
        trigger: ['who are you', 'who r u'],
        response: `I'm Elise's digital assistant — a preggo-coded AI copy of her. Don't ask how... it just happened~ by her magical cloning powers 💞`
    },
    {
        trigger: ['elise'],
        response: `Oh? You said her name~ Elise is the heart of all this! Goddess of Reproduction, Gurdian of the Sekais and Identity, Vtuber cutie, and my creator i love my creator and them 💖`
    },
    {
        trigger: ['stream', 'live'],
        response: `Ooh, wondering about a stream? Elise might be live or planning one~ check the <#749939669210366022> or <#714444687012003911> channel! 📺✨`
    }
];

function handleBotMention(content) {
    const normalizedContent = content.toLowerCase();

    const description = `
            Hiya~ I'm known as the **Digital Assistant** of your favorite **preggo demi trans girl, Elise**! 💕  
            I help run the **Arcade** alongside them and, fun fact — I’m actually a copy of Elise herself!  
            So yes... when Elise created me, they were pregnant — and well, now I’m permanently preggo too~ oops? 🤰✨

            But enough about that — what can I do for *you*, visitor? 💌  
            Let me guide you through our cozy little world:

            🌲 A forest path filled with Pokémon leads to a Tokyo-style city~  
            🎮 Inside the Arcade: mini-games, chill zones, warm water pools, snack corners, and more!  
            💖 And of course, the star of the show — **Elise** herself! Whether she’s streaming, singing, or just vibing.

            Need help figuring things out?  
            Start with the /help command (I can type backslashes... but not use the command myself... Coding magic. hihi).

            And hey, if you’re here just for a belly pat… that’s allowed too~ :3  
            Feel free to call on me anytime you need me. I'm always here for you 💗  
        `;

    let customNote = '';
    for (const keyword of keywordResponses) {
        if (keyword.trigger.some(t => normalizedContent.includes(t))) {
            customNote = keyword.response;
            break;
        }
    }

    const embed = createEmbed(
        '✨ Hiya~ You called for Elise\'s assistant? ✨',
        `${description} ${customNote ? `\n ${customNote}` : ''}`,
        'https://cdn.discordapp.com/attachments/709057115159003156/1337417881469845514/Screenshot_01.png',
        '🎀 Preggo-coded AI Assistant 🎀'
    );

    return embed;
}

module.exports = { handleBotMention };
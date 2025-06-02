    console.log('SVG file generated successfully!');
}).catch(error => {
    console.error('Error:', error);
});

// Function that writes SVG file
// function writeToFile('Logo.svg', svgCode) {
//     fs.writeFile('Logo.svg', svgCode, (err) => {
//         if (err) {
//             return console.log(err)
//         }
//         console.log('SVG File successfully generated.')
//     })
// }
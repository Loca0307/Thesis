}


function parseSpellText(spell) {
  // Extracting relevant properties from the text field
  const regexPatterns = {
    freq: /<p3>Freq:<\/p3>\s*([^<]*)/,
    school: /<p3>School:<\/p3>\s*([^<]*)/,
    range: /<p3>Range:<\/p3>\s*([^<]*)/,
    materials: /<p3>Materials:<\/p3>\s*([^<]*)/,
    effect: /<p3>Effect:<\/p3>\s*([^<]*)/,
    limitations: /<p3>Limitations:<\/p3>\s*([^<]*)/,
    notes: /<p3>Notes:<\/p3>\s*([^<]*)/
  };

  let extractedData = {};

  for (let key in regexPatterns) {
    let match = spell.text.match(regexPatterns[key]);
    extractedData[key] = match ? match[1].trim() : "";
  }

  // Creating the cleaned spell object
  return {
    ...spell,
    freq: extractedData.freq,
    school: extractedData.school,
    range: extractedData.range,
    materials: extractedData.materials,
    effect: extractedData.effect,
    limitations: extractedData.limitations,
    notes: extractedData.notes,
    text: "" // Clear out the original text field
  };
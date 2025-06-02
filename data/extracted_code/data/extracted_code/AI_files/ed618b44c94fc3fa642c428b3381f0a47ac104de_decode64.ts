import fs from 'fs';

function base64ToHex(input: any): any {
  // skip numbers
  if (typeof input === 'string' && /^[0-9]+$/.test(input)) {
    return parseInt(input);
  }

  const base64Regex = /^[A-Za-z0-9+/=]+$/; // regex to match base64 string
  if (typeof input === 'string' && base64Regex.test(input)) {
    const hex = '0x' + Buffer.from(input, 'base64').toString('hex');
    return hex;
  }

  if (Array.isArray(input)) {
    return input.map((val) => base64ToHex(val));
  }

  if (input !== null && typeof input === 'object') {
    const newObj: { [key: string]: any } = {};
    for (const prop in input) {
      newObj[prop] = base64ToHex(input[prop]);
    }
    return newObj;
  }

  return input;
}

// sample usage
const jsonString = fs.readFileSync('./encoded/pool_calls64.json', 'utf-8');
const jsonObject = JSON.parse(jsonString);
const result = base64ToHex(jsonObject);
fs.writeFile("../aave/pool_calls.json", JSON.stringify(result, null, 2), 'utf8', function (fsErr: any) {
  if (fsErr) {
      console.log("An error occured while writing JSON Object to File.");
      return console.log(fsErr);
  }
  console.log("JSON file has been saved.");
});
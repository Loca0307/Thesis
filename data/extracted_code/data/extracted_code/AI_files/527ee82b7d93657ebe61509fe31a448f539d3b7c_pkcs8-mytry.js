<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RSA Key Pair Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        #output {
            margin-top: 20px;
        }
        textarea {
            width: 100%;
            height: 200px;
            margin-top: 10px;
            font-family: monospace;
            white-space: pre-wrap;
        }
        button {
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background-color: #45a049;
        }
        #zipLink {
            display: none;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
</head>
<body>
    <h1>RSA Key Pair Generator</h1>
    <p>Click the button below to generate a 2048-bit RSA key pair and download them, along with the key components in decimal format as a ZIP file.</p>
    <button id="generateBtn">Generate RSA Key Pair</button>
    <div id="output">
        <h3>Download Link:</h3>
        <a id="zipLink" href="#" download="rsa_key_pair.zip">Download RSA Key Pair and Components (ZIP)</a>
        <h3>Key Components (in Decimal):</h3>
        <pre id="keyComponents"></pre>
    </div>

    <script>
        async function generateRSAKeyPair() {
            try {
                // Generate RSA key pair with 2048-bit modulus
                const keyPair = await window.crypto.subtle.generateKey(
                    {
                        name: "RSA-OAEP",
                        modulusLength: 2048, // 2048-bit modulus
                        publicExponent: new Uint8Array([1, 0, 1]), // 65537 in hexadecimal
                        hash: { name: "SHA-256" },
                    },
                    true,
                    ["encrypt", "decrypt"]
                );

                // Export public key in SPKI format (PEM)
                const publicKeySpki = await window.crypto.subtle.exportKey("spki", keyPair.publicKey);
                const publicKeyPem = arrayBufferToPem(publicKeySpki, "PUBLIC KEY");

                // Export private key in PKCS8 format (PEM)
                const privateKeyPkcs8 = await window.crypto.subtle.exportKey("pkcs8", keyPair.privateKey);
                const privateKeyPem = arrayBufferToPem(privateKeyPkcs8, "PRIVATE KEY");

                // Extract key components from private key in JWK format
                const privateKeyJson = await window.crypto.subtle.exportKey("jwk", keyPair.privateKey);
                const publicKeyJson = await window.crypto.subtle.exportKey("jwk", keyPair.publicKey);

                // Extract modulus, public exponent, private exponent, p, q
                const n = publicKeyJson.n;  // Modulus (n)
                const e = publicKeyJson.e;  // Public exponent (e)
                const d = privateKeyJson.d; // Private exponent (d)
                const p = privateKeyJson.p; // Prime factor (p)
                const q = privateKeyJson.q; // Prime factor (q)

                // Convert from Base64URL to Decimal
                const nDecimal = base64urlToDecimal(n);
                const eDecimal = base64urlToDecimal(e);
                const dDecimal = base64urlToDecimal(d);
                const pDecimal = base64urlToDecimal(p);
                const qDecimal = base64urlToDecimal(q);

                // Display extracted key components in decimal
                document.getElementById('keyComponents').textContent = `
Modulus (N): ${nDecimal}
Public Exponent (e): ${eDecimal}
Private Exponent (d): ${dDecimal}
Prime Factor (p): ${pDecimal}
Prime Factor (q): ${qDecimal}
                `;

                // Create ZIP file
                const zip = new JSZip();
                zip.file("public_key.pem", publicKeyPem);
                zip.file("private_key.pem", privateKeyPem);
                zip.file("rsa_key_components.txt", `
Modulus (N): ${nDecimal}
Public Exponent (e): ${eDecimal}
Private Exponent (d): ${dDecimal}
Prime Factor (p): ${pDecimal}
Prime Factor (q): ${qDecimal}
                `);

                // Generate the ZIP file and create a download link
                const zipBlob = await zip.generateAsync({ type: "blob" });
                const zipLink = document.getElementById('zipLink');
                const zipUrl = URL.createObjectURL(zipBlob);
                zipLink.href = zipUrl;
                zipLink.style.display = 'block';  // Show the download link
            } catch (error) {
                console.error("Error generating key pair:", error);
                alert("Error generating RSA keys.");
            }
        }

        // Convert ArrayBuffer to PEM format
        function arrayBufferToPem(buffer, type) {
            const base64 = arrayBufferToBase64(buffer);
            return `-----BEGIN ${type}-----\n${base64}\n-----END ${type}-----`;
        }

        // Convert ArrayBuffer to Base64 encoded string
        function arrayBufferToBase64(buffer) {
            const binary = String.fromCharCode.apply(null, new Uint8Array(buffer));
            return window.btoa(binary);
        }

        // Convert Base64URL string to Decimal string
        function base64urlToDecimal(base64urlStr) {
            // Replace Base64URL specific characters with standard Base64
            const base64Str = base64urlStr.replace(/-/g, '+').replace(/_/g, '/');
            const binaryString = window.atob(base64Str);
            let decimalValue = BigInt(0);

            for (let i = 0; i < binaryString.length; i++) {
                const byteValue = binaryString.charCodeAt(i);
                decimalValue = (decimalValue << 8n) + BigInt(byteValue);
            }

            return decimalValue.toString();
        }

        // Add event listener to button
        document.getElementById('generateBtn').addEventListener('click', generateRSAKeyPair);
    </script>
</body>
</html>
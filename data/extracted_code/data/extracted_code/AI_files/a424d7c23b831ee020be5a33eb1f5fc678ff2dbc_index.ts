{
  "name": "@zereight/mcp-confluence",
  "version": "1.0.1",
  "description": "MCP server for using the Confluence API",
  "license": "MIT",
  "author": "zereight",
  "type": "module",
  "private": false,
  "bin": "./build/index.js",
  "files": [
    "build"
  ],
  "publishConfig": {
    "access": "public"
  },
  "engines": {
    "node": ">=14"
  },
  "scripts": {
    "build": "tsc && node -e \"require('fs').chmodSync('build/index.js', '755')\"",
    "prepare": "npm run build",
    "watch": "tsc --watch",
    "inspector": "npx @modelcontextprotocol/inspector build/index.js",
    "start": "node build/index.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "0.6.0",
    "axios": "^1.7.9",
    "mcp-framework": "^0.1.12",
    "okhttp": "^1.1.0"
  },
  "devDependencies": {
    "@types/node": "^20.11.24",
    "typescript": "^5.7.2"
  }
}
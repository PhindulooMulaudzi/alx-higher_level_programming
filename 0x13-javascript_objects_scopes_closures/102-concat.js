#!/usr/bin/node
'use strict'; // Enforce strict mode

const fs = require ('fs');

// Check if the correct number of command line arguments are provided
if (process.argv.length !== 5) {
  console.error ('Usage: ./script.js <fileA> <fileB> <outputFile>');
  process.exit (1); // Exit with an error code
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const outputFilePath = process.argv[4];

// Read the contents of fileA
let fileAContent;
try {
  fileAContent = fs.readFileSync (fileAPath, 'utf-8');
} catch (error) {
  console.error (`Error reading ${fileAPath}: ${error.message}`);
  process.exit (1); // Exit with an error code
}

// Read the contents of fileB
let fileBContent;
try {
  fileBContent = fs.readFileSync (fileBPath, 'utf-8');
} catch (error) {
  console.error (`Error reading ${fileBPath}: ${error.message}`);
  process.exit (1); // Exit with an error code
}

// Concatenate the contents of fileA and fileB
const concatenatedContent = fileAContent + fileBContent;

// Write the concatenated content to the outputFile
fs.writeFileSync (outputFilePath, concatenatedContent);

console.log (`Contents of ${fileAPath}: "${fileAContent}"`);
console.log (`Contents of ${fileBPath}: "${fileBContent}"`);
console.log (
  `Files concatenated successfully. Result written to ${outputFilePath}.`
);

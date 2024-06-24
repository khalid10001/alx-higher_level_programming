#!/usr/bin/node

const x = process.argv[2];
const num = Number.parseInt(x);

if (num) {
  for (let i = 0; i < num; i++) {
    let text = '';
    for (let l = 0; l < num; l++) {
      text += 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
}

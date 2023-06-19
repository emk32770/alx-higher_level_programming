#!/usr/bin/node

const dict = require('./101-data').dict;
const list = {};

for (const item in dict) {
	if (!(dict[item] in list)) {
		list[dict[item]] = [item];
	} else {
		list[dict[item]].push(item);
	}
}
console.log(list);

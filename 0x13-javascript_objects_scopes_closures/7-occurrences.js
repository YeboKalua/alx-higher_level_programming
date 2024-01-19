#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    nbOccurences = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            nbOccurences++;
        }
    }
    return nbOccurences;
};
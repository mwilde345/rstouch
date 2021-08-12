/*
1340, 55 (camera)
782, 411 (bank)
1493, 166 (preset 10)
1509, 340 (lychee)
30s
*/


const runShell = function(x, y) {
    let randX = getRand(-10, 10);
    let randY = getRand(-10, 10);
    console.log(`Random coords: ${x+randX}, ${y+randY}. ${randX} ${randY}`);
    const execSync = require('child_process').execSync;
    // import { execSync } from 'child_process';  // replace ^ if using ES modules
    const output = execSync(`./adb shell input tap ${x+randX} ${y+randY}`, { encoding: 'utf-8' });  // the default is 'buffer'
    // console.log('Output was:\n', output);
}

async function main() {
    let flag = 0;
    let counter = 0;
    // camera
    runShell(1340, 55);
    console.log('adjusted camera')
    while(flag == 0) {
        console.time('Exec Time');
        await wait(getRand(500, 3000))
        // bank
        runShell(782, 430);
        console.log('clicked banker')
        await wait(getRand(2500, 3800))
        // preset
        // runShell(1485, 166) // preset 10
        runShell(1555, 166) // preset 11
        console.log('clicked preset')
        await wait(getRand(2500, 3800))
        // start
        runShell(1509, 340)
        console.log('clicked item')
        await wait(getRand(2000, 3500));
        // click make
        runShell(1350, 1080)
        console.log('clicked make')
        await wait(getRand(15500, 18000)) // wait for potion
        // await wait(getRand(33000, 36000)) // wait for extract
        counter++;
        console.log('completed iteration ', counter)
        console.timeEnd('Exec Time');
    }
    setTimeout(function(){flag=1}, 1000*60*60*5);
}

function getRand(max, min) {
    var rand = Math.random()*(max-min) + min;
    // var power = Math.pow(10, decimalPlaces);
    // return Math.floor(rand*power) / power;
    return Math.floor(rand);
}

function wait(ms) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            console.log(`Waited ${ms}`);
            res(ms)
        }, ms)
    })
}

main();

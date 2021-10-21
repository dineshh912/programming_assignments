// Promopt package to handle console input
const prompt = require("prompt-sync")({ sigint: true });
// Chalk package to styling of the terminal
const chalk = require('chalk');

// Initialization
console.log(chalk.red("========================================================================"));

console.log(chalk.blue.bold("You've gone fishing! Try to maximize the value of your caught fish.",
    "\n You can fish for six hours (till 12:00pm) and can catch at most 10 lbs of fish."));

console.log(chalk.red("========================================================================"));

// Stroing all fish value
let allFishes = {};


// Generating random fish name, weight and it's value
function generateFish() {

    const fishes = {
        firstName: ["white", "sea", "Red", "Grey", "Blue", "Black", "Yellow", "Enormous", "Small", "Big", "Giant"],
        secondName: ["Pacific", "Finley", "Floaty", "Hulk", "Angel", "Alpha", "Bermuda", "Spotted", "Tetra", "Atlantic"],
        fish: ["Mackeral", "Salmon", "Trout", "Lobster", "shark", "Tilapia", "Tuna", "Billfish", "Catfish", "squid", "Snapper"],
    }

    let fishFullName = fishes.firstName[Math.floor(Math.random() * fishes.firstName.length)] + " " +
        fishes.secondName[Math.floor(Math.random() * fishes.secondName.length)] + " " +
        fishes.fish[Math.floor(Math.random() * fishes.fish.length)]

    let weight = ((Math.random() * 1000) / 100).toFixed(2);
    let value = ((Math.random() * 1000) / 100).toFixed(2);

    allFishes = {};
    allFishes.name = fishFullName;
    allFishes.weight = weight;
    allFishes.value = value;

    return `You caught a ${fishFullName} and it's weight =  ${weight} lbs and it's value = $${value}`;
}

// Random clock generation
function ClockRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

randomMin = ClockRandom(00, 60);

// Array to store catched fishes
const catchedFish = [];

// How many hours can fish
let hour = 6;
let min = 0;

// Store currently catched fish details for further process
let catchFishCount = 0;
let catchFishWeight = 0;
let catchFishValue = 0;
let totalFishWeight = 0;
let totalFishValue = 0;

// Loop to check the time and weight of the fish
while (hour < 12 && catchFishWeight < 10) {
    const fish = generateFish(); // generating random fish array


    if (min < 10) {
        console.log(chalk.yellow.bold(`The time is ${hour}:${min}0am. So far you've caught: ${catchFishCount} fish, ${catchFishWeight.toFixed(2)} lbs, $${catchFishValue.toFixed(2)}`));
    } else {
        console.log(chalk.cyan.bold(`The time is ${hour}:${min}am. So far you've caught: ${catchFishCount} fish, ${catchFishWeight.toFixed(2)} lbs, $${catchFishValue.toFixed(2)}`));
    }

    if (min + randomMin >= 60 || hour >= 12) {
        hour = hour + 1;
        min = 60 - min;
    } else {
        min += randomMin;
    }

    // Action 
    const action = prompt(`Your action: [c]atch or [r]elease?`);
    console.log("");

    if (action === "c") {
        // If keeping the fish add values into array
        console.log(`Keeping the fish -  ${allFishes.name}!`);
        catchedFish.push(allFishes);
        catchFishCount++
        catchFishWeight += parseFloat(allFishes.weight);
        catchFishValue += parseFloat(allFishes.value);
        console.log(chalk.red("============================================"));

    } else if (action === "r") {

        console.log(`Releasing the fish -  ${allFishes.name}!`);
        console.log(chalk.red("============================================"));

    } else {

        console.log("Choose correct option, try again");
        console.log(chalk.red("============================================"));
    }
}

// If time over
if (hour === 12) {
    console.log(chalk.redBright("The time is 12:00pm. Times up!"));
    console.log(chalk.redBright(`You caught ${catchFishCount} fish:`));
    for (let i = 0; i < catchedFish.length; i++) {
        let storedFish = catchedFish[i];
        totalFishWeight += Number(storedFish.weight);
        totalFishValue += Number(storedFish.value);
        console.log(chalk.cyanBright(`* ${storedFish.name}, ${storedFish.weight} lbs, $${storedFish.value}`));
    }
    console.log(chalk.yellowBright.bold(`Total weight: ${totalFishWeight.toFixed(2)} lbs`));
    console.log(chalk.yellowBright.bold(`Total value: $${totalFishValue.toFixed(2)}`));
}

// If weight is more
if (catchFishWeight >= 10) {
    console.log("This fish will increase the limt of 10 lbs, so you release it.");
    const endGame = prompt(`Press [enter] to continue.`);
    endGame;
    console.log(`You caught ${catchFishCount} fish:`);
    for (let i = 0; i < catchedFish.length; i++) {
        let storedFish = catchedFish[i];
        totalFishWeight += Number(storedFish.weight);
        totalFishValue += Number(storedFish.value);
        console.log(chalk.cyanBright(`* ${storedFish.name}, ${storedFish.weight} lbs, $${storedFish.value}`));
    }
    console.log(chalk.yellowBright.bold(`Total weight: ${totalFishWeight.toFixed(2)} lbs`));
    console.log(chalk.yellowBright.bold(`Total value: $${totalFishValue.toFixed(2)}`));
}
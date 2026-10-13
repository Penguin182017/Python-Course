console.log("JavaScript is Working!");

const GAME_NAME = "Penguin Clicker";
const PLAYER_EMOJI = "🐧";
const CURRENCY = "Coins";
const button = document.getElementById('penguinButton')
const upgradeButton = document.getElementById('upgradeButton')
const score = document.getElementById('score')
const clickPowerDisplay = document.getElementById('clickPower')
const fishPenguinDisplay = document.getElementById('fishPerSecond')
const babyPenguinButton = document.getElementById('babyPenguinButton')
const fisherPenguinButton = document.getElementById('fisherPenguinButton')
const fishingBoatButton = document.getElementById('fishingBoatButton')
const penguinHutButton = document.getElementById('penguinHutButton')
const fishFactoryButton = document.getElementById('fishFactoryButton')
const penguinShipButton = document.getElementById('penguinShipButton')
const fishWarehouseButton = document.getElementById('fishWarehouseButton')
const weatherDisplay = document.getElementById('weather');
let scoreNumber = 0
let clickPower = 1
let upgradeCost = 10
let babyPenguinCost = 50
let fisherPenguinCost = 250
let fishingBoatCost = 1000
let penguinHutCost = 5000
let fishFactoryCost = 25000
let penguinShipCost = 100000
let fishWarehouseCost = 500000
let babyPenguins = 0
let fisherPenguins = 0
let fishingBoats = 0
let penguinHuts = 0
let fishFactories = 0
let penguinShips = 0
let fishWarehouses = 0
 
button.addEventListener('click', function() {
    scoreNumber = scoreNumber + clickPower
    console.log(clickPower)
    score.textContent = "Score: " + scoreNumber
});

upgradeButton.addEventListener('click', function() {
    if (scoreNumber >= upgradeCost) {
       scoreNumber = scoreNumber - upgradeCost
       score.textContent = 'Score: ' + scoreNumber 
       clickPower = clickPower + 1
       clickPowerDisplay.textContent = "Click Power: " + clickPower
       upgradeCost = upgradeCost * 2                                
       upgradeButton.textContent = 'BUY FISH POWER = ' + upgradeCost
    }

});

babyPenguinButton.addEventListener('click', function() {
    if (scoreNumber >= babyPenguinCost) {
        scoreNumber = scoreNumber - babyPenguinCost
        babyPenguins = babyPenguins + 1
        clickPower = clickPower + 4
        clickPowerDisplay.textContent = "Click Power: " + clickPower
        console.log("BABY PENGUIN BOUGHT! Power:", clickPower)
    }

});

fisherPenguinButton.addEventListener('click', function() {
    if (scoreNumber >= fisherPenguinCost) {
        scoreNumber = scoreNumber - fisherPenguinCost
        fisherPenguins = fisherPenguins + 1
        clickPower = clickPower + 9
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }    
});

fishingBoatButton.addEventListener('click', function() {
    if (scoreNumber >= fishingBoatCost) {
        scoreNumber = scoreNumber - fishingBoatCost
        fishingBoats = fishingBoats + 1
        clickPower = clickPower + 25
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }
})

penguinHutButton.addEventListener('click', function() {
    if (scoreNumber >= penguinHutCost) {
        scoreNumber = scoreNumber - penguinHutCost
        penguinHuts = penguinHuts + 1
        clickPower = clickPower + 60
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }
})

fishFactoryButton.addEventListener('click', function() {
    if (scoreNumber >= fishFactoryCost) {
        scoreNumber = scoreNumber - fishFactoryCost
        fishFactories = fishFactories + 1
        clickPower = clickPower + 150
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }
})

penguinShipButton.addEventListener('click', function() {
    if (scoreNumber >= penguinShipCost) {
        scoreNumber = scoreNumber - penguinShipCost
        penguinShips = penguinShips + 1
        clickPower = clickPower + 500
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }
})

fishWarehouseButton.addEventListener('click', function() {
    if (scoreNumber >= fishWarehouseCost) {
        scoreNumber = scoreNumber - fishWarehouseCost
        fishWarehouses = fishWarehouses + 1
        clickPower = clickPower + 1500
        clickPowerDisplay.textContent = "Click Power: " + clickPower
    }
})

setInterval(function() {

    scoreNumber = scoreNumber + babyPenguins
    scoreNumber = scoreNumber + (5 * fisherPenguins) + (15 * fishingBoats) + (50 * penguinHuts) + (200 * fishFactories) + (1000 * penguinShips) + (5000 * fishWarehouses)

    let fishPerSecond = babyPenguins + (5 * fisherPenguins) + (15 * fishingBoats) + (50 * penguinHuts) + (200 * fishFactories) + (1000 * penguinShips) + (5000 * fishWarehouses)

    score.textContent = "Score: " + scoreNumber

    fishPenguinDisplay.textContent = "Fish Per Second: " + fishPerSecond

}, 1000)

const weatherTypes = [
    {
        name: "☀️ Sunny",
        rarity: "Common",
        className: "sunny",
        chance: 50
    },
    {
        name: "🌤️ Partly Cloudy",
        rarity: "Common",
        className: "partly-cloudy",
        chance: 50
    },
    {
        name: "🌅 Golden Hour",
        rarity: "Uncommon",
        className: "golden-hour",
        chance: 40
    },
    {
        name: "🌧️ Light Rain",
        rarity: "Uncommon",
        className: "light-rain",
        chance: 35
    },
    {
        name: "🌈 Rainbow",
        rarity: "Uncommon",
        className: "rainbow",
        chance: 25
    },
    {
        name: "🌙 Clear Night",
        rarity: "Rare",
        className: "clear-night",
        chance: 40
    },
    {
        name: "❄️ Light Snow",
        rarity: "Rare",
        className: "light-snow",
        chance: 35
    },
    {
        name: "🌸 Spring Breeze",
        rarity: "Rare",
        className: "spring-breeze",
        chance: 25
    },
    {
        name: "🌌 Aurora",
        rarity: "Very Rare",
        className: "aurora",
        chance: 60
    },
    {
        name: "🌠 Shooting Stars",
        rarity: "Very Rare",
        className: "shooting-stars",
        chance: 40
    },
    {
        name: "🌈 Double Rainbow",
        rarity: "Legendary",
        chance: 100
    },
    {
        name: "✨ Magical Sky",
        rarity: "Mystic",
        chance: 100
    },
    {
        name: "🌌 Cosmic Aurora",
        rarity: "Mythical",
        chance: 100
    }
];

function changeWeather() {
    const roll = Math.random() * 100;

    let rarity;

    if (roll < 1) {
        rarity = "Mythical";
    } else if (roll < 3) {
        rarity = "Mystic";
    } else if (roll < 6) {
        rarity = "Legendary";
    } else if (roll < 12) {
        rarity = "Very Rare";
    } else if (roll < 24) {
        rarity = "Rare";
    } else if (roll < 49) {
        rarity = "Uncommon";
    } else {
        rarity = "Common";
    }

    const possibleWeather = weatherTypes.filter(
        weather => weather.rarity === rarity
    );

    const randomWeather =
        possibleWeather[Math.floor(Math.random() * possibleWeather.length)];

    weatherDisplay.textContent =
        randomWeather.name + " — " + randomWeather.rarity;
    document.body.className = randomWeather.className;
}
changeWeather();
setInterval(changeWeather, 60000);

const rain = document.getElementById("rain");

for (let i = 0; i < 80; i++) {
    const drop = document.createElement("div");

    drop.className = "raindrop";

    drop.style.left = Math.random() * 100 + "%";
    drop.style.animationDelay = Math.random() * 0.8 + "s";

    rain.appendChild(drop);
}

const snow = document.getElementById("snow");

for (let i = 0; i < 50; i++) {
    const flake = document.createElement("div");

    flake.className = "snowflake";
    flake.textContent = "❄";

    flake.style.left = Math.random() * 100 + "%";
    flake.style.animationDelay = Math.random() * 5 + "s";

    snow.appendChild(flake);
}

const petals = document.getElementById("petals");

for (let i = 0; i < 30; i++) {
    const petal = document.createElement("div");

    petal.className = "petal";
    petal.textContent = "🌸";

    petal.style.left = Math.random() * 100 + "%";
    petal.style.animationDelay = Math.random() * 6 + "s";

    petals.appendChild(petal);
}

const shootingStars = document.getElementById("shootingStars");

for (let i = 0; i < 8; i++) {
    const star = document.createElement("div");

    star.className = "shooting-star";

    star.style.left = Math.random() * 80 + "%";
    star.style.top = Math.random() * 50 + "%";
    star.style.animationDelay = Math.random() * 5 + "s";

    shootingStars.appendChild(star);
}



document.title = GAME_NAME;

document.querySelector("h1").textContent = PLAYER_EMOJI + " " + GAME_NAME;

button.textContent = PLAYER_EMOJI;

score.textContent = CURRENCY + ": 0";
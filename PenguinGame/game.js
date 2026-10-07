console.log("JavaScript is Working!");

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
let scoreNumber = 0
let clickPower = 1
let upgradeCost = 10
let babyPenguinCost = 50
let fisherPenguinCost = 250
let fishingBoatCost = 1000
let penguinHutCost = 5000
let fishFactoryCost = 25000
let penguinShipCost = 100000
let babyPenguins = 0
let fisherPenguins = 0
let fishingBoats = 0
let penguinHuts = 0
let fishFactories = 0
let penguinShips = 0
 
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

setInterval(function() {

    scoreNumber = scoreNumber + babyPenguins
    scoreNumber = scoreNumber + (5 * fisherPenguins) + (15 * fishingBoats) + (50 * penguinHuts) + (200 * fishFactories) + (1000 * penguinShips)

    let fishPerSecond = babyPenguins + (5 * fisherPenguins) + (15 * fishingBoats) + (50 * penguinHuts) + (200 * fishFactories) + (1000 * penguinShips)

    score.textContent = "Score: " + scoreNumber

    fishPenguinDisplay.textContent = "Fish Per Second: " + fishPerSecond

}, 1000)
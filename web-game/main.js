const GAME_OPTION = {
    PVP: 'PVP',
    MEDIUM: 'MEDIUM',
    HARD: 'HARD',
    IMPOSSIBLE: 'IMPOSSIBLE'
}

var ballImage = new Image();
ballImage.src = "heart.jpg";

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

var leftPad = {
    x: 0,
    y: innerHeight / 2 - 10,
    w: 20,
    h: 100,
    speed: 0.2,
    color: "white",
};

var rightPad = {
    x: innerWidth - 25,
    y: innerHeight / 2 - 10,
    w: 20,
    h: 100,
    speed: 0.2,
    color: "red",
};

var square = {
    x: 680,
    y: 350,
    w: 50,
    h: 50,
    color: "white",
    xSpeed: 5,
    ySpeed: 5,
};

var dotLine = {
    x: innerWidth / 2,
    y: innerHeight,
    w: 10,
    h: innerHeight,
    speed: 0,
    color: "red",
};

canvas.width = innerWidth - 10;
canvas.height = innerHeight - 10;

var score = 0;
var mySound = new Audio();
mySound.src = "sans.mp3";
var myBGM = new Audio();
myBGM.src = "megalovania.mp3";
var myPad = new Audio();
myPad.src = "myPad.mp3";
var otherPad = new Audio();
otherPad.src = "otherPad.mp3";

var minute1 = 0;
var seconde1 = 0;
var minute10 = 0;
var seconde10 = 0;
var score1 = 0;
var score2 = 0;

var finalPoint = getElementById("lose");

var gameOption;

function drawPoints() {
    if (gameOption == GAME_OPTION.PVP) {
        ctx.fillStyle = "white";
        ctx.font = "24px Arial";
        ctx.fillText("Points :" + score1, 40, 40);

        ctx.fillStyle = "white";
        ctx.font = "24px Arial";
        ctx.fillText("Points :" + score2, canvas.width - 200, 40);
    }

    if (gameOption == GAME_OPTION.MEDIUM) {
        ctx.fillStyle = "white";
        ctx.font = "24px Arial";
        ctx.fillText("Points :" + score, 40, 40);
    }
    if (gameOption == GAME_OPTION.HARD) {
        ctx.fillStyle = "white";
        ctx.font = "24px Arial";
        ctx.fillText("Points :" + score, 40, 40);
    }

    if (gameOption == GAME_OPTION.IMPOSSIBLE) {
        ctx.fillStyle = "white";
        ctx.font = "24px Arial";
        ctx.fillText("Time " + minute10 + minute1 + ":" + seconde10 + seconde1, 40, 40);
        setInterval(timePass(), 1000);
    }
}

function timePass() {
    seconde1 += 1;
    if (seconde1 == 10) {
        seconde10 += 1;
        seconde1 = 0;
    }
    if (seconde10 == 6) {
        minute1 += 1;
        seconde10 = 0;
    }
    if (minute1 == 10) {
        minute1 = 0;
        minute10 += 1;
    }
}

function showMenu() {
    myBGM.play();

    document.getElementById("startMenu").style.display = "block";
    document.getElementById("startButton4").style.display = "block";
    document.getElementById("startButton3").style.display = "block";
    document.getElementById("startButton2").style.display = "block";
    document.getElementById("startButton1").style.display = "block";
    document.getElementById("startCreep").style.display = "none";
    document.getElementById("startYes").style.display = "none";
}

function startGameImpossible() {
    document.getElementById("myCanvas").style.display = "block";
    document.getElementById("startMenu").style.display = "none";
    gameOption = GAME_OPTION.IMPOSSIBLE
    gameLoop();
}

function startGameHard() {
    document.getElementById("myCanvas").style.display = "block";
    document.getElementById("startMenu").style.display = "none";
    gameOption = GAME_OPTION.HARD
    gameLoop();
}

function startGameMeduim() {
    document.getElementById("myCanvas").style.display = "block";
    document.getElementById("startMenu").style.display = "none";
    gameOption = GAME_OPTION.MEDIUM
    gameLoop();
}

function startGamePVP() {
    document.getElementById("myCanvas").style.display = "block";
    document.getElementById("startMenu").style.display = "none";
    gameOption = GAME_OPTION.PVP
    addPVPKeyListener()
    gameLoop();
}

function draw() {
    drawPoints();
    // draw pad
    ctx.fillStyle = leftPad.color;
    ctx.fillRect(leftPad.x, leftPad.y, leftPad.w, leftPad.h);
    // draw pad bot
    ctx.fillStyle = rightPad.color;
    ctx.fillRect(rightPad.x, rightPad.y, rightPad.w, rightPad.h);
    // draw middle line
    ctx.fillRect(dotLine.x, dotLine.y, dotLine.w, dotLine.h);
    ctx.fillStyle = dotLine.color;
    // draw ball
    ctx.fillRect(square.x, square.y, square.w, square.h);
    ctx.drawImage(ballImage, square.x, square.y, square.w, square.h);
}

var upArrowPressed = false;
var downArrowPressed = false;
var wKeyIsPressed = false;
var sKeyIsPressed = false;
/*
Two player mode, needs to handle when two players press the key at the same time
*/
function addPVPKeyListener() {
    function keyDownHandler(e) {
        if (e.key == "ArrowUp") {
            upArrowPressed = true;
        }
        if (e.key == "ArrowDown") {
            downArrowPressed = true;
        }
        if (e.key == "w") {
            wKeyIsPressed = true;
        }
        if (e.key == "s") {
            sKeyIsPressed = true;
        }
    }

    function keyUpHandler(e) {
        if (e.key == "ArrowUp") {
            upArrowPressed = false;
        }
        if (e.key == "ArrowDown") {
            downArrowPressed = false;
        }
        if (e.key == "w") {
            wKeyIsPressed = false;
        }
        if (e.key == "s") {
            sKeyIsPressed = false;
        }
    }

    document.addEventListener("keydown", keyDownHandler);
    document.addEventListener("keyup", keyUpHandler);
}

function PVPModePaddleMove() {
    rightPad.speed = 5;
    leftPad.speed = 5;
    // Move right paddle
    if (downArrowPressed && rightPad.y + rightPad.h < canvas.height) {
        rightPad.y += rightPad.speed
    }
    if (upArrowPressed && rightPad.y > 0) {
        rightPad.y -= rightPad.speed
    }

    // Move left paddle
    if (sKeyIsPressed && leftPad.y + leftPad.h < canvas.height) {
        leftPad.y += leftPad.speed;
    }
    if (wKeyIsPressed && leftPad.y > 0) {
        leftPad.y -= leftPad.speed
    }
}

function ballMove() {
    square.x += square.xSpeed;
    if (square.y + square.h + square.ySpeed > canvas.height || square.y < 0) {
        square.ySpeed = -square.ySpeed;
        mySound.play()
    }
    square.y += square.ySpeed;

    if (square.y + square.h > leftPad.y && square.y < leftPad.y + leftPad.h && square.x < leftPad.x + leftPad.w) {
        square.xSpeed = -square.xSpeed
        myPad.play()
        if (gameOption == GAME_OPTION.IMPOSSIBLE) {
            square.xSpeed = square.xSpeed * 1.05
        }
    }

    if (square.y + square.h > rightPad.y && square.y < rightPad.y + rightPad.h && square.x + square.w > rightPad.x) {
        square.xSpeed = -square.xSpeed
        if (gameOption == GAME_OPTION.IMPOSSIBLE) {
            square.xSpeed = square.xSpeed * 1.05
        }
        otherPad.play()
    }

    if (square.x > rightPad.x + rightPad.w) {
        score++
        score1++
        square.x = 680
        square.y = 350
    }

    if (square.x == 0) {
        square.x = 680
        square.y = 350
        score2++
        if (gameOption == GAME_OPTION.MEDIUM) {
            lose()
        }
    }
}
console.log(score);
finalPoint.innerHTML = "Final Point:" + score;

function lose() {
    // start again
    showMenu();
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    draw();
    ballMove();
    requestAnimationFrame(gameLoop);

    if (gameOption == GAME_OPTION.PVP) {
        PVPModePaddleMove();
    }

    if (gameOption == GAME_OPTION.MEDIUM) {
        rightPad.y = square.y;
        canvas.addEventListener("mousemove", mouse);

        function mouse(e) {
            console.log(e.clientX, e.clientY);

            leftPad.y = e.offsetY - leftPad.h / 2;
        }
    }

    if (gameOption == GAME_OPTION.HARD) {
        rightPad.speed = 1;
        rightPad.y += rightPad.speed;
        console.log(rightPad.y);
        if (rightPad.y < 0) {
            rightPad.speed = -rightPad.speed;
        }
        if (rightPad.y > 500) {
            rightPad.speed = -rightPad.speed;
        }
        canvas.addEventListener("mousemove", mouse);

        function mouse(e) {
            console.log(e.clientX, e.clientY);

            leftPad.y = e.offsetY - leftPad.h / 2;
        }
    }

    if (gameOption == GAME_OPTION.IMPOSSIBLE) {
        rightPad.y = square.y;
        canvas.addEventListener("mousemove", mouse);

        function mouse(e) {
            leftPad.y = e.offsetY - leftPad.h / 2;
        }
    }
}

// gameLoop()

// why awsd and arows speed up
//why no listen when dif 3
//why time weird
//ok si bug on side of pad
//why dif 4 not reset
//how to reset controls
//how to break out of music
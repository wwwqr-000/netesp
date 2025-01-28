let width = window.prompt("Width of screen");
let height = window.prompt("Height of screen");
let screen = document.getElementById("screen");

screen.setAttribute("width", width);
screen.setAttribute("height", height);

document.getElementsByClassName("gen")[0].addEventListener("click", () => {
    totalArr = []
    for (let y = 0; y < height; y++) {
        tmpArr = []
        for (let x = 0; x < width; x++) {
            if (ctx.getImageData(x, y, 1, 1)["data"][0] > 0) {
                document.write("1");
                continue;
            }
            document.write("0");
        }
        document.write("<br>");
    }
});

let ctx = screen.getContext("2d");
ctx.fillRect(0, 0, width, height);
ctx.fillStyle = "rgb(255, 255, 255)";

let onBox = false;

document.getElementById("screen").addEventListener("mousedown", () => {
    onBox = true;
});

document.getElementById("screen").addEventListener("mouseup", () => {
    onBox = false;
});

document.getElementById("screen").addEventListener("mousemove", (m) => {
    if (onBox) {
        ctx.fillRect(m.clientX, m.clientY, 1, 1);
    }
});
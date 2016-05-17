function setup() {
  createCanvas(600, 600);
}

function draw() {
  noLoop();

  var c = color(Math.floor(Math.random(1) * 255), Math.floor(Math.random(1) * 255), Math.floor(Math.random(1) * 255));
  var cell = Math.floor(Math.random(1) * 20 + 5);

  background(c);
  strokeWeight(Math.floor(Math.random(1) * 2) + 1);
  stroke(255);

  for (var i = 0; i < (width / cell); i++) {
    for (var j = 0; j < (height / cell); j++) {
      var drawn = false;
      if (j === 0) {
        line(i * cell, j * cell, (i + 1) * cell, j * cell); //top line
        drawn = true;
      }
      if (i == (width) / cell - 1) {
        line((i + 1) * cell, j * cell, (i + 1) * cell, (j + 1) * cell); //right line
        drawn = true;
      }
      if (!drawn) {
        var wall = Math.floor((Math.random(2) * 2));
        if (wall === 0) {
          line(i * cell, j * cell, (i + 1) * cell, j * cell);
        } else {
          line((i + 1) * cell, j * cell, (i + 1) * cell, (j + 1) * cell);
        }
      }
    }
  }
}

function mousePressed() {
  redraw();
}
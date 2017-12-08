// module aliases
var Engine = Matter.Engine,
  World = Matter.World,
  Bodies = Matter.Bodies;

var engine;
var world;
var boxes = [];

var ground;
var makeBox = false


function setup() {
//setup canvas
  canvas_width = window.innerWidth;
  canvas_height = window.innerHeight;
  canvas = createCanvas(canvas_width, canvas_height);
  canvas = document.getElementById('defaultCanvas0')
  canvas.style.position = "fixed";
  canvas.style.zIndex  = -1
  canvas.style.top = "0px";
  canvas.style.left = "0px";
//  setup world and engine
  engine = Engine.create();
  world = engine.world;
  Engine.run(engine);
  var options = {
    isStatic: true
  }
  ground = Bodies.rectangle(0, canvas_height, 4000, 10, options);
  World.add(world, ground);
  background('rgba(211,211,211, 0.1)');
}


function mousePressed() {
  if (makeBox) {
    boxes.push(new Box(mouseX, mouseY, random(10, 20), random(10, 20)));
  }
}

function keyPressed() {
  if (keyCode == ESCAPE) {
    makeBox = !makeBox
  }
}

function draw() {
  clear();
  background('rgba(211,211,211, 0.1)');
  for (var i = 0; i < boxes.length; i++) {
    boxes[i].show();
  }
   noStroke(255);
   fill(170);
  rectMode(CENTER);
  rect(ground.position.x, ground.position.y, 1000, 1);
}
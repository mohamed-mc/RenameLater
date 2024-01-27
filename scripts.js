const dino = document.getElementById("dino");
function jump(){
    dino.classList.add("jump");
}

document.addEventListener("keydown", function (event) {
    jump();
  });
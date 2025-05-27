function stopDrawing() {
  isPainting = false;
  ctx.closePath();
}

function draw(e) {
  if (!isPainting) return;
  const pos = getMousePosition(e);
  ctx.linecap ="round"
    ctx.lineWidth = penSize;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;

    switch (activeTool) {
        case "pen":
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            break;
        case "eraser":
            ctx.strokeStyle = "white";
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            break;
    }
}
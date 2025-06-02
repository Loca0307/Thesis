// Credit: ChatGPT - https://chat.openai.com/share/a1af86f5-0449-4215-9bab-61b70ea4de84

function doPolygonsIntersect(polygon1, polygon2) {
  function getAxes(polygon) {
    const axes = [];
    const points = polygon.length;

    for (let i = 0; i < points; i++) {
      const p1 = polygon[i];
      const p2 = polygon[(i + 1) % points];
      const edge = { x: p2.x - p1.x, y: p2.y - p1.y };
      const normal = { x: -edge.y, y: edge.x };
      axes.push(normal);
    }

    return axes;
  }

  function project(polygon, axis) {
    const points = polygon.length;
    let min = Infinity;
    let max = -Infinity;

    for (let i = 0; i < points; i++) {
      const dotProduct = polygon[i].x * axis.x + polygon[i].y * axis.y;
      if (dotProduct < min) min = dotProduct;
      if (dotProduct > max) max = dotProduct;
    }

    return { min, max };
  }

  function overlap(projection1, projection2) {
    return (
      projection1.min <= projection2.max && projection1.max >= projection2.min
    );
  }

  const axes1 = getAxes(polygon1);
  const axes2 = getAxes(polygon2);

  for (const axis of [...axes1, ...axes2]) {
    const projection1 = project(polygon1, axis);
    const projection2 = project(polygon2, axis);

    if (!overlap(projection1, projection2)) {
      return false; // No collision, early exit
    }
  }

  return true; // Collided on all axes, there is a collision
}

export default function isBoatColliding(boat, walls) {
  for (const wall of walls) {
    if (doPolygonsIntersect(boat, wall)) {
      return wall; // Collision detected
    }
  }

  return false; // No collision
}
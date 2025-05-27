const transformPointBetweenPolesCases = [
  // {
  //   name: 'where point [1, 0, 0] is transformed from initial pole to new pole',
  //   point: [1, 0, 0],
  //   initialPole: {
  //     lat_of_euler_pole: 30,
  //     lon_of_euler_pole: 60,
  //     rotation_angle: 20,
  //   },
  //   newPole: {
  //     lat_of_euler_pole: 45,
  //     lon_of_euler_pole: 45,
  //     rotation_angle: 30,
  //   },
  //   expected: [0.7392, 0.5732, 0.3536],
  // },
  // {
  //   name: 'where point [0, 1, 0] is transformed from initial pole to new pole',
  //   point: [0, 1, 0],
  //   initialPole: {
  //     lat_of_euler_pole: 30,
  //     lon_of_euler_pole: 60,
  //     rotation_angle: 20,
  //   },
  //   newPole: {
  //     lat_of_euler_pole: 45,
  //     lon_of_euler_pole: 45,
  //     rotation_angle: 30,
  //   },
  //   expected: [0.2803, 0.7392, 0.6124],
  // },
  {
    name: 'where point [1, 0, 0] is transformed from initial pole to new pole',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 30,
    },
    expected: [0.8660254037844387, 0.5, 0],
  },
  {
    name: 'in the series, the same point goes to a third pole',
    point: [0.8660254037844387, 0.5, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 30,
    },
    newPole: {
      lat_of_euler_pole: 20,
      lon_of_euler_pole: 45,
      rotation_angle: 30,
    },
    expected: [0.9251766765758391, 0.23016134445423478, -0.30178448044772743],
  },
  {
    name: 'using test planet',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    expected: [1, 0, 0],
  },
  {
    name: 'using test planet and motion',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: -30,
    },
    expected: [0.8660254037844387, -0.5, 0],
  },
];
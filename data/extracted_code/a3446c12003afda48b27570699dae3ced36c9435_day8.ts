import * as fs8 from "fs";

class Day8Execution {

    private readonly inputFilePath: string;
    private readonly data: string;
    private readonly inputMap: string[][];
    private posAntennas: Map<string, string>;

    constructor() {
        this.inputFilePath = "real-input.txt";
        this.data = fs8.readFileSync(this.inputFilePath, "utf8");
        this.inputMap = this.data.split("\n").map((line) => line.replace("\r", "").split(" "));

        // parse the stringLine of every row to a string array 
        this.inputMap.forEach((stringLine, index) => {
            this.inputMap[index] = stringLine[0].split("");
        });
        // console.log(this.inputMap);
    }

    // search for antennas in inputMap (could be letters or digits) and save the position in posAntennas 
    // (key: position (unique), value: antenna char)
    searchAntennas(): void {
        this.posAntennas = new Map<string, string>();
        for (let i = 0; i < this.inputMap.length; i++) {
            for (let j = 0; j < this.inputMap[i].length; j++) {
                if (RegExp(/[a-zA-Z0-9]/).exec(this.inputMap[i][j])) {
                    this.posAntennas.set(i + "," + j, this.inputMap[i][j]);
                }
            }
        }

        // print the antennas and their positions 
        // this.posAntennas.forEach((value, key) => {
        //     console.log(key + " -> " + value);
        // });
    }

    // calculate antinode positions and return the total count
    calculateAnitnodePositions(): number {
        const antinodePositions = new Set<string>();
    
        const antennasByFreq = this.groupAntennasByFrequency();
        antennasByFreq.forEach((positions, freq) => {
            for (let i = 0; i < positions.length; i++) {
                for (let j = i + 1; j < positions.length; j++) {
                    const [x1, y1] = positions[i];
                    const [x2, y2] = positions[j];
    
                    // Skip if antennas are at the same position
                    if (x1 === x2 && y1 === y2) {
                        continue;
                    }
    
                    // Consider both ratios: 1:2 and 2:1
                    const ratios = [
                        { m: 1, n: 2 },
                        { m: 2, n: 1 },
                    ];
    
                    ratios.forEach(({ m, n }) => {
                        // Calculate internal and external division points
                        const internalPoint = this.dividePoints(x1, y1, x2, y2, m, n, true);
                        const externalPoint = this.dividePoints(x1, y1, x2, y2, m, n, false);
    
                        // Validate and add positions
                        [internalPoint, externalPoint].forEach(point => {
                            if (this.isValidPosition(point[0], point[1])) {
                                antinodePositions.add(`${point[0]},${point[1]}`);
                            }
                        });
                    });
                }
            }
        });
    
        // Return the total count of unique antinode positions
        return antinodePositions.size;
    }

    // group antennas by frequency, return new map with frequency as key and positions of antennas as value
    private groupAntennasByFrequency(): Map<string, Array<[number, number]>> {
        const antennasByFreq = new Map<string, Array<[number, number]>>();
        this.posAntennas.forEach((freq, pos) => {
            const [row, col] = pos.split(',').map(Number);
            if (!antennasByFreq.has(freq)) {
                antennasByFreq.set(freq, []);
            }
            antennasByFreq.get(freq)!.push([row, col]);
        });
        return antennasByFreq;
    }

    private dividePoints(
        x1: number,
        y1: number,
        x2: number,
        y2: number,
        m: number,
        n: number,
        isInternal: boolean
    ): [number, number] {
        let x: number;
        let y: number;
        if (isInternal) {
            x = (n * x1 + m * x2) / (m + n);
            y = (n * y1 + m * y2) / (m + n);
        } else {
            x = (n * x1 - m * x2) / (n - m);
            y = (n * y1 - m * y2) / (n - m);
        }
        return [x, y];
    }

    private isValidPosition(x: number, y: number): boolean {
        return (
            Number.isInteger(x) &&
            Number.isInteger(y) &&
            x >= 0 &&
            y >= 0 &&
            x < this.inputMap.length &&
            y < this.inputMap[x].length 
        );
    }

    getInputString(): string[][] {
        return this.inputMap;
    }
}

function main8() {
    let execution = new Day8Execution();
    execution.searchAntennas();
    let res = execution.calculateAnitnodePositions();
    console.log(`Number of unique antinode positions: ${res}`);
}

main8();
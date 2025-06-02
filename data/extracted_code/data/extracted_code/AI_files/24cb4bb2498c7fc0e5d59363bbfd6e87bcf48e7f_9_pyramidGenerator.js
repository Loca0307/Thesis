function pyramid(pattern, rows, boo) {
    let result = "";

    if (!boo) { // Normal Pyramid
        for (let i = 1; i <= rows; i++) {
            let spaces = " ".repeat(rows - i);
            let py = spaces + pattern.repeat(2 * i - 1);
            result += (i === 1 ? "" : "\n") + py;
        }
    } else { // Inverted Pyramid
        for (let i = rows; i >= 1; i--) {
            let spaces = " ".repeat(rows - i);
            let py = spaces + pattern.repeat(2 * i - 1);
            result += (i === rows ? "" : "\n") + py;
        }
    }

    return "\n" + result + "\n";
}
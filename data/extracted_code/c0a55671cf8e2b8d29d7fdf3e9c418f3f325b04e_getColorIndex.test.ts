import { getColorIndex } from "./getColorIndex";

describe("getColorIndex function", () => {
  it("should return 0 when index is 0", () => {
    const result = getColorIndex(0);
    expect(result).toBe(0);
  });

  it("should return 0 when index is 1", () => {
    const result = getColorIndex(1);
    expect(result).toBe(0);
  });

  it("should return index - 1 when index is even", () => {
    const result = getColorIndex(4);
    expect(result).toBe(3);
  });

  it("should return index - 2 when index is odd", () => {
    const result = getColorIndex(5);
    expect(result).toBe(3);
  });
});
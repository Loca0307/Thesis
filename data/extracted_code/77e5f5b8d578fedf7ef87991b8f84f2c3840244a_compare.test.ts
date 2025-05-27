import { compare } from "./compare";

describe("compare function", () => {
  it("should return -1 if a[key] < b[key]", () => {
    const obj1 = { name: "Alice", age: 30 };
    const obj2 = { name: "Bob", age: 40 };
    const result = compare("age")(obj1, obj2);
    expect(result).toBe(-1);
  });

  it("should return 1 if a[key] > b[key]", () => {
    const obj1 = { name: "Alice", age: 40 };
    const obj2 = { name: "Bob", age: 30 };
    const result = compare("age")(obj1, obj2);
    expect(result).toBe(1);
  });

  it("should return 0 if a[key] === b[key]", () => {
    const obj1 = { name: "Alice", age: 30 };
    const obj2 = { name: "Bob", age: 30 };
    const result = compare("age")(obj1, obj2);
    expect(result).toBe(0);
  });
});
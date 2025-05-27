import { genericSearch } from "./genericSearch";

describe("genericSearch function", () => {
  const obj1 = { name: "Alice", age: 30, address: "123 Main St" };
  const obj2 = { name: "Bob", age: 40, address: "456 Second Ave" };
  const obj3 = { name: "Charlie", age: 50, address: "789 Third St" };
  const objs = [obj1, obj2, obj3];

  it("should return true when query is empty string", () => {
    const result = genericSearch(obj1, ["name"], "");
    expect(result).toBe(true);
  });

  it("should return true when query matches property value", () => {
    const result = genericSearch(obj1, ["name"], "Alice");
    expect(result).toBe(true);
  });

  it("should return false when query does not match any property value", () => {
    const result = genericSearch(obj1, ["name"], "Bob");
    expect(result).toBe(false);
  });

  it("should return true when query matches any property value", () => {
    const result = genericSearch(obj1, ["name", "age", "address"], "123");
    expect(result).toBe(true);
  });

  it("should handle case-sensitive searches when specified", () => {
    const result = genericSearch(obj1, ["name"], "alice", true);
    expect(result).toBe(false);
  });

  it("should handle case-insensitive searches when specified", () => {
    const result = genericSearch(obj1, ["name"], "alice", false);
    expect(result).toBe(true);
  });

  it("should return true when query matches any property value in an array of objects", () => {
    const result = objs.some((obj) =>
      genericSearch(obj, ["name", "age", "address"], "third")
    );
    expect(result).toBe(true);
  });
});
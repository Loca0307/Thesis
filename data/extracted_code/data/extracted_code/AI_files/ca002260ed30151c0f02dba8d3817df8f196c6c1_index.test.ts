import { describe, expect, it } from "bun:test";
import { success, failure, Result } from "./index";

describe("Result Type Tests", () => {
  it("should create a success result", () => {
    const result = success(42);

    expect(result.done).toBe(true);
    expect(result.value).toBe(42);
    expect(result.failure).toBeUndefined();
  });

  it("should create a failure result and throw on value access", () => {
    const error = new Error("Test error");
    const result = failure(error);

    expect(result.done).toBe(true);
    expect(result.failure).toBe(error);

    expect(() => result.value).toThrow(error);
  });

  it("should handle different success types", () => {
    const stringResult = success("Hello, world!");
    expect(stringResult.value).toBe("Hello, world!");

    const objectResult = success({ key: "value" });
    expect(objectResult.value).toEqual({ key: "value" });
  });

  it("should handle different failure types", () => {
    const errorObject = { code: 500, message: "Internal Server Error" };
    const result = failure(errorObject);

    expect(result.failure).toBe(errorObject);
    expect(() => result.value).toThrow(errorObject);
  });
});
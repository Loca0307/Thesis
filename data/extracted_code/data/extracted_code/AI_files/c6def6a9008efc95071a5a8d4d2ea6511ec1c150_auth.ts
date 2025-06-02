import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { login, register, forgotPassword, APIError } from "./auth";
import type {
  LoginFormValues,
  RegisterFormValues,
  ForgotPasswordFormValues,
} from "../validation";

describe("lib/api/auth", () => {
  beforeEach(() => {
    vi.stubGlobal("fetch", vi.fn());
    vi.useFakeTimers();
    process.env.API_BASE_URL = "https://api.escuelajs.co/api/v1";
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.useRealTimers();
    vi.restoreAllMocks();
  });

  describe("login()", () => {
    it("resolves with access_token and refresh_token when API returns 200", async () => {
      const fetchMock = fetch as unknown as ReturnType<typeof vi.fn>;

      fetchMock.mockResolvedValueOnce({
        ok: true,
        status: 200,
        headers: { get: () => "application/json" },
        json: async () => ({
          access_token: "foo-token",
          refresh_token: "bar-token",
        }),
      });

      await expect(
        login({ email: "a@b.com", password: "pw" } as LoginFormValues),
      ).resolves.toEqual({
        access_token: "foo-token",
        refresh_token: "bar-token",
      });

      expect(fetchMock).toHaveBeenCalledWith(
        `${process.env.API_BASE_URL}/auth/login`,
        expect.objectContaining({
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: "a@b.com", password: "pw" }),
        }),
      );
    });

    it("throws APIError with status and message on non-OK response", async () => {
      const fetchMock = fetch as unknown as ReturnType<typeof vi.fn>;

      fetchMock.mockResolvedValueOnce({
        ok: false,
        status: 401,
        headers: { get: () => "application/json" },
        json: async () => ({ message: "Invalid credentials" }),
      });

      await expect(
        login({ email: "a@b.com", password: "wrong" } as LoginFormValues),
      ).rejects.toEqual(new APIError("Invalid credentials", 401));
    });
  });

  describe("register()", () => {
    it("resolves with success message after simulated delay", async () => {
      const payload = {
        email: "new@user.com",
        password: "secret",
        confirmPassword: "secret",
      } as RegisterFormValues;

      const promise = register(payload);
      vi.advanceTimersByTime(500);
      await expect(promise).resolves.toEqual({
        message: "Registration successful!",
      });
    });
  });

  describe("forgotPassword()", () => {
    it("resolves with a reset-email message after simulated delay", async () => {
      const payload = { email: "someone@x.com" } as ForgotPasswordFormValues;

      const promise = forgotPassword(payload);
      vi.advanceTimersByTime(500);
      await expect(promise).resolves.toEqual({
        message:
          "If that account exists, you’ll receive a reset email shortly.",
      });
    });
  });
});
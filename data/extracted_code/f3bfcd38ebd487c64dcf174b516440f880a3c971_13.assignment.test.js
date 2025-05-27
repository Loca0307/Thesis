const AuthService = {
  login: jest.fn(),
  getUserProfile: jest.fn(),
  logout: jest.fn(),
};

describe("User's Login process", () => {
  it("should login user in the first try and fail in second", async () => {
    AuthService.login.mockResolvedValueOnce({
      id: 1,
      name: "John Doe",
    });

    const loggedUser = await AuthService.login();
    expect(loggedUser).toEqual({
      id: 1,
      name: "John Doe",
    });

    AuthService.login.mockRejectedValueOnce(new Error("Invalid credentials."));
    try {
      await AuthService.login();
    } catch (error) {
      expect(error).toEqual(new Error("Invalid credentials."));
    }
  });
});

describe("fetching user's profile multiple times.", () => {});
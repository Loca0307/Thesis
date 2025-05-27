                // User doesn't exist; create a new user
                user = CreateUser();
                await _userStore.SetUserNameAsync(user, email, CancellationToken.None);
                await _emailStore.SetEmailAsync(user, email, CancellationToken.None);

                // Set user properties from external provider
                user.Name = info.Principal.Identity.Name ?? "Unknown";
                user.AuthorId = await _userManager.Users.CountAsync() + 1;

                var createUserResult = await _userManager.CreateAsync(user);
                if (createUserResult.Succeeded)
                {
                    await _userManager.AddClaimAsync(user, new Claim("Name", user.Name));
                    var addLoginResult = await _userManager.AddLoginAsync(user, info);
                    if (!addLoginResult.Succeeded)
                    {
                        ErrorMessage = "Failed to add external login for new user.";
                        return RedirectToPage("./Login", new { ReturnUrl = returnUrl });
                    }
                }
                else
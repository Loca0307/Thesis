        
        //This updates the users (authors) email, which also makes sure that the cheeps have the NewEmail
        user.Email = Input.NewEmail;
        user.UserName = Input.NewEmail;
        var updateResult = await _userManager.UpdateAsync(user);
        if (!updateResult.Succeeded)
        {
            foreach (var error in updateResult.Errors)
            {
                ModelState.AddModelError(string.Empty, error.Description);
            }
            StatusMessage = "Unexpected error when trying to update email.";
            return RedirectToPage();
        }
        
        /*
        // Update email in the user manager with verification
        var userId = await _userManager.GetUserIdAsync(user);
        var code = await _userManager.GenerateChangeEmailTokenAsync(user, Input.NewEmail);
        code = WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(code));
        var callbackUrl = Url.Page(
            "/Account/ConfirmEmailChange",
            pageHandler: null,
            values: new { area = "Identity", userId = userId, email = Input.NewEmail, code = code },
            protocol: Request.Scheme);
        await _emailSender.SendEmailAsync(
            Input.NewEmail,
            "Confirm your email",
            $"Please confirm your account by <a href='{HtmlEncoder.Default.Encode(callbackUrl)}'>clicking here</a>.");
            */

        StatusMessage = "Confirmation link to change email sent. Please check your email.";
        return RedirectToPage();
        
    }

    StatusMessage = "Your email is unchanged.";
    return RedirectToPage();
}

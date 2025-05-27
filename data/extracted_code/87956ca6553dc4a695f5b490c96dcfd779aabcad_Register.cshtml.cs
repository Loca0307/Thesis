                
                var info = await _signInManager.GetExternalLoginInfoAsync(); //get information about the external login(github)
                 
            if (info != null)//check if any external login info is retrieved
        {
            // Check for email claim in external login
            var emailClaim = info.Principal.FindFirst(claim => claim.Type == System.Security.Claims.ClaimTypes.Email)?.Value;
            if (emailClaim != null)
            {
                Input.Email = emailClaim; // Automatically set the email if found
            }
        }
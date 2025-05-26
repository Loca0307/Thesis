LINK NUMBER 1
Error fetching diff

LINK NUMBER 2
Not enough lines

LINK NUMBER 3
Not enough lines

LINK NUMBER 4
Not enough lines

LINK NUMBER 5
Not enough lines

LINK NUMBER 6
Error fetching diff

LINK NUMBER 7
Error fetching diff

LINK NUMBER 8
Error fetching diff

LINK NUMBER 9
Not enough lines

LINK NUMBER 10

File path: src/template_rendering/template_helpers.go
"
func formatDatetime(timestamp int64) string {
	time := time.Unix(timestamp, 0).UTC()
	return time.Format(""2006-01-02 @ 15:04"")
}"

LINK NUMBER 11
Not enough lines

LINK NUMBER 12
Not enough lines

LINK NUMBER 13
Error fetching diff

LINK NUMBER 14
Error fetching diff

LINK NUMBER 15
Error fetching diff

LINK NUMBER 16

File path: src/test/conftest.py
"def init_db():
    """"""Creates the database tables.""""""
    with open(SCHEMA, ""r"") as fp:
            schema = fp.read()
    with psycopg.connect(DATABASE) as con:
        with con.cursor() as cursor:
            for statement in schema.split("";""):
                if statement.strip():  # Avoid empty statements
                    cursor.execute(statement)
            con.commit()

def reset_db():
    """"""Empty the database and initialize the schema again""""""
    with psycopg.connect(DATABASE) as con:
        with con.cursor() as cursor:
            cursor.execute(""DROP SCHEMA public CASCADE;"")
            cursor.execute(""CREATE SCHEMA public;"")  # Resets schema instead of dropping tables one by one
            con.commit()"

LINK NUMBER 17

File path: minitwit.go
"	loggedIn, _ := isUserLoggedIn(c)
    if !loggedIn {
        c.String(http.StatusUnauthorized, ""Unauthorized"")
    }
	text := c.FormValue(""text"")
	userId, err := getSessionUserID(c)
	if err != nil {
		fmt.Printf(""getSessionUserID returned error: %v\n"", err)
		return err
	}
	
	Db.Exec(`insert into message (author_id, text, pub_date, flagged)
			 values (?, ?, ?, 0)`,
			 userId, text, time.Now().Unix(),
	)

	err = addFlash(c, ""Your message was recorded"")
	if err != nil {
		fmt.Printf(""addFlash returned error: %v\n"", err)
	}

	return c.Redirect(http.StatusFound, ""/"")"

LINK NUMBER 18

File path: test/Chirp.Test/E2ETests.cs
"
    [Fact]
    public async Task RegisterNewUserTest()
    {
        // Arrange
        var client = _factory.CreateClient();
        
        var getResponse = await client.GetAsync(""/Identity/Account/Register"");
        var getContent = await getResponse.Content.ReadAsStringAsync();
        

        // Step 2: Parse the anti-forgery token from the page content
        var tokenValue = ExtractAntiForgeryToken(getContent);
        
        var registerData = new Dictionary<string, string>
        {
            {""Input.Email"",""testuser@gmail.com""},
            {""Input.Password"",""Test@12345""}, 
            {""Input.ConfirmPassword"",""Test@12345""},
            { ""__RequestVerificationToken"", tokenValue},
            {""returnUrl"",""/""}
        };
        
        // Act
        var response = await client.PostAsync(""/Identity/Account/Register"", new FormUrlEncodedContent(registerData));
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK); // Expecting HTTP 200
        var responseBody = await response.Content.ReadAsStringAsync();
        responseBody.Should().Contain(""Register confirmation""); 
    }
    
    [Fact]
    public async Task LoginUserTest()
    {
        // Arange 
        //var client = _factory.CreateClient();
        
        //var getResponse = await client.GetAsync(""/Identity/Account/Login"");
        //var 
    }
    
    // Helper method to extract anti forgery token
    private string ExtractAntiForgeryToken(string htmlContent)
    {
        // Updated regex pattern for finding the anti-forgery token value
        var match = Regex.Match(htmlContent, @""<input[^>]*name=""""__RequestVerificationToken""""[^>]*value=""""([^""""]+)"""""", RegexOptions.IgnoreCase);
        if (!match.Success)
        {
            throw new InvalidOperationException(""Anti-forgery token not found"");
        }
        return match.Groups[1].Value;
    }
"

LINK NUMBER 19

File path: src/Chirp.Web/models/MyPage.cshtml.cs
"/// <summary>
/// Represents the page model for displaying the user's timeline and handling account actions like ""Forget Me.""
/// </summary>
/// <remarks>
/// Initializes a new instance of the <see cref=""MyPage""/> class.
/// </remarks>
/// <param name=""cheepService"">The service for managing Cheep-related operations.</param>
/// <param name=""signInManager"">The service for managing sign-in actions.</param>
/// <param name=""userManager"">The service for managing user-related actions.</param>"

LINK NUMBER 20
Error fetching diff

LINK NUMBER 21
Error fetching diff

LINK NUMBER 22
Error fetching diff

LINK NUMBER 23

File path: test/Chirp.Test/E2ETests.cs
"
    [Fact]
    public async Task RegisterNewUserTest()
    {
        // Arrange
        var client = _factory.CreateClient();
        
        var getResponse = await client.GetAsync(""/Identity/Account/Register"");
        var getContent = await getResponse.Content.ReadAsStringAsync();
        

        // Step 2: Parse the anti-forgery token from the page content
        var tokenValue = ExtractAntiForgeryToken(getContent);
        
        var registerData = new Dictionary<string, string>
        {
            {""Input.Email"",""testuser@gmail.com""},
            {""Input.Password"",""Test@12345""}, 
            {""Input.ConfirmPassword"",""Test@12345""},
            { ""__RequestVerificationToken"", tokenValue},
            {""returnUrl"",""/""}
        };
        
        // Act
        var response = await client.PostAsync(""/Identity/Account/Register"", new FormUrlEncodedContent(registerData));
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK); // Expecting HTTP 200
        var responseBody = await response.Content.ReadAsStringAsync();
        responseBody.Should().Contain(""Register confirmation""); 
    }
    
    [Fact]
    public async Task LoginUserTest()
    {
        // Arange 
        //var client = _factory.CreateClient();
        
        //var getResponse = await client.GetAsync(""/Identity/Account/Login"");
        //var 
    }
    
    // Helper method to extract anti forgery token
    private string ExtractAntiForgeryToken(string htmlContent)
    {
        // Updated regex pattern for finding the anti-forgery token value
        var match = Regex.Match(htmlContent, @""<input[^>]*name=""""__RequestVerificationToken""""[^>]*value=""""([^""""]+)"""""", RegexOptions.IgnoreCase);
        if (!match.Success)
        {
            throw new InvalidOperationException(""Anti-forgery token not found"");
        }
        return match.Groups[1].Value;
    }
"

LINK NUMBER 24
Not enough lines

LINK NUMBER 25
Not enough lines

LINK NUMBER 26

File path: itu-minitwit/minitwit.test/API.Tests.cs
"    [Fact]
    public async Task PostMessage_CreatesMessageSuccessfully()
    {
        // Arrange
        var context = fixture.GetDbContext(); // This should return a properly set up in-memory context

        var user = new User { Username = ""Man"", Email = ""Man@test.com"", PwHash = ""hashedpassword"" };
        await context.Users.AddAsync(user);
        await context.SaveChangesAsync();

        var content = ""Hello from Man"";
        
        // Act
        var response = await client.PostAsync(""/msgs/Man"", new FormUrlEncodedContent(new[] { new KeyValuePair<string, string>(""content"", content) }));

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.NoContent); // Expecting 204 No Content
        var savedMessage = await context.Messages.SingleOrDefaultAsync(m => m.AuthorId == user.UserId);
        savedMessage.Should().NotBeNull();
        savedMessage.Text.Should().Be(content);
    }
    "

LINK NUMBER 27
Error fetching diff

LINK NUMBER 28
Error fetching diff

LINK NUMBER 29
Error fetching diff

LINK NUMBER 30

File path: src/Chirp.Infrastructure/Chirp.Repositories/HelperFunctions.cs
"    /// <summary>
    /// Converts a Unix timestamp to a <see cref=""DateTime""/> object.
    /// </summary>
    /// <param name=""unixTime"">The Unix timestamp to convert.</param>
    /// <returns>A <see cref=""DateTime""/> object representing the given Unix timestamp.</returns>
    /// <example>
    /// <code>
    /// long unixTime = 1725801466;
    /// DateTime dateTime = HelperFunctions.FromUnixTimeToDateTime(unixTime);
    /// Console.WriteLine(dateTime);  // Output: 9/8/2024
    /// </code>
    /// </example>"

LINK NUMBER 31

File path: test/Chirp.Razor.Tests/CheepRepositoryUnitTests.cs
"using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;

namespace Chirp.Razor.CheepRepository;

public class CheepRepositoryUnitTests : IAsyncLifetime
{
    private SqliteConnection connection;
    private ChirpDBContext context;
    private CheepRepository repository;
    
    public async Task InitializeAsync()
    {
        connection = new SqliteConnection(""DataSource=:memory:"");
        await connection.OpenAsync();
        var builder = new DbContextOptionsBuilder<ChirpDBContext>().UseSqlite(connection);

        context = new ChirpDBContext(builder.Options);
        await context.Database.EnsureCreatedAsync();

        repository = new CheepRepository(context);
    }
    
    public async Task DisposeAsync()
    {
        await connection.DisposeAsync();
        await context.DisposeAsync();
    }

	[Fact]
    public void DatabaseInitialization()
    {
        var results = repository.GetCheepsFromAuthor(""Helge"", 0);
        
        foreach (var result in results)
            Assert.Equal(""Hello, BDSA students!"", result.Message);
    }
}"

LINK NUMBER 32

File path: itu-minitwit/minitwit.web/Controllers/MessageController.cs
"

    [IgnoreAntiforgeryToken]
    [HttpGet(""msgs/{username}"")]
    public async Task<IActionResult> GetFilteredMessages(string username)
    {
        int pageSize = 100;
        await latestService.UpdateLatest(1);
        
        var user = await db.Users.FirstOrDefaultAsync(u => u.Username == username);
        if (user == null)
        {
            return new JsonResult(new { status = 404, error_msg = ""User does not exist!"" })
            {
                StatusCode = 404
            };
        }
        
        var messages = await db.Messages
            .Where(m => m.AuthorId == user.UserId && m.Flagged == 0)
            .OrderByDescending(m => m.PubDate)
            .Take(pageSize)
            .Select(m => new 
            {
                content = m.Text,
                pub_date = m.PubDate,
                user = username
            })
            .ToListAsync();

        return Ok(messages);
    }"

LINK NUMBER 33

File path: src/Chirp.Web/models/UserTimeline.cshtml.cs
"    /// <summary>
    /// Initializes a new instance of the <see cref=""UserTimelineModel""/> class.
    /// </summary>
    /// <param name=""cheepService"">The service that handles Cheep-related operations.</param>
    public UserTimelineModel(ICheepService cheepService) : base(cheepService)
    {
    }

    /// <summary>
    /// Handles the GET request to display the user's timeline along with their followers' posts.
    /// </summary>
    /// <param name=""author"">The username of the author whose timeline is being viewed.</param>
    /// <returns>An <see cref=""ActionResult""/> representing the page result.</returns>"

LINK NUMBER 34
Error fetching diff

LINK NUMBER 35
Error fetching diff

LINK NUMBER 36
Error fetching diff

LINK NUMBER 37
Not enough lines

LINK NUMBER 38
Not enough lines

LINK NUMBER 39
Not enough lines

LINK NUMBER 40

File path: src/Chirp.Web/Pages/Public.cshtml.cs
"
    public async Task<ActionResult> OnPostLike(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        //adds the cheep to the authors list of liked cheeps
        if (author.LikedCheeps != null)
        {
            author.LikedCheeps.Add(cheep);
        }
        
        cheepDto.Likes = cheepDto.Likes + 1;
        
        likedCheeps = await _authorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }
    
    public async Task<ActionResult> OnPostUnLike(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        //removes the cheep from the user's unlikes from their list of liked cheeps
        if (author.LikedCheeps != null)
        {
            author.LikedCheeps.Remove(cheep);
        }

        cheepDto.Likes = cheepDto.Likes - 1;
        
        likedCheeps = await _authorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    public async Task<bool> UserLikesCheep(CheepDTO cheepDto)
    {
        //Finds the author thats logged in
        var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }
        
        var author = await _authorRepository.FindAuthorWithEmail(authorName);
        var cheep = await _cheepRepository.GetCheepFromCheepDto(cheepDto);
        
        return await  _cheepRepository.DoesUserLikeCheep(cheep, author);
    }"

LINK NUMBER 41
Error fetching diff

LINK NUMBER 42
Error fetching diff

LINK NUMBER 43
Error fetching diff

LINK NUMBER 44

File path: src/ChirpWeb/Pages/CreatingCheep.cshtml.cs
"using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Http;
using ChirpCore.Domain;
using ChirpRepositories;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Identity;

namespace ChirpWeb.Pages
{
    public class CreateCheepModel : PageModel
    {
        private readonly ICheepRepository _repository;
        private readonly UserManager<Author> _userManager;

        public CreateCheepModel(ICheepRepository repository, UserManager<Author> userManager)
        {
            _repository = repository;
            _userManager = userManager;
        }
        [BindProperty]
        [Required(ErrorMessage = ""Please enter a message for your Cheep."")]
        [StringLength(280, ErrorMessage = ""Cheep cannot exceed 280 characters."")]
        public string CheepText { get; set; }

        //currently chat
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            try
            {
                int userId = 0;
                string userName = ""Anonymous"";

                if (User.Identity.IsAuthenticated)
                {
                    userId = int.Parse(User.FindFirst(""sub"")?.Value ?? ""0"");
                    userName = User.Identity.Name ?? ""Anonymous"";
                }

                Console.WriteLine($""Attempting to create Cheep by userId: {userId}, userName: {userName}"");
                Author author = await _userManager.FindByIdAsync(userId.ToString()) ?? await _userManager.FindByNameAsync(userName);
                // Create the Cheep object
                var newCheep = new Cheep
                {
                    CheepId = await _repository.GenerateNextCheepIdAsync(),
                    Text = CheepText,
                    TimeStamp = DateTime.UtcNow,
                    Author = author
                };

                // Save the Cheep using the repository
                await _repository.AddCheepAsync(newCheep);

                Console.WriteLine(""Cheep created successfully!"");

                return RedirectToPage(""/Index""); // Redirect after success
            }
            catch (Exception ex)
            {
                Console.WriteLine($""Error: {ex.Message}"");
                ModelState.AddModelError(string.Empty, ""An error occurred while submitting your Cheep."");
                return Page();
            }
        }

        /*public async Task<IActionResult> OnPostAsync()
        {   
            // Validate input
            if (string.IsNullOrWhiteSpace(CheepText))
            {
                ModelState.AddModelError(string.Empty, ""Message cannot be empty."");
                return Page();
            }

                // Get the user ID, or 0 for anonymous
            int userId = 0; // default for anonymous user
            string userName = ""Anonymous"";

            if (User.Identity.IsAuthenticated)
            {
                // Get the user ID if the user is authenticated (e.g., from a ClaimsPrincipal)
                //userId = int.Parse(User.Identity.Name);
                userName = User.Identity.Name; // Or use User.Claims for more specific handling
            }

            try
            {
                // Call the repository to create the new Cheep
                //int cheepId = await _repository.CreateCheepAsync(userId, Text);
                await _repository.CreateCheepAsync(userId, userName, CheepText);
                return RedirectToPage(""/Timeline""); // Redirect to the homepage

            }
            catch (Exception ex)
            {
                //ErrorMessage = $""Error creating Cheep: {ex.Message}"";
                ModelState.AddModelError(string.Empty, $""Error creating Cheep: {ex.Message}"");
                return Page();
            }
        }*/

    }
}"

LINK NUMBER 45

File path: src/Chirp.Infrastructure/CheepRepository.cs
"
    public List<CheepDTO> GetCheepsNotBlocked(string userEmail)
    {
        var query = (from Author in _context.Authors
            join Cheeps in _context.Cheeps on Author.AuthorId equals Cheeps.AuthorId
            where !_context.Blocked.Any(b => b.User.Email == userEmail && b.BlockedUser.Email == Author.Email)
            orderby Cheeps.TimeStamp descending
            select new CheepDTO
            {
                Author = Author.Name,
                Email = Author.Email,
                Message = Cheeps.Text,
                TimeStamp = ((DateTimeOffset)Cheeps.TimeStamp).ToUnixTimeSeconds(),
                CheepId = Cheeps.CheepId
            });

        return query.ToList();
    }

    public List<CheepDTO> GetLiked(string email)
    {
        var query = (from Cheep in _context.Cheeps
            join Likes in _context.Likes on Cheep.CheepId equals Likes.cheep.CheepId
            orderby Cheep.TimeStamp descending
            where Likes.User.Email == email
            select new CheepDTO
            {
                CheepId = Cheep.CheepId,
                TimeStamp = ((DateTimeOffset)Cheep.TimeStamp).ToUnixTimeSeconds(),
                Author = Cheep.Author.Name,
                Message = Cheep.Text
            });

        return query.ToList();
    }

    public List<Cheep> GetCheep(string userEmail, int cheepId)
    {
        var query = (from Cheep in _context.Cheeps
            where Cheep.Author.Email == userEmail && Cheep.CheepId == cheepId
            select Cheep);

        return query.ToList();
    }

    public List<Cheep> GetCheepFromId(int cheepId)
    {
        var query = (from Cheep in _context.Cheeps
            where Cheep.CheepId == cheepId
            select Cheep);

        return query.ToList();
    }

    // Methods for adding and removing cheeps
"

LINK NUMBER 46
Not enough lines

LINK NUMBER 47
Not enough lines

LINK NUMBER 48
Error fetching diff

LINK NUMBER 49
Error fetching diff

LINK NUMBER 50
Error fetching diff

LINK NUMBER 51
Not enough lines

LINK NUMBER 52

File path: src/Infrastructure/Migrations/CheepDbContextModelSnapshot.cs
"            modelBuilder.Entity(""Core.Notification"", b =>
                {
                    b.Property<int>(""cheepID"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""authorID"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""authorToNotifyId"")
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""tagNotification"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""cheepID"", ""authorID"");

                    b.HasIndex(""authorToNotifyId"");

                    b.ToTable(""notifications"");
                });
"

LINK NUMBER 53

File path: test/Chirp.Tests/CheepRepositoryUnitTests.cs
"        _repository.CreateFollow(userEmail, authorEmail);
        try
        {
            _repository.CreateFollow(userEmail, authorEmail);
        }
        catch (Exception ex)
        {
            ex.GetBaseException();
        }
"

LINK NUMBER 54

File path: src/Chirp.Razor/DBFacade.cs
"    private static List<CheepViewModel> ConnectAndExecute(string query, string author)
    {
        var cheeps = new List<CheepViewModel>();
        using (var connection = new SqliteConnection($""Data Source={sqlDBFilePath}""))
        {
            connection.Open();

            var command = connection.CreateCommand();
            command.CommandText = query;
            command.Parameters.Add(""@Author"", SqliteType.Text);
            command.Parameters[""@Author""].Value = author;

            using var reader = command.ExecuteReader();
            while (reader.Read())
            {
                var message_id = reader.GetString(0);
                var author_id = reader.GetInt32(1);
                var message = reader.GetString(2);
                var date = reader.GetInt32(3);
                
                cheeps.Add(new CheepViewModel(GetAuthorFromID(author_id), message, UnixTimeStampToDateTimeString(date)));
            }
        }
        return cheeps;
    }
    "

LINK NUMBER 55
Error fetching diff

LINK NUMBER 56
Error fetching diff

LINK NUMBER 57
Error fetching diff

LINK NUMBER 58
Not enough lines

LINK NUMBER 59
Not enough lines

LINK NUMBER 60

File path: src/Chirp.Web/Areas/Identity/Pages/Account/ExternalLogin.cshtml.cs
"                    _logger.LogInformation(""User created an account using {Name} provider."", info.LoginProvider);
        
                    var userId = await _userManager.GetUserIdAsync(user);
                    var code = await _userManager.GenerateEmailConfirmationTokenAsync(user);
                    code = WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(code));
                    var callbackUrl = Url.Page(
                        ""/Account/ConfirmEmail"",
                        pageHandler: null,
                        values: new { area = ""Identity"", userId = userId, code = code },
                        protocol: Request.Scheme);
        
                    await _emailSender.SendEmailAsync(email, ""Confirm your email"",
                        $""Please confirm your account by <a href='{HtmlEncoder.Default.Encode(callbackUrl)}'>clicking here</a>."");
        
                    // If account confirmation is required, we need to show the link if we don't have a real email sender
                    if (_userManager.Options.SignIn.RequireConfirmedAccount)"

LINK NUMBER 61

File path: src/Chirp.Web/Program.cs
"        options.DefaultChallengeScheme = ""GitHub"";
    })
    .AddCookie()
    .AddGitHub(o =>
    {
        o.ClientId = builder.Configuration[""authentication_github_clientId""];
        o.ClientSecret = builder.Configuration[""authentication_github_clientSecret""];
        o.CallbackPath = ""/signin-github"";
        o.Scope.Add(""user:email"");"

LINK NUMBER 62
Error fetching diff

LINK NUMBER 63
Error fetching diff

LINK NUMBER 64
Error fetching diff

LINK NUMBER 65

File path: src/Chirp.Web/ViewComponents/TimelineViewComponent.cs
"﻿using Chirp.Web.Pages.Shared;
using Microsoft.AspNetCore.Mvc;

namespace Chirp.Web.ViewComponents;

public class TimelineViewComponent : ViewComponent
{
    public Task<IViewComponentResult> InvokeAsync(TimelineModel model)
    {
        return Task.FromResult<IViewComponentResult>(View(""Timeline""));
    }
}"

LINK NUMBER 66
Not enough lines

LINK NUMBER 67

File path: src/Chirp.Razor/DBFacade.cs
"        var schemaSQL = File.ReadAllText(""data/schema.sql"");
        ExecuteQuery(schemaSQL);

        var dumpSQL = File.ReadAllText(""data/dump.sql"");
        ExecuteQuery(dumpSQL);"

LINK NUMBER 68

File path: src/Chirp.Infrastructure/Chirp.Repositories/CheepRepository.cs
"    public async Task<List<Cheep>> GetAllCheepsFromFollowed(string author) //Made with the help of ChatGPT
    {
        var query = from cheep in _context.Cheeps
            where (from follow in _context.Follows
                    where follow.FollowsAuthorName == author
                    select follow.FollowsAuthorName)
                .Contains(cheep.Author.Name)
            select cheep;
        var result = await query.ToListAsync();
        return result;
    }
    "

LINK NUMBER 69
Error fetching diff

LINK NUMBER 70
Error fetching diff

LINK NUMBER 71
Error fetching diff

LINK NUMBER 72

File path: src/Web/Pages/Notifications.cshtml.cs
"</div> *@
<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Notifications</title>
    @*Entire script by chatgpt*@
    <script>
        async function fetchNewNotifications() {
            try {
                const response = await fetch('/Notifications?handler=NewNotifications');
                if (response.ok) {
                    const newNotifications = await response.json();
                    if (newNotifications.length > 0) {
                        appendNotifications(newNotifications);
                    }
                }
            } catch (error) {
                console.error(""Error fetching new notifications:"", error);
            }
        }

        function appendNotifications(notifications) {
            const ul = document.getElementById('notifications-list');
            notifications.forEach(notification => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <p>
                        <span>
                            <a href=""/${notification.authorName}"">${notification.authorName}</a>
                            ${notification.tagNotification ? 'tagged you!' : 'chirped!'}
                        </span>
                    </p>
                    <p>${notification.cheepContent}</p>`;
                ul.appendChild(li);
            });
        }

        setInterval(fetchNewNotifications, 5000); // Check every 5 seconds
    </script>
</head>
<body>
    <ul id=""notifications-list"">
        @foreach (var notif in Model.notifications)
        {
            <li>
                <p>
                    <span>
                        <a href=""/@notif.authorName"">@notif.authorName</a>
                        @(notif.tagNotification ? ""tagged you!"" : ""chirped!"")
                    </span>
                </p>
                <p>@notif.cheepContent</p>
            </li>
        }
    </ul>
</body>
</html>
"

LINK NUMBER 73

File path: src/ChirpInfrastructure/Migrations/20241205124342_FollowMigration.cs
"﻿// <auto-generated />
using System;
using ChirpInfrastructure;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace ChirpInfrastructure.Migrations
{
    [DbContext(typeof(ChirpDBContext))]
    [Migration(""20241205124342_FollowMigration"")]
    partial class FollowMigration
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder.HasAnnotation(""ProductVersion"", ""8.0.10"");

            modelBuilder.Entity(""AuthorAuthor"", b =>
                {
                    b.Property<int>(""AuthorId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""FollowsId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""AuthorId"", ""FollowsId"");

                    b.HasIndex(""FollowsId"");

                    b.ToTable(""AuthorFollows"", (string)null);
                });

            modelBuilder.Entity(""ChirpCore.Domain.Author"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""AccessFailedCount"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ConcurrencyStamp"")
                        .IsConcurrencyToken()
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Email"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""EmailConfirmed"")
                        .HasColumnType(""INTEGER"");

                    b.Property<bool>(""LockoutEnabled"")
                        .HasColumnType(""INTEGER"");

                    b.Property<DateTimeOffset?>(""LockoutEnd"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedEmail"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedUserName"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""PasswordHash"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""PhoneNumber"")
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""PhoneNumberConfirmed"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""SecurityStamp"")
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""TwoFactorEnabled"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""UserName"")
                        .IsRequired()
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.HasKey(""Id"");

                    b.HasIndex(""Email"")
                        .IsUnique();

                    b.HasIndex(""NormalizedEmail"")
                        .HasDatabaseName(""EmailIndex"");

                    b.HasIndex(""NormalizedUserName"")
                        .IsUnique()
                        .HasDatabaseName(""UserNameIndex"");

                    b.HasIndex(""UserName"")
                        .IsUnique();

                    b.ToTable(""AspNetUsers"", (string)null);
                });

            modelBuilder.Entity(""ChirpCore.Domain.Cheep"", b =>
                {
                    b.Property<int>(""CheepId"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""Id"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""Text"")
                        .IsRequired()
                        .HasMaxLength(160)
                        .HasColumnType(""TEXT"");

                    b.Property<DateTime>(""TimeStamp"")
                        .HasColumnType(""TEXT"");

                    b.HasKey(""CheepId"");

                    b.HasIndex(""Id"");

                    b.ToTable(""Cheeps"");
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ConcurrencyStamp"")
                        .IsConcurrencyToken()
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedName"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.HasKey(""Id"");

                    b.HasIndex(""NormalizedName"")
                        .IsUnique()
                        .HasDatabaseName(""RoleNameIndex"");

                    b.ToTable(""AspNetRoles"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRoleClaim<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ClaimType"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ClaimValue"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""RoleId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""Id"");

                    b.HasIndex(""RoleId"");

                    b.ToTable(""AspNetRoleClaims"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserClaim<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ClaimType"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ClaimValue"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""Id"");

                    b.HasIndex(""UserId"");

                    b.ToTable(""AspNetUserClaims"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserLogin<int>"", b =>
                {
                    b.Property<string>(""LoginProvider"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ProviderKey"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ProviderDisplayName"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""LoginProvider"", ""ProviderKey"");

                    b.HasIndex(""UserId"");

                    b.ToTable(""AspNetUserLogins"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserRole<int>"", b =>
                {
                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""RoleId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""UserId"", ""RoleId"");

                    b.HasIndex(""RoleId"");

                    b.ToTable(""AspNetUserRoles"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserToken<int>"", b =>
                {
                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""LoginProvider"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Value"")
                        .HasColumnType(""TEXT"");

                    b.HasKey(""UserId"", ""LoginProvider"", ""Name"");

                    b.ToTable(""AspNetUserTokens"", (string)null);
                });

            modelBuilder.Entity(""AuthorAuthor"", b =>
                {
                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""AuthorId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""FollowsId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""ChirpCore.Domain.Cheep"", b =>
                {
                    b.HasOne(""ChirpCore.Domain.Author"", ""Author"")
                        .WithMany(""Cheeps"")
                        .HasForeignKey(""Id"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation(""Author"");
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRoleClaim<int>"", b =>
                {
                    b.HasOne(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", null)
                        .WithMany()
                        .HasForeignKey(""RoleId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserClaim<int>"", b =>
                {
                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserLogin<int>"", b =>
                {
                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserRole<int>"", b =>
                {
                    b.HasOne(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", null)
                        .WithMany()
                        .HasForeignKey(""RoleId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserToken<int>"", b =>
                {
                    b.HasOne(""ChirpCore.Domain.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""ChirpCore.Domain.Author"", b =>
                {
                    b.Navigation(""Cheeps"");
                });
#pragma warning restore 612, 618
        }
    }
}"

LINK NUMBER 74

File path: src/Infrastructure/CheepService.cs
"
    public async Task<(byte[] FileData, string ContentType, string FileName)> DownloadAuthorInfo(Author author)
    {
        var name = author.UserName;
        var email = author.Email;
        
        // var followingList = await GetFollowingAuthorsAsync(name);
        // var userCheeps = await cheepRepository.ReadCheeps(-1, 0, );
        
        // Create the textfile
        var content = new StringBuilder();
        content.AppendLine($""{name}'s information:"");
        content.AppendLine($""-----------------------"");
        content.AppendLine($""Name: {name}"");
        content.AppendLine($""Email: {email}"");
        
        content.AppendLine(""Following:"");
        if (author.FollowingList != null && author.FollowingList.Count != 0)
        {
            foreach (var following in author.FollowingList)
            {
                content.AppendLine($""- {following.UserName}"");
            }
        }
        else content.AppendLine(""- No following"");
        
        content.AppendLine(""Cheeps:"");
        if (author.Cheeps != null && author.Cheeps.Count != 0)
        {
            foreach (var cheep in author.Cheeps)
            {
                content.AppendLine($""- \""{cheep.Text}\"" ({cheep.TimeStamp})"");
            }
        }
        else content.AppendLine(""- No Cheeps posted yet"");

        // Convert content into bytes and return file
        var fileBytes = Encoding.UTF8.GetBytes(content.ToString());
        const string contentType = ""text/plain"";
        var fileName = $""{name}_Chirp_data.txt"";
        return (fileBytes, contentType, fileName);
    }"

LINK NUMBER 75
Not enough lines

LINK NUMBER 76
Error fetching diff

LINK NUMBER 77
Error fetching diff

LINK NUMBER 78
Error fetching diff

LINK NUMBER 79

File path: .github/workflows/scripts/move-issue.js
"// Made by ChatGPT
const { graphql } = require(""@octokit/graphql"");

const moveIssue = async (token, issueId, columnName) => {
  const graphqlWithAuth = graphql.defaults({
    headers: {
      authorization: `token ${token}`,
    },
  });

  // Query your project to get column IDs
  const projectData = await graphqlWithAuth(`
    query {
      user(login: ""ITU-BDSA2024-GROUP1"") {  // Replace with your org or user login
        projectNext(number: 1) {  // Replace with your project number
          id
          fields(first: 20) {
            nodes {
              id
              name
            }
          }
        }
      }
    }
  `);

  const columnField = projectData.user.projectNext.fields.nodes.find(
    (field) => field.name === ""Status""
  );
  
  if (!columnField) {
    throw new Error(""Column 'Status' not found in project."");
  }

  const fieldId = columnField.id;

  // Move the issue to the desired column (e.g., ""In Progress"")
  const result = await graphqlWithAuth(`
    mutation {
      updateProjectNextItemField(input: {
        projectId: ""${projectData.user.projectNext.id}"",
        itemId: ""${issueId}"",
        fieldId: ""${fieldId}"",
        value: ""${columnName}""
      }) {
        projectNextItem {
          id
        }
      }
    }
  `);

  console.log(`Issue moved to '${columnName}' column successfully.`);
};

// Grab the token, issue ID, and column name from the command line args
const [_, __, token, issueId, columnName] = process.argv;

moveIssue(token, issueId, columnName)
  .then(() => console.log(""Move completed!""))
  .catch((error) => console.error(`Error moving issue: ${error.message}`));"

LINK NUMBER 80

File path: test/PlaywrightTests/UITests.cs
"        [Test]
        public async Task End_To_End_Test()
        {
            // Arrange
            var username = Faker.Name.First();
            var email = Faker.Internet.Email();
            var password = $""{Faker.Name.First()}!{Faker.Name.Last()}{Faker.RandomNumber.Next()}"";
            var message = Faker.Lorem.Sentence();
            await Page.GotoAsync(_factory.GetBaseAddress());

            // Act
            // Register
            await Page.GetByRole(AriaRole.Link, new() { Name = ""register"", Exact = true }).ClickAsync();
            await Page.GetByPlaceholder(""name@example.com"").ClickAsync();
            await Page.GetByPlaceholder(""name@example.com"").FillAsync(email);
            await Page.GetByPlaceholder(""name"", new() { Exact = true }).ClickAsync();
            await Page.GetByPlaceholder(""name"", new() { Exact = true }).FillAsync(username);
            await Page.GetByLabel(""Password"", new() { Exact = true }).ClickAsync();
            await Page.GetByLabel(""Password"", new() { Exact = true }).FillAsync(password);
            await Page.GetByLabel(""Confirm Password"").ClickAsync();
            await Page.GetByLabel(""Confirm Password"").FillAsync(password);
            await Page.GetByRole(AriaRole.Button, new() { Name = ""Register"" }).ClickAsync();

            // Assert
            // Should be logged in
            await Expect(Page.GetByRole(AriaRole.Heading, new() { Name = $""What's on your mind {username}?"" })).ToBeVisibleAsync();

            // Act
            // Post Cheep
            await Page.Locator(""#Message"").ClickAsync();
            await Page.Locator(""#Message"").FillAsync(message);
            await Page.GetByRole(AriaRole.Button, new() { Name = ""Share"" }).ClickAsync();

            // Assert
            // Cheep should be visible
            var postLocator = Page.Locator(""li"").Filter(new() { HasText = $""{username}"" }).First;
            await Expect(postLocator).ToHaveTextAsync(new Regex($"".*{message}.*""));

            // Act
            // Follow
            var posterToFollow = Page.Locator(""li"").Filter(new() { HasText = ""Follow 0"" }).GetByRole(AriaRole.Button).Nth(1);
            var posterToFollowUsername = await posterToFollow.TextContentAsync();
            await posterToFollow.ClickAsync();

            Console.WriteLine($""Text: {posterToFollowUsername}"");

            // Assert
            // Should be following
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = ""Unfollow"" })).ToBeVisibleAsync();
            await Expect(Page).ToHaveURLAsync(new Regex($"".*{posterToFollowUsername}""));

            // Act
            // Unfollow

            await Page.GetByRole(AriaRole.Button, new() { Name = ""Unfollow"" }).ClickAsync();

            // Assert
            // Should be unfollowed
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = ""Follow"" })).ToBeVisibleAsync();

            // Act
            // Like a post
            await Page.GetByRole(AriaRole.Link, new() { Name = ""public timeline"" }).ClickAsync();
            var postToLike = Page.Locator(""li"").Filter(new() { HasText = ""♡"" }).First;
            var likeButton = postToLike.GetByRole(AriaRole.Button, new() { Name = ""♡"" });
            await likeButton.ClickAsync();

            // Assert
            // Should be liked
            await Expect(Page.GetByRole(AriaRole.Button, new() { Name = ""♥"" })).ToBeVisibleAsync();
            await Expect(postToLike).ToHaveTextAsync(new Regex(@"".*1.*""));

            // Act
            // Unlike a post
            await Page.GetByRole(AriaRole.Button, new() { Name = ""♥"" }).ClickAsync();

            // Assert
            // Should be unliked
            await Expect(postToLike.GetByRole(AriaRole.Button, new() { Name = ""♡"" })).ToBeVisibleAsync();
            await Expect(postToLike).ToHaveTextAsync(new Regex(@"".*0.*""));

            // Act  
            // Logout

            await Page.GetByRole(AriaRole.Link, new() { Name = $""logout [{username}]"" }).ClickAsync();

            // Assert
            // Should be logged out
            await Expect(Page.GetByRole(AriaRole.Link, new() { Name = ""login"" })).ToBeVisibleAsync();
        }"

LINK NUMBER 81

File path: test/Chirp.RazorTest/CheepServiceUnitTest.cs
"    public static async Task<AuthorDTO[]> SetUpTestAuthorDB(IAuthorRepository authorRepository, SqliteConnection connection)
    {
        using (var command = new SqliteCommand(""DELETE FROM authors;"", connection))
        {
            command.ExecuteNonQuery();
        }

        AuthorDTO[] authors = new AuthorDTO[4];
        for (int i = 0; i < authors.Length; i++)
        {
            authors[i] = new AuthorDTO
            {
                Id = i+1,
                Name = $""Test{i+1}"",
                Email = $""Test{i+1}@Tester.com""
            };
            authors[i].Id = await authorRepository.AddAuthorAsync(authors[i]);
        }

        return authors;

    }
    public static async Task<CheepDTO[]> SetUpTestCheepDB(ICheepRepository cheepRepository, SqliteConnection connection, AuthorDTO[] authors)
    {
        using (var command = new SqliteCommand(""DELETE FROM cheeps;"", connection))
        {
            command.ExecuteNonQuery();
        }

        DateTime timeStamp = DateTime.Now;
        long timeStampLong = timeStamp.Ticks;
        CheepDTO[] cheeps = new CheepDTO[160];
        for (int i = 0; i < cheeps.Length; i++)
        {
            timeStampLong += 10000000;
            timeStamp = new DateTime(timeStampLong);
            cheeps[i] = new CheepDTO
            {
                Id = i + 1,
                Name = authors[i % authors.Length].Name,
                Message = $""Text{i + 1}"",
                TimeStamp = timeStamp.ToString(""yyyy\\-MM\\-dd HH\\:mm\\:ss""),
                AuthorId = authors[i % authors.Length].Id
            };
            cheeps[i].Id = await cheepRepository.AddCheepAsync(cheeps[i]);
        }

        Array.Reverse(cheeps);
        return cheeps;

    }


    public static void AssertCheep(CheepDTO expected, CheepDTO actual)
    {
        Assert.Equal(expected.Id, actual.Id);
        Assert.Equal(expected.Name, actual.Name);
        Assert.Equal(expected.TimeStamp, actual.TimeStamp);
        Assert.Equal(expected.AuthorId, actual.AuthorId);
        Assert.Equal(expected.Message, actual.Message);"

LINK NUMBER 82

File path: src/Chirp.Web/Areas/Identity/Pages/Account/Register.cshtml.cs
"                
                var info = await _signInManager.GetExternalLoginInfoAsync(); //get information about the external login(github)
                 
            if (info != null)//check if any external login info is retrieved
        {
            // Check for email claim in external login
            var emailClaim = info.Principal.FindFirst(claim => claim.Type == System.Security.Claims.ClaimTypes.Email)?.Value;
            if (emailClaim != null)
            {
                Input.Email = emailClaim; // Automatically set the email if found
            }
        }"

LINK NUMBER 83
Error fetching diff

LINK NUMBER 84
Error fetching diff

LINK NUMBER 85
Error fetching diff

LINK NUMBER 86
Not enough lines

LINK NUMBER 87
Not enough lines

LINK NUMBER 88

File path: itu-minitwit/minitwit.test/API.Tests.cs
"
    [Fact]
    public async Task GetFilteredMessages_returnsFilteredMessages()
    {
        var context = fixture.GetDbContext();
        var user = new User { Username = ""Man"", Email = ""Man@Man.com"", PwHash = ""23456"" };
    
        var msg = new Message { AuthorId = user.UserId, Text = ""Hello from Man"", PubDate = (int)DateTimeOffset.Now.ToUnixTimeSeconds() };
        var msg2 = new Message { AuthorId = user.UserId, Text = ""Hello again from Man"", PubDate = (int)DateTimeOffset.Now.ToUnixTimeSeconds() };

        await context.Users.AddAsync(user);
        await context.Messages.AddAsync(msg);
        await context.Messages.AddAsync(msg2);

        await context.SaveChangesAsync();

        var response = await client.GetAsync(""/msgs/Man"");
        var json = await response.Content.ReadAsStringAsync();
        

        if (response.StatusCode == HttpStatusCode.OK)
        {
            var messagesResponse = JsonConvert.DeserializeObject<MessagesResponse>(json);
            var messages = messagesResponse.Messages; // Access the messages

            foreach (var message in messages)
            {
                message.User.Should().Be(user.Username);
            }
        }
    }
    
    
    [Fact]
    public async Task GetFilteredMessagesFromNonExistentUser_returnsErrorResponse()
    {
        var context = fixture.GetDbContext();
        
        var response = await client.GetAsync(""/msgs/MysteryMan"");
        
        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
        
            
    }
    
    
    [Fact]
    public async Task GetEmptyFilteredMessages_returnsErrorResponse()
    {
        var context = fixture.GetDbContext();
        var user = new User { Username = ""Man"", Email = ""Man@Man.com"", PwHash = ""23456"" };

        await context.Users.AddAsync(user);
        await context.SaveChangesAsync();

        var response = await client.GetAsync(""/msgs/Man"");
        
        Assert.Equal(HttpStatusCode.NoContent, response.StatusCode);
    }
    
    
    public class MessageDto
    {
        public string Text { get; set; }
        public int PubDate { get; set; }
        public string User { get; set; }
    }
    
    public class MessagesResponse
    {
        public string Status { get; set; }
        public List<MessageDto> Messages { get; set; }
    }"

LINK NUMBER 89

File path: src/Chirp.Razor/Migrations/20241009084314_IntialAdd.cs
"﻿// <auto-generated />
using System;
using Chirp.Razor.CheepRepository;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace Chirp.Razor.Migrations
{
    [DbContext(typeof(ChirpDBContext))]
    [Migration(""20241009084314_IntialAdd"")]
    partial class IntialAdd
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder.HasAnnotation(""ProductVersion"", ""8.0.8"");

            modelBuilder.Entity(""Chirp.Razor.CheepRepository.Author"", b =>
                {
                    b.Property<int>(""AuthorId"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""Email"")
                        .IsRequired()
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .IsRequired()
                        .HasColumnType(""TEXT"");

                    b.HasKey(""AuthorId"");

                    b.ToTable(""Authors"");
                });

            modelBuilder.Entity(""Chirp.Razor.CheepRepository.Cheep"", b =>
                {
                    b.Property<int>(""CheepId"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""AuthorId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""Text"")
                        .IsRequired()
                        .HasColumnType(""TEXT"");

                    b.Property<DateTime>(""TimeStamp"")
                        .HasColumnType(""TEXT"");

                    b.HasKey(""CheepId"");

                    b.HasIndex(""AuthorId"");

                    b.ToTable(""Cheeps"");
                });

            modelBuilder.Entity(""Chirp.Razor.CheepRepository.Cheep"", b =>
                {
                    b.HasOne(""Chirp.Razor.CheepRepository.Author"", ""Author"")
                        .WithMany(""Cheeps"")
                        .HasForeignKey(""AuthorId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation(""Author"");
                });

            modelBuilder.Entity(""Chirp.Razor.CheepRepository.Author"", b =>
                {
                    b.Navigation(""Cheeps"");
                });
#pragma warning restore 612, 618
        }
    }
}
"

LINK NUMBER 90
Error fetching diff

LINK NUMBER 91
Error fetching diff

LINK NUMBER 92
Error fetching diff

LINK NUMBER 93

File path: src/Chirp.Web/Areas/Identity/Pages/Account/Manage/Email.cshtml.cs
"        
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
            StatusMessage = ""Unexpected error when trying to update email."";
            return RedirectToPage();
        }
        
        /*
        // Update email in the user manager with verification
        var userId = await _userManager.GetUserIdAsync(user);
        var code = await _userManager.GenerateChangeEmailTokenAsync(user, Input.NewEmail);
        code = WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(code));
        var callbackUrl = Url.Page(
            ""/Account/ConfirmEmailChange"",
            pageHandler: null,
            values: new { area = ""Identity"", userId = userId, email = Input.NewEmail, code = code },
            protocol: Request.Scheme);
        await _emailSender.SendEmailAsync(
            Input.NewEmail,
            ""Confirm your email"",
            $""Please confirm your account by <a href='{HtmlEncoder.Default.Encode(callbackUrl)}'>clicking here</a>."");
            */

        StatusMessage = ""Confirmation link to change email sent. Please check your email."";
        return RedirectToPage();
        
    }

    StatusMessage = ""Your email is unchanged."";
    return RedirectToPage();
}
"

LINK NUMBER 94

File path: Chirp/test/PlaywrightTests/CustomWebApplicationFactory.cs
"    
    private void WaitUntilServerIsAvailable(string url)
    {
        var uri = new Uri(url);
        using var client = new TcpClient();

        var maxAttempts = 5;
        var attempt = 0;

        while (attempt < maxAttempts)
        {
            try
            {
                client.Connect(uri.Host, uri.Port);
                if (client.Connected)
                {
                    break;
                }
            }
            catch
            {
                attempt++;
                Thread.Sleep(1000);
            }
        }

        if (attempt == maxAttempts)
        {
            throw new Exception(""Server did not start in time."");
        }
    }"

LINK NUMBER 95

File path: src/Chirp.Web/Areas/Identity/Pages/Account/Manage/Email.cshtml.cs
"﻿@page
@model EmailModel
@{
    ViewData[""Title""] = ""Manage Email"";
    ViewData[""ActivePage""] = ManageNavPages.Email;
}

<h3>@ViewData[""Title""]</h3>
<partial name=""_StatusMessage"" for=""StatusMessage"" />
<div class=""row"">
    <div class=""col-md-6"">
        <form id=""email-form"" method=""post"">
            <div asp-validation-summary=""All"" class=""text-danger"" role=""alert""></div>
            @if (Model.IsEmailConfirmed)
            {
                <div class=""form-floating mb-3 input-group"">
                    <div>
                        <label asp-for=""Email"" class=""form-label""></label>
                    </div>
                    <input asp-for=""Email"" class=""form-control"" placeholder=""Please enter your email."" disabled/>
                    <span class=""h-100 input-group-text text-success font-weight-bold"">✓</span>
                    <div style=""height: 20px;""></div>
                    <label class=""form-label"">Change Email:</label>
                </div>
            }
            else
            {
                <div class=""form-floating mb-3"">
                    <input asp-for=""Email"" class=""form-control"" placeholder=""Please enter your email."" disabled />
                    <label asp-for=""Email"" class=""form-label""></label>
                    <button id=""email-verification"" type=""submit"" asp-page-handler=""SendVerificationEmail"" class=""btn btn-link"">Send verification email</button>
                </div>
            }
            <div class=""form-floating mb-3"">
                <input asp-for=""Input.NewEmail"" class=""form-control"" autocomplete=""email"" aria-required=""true"" placeholder=""Please enter new email"" value="""" />
                <label asp-for=""Input.NewEmail"" class=""form-label""></label>
                <span asp-validation-for=""Input.NewEmail"" class=""text-danger""></span>
            </div>

            <button id=""change-email-button"" type=""submit"" asp-page-handler=""ChangeEmail"" class=""w-100 btn btn-lg btn-primary"">Change email</button>
        </form>
    </div>
</div>

@section Scripts {
    <partial name=""_ValidationScriptsPartial"" />
}"

LINK NUMBER 96
Not enough lines

LINK NUMBER 97
Error fetching diff

LINK NUMBER 98
Error fetching diff

LINK NUMBER 99
Error fetching diff

LINK NUMBER 100
Not enough lines

LINK NUMBER 101
Not enough lines

LINK NUMBER 102
Not enough lines

LINK NUMBER 103

File path: src/Chirp.Infrastructure/Migrations/20241204154344_NewMigration.cs
"﻿// <auto-generated />
using System;
using Chirp.Infrastructure;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace Chirp.Infrastructure.Migrations
{
    [DbContext(typeof(CheepDBContext))]
    [Migration(""20241204154344_NewMigration"")]
    partial class NewMigration
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder.HasAnnotation(""ProductVersion"", ""8.0.0"");

            modelBuilder.Entity(""AuthorCheep"", b =>
                {
                    b.Property<int>(""LikedByAuthorsId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""LikedCheepsCheepId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""LikedByAuthorsId"", ""LikedCheepsCheepId"");

                    b.HasIndex(""LikedCheepsCheepId"");

                    b.ToTable(""AuthorLikedCheeps"", (string)null);
                });

            modelBuilder.Entity(""AuthorFollows"", b =>
                {
                    b.Property<int>(""FollowedId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""FollowerId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""FollowedId"", ""FollowerId"");

                    b.HasIndex(""FollowerId"");

                    b.ToTable(""AuthorFollows"");
                });

            modelBuilder.Entity(""Chirp.Core.Author"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""AccessFailedCount"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""AuthorId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ConcurrencyStamp"")
                        .IsConcurrencyToken()
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Email"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""EmailConfirmed"")
                        .HasColumnType(""INTEGER"");

                    b.Property<bool>(""LockoutEnabled"")
                        .HasColumnType(""INTEGER"");

                    b.Property<DateTimeOffset?>(""LockoutEnd"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedEmail"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedUserName"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""PasswordHash"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""PhoneNumber"")
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""PhoneNumberConfirmed"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""SecurityStamp"")
                        .HasColumnType(""TEXT"");

                    b.Property<bool>(""TwoFactorEnabled"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""UserName"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.HasKey(""Id"");

                    b.HasIndex(""Email"")
                        .IsUnique();

                    b.HasIndex(""Name"")
                        .IsUnique();

                    b.HasIndex(""NormalizedEmail"")
                        .HasDatabaseName(""EmailIndex"");

                    b.HasIndex(""NormalizedUserName"")
                        .IsUnique()
                        .HasDatabaseName(""UserNameIndex"");

                    b.ToTable(""AspNetUsers"", (string)null);
                });

            modelBuilder.Entity(""Chirp.Core.Cheep"", b =>
                {
                    b.Property<int>(""CheepId"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""AuthorId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int?>(""Likes"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""Text"")
                        .HasMaxLength(160)
                        .HasColumnType(""TEXT"");

                    b.Property<DateTime>(""TimeStamp"")
                        .HasColumnType(""TEXT"");

                    b.HasKey(""CheepId"");

                    b.HasIndex(""AuthorId"");

                    b.ToTable(""Cheeps"");
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ConcurrencyStamp"")
                        .IsConcurrencyToken()
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""NormalizedName"")
                        .HasMaxLength(256)
                        .HasColumnType(""TEXT"");

                    b.HasKey(""Id"");

                    b.HasIndex(""NormalizedName"")
                        .IsUnique()
                        .HasDatabaseName(""RoleNameIndex"");

                    b.ToTable(""AspNetRoles"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRoleClaim<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ClaimType"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ClaimValue"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""RoleId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""Id"");

                    b.HasIndex(""RoleId"");

                    b.ToTable(""AspNetRoleClaims"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserClaim<int>"", b =>
                {
                    b.Property<int>(""Id"")
                        .ValueGeneratedOnAdd()
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""ClaimType"")
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ClaimValue"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""Id"");

                    b.HasIndex(""UserId"");

                    b.ToTable(""AspNetUserClaims"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserLogin<int>"", b =>
                {
                    b.Property<string>(""LoginProvider"")
                        .HasMaxLength(128)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ProviderKey"")
                        .HasMaxLength(128)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""ProviderDisplayName"")
                        .HasColumnType(""TEXT"");

                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""LoginProvider"", ""ProviderKey"");

                    b.HasIndex(""UserId"");

                    b.ToTable(""AspNetUserLogins"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserRole<int>"", b =>
                {
                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<int>(""RoleId"")
                        .HasColumnType(""INTEGER"");

                    b.HasKey(""UserId"", ""RoleId"");

                    b.HasIndex(""RoleId"");

                    b.ToTable(""AspNetUserRoles"", (string)null);
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserToken<int>"", b =>
                {
                    b.Property<int>(""UserId"")
                        .HasColumnType(""INTEGER"");

                    b.Property<string>(""LoginProvider"")
                        .HasMaxLength(128)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Name"")
                        .HasMaxLength(128)
                        .HasColumnType(""TEXT"");

                    b.Property<string>(""Value"")
                        .HasColumnType(""TEXT"");

                    b.HasKey(""UserId"", ""LoginProvider"", ""Name"");

                    b.ToTable(""AspNetUserTokens"", (string)null);
                });

            modelBuilder.Entity(""AuthorCheep"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""LikedByAuthorsId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne(""Chirp.Core.Cheep"", null)
                        .WithMany()
                        .HasForeignKey(""LikedCheepsCheepId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""AuthorFollows"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""FollowedId"")
                        .OnDelete(DeleteBehavior.Restrict)
                        .IsRequired();

                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""FollowerId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Chirp.Core.Cheep"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", ""Author"")
                        .WithMany(""Cheeps"")
                        .HasForeignKey(""AuthorId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation(""Author"");
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityRoleClaim<int>"", b =>
                {
                    b.HasOne(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", null)
                        .WithMany()
                        .HasForeignKey(""RoleId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserClaim<int>"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserLogin<int>"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserRole<int>"", b =>
                {
                    b.HasOne(""Microsoft.AspNetCore.Identity.IdentityRole<int>"", null)
                        .WithMany()
                        .HasForeignKey(""RoleId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Microsoft.AspNetCore.Identity.IdentityUserToken<int>"", b =>
                {
                    b.HasOne(""Chirp.Core.Author"", null)
                        .WithMany()
                        .HasForeignKey(""UserId"")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });

            modelBuilder.Entity(""Chirp.Core.Author"", b =>
                {
                    b.Navigation(""Cheeps"");
                });
#pragma warning restore 612, 618
        }
    }
}"

LINK NUMBER 104
Error fetching diff

LINK NUMBER 105
Error fetching diff

LINK NUMBER 106
Error fetching diff

LINK NUMBER 107
Not enough lines

LINK NUMBER 108

File path: src/Chirp.Web/Pages/UserTimeline.cshtml.cs
"    public async Task<ActionResult> OnPostLike(string authorDto, string text, string timeStamp, int? likes)
    {
        // Find the author that's logged in
        var authorName = User.FindFirst(""Name"")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }

        var author = await AuthorRepository.FindAuthorWithName(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp, authorDto);
        
        // Adds the cheep to the author's list of liked cheeps
        await CheepRepository.LikeCheep(cheep, author);
        
        likedCheeps = await AuthorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    
    public async Task<ActionResult> OnPostUnLike(string authorDto, string text, string timeStamp, int? likes)
    {
        // Find the author that's logged in
        var authorName = User.FindFirst(""Name"")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }

        var author = await AuthorRepository.FindAuthorWithName(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp,authorDto);
        
        await CheepRepository.UnLikeCheep(cheep, author);
        
        likedCheeps = await AuthorRepository.getLikedCheeps(author.AuthorId);
        
        return RedirectToPage();
    }

    public async Task<bool> DoesUserLikeCheep(string authorDto, string text, string timeStamp)
    {
        var authorName = User.FindFirst(""Name"")?.Value;
        if (string.IsNullOrEmpty(authorName))
        {
            throw new ArgumentException(""Author name cannot be null or empty."");
        }
        
        var author = await AuthorRepository.FindAuthorWithLikes(authorName);
        var cheep = await CheepRepository.FindCheep(text,timeStamp,authorDto);
        
        return await  CheepRepository.DoesUserLikeCheep(cheep, author);
    }
    "

LINK NUMBER 109
Not enough lines

LINK NUMBER 110
Not enough lines

LINK NUMBER 111
Error fetching diff

LINK NUMBER 112
Error fetching diff

LINK NUMBER 113
Error fetching diff

LINK NUMBER 114
Not enough lines

LINK NUMBER 115
Not enough lines

LINK NUMBER 116
Not enough lines

LINK NUMBER 117
Not enough lines

LINK NUMBER 118
Error fetching diff

LINK NUMBER 119
Error fetching diff

LINK NUMBER 120
Error fetching diff

LINK NUMBER 121
Not enough lines

LINK NUMBER 122
Not enough lines

LINK NUMBER 123
Not enough lines

LINK NUMBER 124
Not enough lines

LINK NUMBER 125
Error fetching diff

LINK NUMBER 126
Error fetching diff

LINK NUMBER 127
Error fetching diff

LINK NUMBER 128
Not enough lines

LINK NUMBER 129
Not enough lines

LINK NUMBER 130
Not enough lines

LINK NUMBER 131
Not enough lines

LINK NUMBER 132
Error fetching diff

LINK NUMBER 133
Error fetching diff

LINK NUMBER 134
Error fetching diff

LINK NUMBER 135
Not enough lines

LINK NUMBER 136
Not enough lines

LINK NUMBER 137
Not enough lines

LINK NUMBER 138

File path: src/Chirp.Web/Pages/SearchResult.cshtml.cs
"using Chirp.Core;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using Chirp.Infrastructure;
using Microsoft.AspNetCore.Identity;

namespace Chirp.Web.Pages
{
    public class SearchResultsModel : PageModel
    {
        private readonly IAuthorRepository _authorRepository;
        public readonly SignInManager<Author> _signInManager;
        public List<Author> followedAuthors { get; set; } = new List<Author>();
        string SearchText { get; set; }
        


        public SearchResultsModel(IAuthorRepository authorRepository, SignInManager<Author> signInManager)
        {
            _authorRepository = authorRepository;
            _signInManager = signInManager;
        }

        [BindProperty(SupportsGet = true)]
        public string SearchWord { get; set; }

        public List<Author> Authors { get; set; } = new List<Author>();

        public async Task OnGet()
        {
            if (!string.IsNullOrEmpty(SearchWord))
            {
                // Fetch authors filtered by the search word
                Authors = await _authorRepository.SearchAuthorsAsync(SearchWord);
                SearchText = SearchWord;
                Console.WriteLine(""THIS IS SEARCHTEXT "" + SearchText);
            }
        }
        
        public async Task<ActionResult> OnPostFollow(string followAuthorName)
        {
            //Finds the author thats logged in
            var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
            var author = await _authorRepository.FindAuthorWithEmail(authorName);
        
            //Finds the author that the logged in author wants to follow
            var followAuthor = await _authorRepository.FindAuthorWithName(followAuthorName);
        
            await _authorRepository.FollowUserAsync(author.AuthorId, followAuthor.AuthorId);
        
            //updates the current author's list of followed authors
            followedAuthors = await _authorRepository.getFollowing(author.AuthorId);

            return new RedirectToPageResult(""/SearchResults"", new { SearchWord = SearchText });
        }
        
        
        public async Task<ActionResult> OnPostUnfollow(string followAuthorName)
        {
            //Finds the author thats logged in
            var authorName = User.FindFirst(ClaimTypes.Name)?.Value;
            var author = await _authorRepository.FindAuthorWithEmail(authorName);
        
            //Finds the author that the logged in author wants to follow
            var followAuthor = await _authorRepository.FindAuthorWithName(followAuthorName);
        
            await _authorRepository.UnFollowUserAsync(author.AuthorId, followAuthor.AuthorId);
        
            //updates the current author's list of followed authors
            followedAuthors = await _authorRepository.getFollowing(author.AuthorId);
        
            Console.WriteLine(""Number of followed authors"" + followedAuthors.Count);

            return RedirectToPage(""/SearchResults"", ""jacq"");
        }
    }
}"

LINK NUMBER 139
Error fetching diff

LINK NUMBER 140
Error fetching diff

LINK NUMBER 141
Error fetching diff

LINK NUMBER 142
Not enough lines

LINK NUMBER 143
Not enough lines

LINK NUMBER 144
Not enough lines

LINK NUMBER 145
Not enough lines

LINK NUMBER 146
Error fetching diff

LINK NUMBER 147
Error fetching diff

LINK NUMBER 148
Error fetching diff

LINK NUMBER 149
Not enough lines

LINK NUMBER 150
Not enough lines

LINK NUMBER 151
Not enough lines

LINK NUMBER 152
Not enough lines

LINK NUMBER 153
Error fetching diff

LINK NUMBER 154
Error fetching diff

LINK NUMBER 155
Error fetching diff

LINK NUMBER 156
Not enough lines

LINK NUMBER 157
Not enough lines

LINK NUMBER 158
Not enough lines

LINK NUMBER 159
Not enough lines

LINK NUMBER 160
Error fetching diff

LINK NUMBER 161
Error fetching diff

LINK NUMBER 162
Error fetching diff

LINK NUMBER 163
Not enough lines

LINK NUMBER 164
Not enough lines

LINK NUMBER 165

File path: src/Chirp.Infrastructure/Repositories/AuthorRepository.cs
"    public async Task SetDarkMode(string name, bool isDarkMode)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($""Author {name} does not exist"");
        }
        author.IsDarkMode = isDarkMode;
        await _authorDb.SaveChangesAsync();
    }
    
    public async Task<bool> IsDarkMode(string name)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($""Author {name} does not exist"");
        }
        return author.IsDarkMode;
    }
    
    public async Task SetFontSizeScale(string name, int fontSizeScale)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($""Author {name} does not exist"");
        }
        author.FontSizeScale = fontSizeScale;
        await _authorDb.SaveChangesAsync();
    }
    
    public async Task<int> GetFontSizeScale(string name)
    {
        var author = await _authorDb.Authors.FirstOrDefaultAsync(a => a.Name == name);
        if (author == null)
        {
            throw new ArgumentException($""Author {name} does not exist"");
        }
        return author.FontSizeScale;
    }
    "

LINK NUMBER 166

File path: src/test/conftest.py
"BASE_URL = 'http://localhost:4567'
API_URL = f""{BASE_URL}/api""
BASE_DIR = dirname(abspath(__file__))
DATABASE = join(BASE_DIR, ""tmp"", ""mock.db"")
SCHEMA = join(BASE_DIR, ""tmp"", ""schema.sql"")"

LINK NUMBER 167
Error fetching diff

LINK NUMBER 168
Error fetching diff

LINK NUMBER 169
Error fetching diff

LINK NUMBER 170
Not enough lines

LINK NUMBER 171
Not enough lines

LINK NUMBER 172
Not enough lines

LINK NUMBER 173

File path: src/ChirpInfrastructure/AuthorRepository.cs
"		if (LoggedInAuthorUsername == null || AuthorToFollowUsername == null) {
			throw new ArgumentNullException(""Usernames null"");
		}
		Author LoggedInAuthor = GetAuthorFromUsername(LoggedInAuthorUsername);
		Author AuthorToFollow = GetAuthorFromUsername(AuthorToFollowUsername);
		if (LoggedInAuthor.Follows.Contains(AuthorToFollow))"

LINK NUMBER 174
Error fetching diff

LINK NUMBER 175
Error fetching diff

LINK NUMBER 176
Error fetching diff

LINK NUMBER 177
Not enough lines

LINK NUMBER 178
Not enough lines

LINK NUMBER 179
Not enough lines

LINK NUMBER 180
Not enough lines

LINK NUMBER 181
Error fetching diff

LINK NUMBER 182
Error fetching diff

LINK NUMBER 183
Error fetching diff

LINK NUMBER 184
Not enough lines

LINK NUMBER 185
Not enough lines

LINK NUMBER 186
Not enough lines

LINK NUMBER 187
Not enough lines

LINK NUMBER 188
Error fetching diff

LINK NUMBER 189
Error fetching diff

LINK NUMBER 190
Error fetching diff

LINK NUMBER 191
Not enough lines

LINK NUMBER 192
Not enough lines

LINK NUMBER 193
Not enough lines

LINK NUMBER 194
Not enough lines

LINK NUMBER 195
Error fetching diff

LINK NUMBER 196
Error fetching diff

LINK NUMBER 197
Error fetching diff

LINK NUMBER 198
Not enough lines

LINK NUMBER 199
Not enough lines

LINK NUMBER 200
Not enough lines

LINK NUMBER 201
Not enough lines

LINK NUMBER 202
Error fetching diff

LINK NUMBER 203
Error fetching diff

LINK NUMBER 204
Error fetching diff

LINK NUMBER 205
Not enough lines

LINK NUMBER 206
Not enough lines

LINK NUMBER 207
Not enough lines

LINK NUMBER 208
Not enough lines

LINK NUMBER 209
Error fetching diff

LINK NUMBER 210
Error fetching diff

LINK NUMBER 211
Error fetching diff

LINK NUMBER 212
Not enough lines

LINK NUMBER 213

File path: src/Chirp.Infrastructure/CheepService.cs
"        {
            Name = authors[0].Name,
            Email = authors[0].Email
        };
    }

    public void CreateAuthor(string name, string email)
    {
        _repository.CreateAuthor(name, email);
       
"

LINK NUMBER 214
Not enough lines

LINK NUMBER 215

File path: MiniTwit/Utility.cs
"using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using MiniTwit.Data;
using MiniTwit.Models;

namespace MiniTwit.Pages;

public class UserTimelineModel : PageModel
{
    private readonly ILogger<IndexModel> _logger;
    private readonly MiniTwitContext _context;

    private readonly int PER_PAGE = 30;

    public UserTimelineModel(ILogger<IndexModel> logger, MiniTwitContext context)
    {
        _logger = logger;
        _context = context;
    }

    public async Task<IActionResult> OnGet(string username)
    {
        var tempData = TempData[""message""];
        if (tempData != null)
        {
            ViewData[""message""] = tempData.ToString();
        }

        User pageUser = await _context.Users.FirstOrDefaultAsync(u => u.UserName == username);

        if (pageUser == null)
        {
            return new NotFoundResult();
        }

        if (await Utility.ValidUserIsLoggedIn(HttpContext, _context))
        {
            int loggedInUserIdFromSesssion;
            User loggedInUser;

            loggedInUserIdFromSesssion = Utility.GetUserIdFromHttpSession(HttpContext);

            loggedInUser = await Models.User.GetUserFromUserIdAsync(
                loggedInUserIdFromSesssion,
                _context
            );

            ViewData[""user""] = loggedInUser.Id;

            bool followed = _context.Followers.Any(f =>
                f.WhoId == loggedInUser.Id && f.WhomId == pageUser.Id
            );
            ViewData[""followed""] = followed;
        }

        var messagesWithUsers = await _context
            .Twits.Where(t => t.AuthorId == pageUser.Id)
            .OrderByDescending(t => t.PubDate)
            .Take(PER_PAGE)
            .Join(
                _context.Users,
                message => message.AuthorId,
                user => user.Id,
                (message, user) =>
                    new TwitViewModel
                    {
                        AuthorUsername = user.UserName,
                        Text = message.Text,
                        PubDate = message.PubDate,
                        GravatarString = Utility.GetGravatar(user.Email, 48)
                    }
            )
            .ToListAsync();

        ViewData[""twits""] = messagesWithUsers;
        ViewData[""timelineof""] = pageUser.Id;

        return Page();
    }

    public async Task<IActionResult> OnGetFollow(string username)
    {
        User whomUser;

        whomUser = await _context.Users.FirstOrDefaultAsync(u => u.UserName == username);

        if (whomUser == null)
        {
            return new NotFoundResult();
        }

        bool validUserIsLoggedIn = await Utility.ValidUserIsLoggedIn(HttpContext, _context);

        if (!validUserIsLoggedIn)
        {
            return new UnauthorizedResult();
        }

        int loggedInUserIdFromSesssion;
        User loggedInUser;

        loggedInUserIdFromSesssion = Utility.GetUserIdFromHttpSession(HttpContext);

        loggedInUser = await Models.User.GetUserFromUserIdAsync(
            loggedInUserIdFromSesssion,
            _context
        );

        if (!await Follower.DoesFollowerExistAsync(loggedInUser.Id, whomUser.Id, _context))
        {
            string sqlQuery = $""INSERT INTO Follower VALUES ({loggedInUser.Id}, {whomUser.Id})"";
            await _context.Database.ExecuteSqlRawAsync(sqlQuery);
        }

        TempData[""message""] = $""You are now following \""{whomUser.UserName}\"""";

        return await OnGet(username);
    }

    public async Task<IActionResult> OnGetUnfollow(string username)
    {
        User whomUser;

        whomUser = await _context.Users.FirstOrDefaultAsync(u => u.UserName == username);

        if (whomUser == null)
        {
            return new NotFoundResult();
        }

        if (!await Utility.ValidUserIsLoggedIn(HttpContext, _context))
        {
            return new UnauthorizedResult();
        }

        int loggedInUserIdFromSesssion;
        User loggedInUser;

        loggedInUserIdFromSesssion = Utility.GetUserIdFromHttpSession(HttpContext);

        loggedInUser = await Models.User.GetUserFromUserIdAsync(
            loggedInUserIdFromSesssion,
            _context
        );

        if (await Follower.DoesFollowerExistAsync(loggedInUser.Id, whomUser.Id, _context))
        {
            string sqlQuery =
                $""DELETE FROM Follower WHERE who_id={loggedInUser.Id} AND whom_id={whomUser.Id}"";

            await _context.Database.ExecuteSqlRawAsync(sqlQuery);
        }

        TempData[""message""] = $""You are no longer following \""{whomUser.UserName}\"""";

        return await OnGet(username);
    }
}"

LINK NUMBER 216
Error fetching diff

LINK NUMBER 217
Error fetching diff

LINK NUMBER 218
Error fetching diff

LINK NUMBER 219
Not enough lines

LINK NUMBER 220
Not enough lines

LINK NUMBER 221
Not enough lines

LINK NUMBER 222
Not enough lines

LINK NUMBER 223
Error fetching diff

LINK NUMBER 224
Error fetching diff

LINK NUMBER 225
Error fetching diff

LINK NUMBER 226
Not enough lines

LINK NUMBER 227
Not enough lines

LINK NUMBER 228

File path: test/Chirp.Tests/IntergrationTests.cs
"    private readonly WebApplicationFactory<Program> _factory;
    private readonly HttpClient _client;

    public TestGetHttpClient(WebApplicationFactory<Program> factory)
    {
        _factory = factory;
        _client = factory.CreateClient();
    }

    [Fact]
    public async void TimeLineTest()
    {
        var response = await _client.GetAsync(""/"");
        response.EnsureSuccessStatusCode();

        var publicTL = await response.Content.ReadAsStringAsync();
        Assert.Contains(""Public Timeline"", publicTL);
    }

    [Fact]
    public async void AuthorTest()
    {
        var response = await _client.GetAsync(""/Helge"");
        response.EnsureSuccessStatusCode();

        var helgeCheep = await response.Content.ReadAsStringAsync();
        Assert.Contains(""Hello, BDSA students!"", helgeCheep);
    }

    [Fact]
    public async void PrivateTimeLineTest()
    {
        var response = await _client.GetAsync(""/Adrian"");
        response.EnsureSuccessStatusCode();

        var responseString = await response.Content.ReadAsStringAsync();
        Assert.Contains(""Hej, velkommen til kurset"", responseString);
        Assert.Contains(""Adrian"", responseString);
    }
}"

LINK NUMBER 229
Not enough lines

LINK NUMBER 230
Error fetching diff

LINK NUMBER 231
Error fetching diff

LINK NUMBER 232
Error fetching diff

LINK NUMBER 233
Not enough lines

LINK NUMBER 234
Not enough lines

LINK NUMBER 235
Not enough lines

LINK NUMBER 236

File path: src/Chirp.Web/DbInitializer.cs
"            var a1 = new Author() { AuthorId = 1, Id = 1, Name = ""Roger Histand"", Email = ""Roger+Histand@hotmail.com"", Cheeps = new List<Cheep>() };
            var a2 = new Author() { AuthorId = 2, Id = 2, Name = ""Luanna Muro"", Email = ""Luanna-Muro@ku.dk"", Cheeps = new List<Cheep>() };
            var a3 = new Author() { AuthorId = 3, Id = 3, Name = ""Wendell Ballan"", Email = ""Wendell-Ballan@gmail.com"", Cheeps = new List<Cheep>() };
            var a4 = new Author() { AuthorId = 4, Id = 4, Name = ""Nathan Sirmon"", Email = ""Nathan+Sirmon@dtu.dk"", Cheeps = new List<Cheep>() };
            var a5 = new Author() { AuthorId = 5, Id = 5, Name = ""Quintin Sitts"", Email = ""Quintin+Sitts@itu.dk"", Cheeps = new List<Cheep>() };
            var a6 = new Author() { AuthorId = 6, Id = 6, Name = ""Mellie Yost"", Email = ""Mellie+Yost@ku.dk"", Cheeps = new List<Cheep>() };
            var a7 = new Author() { AuthorId = 7, Id = 7, Name = ""Malcolm Janski"", Email = ""Malcolm-Janski@gmail.com"", Cheeps = new List<Cheep>() };
            var a8 = new Author() { AuthorId = 8, Id = 8, Name = ""Octavio Wagganer"", Email = ""Octavio.Wagganer@dtu.dk"", Cheeps = new List<Cheep>() };
            var a9 = new Author() { AuthorId = 9, Id = 9, Name = ""Johnnie Calixto"", Email = ""Johnnie+Calixto@itu.dk"", Cheeps = new List<Cheep>() };
            var a10 = new Author() { AuthorId = 10, Id = 10, Name = ""Jacqualine Gilcoine"", Email = ""Jacqualine.Gilcoine@gmail.com"", Cheeps = new List<Cheep>() };
            var a11 = new Author() { AuthorId = 11, Id = 11, Name = ""Helge"", Email = ""ropf@itu.dk"", Cheeps = new List<Cheep>() };
            var a12 = new Author() { AuthorId = 12, Id = 12, Name = ""Adrian"", Email = ""adho@itu.dk"", Cheeps = new List<Cheep>() };"

LINK NUMBER 237
Error fetching diff

LINK NUMBER 238
Error fetching diff

LINK NUMBER 239
Error fetching diff

LINK NUMBER 240
Not enough lines

LINK NUMBER 241
Not enough lines

LINK NUMBER 242

File path: MiniTwitAPI/Controllers/MsgsController.cs
"using Microsoft.AspNetCore.Mvc;
using MiniTwitInfra.Models.DataModels;
using MiniTwitInfra.Data;
using Microsoft.Extensions.Caching.Memory;
using Newtonsoft.Json;
using Microsoft.EntityFrameworkCore;

using System.ComponentModel.DataAnnotations;



namespace MiniTwitAPI.Controllers;

[Route(""/fllws"")]
[ApiController]
public class FollowController : ControllerBase
{
    private readonly MiniTwitContext _context;
    private readonly IMemoryCache _memoryCache;
    public string cacheKey = ""latest"";


    public FollowController(MiniTwitContext context, IMemoryCache memoryCache)
    {
        _context = context;
        _memoryCache = memoryCache;
    }

    /// <summary>
    /// Used to get a given no. of follow for the a given user
    /// </summary>
    /// <param name=""no""></param>
    /// <param name=""latest""></param>
    /// <returns></returns>
    [HttpGet]
    public async Task<ActionResult<IEnumerable<int>>> GetFollow(string username, int no, int latest)
    {
        _memoryCache.Set(cacheKey, latest.ToString());

        User user;
        try
        {
            user = _context.Users.FirstOrDefault(u => u.UserName == username);
        }
        catch (ArgumentException e)
        {
            throw new ArgumentException(e.Message);
        }

        var followingIds = _context
        .Followers.Where(f => f.WhoId == user.Id)
        .Select(f => f.WhomId)
        .ToList();

        Response.ContentType = ""application/json"";
        return followingIds;

    }

    [HttpPost]
    public async Task<ActionResult<string>> FollowAction(string username, int latest)
    {
        _memoryCache.Set(cacheKey, latest.ToString());

        string body;
        using (StreamReader stream = new StreamReader(HttpContext.Request.Body))
        {
            body = await stream.ReadToEndAsync();
        }

        Dictionary<string, string> dataDic = JsonConvert.DeserializeObject<Dictionary<string, string>>(body);

        Response.ContentType = ""application/json"";

        if (dataDic.ContainsKey(""follow""))
        {
            // followed person 
            User user;
            User whom;
            try
            {
                user = _context.Users.FirstOrDefault(u => u.UserName == username);
                whom = _context.Users.FirstOrDefault(u => u.UserName == dataDic[""follow""]);
            }
            catch (ArgumentException e)
            {
                throw new ArgumentException(e.Message);
            }

            string sqlQuery = $""INSERT INTO Follower VALUES ({user.Id}, {whom.Id})"";
            await _context.Database.ExecuteSqlRawAsync(sqlQuery);

            return ""successful followed person"";

        }
        else if (dataDic.ContainsKey(""unfollow""))
        {
            // unfollow person
            User user;
            User whom;
            try
            {
                user = _context.Users.FirstOrDefault(u => u.UserName == username);
                whom = _context.Users.FirstOrDefault(u => u.UserName == dataDic[""unfollow""]);
            }
            catch (ArgumentException e)
            {
                throw new ArgumentException(e.Message);
            }

            string sqlQuery =
            $""DELETE FROM Follower WHERE who_id={user.Id} AND whom_id={whom.Id}"";
            await _context.Database.ExecuteSqlRawAsync(sqlQuery);
            return ""successful Unfollowed person"";
        }

        Response.ContentType = ""application/json"";
        return ""Error Eccour"";
    }

}
"

LINK NUMBER 243
Not enough lines

LINK NUMBER 244
Error fetching diff

LINK NUMBER 245
Error fetching diff

LINK NUMBER 246
Error fetching diff

LINK NUMBER 247
Not enough lines

LINK NUMBER 248
Not enough lines

LINK NUMBER 249
Not enough lines

LINK NUMBER 250

File path: test/Chirp.CLI.Tests/Chirp.CLI.IntegrationTests.cs
"    
    [Fact]
    public void CsvToCheepInConsole() //tror den er e2e
    {
        // Arrange
        string path = ""../../../../../data/CsvParseTest.csv"";

        // Act
        var cheeps = CSVParser.Parse<Cheep>(path);
        using (var consoleOutput = new StringWriter())
        {
            Console.SetOut(consoleOutput);


            // Act
            UserInterface.PrintCheeps(cheeps);
            var outputLines = consoleOutput.ToString().Trim().Split(Environment.NewLine); //source: https://stackoverflow.com/a/22878533 .newLine sikrer at det virker både på mac og windows


            // Assert
            Assert.Equal(""ageh @ 01/08/23 14:09:20: SIIIIIUUUUUUUU!"", outputLines[0].Trim());
            Assert.Equal(""nitn @ 02/08/23 14:19:38: Recently engaged"", outputLines[1].Trim());
        }
    }"

LINK NUMBER 251
Error fetching diff

LINK NUMBER 252
Error fetching diff

LINK NUMBER 253
Error fetching diff

LINK NUMBER 254
Not enough lines

LINK NUMBER 255
Not enough lines

LINK NUMBER 256

File path: services/userService.js
"const sqlite3 = require('sqlite3').verbose();

class UserService {
    constructor() {
        this.db = new sqlite3.Database('./db/minitwit.db', sqlite3.OPEN_READWRITE, (err) => {
            if (err) {
                console.error(err.message);
            } else {
                console.log('Added db connection from user service');
            }
        });
    }

    async addMessage(userId, messageContent, currentDate) {
        const flagged = 0;
        const sql = `INSERT INTO message (author_id, text, pub_date, flagged) VALUES (?, ?, ?, ?)`;
        return new Promise((resolve, reject) => {
            this.db.run(sql, [userId, messageContent, currentDate, flagged], (err) => {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    }

    async getMessagesByUserId(id) {
        const sql = `SELECT message.text, message.pub_date, message.flagged, user.username, user.email 
                    FROM message
                    JOIN user ON message.author_id = user.user_id
                    WHERE message.flagged != 1 AND message.author_id = ?
                    ORDER BY message.pub_date DESC
                    LIMIT 50`;
        return new Promise((resolve, reject) => {
            this.db.all(sql, [id], (err, messages) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(messages);
                }
            });
        });
    }

    async getMessagesFromUserAndFollowedUsers(userId) {
        const sql = `SELECT message.text, message.pub_date, message.flagged, user.username, user.email 
                    FROM message
                    JOIN user ON message.author_id = user.user_id
                    JOIN follower ON user.user_id = follower.who_id
                    WHERE message.flagged != 1 AND (follower.whom_id = message.author_id OR message.author_id = ?)
                    ORDER BY message.pub_date DESC
                    LIMIT 50`;
        return new Promise((resolve, reject) => {
            this.db.all(sql, [userId], (err, messages) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(messages);
                }
            });
        });
    }

    async getPublicTimelineMessages() {
        const sql = `SELECT message.text, message.pub_date, message.flagged, user.username, user.email 
                    FROM message
                    JOIN user ON message.author_id = user.user_id
                    WHERE message.flagged != 1
                    ORDER BY message.pub_date DESC
                    LIMIT 50`;
        return new Promise((resolve, reject) => {
            this.db.all(sql, [], (err, messages) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(messages);
                }
            });
        });
    }

    async getUserIdByUsername(username) {
        const sql = `SELECT user_id FROM user 
                    JOIN message m 
                    ON m.author_id = user.user_id 
                    WHERE user.username = ?`;
        return new Promise((resolve, reject) => {
            this.db.get(sql, [username], (err, row) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(row ? row.user_id : null);
                }
            });
        });
    }
}

module.exports = UserService;"

LINK NUMBER 257
Not enough lines

LINK NUMBER 258
Error fetching diff

LINK NUMBER 259
Error fetching diff

LINK NUMBER 260
Error fetching diff

LINK NUMBER 261
Not enough lines

LINK NUMBER 262

File path: backend/repository/repository.go
"
func NewServer() Server {
	db, err := gorm.Open(sqlite.Open(""../tmp/minitwit.db""), &gorm.Config{})

	if err != nil {
		log.Fatalln(""Could not open Database"", err)
	}

	s := Server{
		r:  mux.NewRouter(),
		db: db,
	}

	return s
}

func (s *Server) StartServer() {
	log.Println(""Starting server on port"", port)
	log.Fatal(http.ListenAndServe(port, s.r))
}

func (s *Server) InitRoutes() error {
	repo := repository.CreateRepository(s.db)
	rH := handler.CreateRegisterHandler(repo)
	lH := handler.CreateLoginHandler(repo)

	s.r.Handle(""/register"", mw.Auth(http.HandlerFunc(rH.RegisterHandler)))
	s.r.Handle(""/login"", mw.Auth(http.HandlerFunc(lH.LoginHandler)))

	s.r.PathPrefix(""/static/"").Handler(http.StripPrefix(""/static/"", http.FileServer(http.Dir(""web/static""))))

	// s.Get(""/latest"", s.LatestHandler)
	// s.Post(""/sim/register"", s.RegisterSimHandler)

	// s.Get(""/msgs/{username}"", s.GetUserMsgsHandler)
	// s.Post(""/msgs/{username}"", s.PostUserMsgsHandler)
	// s.Get(""/msgs"", s.MsgsHandler)
	// s.Get(""/fllws/{username}"", s.GetUserFollowsHandler)
	// s.Post(""/fllws/{username}"", s.PostUserFollowsHandler)

	return nil
}

func (s *Server) InitDB() error {
	err := s.db.AutoMigrate(
		&model.User{},
		&model.Follower{},
		&model.Message{},
	)
	return err
}"

LINK NUMBER 263
Not enough lines

LINK NUMBER 264
Not enough lines

LINK NUMBER 265
Error fetching diff

LINK NUMBER 266
Error fetching diff

LINK NUMBER 267
Error fetching diff

LINK NUMBER 268

File path: src/Chirp.Web/Areas/Identity/Pages/Account/Manage/ManageNavPages.cs
"// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.
#nullable disable

using System;
using System.ComponentModel.DataAnnotations;
using System.Security.Claims;
using System.Text;
using System.Text.Encodings.Web;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.Extensions.Options;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.UI.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.WebUtilities;
using Microsoft.Extensions.Logging;
using Chirp.Infrastructure;

namespace Chirp.Web.Areas.Identity.Pages.Account
{
    [AllowAnonymous]
    public class ExternalLoginModel : PageModel
    {
        private readonly SignInManager<ChirpUser> _signInManager;
        private readonly UserManager<ChirpUser> _userManager;
        private readonly IUserStore<ChirpUser> _userStore;
        private readonly IUserEmailStore<ChirpUser> _emailStore;
        private readonly IEmailSender _emailSender;
        private readonly ILogger<ExternalLoginModel> _logger;

        public ExternalLoginModel(
            SignInManager<ChirpUser> signInManager,
            UserManager<ChirpUser> userManager,
            IUserStore<ChirpUser> userStore,
            ILogger<ExternalLoginModel> logger,
            IEmailSender emailSender)
        {
            _signInManager = signInManager;
            _userManager = userManager;
            _userStore = userStore;
            _emailStore = GetEmailStore();
            _logger = logger;
            _emailSender = emailSender;
        }

        /// <summary>
        ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
        ///     directly from your code. This API may change or be removed in future releases.
        /// </summary>
        [BindProperty]
        public InputModel Input { get; set; }

        /// <summary>
        ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
        ///     directly from your code. This API may change or be removed in future releases.
        /// </summary>
        public string ProviderDisplayName { get; set; }

        /// <summary>
        ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
        ///     directly from your code. This API may change or be removed in future releases.
        /// </summary>
        public string ReturnUrl { get; set; }

        /// <summary>
        ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
        ///     directly from your code. This API may change or be removed in future releases.
        /// </summary>
        [TempData]
        public string ErrorMessage { get; set; }

        /// <summary>
        ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
        ///     directly from your code. This API may change or be removed in future releases.
        /// </summary>
        public class InputModel
        {
            /// <summary>
            ///     This API supports the ASP.NET Core Identity default UI infrastructure and is not intended to be used
            ///     directly from your code. This API may change or be removed in future releases.
            /// </summary>
            [Required]
            [EmailAddress]
            public string Email { get; set; }
        }

        public IActionResult OnGet() => RedirectToPage(""./Login"");

        public IActionResult OnPost(string provider, string returnUrl = null)
        {
            // Request a redirect to the external login provider.
            var redirectUrl = Url.Page(""./ExternalLogin"", pageHandler: ""Callback"", values: new { returnUrl });
            var properties = _signInManager.ConfigureExternalAuthenticationProperties(provider, redirectUrl);

            return new ChallengeResult(provider, properties);
        }

        public async Task<IActionResult> OnGetCallbackAsync(string returnUrl = null, string remoteError = null)
        {
            returnUrl = returnUrl ?? Url.Content(""~/"");
            if (remoteError != null)
            {
                ErrorMessage = $""Error from external provider: {remoteError}"";
                return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
            }

            var info = await _signInManager.GetExternalLoginInfoAsync();
            if (info == null)
            {
                ErrorMessage = ""Error loading external login information."";
                return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
            }

            // Attempt to sign in the user with the external login info
            var result = await _signInManager.ExternalLoginSignInAsync(info.LoginProvider, info.ProviderKey, isPersistent: false, bypassTwoFactor: true);
            if (result.Succeeded)
            {
                _logger.LogInformation(""{Name} logged in with {LoginProvider} provider."", info.Principal.Identity.Name, info.LoginProvider);
                return LocalRedirect(returnUrl);
            }
            if (result.IsLockedOut)
            {
                return RedirectToPage(""./Lockout"");
            }

            // If user doesn't exist, create the user automatically and log them in
            var email = info.Principal.FindFirstValue(ClaimTypes.Email);
            var userName = info.Principal.FindFirstValue(ClaimTypes.Name);

            if (email == null)
            {
                ErrorMessage = ""Email not provided by external provider."";
                return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
            }

            var user = new ChirpUser
            {
                UserName = userName,
                Email = email
            };

            var createResult = await _userManager.CreateAsync(user);
            if (createResult.Succeeded)
            {
                var addLoginResult = await _userManager.AddLoginAsync(user, info);
                if (addLoginResult.Succeeded)
                {
                    _logger.LogInformation(""User created and logged in with {LoginProvider} provider."", info.LoginProvider);

                    await _signInManager.SignInAsync(user, isPersistent: false, info.LoginProvider);
                    return LocalRedirect(returnUrl);
                }
            }

            foreach (var error in createResult.Errors)
            {
                ModelState.AddModelError(string.Empty, error.Description);
            }

            // If creation or login failed, redirect to login with an error
            return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
        }
        public async Task<IActionResult> OnPostConfirmationAsync(string returnUrl = null)
        {
            returnUrl = returnUrl ?? Url.Content(""~/"");
            // Get the information about the user from the external login provider
            var info = await _signInManager.GetExternalLoginInfoAsync();
            if (info == null)
            {
                ErrorMessage = ""Error loading external login information during confirmation."";
                return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
            }

            if (ModelState.IsValid)
            {
                var user = CreateUser();

                // Use the email provided by the external login provider directly
                var userEmail = info.Principal.FindFirstValue(ClaimTypes.Email);
                var userName = info.Principal.FindFirstValue(ClaimTypes.Name);

                Console.WriteLine($""{userName} {userEmail}"");

                await _userStore.SetUserNameAsync(user, userName, CancellationToken.None);
                await _emailStore.SetEmailAsync(user, Input.Email, CancellationToken.None);

                var result = await _userManager.CreateAsync(user);
                if (result.Succeeded)
                {
                    result = await _userManager.AddLoginAsync(user, info);
                    if (result.Succeeded)
                    {
                        _logger.LogInformation(""User created an account using {Name} provider."", info.LoginProvider);

                        // Skip email confirmation and sign the user in directly
                        await _signInManager.SignInAsync(user, isPersistent: false, info.LoginProvider);
                        return LocalRedirect(returnUrl);
                    }
                }
                foreach (var error in result.Errors)
                {
                    ModelState.AddModelError(string.Empty, error.Description);
                }
            }

            ProviderDisplayName = info.ProviderDisplayName;
            ReturnUrl = returnUrl;
            return Page();
        }


        private ChirpUser CreateUser()
        {
            try
            {
                return Activator.CreateInstance<ChirpUser>();
            }
            catch
            {
                throw new InvalidOperationException($""Can't create an instance of '{nameof(ChirpUser)}'. "" +
                    $""Ensure that '{nameof(ChirpUser)}' is not an abstract class and has a parameterless constructor, or alternatively "" +
                    $""override the external login page in /Areas/Identity/Pages/Account/ExternalLogin.cshtml"");
            }
        }

        private IUserEmailStore<ChirpUser> GetEmailStore()
        {
            if (!_userManager.SupportsUserEmail)
            {
                throw new NotSupportedException(""The default UI requires a user store with email support."");
            }
            return (IUserEmailStore<ChirpUser>)_userStore;
        }
    }
}"

LINK NUMBER 269
Not enough lines

LINK NUMBER 270

File path: src/Chirp.Web/Pages/Shared/SubmitCheepComponent.cshtml.cs
"﻿using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Chirp.Web.Pages;

namespace Chirp.Web.Pages.Shared;

public class SubmitCheepComponent : ViewComponent
{
    public void OnGet()
    {
        
    }
}"

LINK NUMBER 271

File path: src/Chirp.CSVDB/CSVDatabase.cs
"        private string _filePath;

        public CsvDatabase(string filePath)
        {
            _filePath = filePath;
        }

        public void AddCheep(Cheep cheep)
        {
            using (var sw = new StreamWriter(_filePath, append: true))
            using (var csv = new CsvWriter(sw, CultureInfo.InvariantCulture))
            {
                csv.WriteRecord(cheep);
                sw.WriteLine();
            }
        }

        public List<String> GetCheeps()
        {
            List<string> cheepsList = new List<string>();

            using (StreamReader sr = new StreamReader(_filePath))
            using (var csv = new CsvReader(sr, CultureInfo.InvariantCulture))
            {
                while (csv.Read())
                {
                    var cheep = csv.GetRecord<Cheep>();
                    cheepsList.Add($""{cheep.Author} @ {TimeStampConversion(cheep.Timestamp)}: {cheep.Message}"");
                }
            }

            return cheepsList;
        }
        static string TimeStampConversion(long unix)
        {
            DateTimeOffset dto = DateTimeOffset.FromUnixTimeSeconds(unix);
            string Date = dto.ToString(""dd/MM/yyyy HH:mm:ss"");
            return Date;
        }"

LINK NUMBER 272
Error fetching diff

LINK NUMBER 273
Error fetching diff

LINK NUMBER 274
Error fetching diff

LINK NUMBER 275

File path: src/Chirp.CLI.Client/Program.cs
"        public static void Main(string[] args)
        {
            try
            {
                switch (args[0])
                {
                    case ""read"":
                        Read();
                        break;

                    case ""cheep"":
                        CheepWrite(args.Skip(1).ToArray());
                        break;

                    default:
                        Console.WriteLine(""Error: Invalid command."");
                        break;
                }
            }
            catch (IndexOutOfRangeException e)
            {
                Console.WriteLine(""Error: "" + e.Message);
                Console.WriteLine(""It appears that you did not specify a command."");
                Console.WriteLine(""* Try: read or cheep"");"

LINK NUMBER 276
Not enough lines

LINK NUMBER 277
Not enough lines

LINK NUMBER 278
Not enough lines

LINK NUMBER 279
Error fetching diff

LINK NUMBER 280
Error fetching diff

LINK NUMBER 281
Error fetching diff

LINK NUMBER 282
Not enough lines

LINK NUMBER 283

File path: src/Chirp.Web/Pages/Public.cshtml.cs
"    /// <summary>
    /// Initializes a new instance of public timeline.
    /// </summary>
    /// <param name=""cheepRepo""></param>
    /// <param name=""authorRepo""></param>"

LINK NUMBER 284
Not enough lines

LINK NUMBER 285
Not enough lines

LINK NUMBER 286
Error fetching diff

LINK NUMBER 287
Error fetching diff

LINK NUMBER 288
Error fetching diff

LINK NUMBER 289
Not enough lines

LINK NUMBER 290
Not enough lines

LINK NUMBER 291

File path: src/Chirp.CLI/Program.cs
"                IDatabase<Cheep> db = new CSVDatabase<Cheep>();
                //Read cheeps
                if (options.CheepCount != null)
                {

                    var cheeps = db.Read(options.CheepCount.Value);
                    UserInterface.PrintCheeps(cheeps);
                }

                //Cheep a cheep
                if (!string.IsNullOrWhiteSpace(options.CheepMessage))
                {

                    string Author = Environment.UserName;
                    string Message = options.CheepMessage;
                    long Timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();

                    db.Store(new Cheep(Author, Message, Timestamp));

                    UserInterface.PrintMessage($""Cheeped a cheep! The cheep is: {options.CheepMessage}"");
                }
"

LINK NUMBER 292
Not enough lines

LINK NUMBER 293
Error fetching diff

LINK NUMBER 294
Error fetching diff

LINK NUMBER 295
Error fetching diff

LINK NUMBER 296
Not enough lines

LINK NUMBER 297
Too many lines

LINK NUMBER 298

File path: MiniTwit/Areas/Api/Controllers/FollowerController.cs
"                        // Save changes to the database
                        await _context.SaveChangesAsync();
                        return Ok($""You are now following \""{whom.UserName}\"""");
                    }
                    else
                    {
                        return BadRequest(""You are already not following the user"");
                    }
                }
                else
                {
                    return NotFound(""Follower user not found"");
                }"

LINK NUMBER 299

File path: src/Chirp.WebService/Pages/Public.cshtml.cs
"
        totalCheeps = Cheeps.Count;
        cheepsPerPage = 32;

        if (page == 0) 
        {
            page = 1;
        }"

LINK NUMBER 300
Error fetching diff

LINK NUMBER 301
Error fetching diff

LINK NUMBER 302
Error fetching diff

LINK NUMBER 303
Not enough lines

LINK NUMBER 304
Not enough lines

LINK NUMBER 305
Not enough lines

LINK NUMBER 306

File path: tools/machine-learning/mujoco/standup.py
"from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import get_device
from stable_baselines3.common.vec_env import DummyVecEnv, VecVideoRecorder
from wandb.integration.sb3 import WandbCallback

if get_device() != torch.device(""cpu""):
    NVIDIA_ICD_CONFIG_PATH = ""/usr/share/glvnd/egl_vendor.d/10_nvidia.json""
    if not os.path.exists(NVIDIA_ICD_CONFIG_PATH):
        with open(NVIDIA_ICD_CONFIG_PATH, ""w"") as f:
            _ = f.write(""""""{
                                ""file_format_version"" : ""1.0.0"",
                                ""ICD"" : {
                                    ""library_path"" : ""libEGL_nvidia.so.0""
                                }
                            }"""""")

    # Configure MuJoCo to use the EGL rendering backend (requires GPU)
    os.environ[""MUJOCO_GL""] = ""egl""


# taken from https://gymnasium.farama.org/main/_modules/gymnasium/wrappers/record_video/
def capped_cubic_video_schedule(episode_id: int) -> bool:
    """"""The default episode trigger.

    This function will trigger recordings at the episode indices 0, 1, 8, 27, ..., :math:`k^3`, ..., 729, 1000, 2000, 3000, ...

    Args:
        episode_id: The episode number

    Returns:
        If to apply a video schedule number
    """"""
    if episode_id < 10000:
        return int(round(episode_id ** (1.0 / 3))) ** 3 == episode_id
    else:
        return episode_id % 10000 == 0


gym.register(
    id=""NaoStandup-v1"",
    entry_point=""nao_env:NaoStandup"",
    max_episode_steps=2500,
)

config = {
    ""policy_type"": ""MlpPolicy"",
    ""total_timesteps"": 1000000,
    ""env_name"": ""NaoStandup-v1"",
    ""render_mode"": ""rgb_array"",
}
"

LINK NUMBER 307
Error fetching diff

LINK NUMBER 308
Error fetching diff

LINK NUMBER 309
Error fetching diff

LINK NUMBER 310
Not enough lines

LINK NUMBER 311
Not enough lines

LINK NUMBER 312
Not enough lines

LINK NUMBER 313

File path: Chirp.CLI/obj/Debug/net7.0/Chrip.CLI.GlobalUsings.g.cs
"is_global = true
build_property.TargetFramework = net7.0
build_property.TargetPlatformMinVersion = 
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = Chrip.CLI
build_property.ProjectDir = /Users/bergurdavidsen/Downloads/Chirp/Chirp.CLI/"

LINK NUMBER 314
Error fetching diff

LINK NUMBER 315
Error fetching diff

LINK NUMBER 316
Error fetching diff

LINK NUMBER 317

File path: src/overworld.js
"// Credit: ChatGPT - https://chat.openai.com/share/a1af86f5-0449-4215-9bab-61b70ea4de84

function doPolygonsIntersect(polygon1, polygon2) {
  function getAxes(polygon) {
    const axes = [];
    const points = polygon.length;

    for (let i = 0; i < points; i++) {
      const p1 = polygon[i];
      const p2 = polygon[(i + 1) % points];
      const edge = { x: p2.x - p1.x, y: p2.y - p1.y };
      const normal = { x: -edge.y, y: edge.x };
      axes.push(normal);
    }

    return axes;
  }

  function project(polygon, axis) {
    const points = polygon.length;
    let min = Infinity;
    let max = -Infinity;

    for (let i = 0; i < points; i++) {
      const dotProduct = polygon[i].x * axis.x + polygon[i].y * axis.y;
      if (dotProduct < min) min = dotProduct;
      if (dotProduct > max) max = dotProduct;
    }

    return { min, max };
  }

  function overlap(projection1, projection2) {
    return (
      projection1.min <= projection2.max && projection1.max >= projection2.min
    );
  }

  const axes1 = getAxes(polygon1);
  const axes2 = getAxes(polygon2);

  for (const axis of [...axes1, ...axes2]) {
    const projection1 = project(polygon1, axis);
    const projection2 = project(polygon2, axis);

    if (!overlap(projection1, projection2)) {
      return false; // No collision, early exit
    }
  }

  return true; // Collided on all axes, there is a collision
}

export default function isBoatColliding(boat, walls) {
  for (const wall of walls) {
    if (doPolygonsIntersect(boat, wall)) {
      return wall; // Collision detected
    }
  }

  return false; // No collision
}"

LINK NUMBER 318

File path: src/Chirp.DBService/Repositories/CheepRepository.cs
"
    public List<Cheep> GetCheepsFromAuthorNameForPage(string authorName, int pageNumber)
    {
        return GetCheepsFromAuthorNameWithAuthors(authorName)
            .Skip((pageNumber - 1) * 32)
            .Take(32)//Refactor
            .ToList();
    }"

LINK NUMBER 319

File path: src/Program.cs
"string wwwrootPath = Path.Combine(Directory.GetCurrentDirectory(), ""UserFacade"");
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new PhysicalFileProvider(wwwrootPath),
    RequestPath = ""/wwwroot""
});
//app.UseStaticFiles();"

LINK NUMBER 320

File path: test/Chirp.WebService.Tests/PublicTimeline/PublicTimelineIntegrationTest.cs
"
    [Fact]
    public async void FrontPageContains32Cheeps()
    {
        //Arrange & Act
        var rsp = await usableClient.GetAsync(""/"");
        string htmlContent = await rsp.Content.ReadAsStringAsync();

        //Parse the htmlContent to a HTMLDocument
        HtmlDocument doc = new HtmlDocument();
        doc.LoadHtml(htmlContent);

        int amountOfListItems = doc.DocumentNode.SelectNodes(""//li"").Count();

        Assert.Equal(32, amountOfListItems);
    }"

LINK NUMBER 321
Error fetching diff

LINK NUMBER 322
Error fetching diff

LINK NUMBER 323
Error fetching diff

LINK NUMBER 324

File path: src/Chirp.CLI.Client/Program.cs
"    static string filePath = @""../../data/Chirp.CLI/chirp_cli_db.csv"";
    IDatabaseRepository db = new CsvDatabase(filePath);
    static string userName = Environment.UserName;
    static long timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    static int count = 0;
    
    public record Cheep(string Author, string Message, long Timestamp);
        
    static void Main(string[] args)
    {
        try"

LINK NUMBER 325
Not enough lines

LINK NUMBER 326

File path: src/Chirp.CLI.Client/Program.cs
"    static string filePath = @""../../data/Chirp.CLI/chirp_cli_db.csv"";
    IDatabaseRepository db = new CsvDatabase(filePath);
    static string userName = Environment.UserName;
    static long timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    static int count = 0;
    
    public record Cheep(string Author, string Message, long Timestamp);
        
    static void Main(string[] args)
    {
        try"

LINK NUMBER 327
Not enough lines

LINK NUMBER 328
Error fetching diff

LINK NUMBER 329
Error fetching diff

LINK NUMBER 330
Error fetching diff

LINK NUMBER 331

File path: src/Chirp.Web/Pages/Public.cshtml.cs
"        Cheeps = _cheepRepository.GetCheepsFromPage(CurrentPage);

        // Set follow status for each cheep author
        if (User.Identity?.IsAuthenticated == true)
        {
            foreach (var cheep in Cheeps)
            {
                var authorName = cheep.AuthorName;
                var isFollowing = _followerRepository
                    .GetFollowersFromAuthor(authorName)
                    .Any(follower => follower.Name == User.Identity.Name);

                FollowStatus[authorName] = isFollowing;
            }
        }
"

LINK NUMBER 332

File path: donut.py
"import numpy as np
import time
import json

# Create a class for the donut
class SpinningDonut:
    """"""
    A class representing a spinning 3D donut.
    """"""

    # Initialize the donut
    def __init__(self, screen_size=40, theta_spacing=0.07, phi_spacing=0.02, delay=0.01):
        """"""
        Initialize the donut with certain parameters.

        Parameters:
        screen_size (int): The size of the screen.
        theta_spacing (float): The spacing between thetas.
        phi_spacing (float): The spacing between phis.
        delay (float): The delay between frames.
        """"""
        # Set the variables
        # screen_size: The size of the screen
        self.screen_size = screen_size
        # theta_spacing: The spacing between thetas
        self.theta_spacing = theta_spacing
        # phi_spacing: The spacing between phis
        self.phi_spacing = phi_spacing
        # illumination: The illumination of the donut
        self.illumination = np.fromiter("".,-~:;=!*#$@"", dtype=""<U1"")
        self.A = 1
        self.B = 1
        self.R1 = 1
        self.R2 = 2
        self.K2 = 5
        self.K1 = self.screen_size * self.K2 * 3 / (8 * (self.R1 + self.R2))
        # delay: The delay between frames
        self.delay = delay

    # Get the frame to render
    def get_render_frame(self):
        """"""
        Calculate the frame to render.

        Returns:
        output (np.array): The frame to render.
        """"""
        # Get the cos and sin of A and B
        cos_A = np.cos(self.A)
        sin_A = np.sin(self.A)
        cos_B = np.cos(self.B)
        sin_B = np.sin(self.B)
        # Create the output and zbuffer
        output = np.full((self.screen_size, self.screen_size), "" "")
        # zbuffer: The zbuffer of the donut
        zbuffer = np.zeros((self.screen_size, self.screen_size))
        # Get the cos and sin of phi and theta
        cos_phi = np.cos(phi := np.arange(0, 2 * np.pi, self.phi_spacing))
        # sin_phi: The sin of phi
        sin_phi = np.sin(phi)
        # Get the cos and sin of theta
        cos_theta = np.cos(theta := np.arange(0, 2 * np.pi, self.theta_spacing))
        # sin_theta: The sin of theta
        sin_theta = np.sin(theta)
        # Get the circle x and y
        circle_x = self.R2 + self.R1 * cos_theta
        # circle_y: The y of the circle
        circle_y = self.R1 * sin_theta

        # Get the x, y, and z
        x = (np.outer(cos_B * cos_phi + sin_A * sin_B * sin_phi, circle_x) - circle_y * cos_A * sin_B).T
        y = (np.outer(sin_B * cos_phi - sin_A * cos_B * sin_phi, circle_x) + circle_y * cos_A * cos_B).T
        z = ((self.K2 + cos_A * np.outer(sin_phi, circle_x)) + circle_y * sin_A).T
        # ooz: The reciprocal of z
        ooz = np.reciprocal(z)
        # xp: The x position
        xp = (self.screen_size / 2 + self.K1 * ooz * x).astype(int)
        # yp: The y position
        yp = (self.screen_size / 2 - self.K1 * ooz * y).astype(int)
        L1 = (((np.outer(cos_phi, cos_theta) * sin_B) - cos_A * np.outer(sin_phi, cos_theta)) - sin_A * sin_theta)
        L2 = cos_B * (cos_A * sin_theta - np.outer(sin_phi, cos_theta * sin_A))
        L = np.around(((L1 + L2) * 8)).astype(int).T
        mask_L = L >= 0
        # chars: The characters to use
        chars = self.illumination[L]

        # Render the frame
        for i in range(90):
            # mask: The mask
            mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])
            # zbuffer: The zbuffer
            zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
            # output: The output
            output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])

        return output

    # Render the frame
    def render(self, array):
        """"""
        Render the frame on the console.

        Parameters:
        array (np.array): The frame to render.
        """"""
        # Print the array
        print(*["" "".join(row) for row in array], sep=""\n"")
        # Sleep
        time.sleep(self.delay)

    def save_frames_to_json(self, filename):
        """"""
        Save the frames to a JSON file.

        Parameters:
        filename (str): The name of the file to save.
        """"""
        frames = []
        for _ in range(self.screen_size * self.screen_size):
            self.A += self.theta_spacing
            self.B += self.phi_spacing
            frame = self.get_render_frame()
            # Convert the entire frame to a single string with ""\n"" as line separators
            frame_string = ""\n"".join("""".join(row) for row in frame)
            frames.append(frame_string)

        # Save the frames to a JSON file
        with open(filename, 'w') as f:
            json.dump(frames, f)

    # Run the donut
    def run(self):
        """"""
        Run the donut animation. This method loops indefinitely.
        """"""
        # Run the donut
        for _ in range(self.screen_size * self.screen_size):
            # Increment A and B
            self.A += self.theta_spacing
            self.B += self.phi_spacing
            # Clear the screen
            print(""\x1b[H"")
            self.render(self.get_render_frame())
           
# If the file is run directly:
if __name__ == ""__main__"":
    # Create the donut
    donut = SpinningDonut()
    # Run the donut
    # donut.run()
    donut.save_frames_to_json(""donut.json"")
    print(""done"")"

LINK NUMBER 333
Not enough lines

LINK NUMBER 334
Not enough lines

LINK NUMBER 335
Error fetching diff

LINK NUMBER 336
Error fetching diff

LINK NUMBER 337
Error fetching diff

LINK NUMBER 338

File path: test/Chirp.WebService.Tests/E2ETests/WebApplicationFactoryWithAuth.cs
"﻿using System.Security.Claims;
using System.Text.Encodings.Web;
using Chirp.Infrastructure.Contexts;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Options;
namespace Chirp.WebService.Tests.E2ETests;

public class WebApplicationFactoryWithAuth<TProgram> : WebApplicationFactory<TProgram> where TProgram : class
{
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.ConfigureServices(s =>
        {
            //Remove the default DBContext configuration
            var descriptor = s.SingleOrDefault(
                d => d.ServiceType ==
                     typeof(DbContextOptions<ChirpDbContext>));

            if (descriptor != null)
            {
                s.Remove(descriptor);
            }
            
            //Create an in-memory DB instance
            s.AddDbContext<ChirpDbContext>(options =>
            {
                options.UseInMemoryDatabase(""MemoryDB"");
            });
            
            s.AddAuthentication(defaultScheme: ""E2EScheme"")
                .AddScheme<AuthenticationSchemeOptions, MockAuth>(
                    ""E2EScheme"",options => {});
        });

        builder.UseEnvironment(""Development"");
    }
}

public class MockAuth : AuthenticationHandler<AuthenticationSchemeOptions>
{
    public MockAuth(IOptionsMonitor<AuthenticationSchemeOptions> options,
        ILoggerFactory logger, UrlEncoder encoder, ISystemClock clock)
        : base(options, logger, encoder, clock)
    {
    }

    protected override Task<AuthenticateResult> HandleAuthenticateAsync()
    {
        var claims = new[] { 
            new Claim(ClaimTypes.Name, ""PlaywrightTester""), 
            new Claim(ClaimTypes.Email, ""bdsagrup11@gmail.com""), 
            new Claim(ClaimTypes.GivenName, ""E2E""), 
            new Claim(ClaimTypes.Surname, ""User"") 
        };
        var identity = new ClaimsIdentity(claims, ""E2ETest"");
        var principal = new ClaimsPrincipal(identity);
        var ticket = new AuthenticationTicket(principal, ""E2EScheme"");

        var result = AuthenticateResult.Success(ticket);

        return Task.FromResult(result);
    }
}"

LINK NUMBER 339
Not enough lines

LINK NUMBER 340

File path: src/Chirp.Web/Areas/Identity/Pages/Account/ExternalLogin.cshtml.cs
"                // User doesn't exist; create a new user
                user = CreateUser();
                await _userStore.SetUserNameAsync(user, email, CancellationToken.None);
                await _emailStore.SetEmailAsync(user, email, CancellationToken.None);

                // Set user properties from external provider
                user.Name = info.Principal.Identity.Name ?? ""Unknown"";
                user.AuthorId = await _userManager.Users.CountAsync() + 1;

                var createUserResult = await _userManager.CreateAsync(user);
                if (createUserResult.Succeeded)
                {
                    await _userManager.AddClaimAsync(user, new Claim(""Name"", user.Name));
                    var addLoginResult = await _userManager.AddLoginAsync(user, info);
                    if (!addLoginResult.Succeeded)
                    {
                        ErrorMessage = ""Failed to add external login for new user."";
                        return RedirectToPage(""./Login"", new { ReturnUrl = returnUrl });
                    }
                }
                else"

LINK NUMBER 341

File path: test/Chirp.WebService.Tests/E2ETests/WebApplicationFactoryWithAuth.cs
"﻿using System.Security.Claims;
using System.Text.Encodings.Web;
using Chirp.Infrastructure.Contexts;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Options;
namespace Chirp.WebService.Tests.E2ETests;

public class WebApplicationFactoryWithAuth<TProgram> : WebApplicationFactory<TProgram> where TProgram : class
{
    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.ConfigureServices(s =>
        {
            //Remove the default DBContext configuration
            var descriptor = s.SingleOrDefault(
                d => d.ServiceType ==
                     typeof(DbContextOptions<ChirpDbContext>));

            if (descriptor != null)
            {
                s.Remove(descriptor);
            }
            
            //Create an in-memory DB instance
            s.AddDbContext<ChirpDbContext>(options =>
            {
                options.UseInMemoryDatabase(""MemoryDB"");
            });
            
            s.AddAuthentication(defaultScheme: ""E2EScheme"")
                .AddScheme<AuthenticationSchemeOptions, MockAuth>(
                    ""E2EScheme"",options => {});
        });

        builder.UseEnvironment(""Development"");
    }
}

public class MockAuth : AuthenticationHandler<AuthenticationSchemeOptions>
{
    public MockAuth(IOptionsMonitor<AuthenticationSchemeOptions> options,
        ILoggerFactory logger, UrlEncoder encoder, ISystemClock clock)
        : base(options, logger, encoder, clock)
    {
    }

    protected override Task<AuthenticateResult> HandleAuthenticateAsync()
    {
        var claims = new[] { 
            new Claim(ClaimTypes.Name, ""PlaywrightTester""), 
            new Claim(ClaimTypes.Email, ""bdsagrup11@gmail.com""), 
            new Claim(ClaimTypes.GivenName, ""E2E""), 
            new Claim(ClaimTypes.Surname, ""User"") 
        };
        var identity = new ClaimsIdentity(claims, ""E2ETest"");
        var principal = new ClaimsPrincipal(identity);
        var ticket = new AuthenticationTicket(principal, ""E2EScheme"");

        var result = AuthenticateResult.Success(ticket);

        return Task.FromResult(result);
    }
}"

LINK NUMBER 342
Error fetching diff

LINK NUMBER 343
Error fetching diff

LINK NUMBER 344
Error fetching diff

LINK NUMBER 345
Not enough lines

LINK NUMBER 346

File path: tools/load_fallbacks.py
"import os
import json
from pathlib import Path
import importlib.resources


def load_fallbacks():
    """"""
    Load fallback personality messages from user, local, or default locations.

    Priority:
    1. ~/.chatcraft/fallbacks.json
    2. ./chatcraft/data/fallbacks.local.json
    3. packaged fallback (chatcraft/data/fallbacks.json)

    Returns:
        dict: fallback personality responses
    """"""
    user_file = Path.home() / "".chatcraft"" / ""fallbacks.json""
    local_file = Path(""chatcraft/data/fallbacks.local.json"")

    if user_file.exists():
        with user_file.open(""r"", encoding=""utf-8"") as f:
            return json.load(f)

    elif local_file.exists():
        with local_file.open(""r"", encoding=""utf-8"") as f:
            return json.load(f)

    else:
        with importlib.resources.open_text(""chatcraft.data"", ""fallbacks.json"") as f:
            return json.load(f)"

LINK NUMBER 347

File path: attic/cs_test/cs_test_subprocess.cpp
"#include <iostream>
#include <string>
#include <winsock2.h>
#include <windows.h>

#pragma comment(lib, ""ws2_32.lib"")

int main()
{
    // Initialize Winsock
    WSADATA wsaData;
    int iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0) {
        std::cerr << ""WSAStartup failed: "" << iResult << std::endl;
        return 1;
    }

    // Create a socket for the subprocess to connect to
    SOCKET listenSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (listenSocket == INVALID_SOCKET) {
        std::cerr << ""Error creating socket: "" << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;
    }

    // Bind the socket to any available address and port 0 to let the operating system choose a free port
    sockaddr_in listenAddr;
    listenAddr.sin_family = AF_INET;
    listenAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    listenAddr.sin_port = htons(0);
    iResult = bind(listenSocket, (sockaddr*)&listenAddr, sizeof(listenAddr));
    if (iResult == SOCKET_ERROR) {
        std::cerr << ""Error binding socket: "" << WSAGetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Get the local address and port of the socket
    sockaddr_in localAddr;
    int localAddrLen = sizeof(localAddr);
    iResult = getsockname(listenSocket, (sockaddr*)&localAddr, &localAddrLen);
    if (iResult == SOCKET_ERROR) {
        std::cerr << ""Error getting socket name: "" << WSAGetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Start the subprocess with the local address and port as arguments
    STARTUPINFO startupInfo;
    PROCESS_INFORMATION processInfo;
    ZeroMemory(&startupInfo, sizeof(startupInfo));
    ZeroMemory(&processInfo, sizeof(processInfo));
    startupInfo.cb = sizeof(startupInfo);
    std::string commandLine = ""C:\\dev\\mercury_steamvr_driver\\build\\attic\\cs_test\\cs_test_subprocess.exe "" + std::to_string(ntohs(localAddr.sin_port));
    std::wstring wideCommandLine(commandLine.begin(), commandLine.end());
    if (!CreateProcess(NULL, commandLine.data(), NULL, NULL, FALSE, 0, NULL, NULL, &startupInfo, &processInfo)) {
        std::cerr << ""Error creating subprocess: "" << GetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Listen for the subprocess to connect
    iResult = listen(listenSocket, SOMAXCONN);
    if (iResult == SOCKET_ERROR) {
        std::cerr << ""Error listening for connection: "" << WSAGetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Accept the connection
    SOCKET clientSocket = accept(listenSocket, NULL, NULL);
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << ""Error accepting connection: "" << WSAGetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Receive data from the subprocess
    char recvBuffer[1024];
    iResult = recv(clientSocket, recvBuffer, sizeof(recvBuffer), 0);
    if (iResult == SOCKET_ERROR) {
        std::cerr << ""Error receiving data: "" << WSAGetLastError() << std::endl;
        closesocket(clientSocket);
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }
    recvBuffer[iResult] = '\0';
    std::cout << ""Received data from subprocess: "" << recvBuffer << std::endl;

    // Send data to the subprocess
    const char* sendBuffer = ""Hello, subprocess!"";
    iResult = send(clientSocket, sendBuffer, strlen(sendBuffer), 0);
    if (iResult == SOCKET_ERROR) {
        std::cerr << ""Error sending data: "" << WSAGetLastError() << std::endl;
        closesocket(clientSocket);
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    // Close the sockets and cleanup Winsock
    closesocket(clientSocket);
    closesocket(listenSocket);
    WSACleanup();

    return 0;
}
"

LINK NUMBER 348

File path: src/Chirp.Web/Pages/AboutMe.cshtml.cs
"            //! ChatGPT's parser -  Parse the page parameter
            var pageValues = Request.Query[""page""].ToString();
            if (int.TryParse(pageValues, out int parsedPage) && parsedPage > 0)
            {
                CurrentPage = parsedPage;
            }
"
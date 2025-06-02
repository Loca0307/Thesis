string wwwrootPath = Path.Combine(Directory.GetCurrentDirectory(), "UserFacade");
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new PhysicalFileProvider(wwwrootPath),
    RequestPath = "/wwwroot"
});
//app.UseStaticFiles();
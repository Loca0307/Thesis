<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Personal Page</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <header>
      <h1>Hello, I'm Your Name</h1>
      <nav>
        <ul>
          <li><a href="#about">About Me</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="about">
        <h2>About Me</h2>
        <p>Write a short bio here.</p>
      </section>

      <section id="projects">
        <h2>Projects</h2>
        <ul>
          <li>Project 1</li>
          <li>Project 2</li>
          <li>Project 3</li>
        </ul>
      </section>

      <section id="contact">
        <h2>Contact Me</h2>
        <form action="#" method="post">
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" required>
          <br><br>
          <label for="message">Message:</label>
          <textarea id="message" name="message" required></textarea>
          <br><br>
          <input type="submit" value="Submit">
        </form>
      </section>
    </main>

    <footer>
      <p>Copyright &copy; 2023 Your Name</p>
    </footer>
  </body>
</html>
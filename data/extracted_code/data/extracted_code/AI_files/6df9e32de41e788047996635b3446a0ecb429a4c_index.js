function App() {
  return (
    <div>
      <h1>Welcome to Larry's personal website!</h1>
      <p>This is the landing page for Larry's personal website. Here, you can learn more about Larry and see some of his work.</p>
    </div>
  );
}

// Create a new About component
function About() {
  return (
    <div>
      <h1>About Larry</h1>
      <p>Larry is a software engineer who enjoys building web and mobile applications. He has experience with a variety of programming languages and frameworks, including React, Angular, and Node.js.</p>
      <p>In his free time, Larry enjoys hiking, reading, and playing video games.</p>
    </div>
  );
}

// Create a new Projects component
function Projects() {
  return (
    <div>
      <h1>Larry's Projects</h1>
      <p>Here are some of the projects that Larry has worked on:</p>
      <ul>
        <li><a href="https://github.com/larry/react-todo-app">React Todo App</a></li>
        <li><a href="https://github.com/larry/node-chat-app">Node.js Chat App</a></li>
        <li><a href="https://github.com/larry/angular-blog">Angular Blog</a></li>
      </ul>
    </div>
  );
}

// Create a new Contact component
function Contact() {
  return (
    <div>
      <h1>Contact Larry</h1>
      <p>You can contact Larry using the following methods:</p>
      <ul>
        <li>Email: larry@example.com</li>
        <li>Twitter: @larry</li>
        <li>GitHub: larry</li>
      </ul>
    </div>
  );
}

// Render the About, Projects, and Contact components
ReactDOM.render(
  <>
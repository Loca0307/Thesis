# Chat App Component

The Chat App Component is a real-time chat application built as a web component. It allows users to send and receive messages instantly, with support for emoji input and user nicknames.

## Author

Sabrina Prichard-Lybeck  
Email: <sp223kz@student.lnu.se>  

## Version

1.1.0

## Features

- Real-time messaging using WebSockets.
- Emoji picker for adding emojis to messages.
- Persistent nickname storage using local storage.
- Prevents XSS attacks by sanitizing user inputs.
- Color-coded messages for different users.

## Usage

### Installation

Include the component in your project:

```html
<script type="module" src="path/to/chat-app.js"></script>
```

## Add the component to your HTML

```html
<chat-app></chat-app>
```

## JavaScript

```html
customElements.define('chat-app', class extends HTMLElement {
  // The class implementation goes here.
})
```

### Dependencies

*emoji-picker-element for emoji input.
*DOMPurify for sanitizing user inputs to prevent XSS attacks.
*A nickname-form component for setting user nicknames.

### Styles

Customize the appearance of the chat app component by modifying the embedded styles within the template.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

*The creators of emoji-picker-element for providing the emoji picker component.
*The authors of DOMPurify for ensuring safe user inputs.
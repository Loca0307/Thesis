LINK NUMBER 1
Error fetching diff

LINK NUMBER 2
Error fetching diff

LINK NUMBER 3
Error fetching diff

LINK NUMBER 4

File path: src/components/DishdetailComponent.js
"import React, { Component } from 'react';
import {
  Button, Modal, ModalHeader, ModalBody,
  Form, FormGroup, Input, Label
} from 'reactstrap';

class CommentForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isModalOpen: false
    };

    this.toggleModal = this.toggleModal.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  toggleModal() {
    this.setState({ isModalOpen: !this.state.isModalOpen });
  }

  handleSubmit(event) {
    event.preventDefault();
    this.toggleModal();
    this.props.addComment(
      this.props.dishId,
      this.rating.value,
      this.author.value,
      this.comment.value
    );
  }

  render() {
    return (
      <div>
        <Button outline onClick={this.toggleModal}>
          <span className=""fa fa-pencil fa-lg""></span> Submit Comment
        </Button>

        <Modal isOpen={this.state.isModalOpen} toggle={this.toggleModal}>
          <ModalHeader toggle={this.toggleModal}>Submit Comment</ModalHeader>
          <ModalBody>
            <Form onSubmit={this.handleSubmit}>
              <FormGroup>
                <Label htmlFor=""rating"">Rating</Label>
                <Input type=""select"" id=""rating"" innerRef={(input) => this.rating = input}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Input>
              </FormGroup>
              <FormGroup>
                <Label htmlFor=""author"">Your Name</Label>
                <Input type=""text"" id=""author"" innerRef={(input) => this.author = input} />
              </FormGroup>
              <FormGroup>
                <Label htmlFor=""comment"">Comment</Label>
                <Input type=""textarea"" id=""comment"" rows=""6"" innerRef={(input) => this.comment = input} />
              </FormGroup>
              <Button type=""submit"" value=""submit"" color=""primary"">Submit</Button>
            </Form>
          </ModalBody>
        </Modal>
      </div>
    );
  }
}

export default CommentForm;"

LINK NUMBER 5
Not enough lines

LINK NUMBER 6
Not enough lines

LINK NUMBER 7
Not enough lines

LINK NUMBER 8
Error fetching diff

LINK NUMBER 9
Error fetching diff

LINK NUMBER 10
Error fetching diff

LINK NUMBER 11

File path: lang/messages/en/user.js
"// server.js (Origin 2)
const http = require('http');
const mysql = require('mysql2');
const url = require('url');

// MySQL Connection Setup
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root', // Change to your MySQL username
    password: '', // Change to your MySQL password
    database: 'patients_db'
});

db.connect(err => {
    if (err) throw err;
    console.log('Connected to MySQL');
    db.query(""CREATE DATABASE IF NOT EXISTS patients_db"", err => {
        if (err) throw err;
        db.query(`CREATE TABLE IF NOT EXISTS patients (
            patientid INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            date_of_birth DATE
        ) ENGINE=InnoDB;`, err => {
            if (err) throw err;
        });
    });
});

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);

    if (req.method === 'POST' && parsedUrl.pathname === '/insert') {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            const data = JSON.parse(body);
            const sql = ""INSERT INTO patients (name, date_of_birth) VALUES ?"";
            const values = data.patients.map(p => [p.name, p.date_of_birth]);
            db.query(sql, [values], (err, result) => {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: !err, message: err ? err.message : 'Inserted successfully' }));
            });
        });
    } else if (req.method === 'GET' && parsedUrl.pathname === '/query') {
        const sql = parsedUrl.query.sql;
        if (!sql.trim().toUpperCase().startsWith('SELECT')) {
            res.writeHead(403, { 'Content-Type': 'application/json' });
            return res.end(JSON.stringify({ success: false, message: 'Only SELECT queries allowed' }));
        }
        db.query(sql, (err, result) => {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: !err, data: err ? err.message : result }));
        });
    } else {
        res.writeHead(404);
        res.end();
    }
});

server.listen(3000, () => console.log('Server running on port 3000'));"

LINK NUMBER 12

File path: src/main.cpp
"    // Define triangle vertices
    float vertices[] = {
         0.0f,  0.5f, 0.0f,  // Top vertex
        -0.5f, -0.5f, 0.0f,  // Bottom-left vertex
         0.5f, -0.5f, 0.0f   // Bottom-right vertex
    };

    // Create a Vertex Buffer Object (VBO) and Vertex Array Object (VAO)
    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    // Bind VAO (stores vertex attribute state)
    glBindVertexArray(VAO);

    // Bind and set VBO
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // Define vertex attributes
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    // Unbind VBO/VAO
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    // Compile Vertex Shader
    unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    // Check for shader compile errors
    int success;
    char infoLog[512];
    glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
        std::cerr << ""ERROR::SHADER::VERTEX::COMPILATION_FAILED\n"" << infoLog << std::endl;
    }

    // Compile Fragment Shader
    unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    // Check for shader compile errors
    glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
        std::cerr << ""ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n"" << infoLog << std::endl;
    }

    // Create Shader Program and link shaders
    unsigned int shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    // Check for linking errors
    glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
    if (!success) {
        glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
        std::cerr << ""ERROR::SHADER::PROGRAM::LINKING_FAILED\n"" << infoLog << std::endl;
    }

    // Delete shaders as they're linked now
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

"

LINK NUMBER 13
Not enough lines

LINK NUMBER 14
Not enough lines

LINK NUMBER 15
Error fetching diff

LINK NUMBER 16
Error fetching diff

LINK NUMBER 17
Error fetching diff

LINK NUMBER 18
Not enough lines

LINK NUMBER 19
Not enough lines

LINK NUMBER 20
Not enough lines

LINK NUMBER 21

File path: armor_generator.py
"import streamlit as st

# App Title
st.title(""Custom Armor Generator"")
st.subheader(""Design your own armor and create AI prompts for it."")

# Sidebar for Armor Customization
st.sidebar.header(""Customize Your Armor"")

# Under Armor Options
under_armor = st.sidebar.selectbox(
    ""Under Armor (Base Layer)"", 
    [""None"", ""Simple Tunic"", ""Quilted Gambeson"", ""Richly Embroidered Gambeson"", ""Chainmail Hauberk""]
)

# Over Armor Options
over_armor = st.sidebar.multiselect(
    ""Over Armor (Accessories)"", 
    [""None"", ""Hooded Cloak"", ""Flowing Cape"", ""Heraldic Surcoat"", ""Fur-Lined Mantle""]
)

# Armor Material
armor_material = st.sidebar.selectbox(
    ""Armor Material"", 
    [""Steel"", ""Bronze"", ""Gold"", ""Blackened Iron""]
)

# Engraving Style
engraving_style = st.sidebar.selectbox(
    ""Engraving Style"", 
    [""None"", ""Floral"", ""Runes"", ""Geometric""]
)

# Color Customization
st.sidebar.header(""Color Customizations"")
base_layer_color = st.sidebar.color_picker(""Base Layer Color (Tunic/Gambeson)"", ""#B87333"")
armor_accent_color = st.sidebar.color_picker(""Armor Accent Color"", ""#FFD700"")
cloak_color = st.sidebar.color_picker(""Cloak or Cape Color"", ""#5B84B1"")

# Generate Prompt
st.header(""Generated AI Prompt"")

prompt = f""A warrior clad in {armor_material.lower()} armor. ""
if under_armor != ""None"":
    prompt += f""Underneath, they wear a {under_armor.lower()} dyed {base_layer_color}. ""
if over_armor and ""None"" not in over_armor:
    prompt += f""Over the armor, they wear {', '.join(over_armor).lower()}, dyed {cloak_color}. ""
prompt += f""The armor features {engraving_style.lower()} engravings and accents of {armor_accent_color}.""

st.write(prompt)

# Color Preview
st.header(""Color Preview"")
st.write(""Base Layer Color:"")
st.color_picker(""Preview Base Layer"", base_layer_color, key=""preview_base"")
st.write(""Armor Accent Color:"")
st.color_picker(""Preview Armor Accents"", armor_accent_color, key=""preview_accent"")
if ""None"" not in over_armor:
    st.write(""Cloak or Cape Color:"")
    st.color_picker(""Preview Cloak"", cloak_color, key=""preview_cloak"")

# Next Steps Placeholder
st.header(""Next Steps"")
st.write(""In the next phase, we will integrate AI image generation to visualize your armor."")"

LINK NUMBER 22
Error fetching diff

LINK NUMBER 23
Error fetching diff

LINK NUMBER 24
Error fetching diff

LINK NUMBER 25

File path: sb-ecom-frontend/src/store/reducers/cartReducer.js
"const intialState={
    cart:[],
    totalPrice:0,
    cartId:null, 
}

export const cartReducer=(state=intialState,action)=>{
    switch(action.type){
        case ""ADD_CART"":
            const productToAdd=action.payload;
            const exsistingProduct=state.cart.find(
                (item)=>item.productId===productToAdd.productId
            );
            if(exsistingProduct){
                const updatedCart=state.cart.map((item)=>{
                    if(item.productId===productToAdd.productId){
                        return productToAdd;
                    }
                    else{
                        return item;
                    }
                });
                return{
                    ...state,
                    cart:updatedCart,
                }
            }
            else{
                const newCart=[...state.cart,productToAdd];
                return{
                    ...state,
                    cart:newCart,
                }
            }
        default:
             return state;
    }
}"

LINK NUMBER 26
Not enough lines

LINK NUMBER 27
Not enough lines

LINK NUMBER 28

File path: chat_cyclic_cellular_automaton.py
"import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scipy.ndimage as ndimage
from scipy.ndimage import generate_binary_structure, iterate_structure

# Parameters
x, y = 200, 200  # Grid size
range_ = 2  # Neighborhood range
threshold = 3  # Activation threshold
states = 5  # Number of states
neighborhood_type = 1  # 1 for Von Neumann, 2 for Moore

# Initialize the automaton grid
array = np.random.randint(0, states, (y, x))

# Generate the neighborhood footprint
footprint = np.array(
    iterate_structure(generate_binary_structure(2, neighborhood_type), range_), dtype=int
)


def compute_func(values):
    """"""Rule function for the cellular automaton.""""""
    cur = values[int(len(values) / 2)]
    if cur == (states - 1):
        count = np.count_nonzero(values == 0)
    else:
        count = np.count_nonzero(values == cur + 1)
    if count >= threshold:
        cur += 1
    if cur == states:
        cur = 0
    return cur


def update(frame):
    global array
    array = ndimage.generic_filter(array, compute_func, footprint=footprint, mode=""wrap"")
    img.set_array(array)
    return (img,)


# Plot setup
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_axis_off()
img = ax.imshow(array, interpolation=""none"")

# Animation setup
ani = animation.FuncAnimation(fig, update, interval=100, blit=True, save_count=1000)
plt.show()

# # Directory for saving GIFs
# output_dir = ""CCA_gifs""
# os.makedirs(output_dir, exist_ok=True)

# # Save as GIF
# gif_filename = f""{output_dir}/automaton_R{range_}_T{threshold}_S{states}_N{neighborhood_type}.gif""
# ani.save(gif_filename, writer=""pillow"", fps=10)
# print(f""Animation saved as {gif_filename}"")"

LINK NUMBER 29
Error fetching diff

LINK NUMBER 30
Error fetching diff

LINK NUMBER 31
Error fetching diff

LINK NUMBER 32
Not enough lines

LINK NUMBER 33

File path: test/helpersTest.js
"});




describe('urlsForUser', function() {
  const urlDatabase = {
    'b2xVn2': { longURL: 'http://www.lighthouselabs.ca', userID: 'user123' },
    '9sm5xK': { longURL: 'http://www.google.com', userID: 'user456' },
    'h3pVn3': { longURL: 'http://www.example.com', userID: 'user123' }
  };

  it('should return only the URLs that belong to the specified user', function() {
    const userID = 'user123';
    const expectedOutput = {
      'b2xVn2': { longURL: 'http://www.lighthouselabs.ca', userID: 'user123' },
      'h3pVn3': { longURL: 'http://www.example.com', userID: 'user123' }
    };
    
    const result = urlsForUser(userID, urlDatabase);
    
    assert.deepEqual(result, expectedOutput);
  });

  it('should return an empty object if the user has no URLs', function() {
    const userID = 'user999'; // User with no URLs
    const expectedOutput = {};
    
    const result = urlsForUser(userID, urlDatabase);
    
    assert.deepEqual(result, expectedOutput);
  });

  it('should return an empty object if the urlDatabase is empty', function() {
    const userID = 'user123';
    const expectedOutput = {};
    
    const result = urlsForUser(userID, {}); // Passing an empty database
    
    assert.deepEqual(result, expectedOutput);
  });

  it('should not return any URLs that do not belong to the specified user', function() {
    const userID = 'user456'; // This user has one URL
    const expectedOutput = {
      '9sm5xK': { longURL: 'http://www.google.com', userID: 'user456' }
    };
    
    const result = urlsForUser(userID, urlDatabase);
    
    assert.deepEqual(result, expectedOutput);
    
    const otherUserId = 'user123'; // This user has two URLs
    const otherExpectedOutput = {
      'b2xVn2': { longURL: 'http://www.lighthouselabs.ca', userID: 'user123' },
      'h3pVn3': { longURL: 'http://www.example.com', userID: 'user123' }
    };
    
    const otherResult = urlsForUser(otherUserId, urlDatabase);
    
    // Assert that the other user does not include the URLs of user456
    assert.notDeepEqual(otherResult, expectedOutput);
  });
});"

LINK NUMBER 34
Not enough lines

LINK NUMBER 35

File path: server/server.js
"
    let imageUrl;
    if (USE_OPENAI_API) {
      const response = await openai.images.generate({
        model: ""dall-e-3"",
        prompt: generatedPrompt,
        n: 1,
        size: ""1024x1024"",
      });
      imageUrl = response.data[0].url;
      const imageId = uuidv4();
      imageUrl = await saveImage(imageUrl, imageId);
    } else {
      imageUrl = generateMockImage(generatedPrompt);
    }

    const metadata = {
      originalPrompt: prompt,
      generatedPrompt: generatedPrompt,
      imageUrl: imageUrl,
      createdAt: new Date().toISOString(),
    };

    // Add to gallery
    galleryItems.push(metadata);

    res.json({ 
      imageUrl: imageUrl, 
      generatedPrompt: generatedPrompt,
      originalPrompt: prompt 
    });"

LINK NUMBER 36
Error fetching diff

LINK NUMBER 37
Error fetching diff

LINK NUMBER 38
Error fetching diff

LINK NUMBER 39
Not enough lines

LINK NUMBER 40

File path: scripts/levels.js
"//ChatGPT Generated level
	  [
    ""=     =                 O============="",
    ""=     =                  =            "",
    ""=     =                  =            "",
    ""=     =   ^   ==  ^^     =            "",
    ""=     ===========    ====             "",
    ""=     =              =                "",
    ""=     =        ^     =                "",
    ""=      ^^^^^  ==^^^  =                "",
    ""=      =    =====>   =                "",
    ""=      =             =                "",
    ""=      =             =                "",
    ""=      =         ^^  =                "",
    ""=      =     ===========             "",
    ""=      =^^   =          =            "",
    ""=      ==    =          =            "",
    ""=     <     ==^^^       =            "",
    ""=           =========== =            "",
    ""=          <        = =              "",
    ""=      l         =^^^== =            "",
    ""<<<>>>><><<<<>>><<llllllllllllllllll "",
],
"

LINK NUMBER 41
Not enough lines

LINK NUMBER 42
Not enough lines

LINK NUMBER 43
Error fetching diff

LINK NUMBER 44
Error fetching diff

LINK NUMBER 45
Error fetching diff

LINK NUMBER 46
Not enough lines

LINK NUMBER 47
Not enough lines

LINK NUMBER 48
Not enough lines

LINK NUMBER 49

File path: src/chatgpt_tool.py
"from openai import OpenAI
import os
from dotenv import load_dotenv
import queue
import cv2
import random
import time
import threading
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
client = OpenAI(api_key=os.getenv(""OPENAI_API_KEY""))
TEXT_TO_FRAME_SCALE = 900
COUNTDOWN_DURATION_S = 5
POEM_FONT_COLOR = (166, 0, 0)
INITIAL_PROMPT = (
    ""You are a tanka poet. You and I will have a conversation in tanka poems. Wait for my next message, I will continuously give you a list of words and every time you need to incorporate them into a tanka poem. ""
    ""In every round, you need to switch between two people. One person is from the present time, and the other is a lover ""
    ""from 7th-century Japan. Tell me which role you are first followed by a tanka. The back-and-forth structure can continue evolving, reflecting shifts in tone, perspective, ""
    ""or subject matter. To maintain coherence, please feel free to respond dynamically to themes introduced in previous poems, ""
    ""adjust the tone to reflect contrasting or complementary viewpoints, and incorporate new words or ideas from outside the ""
    ""provided sources to embrace fresh inputs.""
)


def chat_with_gpt(prompt, model=""gpt-4o-mini""):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                # {""role"": ""system"", ""content"": ""You are a tanka poem generator.""},
                {""role"": ""user"", ""content"": prompt}
            ]
        )
        # Ensure the response is properly encoded
        ret = response.choices[0].message.content.strip().encode('utf-8').decode('utf-8')
        print(ret)
        return ret
    except Exception as e:
        print(f""An error occurred: {str(e)}"")
        return ""Sorry, I'm not able to generate a tanka poem right now.""

class CameraStream:
    def __init__(self):
        # Load the local CSV file
        self.data = pd.read_csv('doc/1200_words_30x40_grid.csv', header=None)  # Update with your CSV file path
        self.word_grid = self.parse_csv_content()  # Parse the content into a grid format
        self.words_for_poem = []
        self.capture = cv2.VideoCapture(0)
        self.q = queue.Queue(maxsize=2)  # Limit queue size
        self.stop_event = threading.Event()
        self.text_to_display = ""Press SPACE to generate a tanka poem...""
        self.text_lock = threading.Lock()
        self.generate_a_new_poem = False
        self.x, self.y = 50, 50
        # Get the width and height of the captured frames
        self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.last_clock = 0
        self.previous_motion_coordinates = []  # Store previous motion coordinates
        # self.map_coordinates_to_words(self.previous_motion_coordinates)
        
        # Create OpenAI client once during initialization
        self.client = OpenAI(api_key=os.getenv(""OPENAI_API_KEY""))

    def parse_csv_content(self):
        # Convert the DataFrame to a 2D list (grid format)
        return self.data.values.tolist()  # Convert DataFrame to a list of lists

    @staticmethod
    def draw_multiline_text(frame, text, position, font_scale, color, thickness):
        # Ensure text is properly formatted
        text = text.encode('utf-8').decode('utf-8')  # Ensure text is in UTF-8
        x, y = position
        for line in text.split('\n'):
            # Calculate font scale based on frame size
            frame_height, frame_width = frame.shape[:2]
            font_scale = min(frame_width, frame_height) / TEXT_TO_FRAME_SCALE  # Adjust this factor as needed

            # Use a more visible font and color
            font = cv2.FONT_HERSHEY_DUPLEX
            thickness = max(2, int(font_scale * 2))  # Thicker lines for better visibility

            # Add a dark background behind the text for better contrast
            (text_width, text_height), _ = cv2.getTextSize(line, font, font_scale, thickness)

            # Replace unsupported characters with a placeholder or remove them
            line = line.replace('—', '-')  # Replace em dash with a hyphen

            cv2.putText(frame, line, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
            y += int(text_height * 1.5)  # Adjust line spacing based on text height

    def detect_motion(self, frame, previous_frame):
        # Convert frames to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_previous = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

        # Compute the absolute difference between the current frame and previous frame
        delta_frame = cv2.absdiff(gray_previous, gray_frame)
        thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]

        # Find contours of the motion areas
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_coordinates = []

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Minimum area to consider as motion
                (x, y, w, h) = cv2.boundingRect(contour)
                motion_coordinates.append((x + w // 2, y + h // 2))  # Store center of the bounding box

        return motion_coordinates

    def draw_motion_coordinates(self, frame, motion_coordinates):
        for (x, y) in motion_coordinates:
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Draw circles at the coordinates

    def draw_random_motion_coordinates(self, frame, motion_coordinates):
        if motion_coordinates:
            self.previous_motion_coordinates = random.choices(motion_coordinates, k=5)  # Pick 5 random coordinates
            self.draw_motion_coordinates(frame, self.previous_motion_coordinates)

    def map_coordinates_to_words(self, coordinates):
        self.words_for_poem = []
        print(""new coordinates: "")
        for (x, y) in coordinates:
            # Ensure the coordinates are within the bounds of the grid
            word_x = x // (self.frame_width // len(self.word_grid[0]))
            word_y = y // (self.frame_height // len(self.word_grid))
            self.words_for_poem.append(self.word_grid[word_y][word_x])  # Append the word at the (row, column) position
            print(word_x, word_y, self.word_grid[word_y][word_x])

    def capture_frames(self):
        previous_frame = None
        last_detection_time = time.time()  # Initialize the last detection time
        while not self.stop_event.is_set():
            ret, frame = self.capture.read()
            if not ret:
                break

            current_time = time.time()
            elapsed_time = current_time - last_detection_time
            remaining_time = max(0, COUNTDOWN_DURATION_S - int(elapsed_time))  # Calculate remaining time

            if previous_frame is not None and elapsed_time >= COUNTDOWN_DURATION_S:  # Check if 5 seconds have passed
                motion_coordinates = self.detect_motion(frame, previous_frame)
                self.draw_random_motion_coordinates(frame, motion_coordinates)
                self.map_coordinates_to_words(self.previous_motion_coordinates)
                last_detection_time = current_time  # Update the last detection time

            # Draw previously detected motion coordinates
            self.draw_motion_coordinates(frame, self.previous_motion_coordinates)
            # Draw countdown timer
            countdown_text = f""{remaining_time}""
            self.draw_multiline_text(frame, countdown_text, (10, 30), 1, POEM_FONT_COLOR, 2)
           
            with self.text_lock:
                text = self.text_to_display

            self.draw_multiline_text(frame, text, (self.x, self.y), 1.5, POEM_FONT_COLOR, 2)
             
            if not self.q.full():
                self.q.put(frame)
            previous_frame = frame  # Update previous frame
            time.sleep(0.01)  # Small delay to prevent excessive CPU usage

    def display_frames(self):
        cv2.namedWindow('Tanka Poem Generator', cv2.WINDOW_NORMAL)
        while not self.stop_event.is_set():
            if not self.q.empty():
                frame = self.q.get()
                try:
                    cv2.imshow('Tanka Poem Generator', frame)
                except cv2.error:
                    print(""Error displaying frame"")
                    continue
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    self.stop_event.set()
                elif key == ord(' '):
                    with self.text_lock:
                        self.text_to_display = ""Generating a new tanka poem...""
                    self.last_clock = time.time()
                    self.generate_a_new_poem = True
                    frame_height, frame_width = frame.shape[:2]
                    self.x = random.randint(50, frame_width // 2)  # Adjust based on expected text width
                    self.y = random.randint(50, frame_height // 2)  # Adjust based on expected text height
            time.sleep(0.01)  # Small delay to prevent excessive CPU usage

    def update_text(self):
        while not self.stop_event.is_set():
            if self.generate_a_new_poem:
                poem = self.generate_tanka()
                time_spent = round(time.time() - self.last_clock, 2)
                print(f""Time spent: {time_spent} seconds"")
                print(poem)
                print()
                with self.text_lock:
                    self.text_to_display = poem
                self.generate_a_new_poem = False

    def generate_tanka(self):
        return chat_with_gpt(""Generate a tanka poem that's in response to the previous ones, with following words: "" + "", "".join(self.words_for_poem))

    def setup_chatgpt_initial_prompt(self):
        chat_with_gpt(INITIAL_PROMPT)

    def start(self):
        threads = [
            threading.Thread(target=self.setup_chatgpt_initial_prompt),
            threading.Thread(target=self.capture_frames),
            threading.Thread(target=self.update_text)
        ]
        for thread in threads:
            thread.start()

        # Run display_frames in the main thread
        self.display_frames()

        for thread in threads:
            thread.join()
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    stream = CameraStream()
    stream.start()"

LINK NUMBER 50
Error fetching diff

LINK NUMBER 51
Error fetching diff

LINK NUMBER 52
Error fetching diff

LINK NUMBER 53
Not enough lines

LINK NUMBER 54
Not enough lines

LINK NUMBER 55

File path: frontend/src/Student.js
"            {student.length === 0 ? ( //Conditional Rendering: handle cases when there are no students in the list
              <p>No students available</p>
            ) : (
              student.map((data, i) => (
                <tr key={i}>
                  <td>{data.Name}</td>
                  <td>{data.Email}</td>
                  <td>
                    <Link to={`update/${data.ID}`} className=""btn btn-primary"">
                      Update
                    </Link>
                    <Link
                      to={`view/${data.ID}`}
                      className=""btn btn-success ms-2""
                    >
                      View
                    </Link>
                    <button
                      className=""btn btn-danger ms-2""
                      onClick={(e) => handleDelete(data.ID)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))
            )}"

LINK NUMBER 56
Not enough lines

LINK NUMBER 57
Error fetching diff

LINK NUMBER 58
Error fetching diff

LINK NUMBER 59
Error fetching diff

LINK NUMBER 60

File path: openai.ts
"import { Board, Todo, TypedColumn } from ""@/typings"";

const formatTodosForAI = (board: Board) => {
  const todos = Array.from(board.columns.entries());

  const flatArray = todos.reduce((map, [key, value]) => {
    map[key] = value.todos;
    return map;
  }, {} as { [key in TypedColumn]: Todo[] });

  // reduce to key: value(length)
  const flatArrayCounted = Object.entries(flatArray).reduce(
    (map, [key, value]) => {
      map[key as TypedColumn] = value.length;
      return map;
    },
    {} as { [key in TypedColumn]: number }
  );

  return flatArrayCounted;
};

export default formatTodosForAI;"

LINK NUMBER 61
Not enough lines

LINK NUMBER 62
Not enough lines

LINK NUMBER 63
Not enough lines

LINK NUMBER 64
Error fetching diff

LINK NUMBER 65
Error fetching diff

LINK NUMBER 66
Not enough lines

LINK NUMBER 67
Not enough lines
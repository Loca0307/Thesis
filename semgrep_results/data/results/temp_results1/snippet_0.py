LINK NUMBER 1
Error fetching diff

LINK NUMBER 2
Error fetching diff

LINK NUMBER 3
Error fetching diff

LINK NUMBER 4
Not enough lines

LINK NUMBER 5
Not enough lines

LINK NUMBER 6
Not enough lines

LINK NUMBER 7

File path: update.go
"package main

import (
	""log""
	""os""
	""os/exec""
	""path/filepath""
)

func main() {
	// Define the repository URL and the temporary directory for cloning
	repoURL := ""https://github.com/abnormalhare/elemental-on-cards.git""
	tempDir := filepath.Join(os.TempDir(), ""discord-bot-game"")

	// Remove the temporary directory if it exists
	if _, err := os.Stat(tempDir); err == nil {
		if err := os.RemoveAll(tempDir); err != nil {
			log.Fatalf(""Failed to remove temporary directory: %v"", err)
		}
	}

	// Clone the repository
	log.Println(""Cloning repository..."")
	cmd := exec.Command(""git"", ""clone"", repoURL, tempDir)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		log.Fatalf(""Failed to clone repository: %v"", err)
	}

	// Copy files from the cloned repository to the current directory
	log.Println(""Updating files..."")
	err := filepath.Walk(tempDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// Skip the root directory
		if path == tempDir {
			return nil
		}

		// Determine the relative path and destination path
		relPath, err := filepath.Rel(tempDir, path)
		if err != nil {
			return err
		}
		destPath := filepath.Join(""."", relPath)

		// If it's a directory, create it
		if info.IsDir() {
			if err := os.MkdirAll(destPath, os.ModePerm); err != nil {
				return err
			}
		} else {
			// If it's a file, copy it
			srcFile, err := os.Open(path)
			if err != nil {
				return err
			}
			defer srcFile.Close()

			destFile, err := os.Create(destPath)
			if err != nil {
				return err
			}
			defer destFile.Close()

			if _, err := destFile.ReadFrom(srcFile); err != nil {
				return err
			}
		}
		return nil
	})
	if err != nil {
		log.Fatalf(""Failed to update files: %v"", err)
	}

	// Clean up the temporary directory
	log.Println(""Cleaning up..."")
	if err := os.RemoveAll(tempDir); err != nil {
		log.Fatalf(""Failed to remove temporary directory: %v"", err)
	}

	// Restart the bot
	log.Println(""Restarting the bot..."")
	botCmd := exec.Command(""python"", ""eoc.py"")
	botCmd.Stdout = os.Stdout
	botCmd.Stderr = os.Stderr
	if err := botCmd.Start(); err != nil {
		log.Fatalf(""Failed to restart the bot: %v"", err)
	}

	log.Println(""Update completed successfully."")
}"

LINK NUMBER 8
Error fetching diff

LINK NUMBER 9
Error fetching diff

LINK NUMBER 10
Error fetching diff

LINK NUMBER 11

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

LINK NUMBER 12

File path: MovieRecApp.Server/Services/RecommendationService.cs
"    
    public async Task EvaluateHoldoutAsync(float testFraction = 0.2f)
    {
        // 1) Fetch & filter
        var allRatings = await _db.Ratings
            .Select(r => new RatingInput {
                UserName = r.UserName,
                MovieId  = r.MovieId,
                Score    = r.Score
            })
            .ToListAsync();
        var popularMovieIds = allRatings
            .GroupBy(r => r.MovieId)
            .Where(g => g.Count() >= 5)
            .Select(g => g.Key)
            .ToHashSet();
        var filtered = allRatings
            .Where(r => popularMovieIds.Contains(r.MovieId))
            .ToList();

        // 2) Apply the same weighting‐by‐duplication
        var weighted = new List<RatingInput>();
        foreach (var r in filtered)
        {
            weighted.Add(r);
            if (r.Score <= 2 || r.Score >= 9)
                weighted.Add(r);
        }

        // 3) Split train/test
        var dataView = _mlContext.Data.LoadFromEnumerable(weighted);
        var split    = _mlContext.Data.TrainTestSplit(dataView, testFraction: testFraction);
        var trainSet = split.TrainSet;
        var testSet  = split.TestSet;

        // 4) Train & evaluate
        var pipeline = _mlContext.Transforms
            .Conversion.MapValueToKey(""userKey"", nameof(RatingInput.UserName))
            .Append(_mlContext.Transforms
                .Conversion.MapValueToKey(""movieKey"", nameof(RatingInput.MovieId)))
            .Append(_mlContext.Recommendation()
                .Trainers.MatrixFactorization(new MatrixFactorizationTrainer.Options
                {
                    MatrixColumnIndexColumnName = ""userKey"",
                    MatrixRowIndexColumnName    = ""movieKey"",
                    LabelColumnName             = ""Label"",
                    NumberOfIterations          = 30,
                    ApproximationRank           = 150,
                    Lambda                      = 0.1
                }));
        var model   = pipeline.Fit(trainSet);
        var preds   = model.Transform(testSet);
        var metrics = _mlContext.Regression.Evaluate(preds, ""Label"", ""Score"");

        Console.WriteLine($""=== Hold-out (weighted+filtered) {1-testFraction:P0}/{testFraction:P0} ==="");
        Console.WriteLine($""  RMSE = {metrics.RootMeanSquaredError:F3}"");
        Console.WriteLine($""  MAE  = {metrics.MeanAbsoluteError:F3}"");
        Console.WriteLine($""  R²   = {metrics.RSquared:F3}"");
    }"

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

File path: server/src/service/weatherService.ts
"  async getWeatherForCity(city: string): Promise<Weather[]> {
    try {
      this.cityName = city;

      console.log(`📍 Fetching weather data for: ${city}`);

      // Step 1: Get coordinates for the city
      const coordinates = await this.fetchAndDestructureLocationData();

      // Step 2: Fetch weather data using coordinates
      const weatherData = await this.fetchWeatherData(coordinates);

      // Step 3: Parse current weather
      const currentWeather = this.parseCurrentWeather(weatherData);

      // Step 4: Build the 5-day forecast
      return this.buildForecastArray(currentWeather, weatherData.list);
    } catch (error: any) {
      console.error(`❌ Error retrieving weather for city (${city}):`, error.message);
      throw error;
    }"

LINK NUMBER 21

File path: Dashboard/streamlit/district_dashboard.py
"monthly_fig.update_traces(textposition='top center')  # Adjust label positioning

col2.subheader(""Monthly Accident Trend"")
col2.plotly_chart(monthly_fig)

# Weekly Trend
st.subheader(""Weekly Accident Trend"")
weekday_counts = final_filtered_df['Weekday'].value_counts().sort_index()
weekday_fig = px.bar(
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    y=weekday_counts.values,
    labels={'x': 'Day of the Week', 'y': 'Number of Accidents'}
)
st.plotly_chart(weekday_fig)

# Urban/Rural & Vehicle Breakdown
col3, col4 = st.columns(2)
urban_rural_counts = final_filtered_df['Urban_or_Rural_Area'].value_counts()
urban_rural_fig = px.bar(x=urban_rural_counts.index, y=urban_rural_counts.values, text=urban_rural_counts.values,
                          labels={'x': 'Location Type', 'y': 'Number of Accidents'})
col3.subheader(""Urban vs. Rural Accidents"")
col3.plotly_chart(urban_rural_fig)

vehicle_category_counts = final_filtered_df['Vehicle_Category'].value_counts()
vehicle_category_fig = px.bar(x=vehicle_category_counts.index, y=vehicle_category_counts.values, text=vehicle_category_counts.values,
                              labels={'x': 'Vehicle Type', 'y': 'Number of Accidents'})
col4.subheader(""Vehicle Type Breakdown"")
col4.plotly_chart(vehicle_category_fig)

# Light Conditions vs Severity & Road Surface Conditions vs Severity
col5, col6 = st.columns(2)
light_severity_fig = px.histogram(final_filtered_df, x='Light_Conditions', color='Accident_Severity', barmode='group',
                                  labels={'Light_Conditions': 'Lighting', 'Accident_Severity': 'Severity'})
col5.subheader(""Light Conditions vs. Severity"")
col5.plotly_chart(light_severity_fig)

road_surface_fig = px.histogram(final_filtered_df, x='Road_Surface_Conditions', color='Accident_Severity', barmode='group',
                                labels={'Road_Surface_Conditions': 'Road Surface', 'Accident_Severity': 'Severity'})
col6.subheader(""Road Surface Conditions vs. Severity"")
col6.plotly_chart(road_surface_fig)"

LINK NUMBER 22
Error fetching diff

LINK NUMBER 23
Error fetching diff

LINK NUMBER 24
Error fetching diff

LINK NUMBER 25
Not enough lines

LINK NUMBER 26
Not enough lines

LINK NUMBER 27

File path: BlackWidow.py
"    messages = {
        ""Empty"": ""****WARNING - YOU ARE OUT OF GAS****\nCalling AAA..."",
        ""Low"": f""Your gas tank is extremely low, checking GPS for the closest gas station...\n""
               f""The closest gas station is {gas_stations()} which is {miles_to_gas_station['Low']} miles away."",
        ""Quarter Tank"": f""Your gas tank is at a Quarter Tank, checking GPS for the closest gas station...\n""
                        f""The closest gas station is {gas_stations()} which is {miles_to_gas_station['Quarter Tank']} miles away."",
        ""Half Tank"": ""Your gas tank is Half Full, plenty to get to your destination!"",
        ""Three Quarter Tank"": ""Your gas tank is Three Quarters Full!"",
        ""Full Tank"": ""Your gas tank is FULL, Vroom Vroom!""
    }

    print(messages[gas_level])

print(""\n****************************************\n"")
print(""Gasoline Branch - Developer Linus Riddle\n"")"

LINK NUMBER 28

File path: test/unit/test_translator.py
"# def test_japanese():
#     is_english, translated_content = translate_content(""これは日本語のメッセージです"")
#     assert is_english == False
#     assert translated_content == ""This is a Japanese message""

# def test_detect_chinese():
#     is_english, translated_content = translate_content(""这是中文"")
#     assert is_english == False
#     assert translated_content == ""This is Chinese""

# Evaluation dataset
translation_eval_set = [
    {
        ""post"": ""Hier ist dein erstes Beispiel."",
        ""expected_answer"": ""Here is your first example.""
    },
    {
        ""post"": ""¿Dónde está la biblioteca?"",
        ""expected_answer"": ""Where is the library?""
    },
    {
        ""post"": ""Je t’aime beaucoup."",
        ""expected_answer"": ""I love you very much.""
    },
    {
        ""post"": ""今日は天気がいいですね。"",
        ""expected_answer"": ""The weather is nice today, isn't it?""
    },
    {
        ""post"": ""Ciao, come stai?"",
        ""expected_answer"": ""Hi, how are you?""
    },
    {
        ""post"": ""나는 한국어를 배우고 있어요."",
        ""expected_answer"": ""I am learning Korean.""
    },
    {
        ""post"": ""Спасибо за помощь!"",
        ""expected_answer"": ""Thank you for the help!""
    },
    {
        ""post"": ""Buongiorno, signore."",
        ""expected_answer"": ""Good morning, sir.""
    },
    {
        ""post"": ""J'ai besoin d'aide."",
        ""expected_answer"": ""I need help.""
    },
    {
        ""post"": ""这是什么东西？"",
        ""expected_answer"": ""What is this thing?""
    },
]

@pytest.mark.parametrize(""test_case"", translation_eval_set)
def test_translation(test_case):
    post = test_case[""post""]
    expected_answer = test_case[""expected_answer""]

    # Call the function to test
    is_english, translated_content = translate_content(post)

    # Assert that the translation matches the expected answer
    assert is_english == False  # Assuming all posts are non-English
    assert translated_content == expected_answer



# Language detection evaluation dataset
language_detection_eval_set = [
    {
        ""post"": ""Hier ist dein erstes Beispiel."",
        ""expected_answer"": ""German""
    },
    {
        ""post"": ""¿Dónde está la biblioteca?"",
        ""expected_answer"": ""Spanish""
    },
    {
        ""post"": ""Je t’aime beaucoup."",
        ""expected_answer"": ""French""
    },
    {
        ""post"": ""今日は天気がいいですね。"",
        ""expected_answer"": ""Japanese""
    },
    {
        ""post"": ""Ciao, come stai?"",
        ""expected_answer"": ""Italian""
    },
    {
        ""post"": ""나는 한국어를 배우고 있어요."",
        ""expected_answer"": ""Korean""
    },
    {
        ""post"": ""Спасибо за помощь!"",
        ""expected_answer"": ""Russian""
    },
    {
        ""post"": ""Buongiorno, signore."",
        ""expected_answer"": ""Italian""
    },
    {
        ""post"": ""J'ai besoin d'aide."",
        ""expected_answer"": ""French""
    },
    {
        ""post"": ""这是什么东西？"",
        ""expected_answer"": ""Chinese""
    },
]

@pytest.mark.parametrize(""test_case"", language_detection_eval_set)
def test_detect_language(test_case):
    post = test_case[""post""]
    expected_answer = test_case[""expected_answer""]

    # Call the function to test
    detected_language = detect_language(post)

    # Assert that the detected language matches the expected answer
    assert detected_language == expected_answer"

LINK NUMBER 29
Error fetching diff

LINK NUMBER 30
Error fetching diff

LINK NUMBER 31
Error fetching diff

LINK NUMBER 32
Not enough lines

LINK NUMBER 33
Not enough lines

LINK NUMBER 34
Not enough lines

LINK NUMBER 35
Not enough lines

LINK NUMBER 36
Error fetching diff

LINK NUMBER 37
Error fetching diff

LINK NUMBER 38
Error fetching diff

LINK NUMBER 39

File path: An Animal Contest 2 P0 - Koala Matchmaking.py
"# https://dmoj.ca/problem/aac2p0

n = int(input())

if n%2 ==0:
    x=n-2
else:
    x=n-1

a = (n+x)//2
print(a)"

LINK NUMBER 40

File path: sappyspellbook/quizzes/script.js
"}


function parseSpellText(spell) {
  // Extracting relevant properties from the text field
  const regexPatterns = {
    freq: /<p3>Freq:<\/p3>\s*([^<]*)/,
    school: /<p3>School:<\/p3>\s*([^<]*)/,
    range: /<p3>Range:<\/p3>\s*([^<]*)/,
    materials: /<p3>Materials:<\/p3>\s*([^<]*)/,
    effect: /<p3>Effect:<\/p3>\s*([^<]*)/,
    limitations: /<p3>Limitations:<\/p3>\s*([^<]*)/,
    notes: /<p3>Notes:<\/p3>\s*([^<]*)/
  };

  let extractedData = {};

  for (let key in regexPatterns) {
    let match = spell.text.match(regexPatterns[key]);
    extractedData[key] = match ? match[1].trim() : """";
  }

  // Creating the cleaned spell object
  return {
    ...spell,
    freq: extractedData.freq,
    school: extractedData.school,
    range: extractedData.range,
    materials: extractedData.materials,
    effect: extractedData.effect,
    limitations: extractedData.limitations,
    notes: extractedData.notes,
    text: """" // Clear out the original text field
  };"

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

File path: src/components/HomePage.js
"  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const loadFont = async () => {
      await document.fonts.load('1rem ""Inter""');
      document.body.classList.add('font-inter');
    };
    
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap';
    link.rel = 'stylesheet';
    document.head.appendChild(link);
    
    loadFont();
  }, []);

  return (
    <header className=""w-full bg-gradient-to-r from-purple-500/10 to-purple-600/5 backdrop-blur-sm border-b border-purple-100/20"">
      <div className=""max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"">
        <nav className=""flex items-center justify-between h-16"">
          {/* Logo/Name */}
          <div className=""flex-shrink-0"">
            <Link 
              to=""/"" 
              className=""text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-semibold bg-gradient-to-r from-purple-600 to-purple-800 bg-clip-text text-transparent hover:opacity-80 transition-opacity font-inter""
            >
              Marcus Lam
            </Link>
          </div>

          {/* Desktop Navigation Links */}
          <div className=""hidden sm:flex sm:space-x-8"">
            <Link
              to=""/projects""
              className=""group relative px-3 py-2 text-base md:text-lg font-medium text-gray-700 transition-colors font-inter""
            >
              <span className=""relative"">
                Projects
                <span className=""absolute bottom-[-24px] left-0 h-[2px] w-full origin-left scale-x-0 transform bg-purple-600 transition-transform duration-300 ease-out group-hover:scale-x-100""></span>
              </span>
            </Link>
            <Link
              to=""/news""
              className=""group relative px-3 py-2 text-base md:text-lg font-medium text-gray-700 transition-colors font-inter""
            >
              <span className=""relative"">
                News
                <span className=""absolute bottom-[-24px] left-0 h-[2px] w-full origin-left scale-x-0 transform bg-purple-600 transition-transform duration-300 ease-out group-hover:scale-x-100""></span>
              </span>
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <div className=""sm:hidden"">
            <button
              type=""button""
              className=""text-gray-700 hover:text-purple-600 p-2 rounded-md transition-colors""
              aria-label=""Toggle menu""
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            >
              <svg
                className=""h-6 w-6""
                fill=""none""
                viewBox=""0 0 24 24""
                stroke=""currentColor""
              >
                <path
                  strokeLinecap=""round""
                  strokeLinejoin=""round""
                  strokeWidth={2}
                  d={isMobileMenuOpen ? ""M6 18L18 6M6 6l12 12"" : ""M4 6h16M4 12h16M4 18h16""}
                />
              </svg>
            </button>
          </div>
        </nav>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className=""sm:hidden pb-4"">
            <div className=""flex flex-col space-y-4"">
              <Link
                to=""/projects""
                className=""px-3 py-2 text-base font-medium text-gray-700 hover:text-purple-600 transition-colors""
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Projects
              </Link>
              <Link
                to=""/news""
                className=""px-3 py-2 text-base font-medium text-gray-700 hover:text-purple-600 transition-colors""
                onClick={() => setIsMobileMenuOpen(false)}
              >
                News
              </Link>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;"

LINK NUMBER 48

File path: main.cpp
"	Piece(Piece&& other) noexcept :
		_attrs_map(std::move(other._attrs_map)),
		_current_loc(std::move(other._current_loc)),
		_name(std::move(other._name)),
		_symbol(other._symbol)
	{}
	
	Piece& operator=(Piece&& other) noexcept {
		if(this != &other) {
			_attrs_map = std::move(other._attrs_map);
			_current_loc = std::move(other._current_loc);
			_name = std::move(other._name);
			_symbol = other._symbol;
		}
		return *this;
	}
	
	Piece(const Piece& other)
	: _attrs_map(other._attrs_map),
	_name(other._name),
	_symbol(other._symbol) {
		if(other._current_loc) 
			_current_loc = std::make_unique<cc::BoardCoord>(*other._current_loc);
		else _current_loc = nullptr;
	}
	
	// Copy assignment (deep copy)
    Piece& operator=(const Piece& other) {
        if (this != &other) {
            _attrs_map = other._attrs_map;
            _name = other._name;
            _symbol = other._symbol;
            if (other._current_loc) {
                _current_loc = std::make_unique<cc::BoardCoord>(*other._current_loc);
            } else {
                _current_loc.reset();
            }
        }
        return *this;
    }
"

LINK NUMBER 49

File path: pkcs8-mytry.js
"<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>RSA Key Pair Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        #output {
            margin-top: 20px;
        }
        textarea {
            width: 100%;
            height: 200px;
            margin-top: 10px;
            font-family: monospace;
            white-space: pre-wrap;
        }
        button {
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background-color: #45a049;
        }
        #zipLink {
            display: none;
        }
    </style>
    <script src=""https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js""></script>
</head>
<body>
    <h1>RSA Key Pair Generator</h1>
    <p>Click the button below to generate a 2048-bit RSA key pair and download them, along with the key components in decimal format as a ZIP file.</p>
    <button id=""generateBtn"">Generate RSA Key Pair</button>
    <div id=""output"">
        <h3>Download Link:</h3>
        <a id=""zipLink"" href=""#"" download=""rsa_key_pair.zip"">Download RSA Key Pair and Components (ZIP)</a>
        <h3>Key Components (in Decimal):</h3>
        <pre id=""keyComponents""></pre>
    </div>

    <script>
        async function generateRSAKeyPair() {
            try {
                // Generate RSA key pair with 2048-bit modulus
                const keyPair = await window.crypto.subtle.generateKey(
                    {
                        name: ""RSA-OAEP"",
                        modulusLength: 2048, // 2048-bit modulus
                        publicExponent: new Uint8Array([1, 0, 1]), // 65537 in hexadecimal
                        hash: { name: ""SHA-256"" },
                    },
                    true,
                    [""encrypt"", ""decrypt""]
                );

                // Export public key in SPKI format (PEM)
                const publicKeySpki = await window.crypto.subtle.exportKey(""spki"", keyPair.publicKey);
                const publicKeyPem = arrayBufferToPem(publicKeySpki, ""PUBLIC KEY"");

                // Export private key in PKCS8 format (PEM)
                const privateKeyPkcs8 = await window.crypto.subtle.exportKey(""pkcs8"", keyPair.privateKey);
                const privateKeyPem = arrayBufferToPem(privateKeyPkcs8, ""PRIVATE KEY"");

                // Extract key components from private key in JWK format
                const privateKeyJson = await window.crypto.subtle.exportKey(""jwk"", keyPair.privateKey);
                const publicKeyJson = await window.crypto.subtle.exportKey(""jwk"", keyPair.publicKey);

                // Extract modulus, public exponent, private exponent, p, q
                const n = publicKeyJson.n;  // Modulus (n)
                const e = publicKeyJson.e;  // Public exponent (e)
                const d = privateKeyJson.d; // Private exponent (d)
                const p = privateKeyJson.p; // Prime factor (p)
                const q = privateKeyJson.q; // Prime factor (q)

                // Convert from Base64URL to Decimal
                const nDecimal = base64urlToDecimal(n);
                const eDecimal = base64urlToDecimal(e);
                const dDecimal = base64urlToDecimal(d);
                const pDecimal = base64urlToDecimal(p);
                const qDecimal = base64urlToDecimal(q);

                // Display extracted key components in decimal
                document.getElementById('keyComponents').textContent = `
Modulus (N): ${nDecimal}
Public Exponent (e): ${eDecimal}
Private Exponent (d): ${dDecimal}
Prime Factor (p): ${pDecimal}
Prime Factor (q): ${qDecimal}
                `;

                // Create ZIP file
                const zip = new JSZip();
                zip.file(""public_key.pem"", publicKeyPem);
                zip.file(""private_key.pem"", privateKeyPem);
                zip.file(""rsa_key_components.txt"", `
Modulus (N): ${nDecimal}
Public Exponent (e): ${eDecimal}
Private Exponent (d): ${dDecimal}
Prime Factor (p): ${pDecimal}
Prime Factor (q): ${qDecimal}
                `);

                // Generate the ZIP file and create a download link
                const zipBlob = await zip.generateAsync({ type: ""blob"" });
                const zipLink = document.getElementById('zipLink');
                const zipUrl = URL.createObjectURL(zipBlob);
                zipLink.href = zipUrl;
                zipLink.style.display = 'block';  // Show the download link
            } catch (error) {
                console.error(""Error generating key pair:"", error);
                alert(""Error generating RSA keys."");
            }
        }

        // Convert ArrayBuffer to PEM format
        function arrayBufferToPem(buffer, type) {
            const base64 = arrayBufferToBase64(buffer);
            return `-----BEGIN ${type}-----\n${base64}\n-----END ${type}-----`;
        }

        // Convert ArrayBuffer to Base64 encoded string
        function arrayBufferToBase64(buffer) {
            const binary = String.fromCharCode.apply(null, new Uint8Array(buffer));
            return window.btoa(binary);
        }

        // Convert Base64URL string to Decimal string
        function base64urlToDecimal(base64urlStr) {
            // Replace Base64URL specific characters with standard Base64
            const base64Str = base64urlStr.replace(/-/g, '+').replace(/_/g, '/');
            const binaryString = window.atob(base64Str);
            let decimalValue = BigInt(0);

            for (let i = 0; i < binaryString.length; i++) {
                const byteValue = binaryString.charCodeAt(i);
                decimalValue = (decimalValue << 8n) + BigInt(byteValue);
            }

            return decimalValue.toString();
        }

        // Add event listener to button
        document.getElementById('generateBtn').addEventListener('click', generateRSAKeyPair);
    </script>
</body>
</html>"

LINK NUMBER 50
Error fetching diff

LINK NUMBER 51
Error fetching diff

LINK NUMBER 52
Error fetching diff

LINK NUMBER 53

File path: gen_ai/task2.2/Jaydan_docstring_update.cpp
"// Old undocumented code
void placeRandomPiece(int gameBoard[BOARD_HEIGHT][BOARD_WIDTH], bool& startOfGame)
{
	srand(time(0));

	if(startOfGame == true)
	{
		for(int i = 0; i < 2; i++)
		{
			int row = rand() % 4;
			int column = rand() % 4;

			if(gameBoard[row][column] == EMPTY)
			{
				gameBoard[row][column] = 1;
				continue;
			}
			else
			{
				continue;
			}
		}
		startOfGame = false;
	}
	else
	{
		do
		{
			int row = rand() % 4;
			int column = rand() % 4;

			if(gameBoard[row][column] == EMPTY)
			{
				gameBoard[row][column] = 1;
				break;
			}
			else
			{
				continue;
			}
		} while(true);
	}

	
}


// New documented code
void placeRandomPiece(int gameBoard[BOARD_HEIGHT][BOARD_WIDTH], bool& startOfGame)
{
    // Seed the random number generator with the current time to ensure different outputs each run
    srand(time(0));

    // Check if it's the start of the game
    if(startOfGame == true)
    {
        // At the beginning of the game, place two pieces randomly on the board
        for(int i = 0; i < 2; i++)
        {
            int row = rand() % 4;    // Generate a random row index (0 to 3)
            int column = rand() % 4; // Generate a random column index (0 to 3)

            // Check if the chosen position is empty
            if(gameBoard[row][column] == EMPTY)
            {
                gameBoard[row][column] = 1; // Place a new tile with the value 1
                continue; // Continue to the next piece placement
            }
            else
            {
                continue; // If the position is occupied, try again in the next loop iteration
            }
        }
        // After placing the initial two pieces, set startOfGame to false
        startOfGame = false;
    }
    else
    {
        // During normal gameplay, place a single piece in a random empty spot
        do
        {
            int row = rand() % 4;    // Generate a random row index
            int column = rand() % 4; // Generate a random column index

            // Check if the chosen position is empty
            if(gameBoard[row][column] == EMPTY)
            {
                gameBoard[row][column] = 1; // Place a new tile with the value 1
                break; // Exit the loop once a piece is placed successfully
            }
            else
            {
                continue; // If the position is occupied, retry until a valid position is found
            }
        } while(true); // Infinite loop until a valid placement is made
    }
}"

LINK NUMBER 54
Too many lines

LINK NUMBER 55
Not enough lines

LINK NUMBER 56
Not enough lines

LINK NUMBER 57
Error fetching diff

LINK NUMBER 58
Error fetching diff

LINK NUMBER 59
Error fetching diff

LINK NUMBER 60
Not enough lines

LINK NUMBER 61
Not enough lines

LINK NUMBER 62
Not enough lines

LINK NUMBER 63

File path: src/lptlib/io/dataio.py
"            final_data = None

        # Flatten the local data for sending
        sendbuf = local_data.ravel()

        # Determine the MPI datatype corresponding to the numpy dtype.
        # This works for common types (e.g. 'd' for float64, 'i' for int32, etc.).
        mpi_dtype = MPI._typedict[local_data.dtype.char]

        # On root, prepare counts and displacements for Gatherv.
        if rank == 0:
            counts = [r * local_cols for r in all_rows]
            displacements = [sum(counts[:i]) for i in range(len(counts))]
        else:
            counts = None
            displacements = None

        # Use Gatherv to gather the flattened arrays into final_data (also flattened).
        comm.Gatherv(sendbuf, [final_data, counts, displacements, mpi_dtype], root=0)

        comm.Barrier()  # Synchronize processes
        return final_data if rank == 0 else None"

LINK NUMBER 64
Error fetching diff

LINK NUMBER 65
Error fetching diff

LINK NUMBER 66
Error fetching diff

LINK NUMBER 67
Not enough lines

LINK NUMBER 68
Not enough lines

LINK NUMBER 69
Not enough lines

LINK NUMBER 70
Not enough lines

LINK NUMBER 71
Error fetching diff

LINK NUMBER 72
Error fetching diff

LINK NUMBER 73
Error fetching diff

LINK NUMBER 74
Not enough lines

LINK NUMBER 75

File path: debugging/tic.py
"def print_board(board):
    for row in board:
        print("" | "".join(row))
        print(""-"" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "" "":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "" "":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "" "":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "" "":
        return True

    return False

def tic_tac_toe():
    board = [["" ""]*3 for _ in range(3)]
    player = ""X""
    move_count = 0  # To track the number of moves

    while move_count < 9 and not check_winner(board):  # Max 9 moves
        print_board(board)

        # Get valid user input
        while True:
            try:
                row = int(input(f""Enter row (0, 1, or 2) for player {player}: ""))
                col = int(input(f""Enter column (0, 1, or 2) for player {player}: ""))
                if 0 <= row < 3 and 0 <= col < 3:  # Ensure valid range for row and column
                    if board[row][col] == "" "":
                        break  # If the spot is empty, exit the loop
                    else:
                        print(""That spot is already taken! Try again."")
                else:
                    print(""Invalid input! Row and column must be between 0 and 2."")
            except ValueError:
                print(""Invalid input! Please enter integer values for row and column."")

        # Make the move
        board[row][col] = player
        move_count += 1

        # Switch player
        if player == ""X"":
            player = ""O""
        else:
            player = ""X""

    print_board(board)

    # After the loop ends, check for the winner
    if check_winner(board):
        # The player who made the last move is the winner
        if player == ""X"":
            print(""Player O wins!"")
        else:
            print(""Player X wins!"")
    else:
        print(""It's a draw!"")

tic_tac_toe()
"

LINK NUMBER 76
Not enough lines

LINK NUMBER 77
Not enough lines

LINK NUMBER 78
Error fetching diff

LINK NUMBER 79
Error fetching diff

LINK NUMBER 80
Error fetching diff

LINK NUMBER 81
Not enough lines

LINK NUMBER 82
Not enough lines

LINK NUMBER 83
Not enough lines

LINK NUMBER 84

File path: LeaveManagementSystem.Common/Functions.cs
"
    //-------------------------------------------------------------------------------------------------
    //-------------------------------------------------------------------------------------------------
    //-------------------------------------------------------------------------------------------------

    public class DateValidationAttribute : ValidationAttribute //27/04/25 from chstGPT
    {
        private readonly int _minimumDate;
        private readonly int _maximumDate; //mine
        private readonly string _prefix; //mine
        private readonly string _suffix;

        public DateValidationAttribute(int minimumDate, int maximumDate, string prefix = ""Employee"", string suffix = "" years old"")
        {
            //note: prefix & suffix jic i need to expand this in the future. 27/04/25
            _minimumDate = minimumDate;
            _maximumDate = maximumDate; //mine
            _prefix = prefix; //mine
            this._suffix = suffix;
            ErrorMessage = $""{_prefix} must be between {_minimumDate} and {_maximumDate}{_suffix}.""; //mine
        }

        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if ((value is DateOnly) || (value is DateTime))
            {
                DateOnly dob = value is DateTime ? DateOnly.FromDateTime((DateTime)value) : (DateOnly)value;

                var today = DateTime.Today;
                var age = today.Year - dob.Year;
                if (dob > DateOnly.FromDateTime(today.AddYears(-age))) age--;

                if ((age < _minimumDate) || (age > _maximumDate)) //mine
                {
                    return new ValidationResult(ErrorMessage);
                }

                return ValidationResult.Success!;
            }

            return new ValidationResult(""Invalid date format."");
        }
    }
"

LINK NUMBER 85
Error fetching diff

LINK NUMBER 86
Error fetching diff

LINK NUMBER 87
Not enough lines

LINK NUMBER 88
Not enough lines

LINK NUMBER 89
Not enough lines

LINK NUMBER 90
Not enough lines

LINK NUMBER 91
Error fetching diff

LINK NUMBER 92
Error fetching diff

LINK NUMBER 93
Error fetching diff

LINK NUMBER 94
Not enough lines

LINK NUMBER 95
Not enough lines

LINK NUMBER 96

File path: Project-Files/smtp_server.py
"import aiosmtpd
from aiosmtpd.handlers import Message
from email.parser import Parser

class EmailHandler(Message):
    def __init__(self):
        super().__init__()

    async def handle_DATA(self, server, session, envelope):
        # Parse the email message content
        message = Parser().parsestr(envelope.content.decode())
        subject = message.get(""Subject"", ""No Subject"")
        sender = message.get(""From"", ""Unknown Sender"")
        recipient = message.get(""To"", ""Unknown Recipient"")
        body = envelope.content.decode()

        # Create or append to a .txt file
        with open(""emails_received.txt"", ""a"") as file:
            file.write(f""--- New Email ---\n"")
            file.write(f""From: {sender}\n"")
            file.write(f""To: {recipient}\n"")
            file.write(f""Subject: {subject}\n"")
            file.write(f""Body:\n{body}\n"")
            file.write(""-"" * 40 + ""\n"")

        print(f""✅ Email saved to emails_received.txt"")
        return ""250 Message accepted for delivery""

# Set up the SMTP server
async def run_server():
    handler = EmailHandler()
    server = aiosmtpd.controller.Controller(handler, hostname='localhost', port=1025)
    server.start()
    print(""🚀 Local SMTP server running on localhost:1025"")

if __name__ == ""__main__"":
    import asyncio
    asyncio.run(run_server())"

LINK NUMBER 97
Not enough lines

LINK NUMBER 98
Error fetching diff

LINK NUMBER 99
Error fetching diff

LINK NUMBER 100
Error fetching diff

LINK NUMBER 101
Not enough lines

LINK NUMBER 102

File path: snoot-city/src/utilities/petfinder-Api.js
"

const getAuthToken = async () => {
    const response = await fetch(""https://api.petfinder.com/v2/oauth2/token"", {
        method: ""POST"",
        headers: {
            ""Content-Type"": ""application/x-www-form-urlencoded"",
        },
        body: new URLSearchParams({
            grant_type: ""client_credentials"",
            client_id: import.meta.env.VITE_PETFINDER_CLIENT_ID,
            client_secret: import.meta.env.VITE_PETFINDER_CLIENT_SECRET,
        }),
    });

    const data = await response.json();
    return data.access_token;
};

async function GetSighthounds() { // Default location = UK
    const token = await getAuthToken();

    const sighthoundBreeds = [
        ""Greyhound"",
        ""Whippet"",
        ""Saluki"",
        ""Afghan Hound"",
        ""Borzoi"",
        ""Ibizan Hound"",
        ""Italian Greyhound"",
        ""Scottish Deerhound"",
        ""Sloughi"",
    ];

    const response = await fetch(
        `https://api.petfinder.com/v2/animals?type=dog&breed=${sighthoundBreeds.join("","")}`,
        {
            method: ""GET"",
            headers: {
                Authorization: `Bearer ${token}`,
                ""Content-Type"": ""application/json"",
            },
        }
    );

    const data = await response.json();
    console.log(data)
    console.log(data.animals)
    return data.animals; // Return only the list of animals
}

// GetSighthounds();

export default GetSighthounds"

LINK NUMBER 103
Not enough lines

LINK NUMBER 104

"File path: Code_exercise1,4.py"
"import os
import random
import matplotlib.pyplot as plt
from PIL import Image

def visualize_Images(directory, nr_samples=5):
    classes = {""0"": ""Without Metastases"", ""1"": ""With Metastases""}     #train and validation map exists of a '0' and a '1' map
    samples = {}	
    for Group in classes.keys():
        samples[Group] = get_sample_images(directory, Group, nr_samples)
    print(samples)


    fig, axes = plt.subplots(2, nr_samples, figsize=(15, 6))          #create figure
    fig.suptitle(""Comparison of tissue with or without metastases"", fontsize=14)


    for i, Group in enumerate(classes.keys()):
        for j, img_name in enumerate(samples[Group]):
            img_path = os.path.join(directory, Group, img_name)
            img = Image.open(img_path)

            axes[i, j].imshow(img)
            axes[i, j].axis(""off"")
            if j == 0:  # Label only the first image in each row
                axes[i, j].set_title(classes[Group], fontsize=12)

    plt.tight_layout()
    plt.show()


#Function to get the sample images from each class
def get_sample_images(directory, Classnr, num_samples=5):
    Class_path = os.path.join(directory, Classnr)
    image_files = [f for f in os.listdir(Class_path) if f.endswith(("".jpg""))]
    return random.sample(image_files, min(num_samples, len(image_files)))               #take random samples from data


# Run for training dataset
visualize_Images(""train"")


# Run for validation dataset
visualize_Images(""valid"")
"

LINK NUMBER 105
Error fetching diff

LINK NUMBER 106
Error fetching diff

LINK NUMBER 107
Not enough lines

LINK NUMBER 108
Not enough lines

LINK NUMBER 109

File path: CastleBravo.py
"# Reset display cursor after running a test
print(TextColors.RESET, end="""")

# Initialize counters for the boot process
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis effect

timetosleep = 4  # variable to set the time library to 4 seconds when called
time.sleep(timetosleep)  # calling the time to sleep library with the variable time

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the boot counter
    # Create a booting message with an ellipsis effect and cyan color
    message = f""{TextColors.CYAN}InfoTech Center System Booting"" + ""."" * ellipsis + f""{TextColors.RESET}""
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write(""\r"" + message)  # Overwrite the current line with the message
    time.sleep(0.2)  # Pause for half a second

    # Reset ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

Certainly! Here’s the code without the comments:

python
Copy code
import time
import sys

class TextColors:
    RESET = ""\033[0m""
    RED = ""\033[91m""
    GREEN = ""\033[92m""
    YELLOW = ""\033[93m""
    CYAN = ""\033[96m""

def log(message, level=""INFO"", color=TextColors.RESET):
    print(f""{color}[{level}] {message}{TextColors.RESET}"")

LOG_LEVELS = {
    ""INFO"": (TextColors.GREEN, ""INFO""),
    ""WARNING"": (TextColors.YELLOW, ""WARNING""),
    ""ERROR"": (TextColors.RED, ""ERROR""),
}

def log_message(level, message):
    color, level_str = LOG_LEVELS.get(level, (TextColors.RESET, ""INFO""))
    log(message, level=level_str, color=color)

for i in range(5):
    if i == 0:
        log_message(""INFO"", ""Process started"")
    elif i == 3:
        log_message(""WARNING"", ""CPU usage is high"")
    elif i == 4:
        log_message(""ERROR"", ""Process failed"")
    else:
        log_message(""INFO"", f""Running iteration {i}"")

print(TextColors.RESET, end="""")
"

LINK NUMBER 110

File path: popup.js
"<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Blocking Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            width: 200px;
        }
        .time-remaining {
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <h2>Time Remaining:</h2>
    <div class=""time-remaining"" id=""timeRemaining"">Loading...</div>
    <script src=""popup.js""></script>
</body>
</html>
"

LINK NUMBER 111
Error fetching diff

LINK NUMBER 112
Error fetching diff

LINK NUMBER 113
Error fetching diff

LINK NUMBER 114
Error fetching diff

LINK NUMBER 115
Not enough lines

LINK NUMBER 116
Not enough lines

LINK NUMBER 117

File path: LeetCode/1371.py
"# 1371. Find the Longest Substring Containing Vowels in Even Counts

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = 0
        max_length = 0
        seen = {0: -1} # bitmask 0 at index -1

        for i in range(len(s)):
            c = s[i]
            if c == 'a':
                bitmask ^= 1 << 0  # Flip the 0th bit for 'a'
            elif c == 'e':
                bitmask ^= 1 << 1  # Flip the 1st bit for 'e'
            elif c == 'i':
                bitmask ^= 1 << 2  # Flip the 2nd bit for 'i'
            elif c == 'o':
                bitmask ^= 1 << 3  # Flip the 3rd bit for 'o'
            elif c == 'u':
                bitmask ^= 1 << 4  # Flip the 4th bit for 'u'
            
            # Check if the current bitmask has been seen before
            if bitmask in seen:
                # Calculate the length of the valid substring
                max_length = max(max_length, i - seen[bitmask])
                #print(s[i:seen[bitmask]])
            else:
                # If it's the first time we see this bitmask, store the index
                seen[bitmask] = i
        return max_length"

LINK NUMBER 118
Error fetching diff

LINK NUMBER 119
Error fetching diff

LINK NUMBER 120
Not enough lines

LINK NUMBER 121
Not enough lines

LINK NUMBER 122

File path: src/intrumentation.ts
"/**
 * @file instrumentation.ts
 *
 * 🎭 **Welcome to the Instrumentation Zone!** 🎭
 *
 * This file is currently **as empty as a production database on day one** – but fear not!
 * It's the **designated home** for all things related to **performance monitoring, logging, and tracing**
 * in our Next.js App Router project.
 *
 * ## 🎯 Purpose:
 * - Next.js offers an **Instrumentation API** that lets us **peek under the hood**
 *   and understand how our app is behaving.
 * - This file will (eventually) be responsible for **tracking, measuring, and logging**
 *   critical performance and error metrics.
 * - Think of it as **a fitness tracker for your Next.js app** – but instead of counting steps,
 *   it counts **request times, rendering delays, and unexpected ""uh-ohs.""**
 *
 * ## 🔥 What Can We Do With This?
 * - **Monitor API requests** 🕵️‍♂️ – Ever wondered why your API response takes ages? We’ll find out!
 * - **Trace execution paths** 🗺️ – See where your requests are coming from and how they flow.
 * - **Collect error logs** 🚨 – Because ""works on my machine"" isn’t a logging strategy.
 * - **Profile React Server Components** 🏋️ – Lift those rendering weights, optimize performance!
 * - **Track middleware performance** ⏳ – Why did my middleware take longer than my coffee break?
 * - **Integrate with external monitoring tools** 📡 – Datadog, OpenTelemetry, Sentry, or whatever
 *   fancy logging tool your ops team loves.
 *
 * ## 📚 Useful References (for those who like to read before coding 🙃):
 * - 📖 Next.js Instrumentation API: https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation
 * - 🕵️ OpenTelemetry (Tracing in Next.js): https://opentelemetry.io/
 * - 🚨 Sentry (Error Monitoring for Next.js): https://docs.sentry.io/platforms/javascript/guides/nextjs/
 * - 📡 Datadog (Monitoring Next.js Apps): https://docs.datadoghq.com/tracing/setup_overview/setup/nodejs/
 *
 * ## 🤔 What's Next?
 * - 📌 **TODO:** Actually write some instrumentation logic.
 * - 🎤 **TODO:** Figure out why this file still isn't doing anything useful.
 * - 🔧 **TODO:** Add a coffee consumption tracker? (Okay, maybe not.)
 *
 * Until then, this file remains a **peaceful void**. 🌌
 */
"

LINK NUMBER 123
Not enough lines

LINK NUMBER 124
Error fetching diff

LINK NUMBER 125
Error fetching diff

LINK NUMBER 126
Error fetching diff

LINK NUMBER 127
Not enough lines

LINK NUMBER 128
Not enough lines

LINK NUMBER 129

File path: 9_pyramidGenerator.js
"function pyramid(pattern, rows, boo) {
    let result = """";

    if (!boo) { // Normal Pyramid
        for (let i = 1; i <= rows; i++) {
            let spaces = "" "".repeat(rows - i);
            let py = spaces + pattern.repeat(2 * i - 1);
            result += (i === 1 ? """" : ""\n"") + py;
        }
    } else { // Inverted Pyramid
        for (let i = rows; i >= 1; i--) {
            let spaces = "" "".repeat(rows - i);
            let py = spaces + pattern.repeat(2 * i - 1);
            result += (i === rows ? """" : ""\n"") + py;
        }
    }

    return ""\n"" + result + ""\n"";
}"

LINK NUMBER 130

File path: source_tracking/terminal_controls.py
"from Tracking import *
from Controls import *

def print_help():
    """"""
    Print usage instructions for the interactive commands.
    """"""
    print(
        """"""
    Available Commands:
    ------------------
    help or h
        Show this help message.

    t <L> <B>
        Track a target at galactic coordinates L, B continuously.
        Example: t 10 10

    s <L> <B>
        Slew immediately to the specified galactic coordinates (L, B).
        Example: s 10 15

    s <Az> <El> azel
        Slew immediately to specified horizontal coords (Az, El) in degrees.
        Example: s 180 45 azel

    r
        Restart the rotator.

    off or exit or q
        Terminate the program and exit.
    """"""
    )


def main():
    print(""Welcome to the Interactive Telescope Terminal"")

    # Instantiate the hardware control
    try:
        control = Rot2Prog()
        print(""Rot2Prog control initialized."")
    except Exception as e:
        print(f""Error initializing Rot2Prog: {e}"")
        control = None

    # Instantiate the high-level source tracking, passing in the control
    rotor = source_tracking(control=control)

    # Main command loop
    while True:
        cmd = input(""\nEnter command (type 'help' for options): "").strip().lower()

        if not cmd:
            continue

        if cmd in [""help"", ""h""]:
            print_help()
            continue

        if cmd in [""off"", ""exit"", ""quit"", ""q"", 'shutdown','off']:
            print(""\n ...Shutting down... \n"")
            # The rotator will be moved to stow mode.Need to add this 
            break

        if cmd == ""r"":
            if control is not None:
                try:
                    control.Restart()
                except Exception as e:
                    print(f""Error restarting rotator: {e}"")
            else:
                print(""No rotator control available to restart."")
            continue

        # ----------------------------------------------------------
        # T <L> <B> => continuous tracking
        # This starts or continues the 5-second update cycle
        # ----------------------------------------------------------
        if cmd.startswith(""t ""):
            parts = cmd.split()
            if len(parts) != 3:
                print(""Error: Usage: t <L> <B> (e.g., t 10 10)"")
                continue
            try:
                l_val = float(parts[1])
                b_val = float(parts[2])
            except ValueError:
                print(""Invalid numeric values for L, B."")
                continue

            # Set the rotor's current galactic coords
            rotor.current_lb = SkyCoord(l=l_val*u.deg, b=b_val*u.deg, frame='galactic')
            print(f""\nTarget galactic coordinates set to: L={l_val:.2f}°, B={b_val:.2f}°.\n"")
            # Start or continue the monitoring loop
            rotor._monitor_pointing(update_time=5)
            # If user hits Ctrl+C, we'll return here
            continue

        # ----------------------------------------------------------
        # Slew => s ...
        #   s <L> <B>  or  s <Az> <El> azel
        # ----------------------------------------------------------
        if cmd.startswith(""s ""):
            parts = cmd.split()

            # 3 parts => presumably s <L> <B> (galactic)
            if len(parts) == 3:
                try:
                    L = float(parts[1])
                    B = float(parts[2])
                except ValueError:
                    print(""Invalid numeric values for L, B."")
                    continue

                current_time, az, el = rotor.tracking_galactic_coordinates(L, B)
                # Attempt immediate slew
                try:
                    rotor.set_pointing(az, el)
                    rotor.current_azel = SkyCoord(alt=el*u.deg, az=az*u.deg, frame='altaz')
                    rotor.current_lb = SkyCoord(l=L*u.deg, b=B*u.deg, frame='galactic')
                    rotor.telescope_pointing = rotor.current_azel
                    print(f""Slewed to galactic L={L:.2f}°, B={B:.2f}° => ""
                        f""Az={round(az)}°, El={round(el)}°"")
                except Exception as e:
                    print(f""Error in galactic slew: {e}"")

            # 4 parts => s <Az> <El> azel
            elif len(parts) == 4 and parts[-1] == ""azel"":
                try:
                    az = float(parts[1])
                    el = float(parts[2])
                except ValueError:
                    print(""Invalid numeric values for Az, El."")
                    continue

                # Attempt to slew to these horizontal coordinates
                try:
                    rotor.set_pointing(az, el)
                    rotor.current_azel = SkyCoord(alt=el*u.deg, az=az*u.deg, frame='altaz')
                    rotor.telescope_pointing = rotor.current_azel
                    rotor.current_lb = None  # We don't know the galactic coords here
                    print(f""Slewed to horizontal Az={round(az)}°, El={round(el)}°"")
                except Exception as e:
                    print(f""Error in az/el slew: {e}"")
            else:
                print(""Invalid usage. Try:\n  s <L> <B>\n  s <Az> <El> azel"")
            continue"

LINK NUMBER 131
Error fetching diff

LINK NUMBER 132
Error fetching diff

LINK NUMBER 133
Error fetching diff

LINK NUMBER 134
Not enough lines

LINK NUMBER 135
Not enough lines

LINK NUMBER 136
Not enough lines

LINK NUMBER 137
Not enough lines

LINK NUMBER 138
Error fetching diff

LINK NUMBER 139
Error fetching diff

LINK NUMBER 140
Error fetching diff

LINK NUMBER 141

File path: script.js
"
// Create function to create new palette board

let newButton = document.querySelector('.new-button');
newButton.addEventListener('click', () => {
  localStorage.setItem(`currentName`, ``);
  localStorage.setItem(`currentColor1`, `null`);
  localStorage.setItem(`currentColor2`, `null`);
  localStorage.setItem(`currentColor3`, `null`);
  localStorage.setItem(`currentColor4`, `null`);
  localStorage.setItem(`currentColor5`, `null`);
  localStorage.setItem(`currentColor6`, `null`);
  localStorage.setItem(`currentColor7`, `null`);
  currentColor1 = localStorage.getItem('currentColor1');
  currentColor2 = localStorage.getItem('currentColor2');
  currentColor3 = localStorage.getItem('currentColor3');
  currentColor4 = localStorage.getItem('currentColor4');
  currentColor5 = localStorage.getItem('currentColor5');
  currentColor6 = localStorage.getItem('currentColor6');
  currentColor7 = localStorage.getItem('currentColor7');
  for(let i = 1; i < 8; i++) {
    console.log(localStorage.getItem(`currentColor${i}`));
    if ((localStorage.getItem(`currentColor${i}`)) === 'null') {
      document.querySelector(`.column${i} label`).style.backgroundColor = 'lightgray';
      for(let j = 1; j < 10; j++) {
        document.querySelector(`.column${i} .shade${j}`).style.backgroundColor = 'lightgray';
        document.querySelector(`.column${i} .shade${j}`).textContent = null;
      }
      continue;
    } else {
      console.log('working');
      let hue = hexToHue(localStorage.getItem(`currentColor${i}`));
      shadeHue(hue, `${i}`);
      applyTrueColor((localStorage.getItem(`currentColor${i}`)), `${i}`);
    }
  }
  nameBox.value = null;
  while(savedNameBox.firstChild) {
    savedNameBox.removeChild(savedNameBox.firstChild);
  };
  savedNameBox.style.zIndex = 0;
})"

LINK NUMBER 142
Not enough lines

LINK NUMBER 143

File path: linkedlist.cpp
"
class Node{
        public:
        int data;
        Node* next;
        // defined a class node
        // defining a constructor
        Node(int val){
            data=val;
            next=nullptr;
        }
        
    };
class linkedlist{"
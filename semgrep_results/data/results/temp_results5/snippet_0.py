LINK NUMBER 1
Not enough lines

LINK NUMBER 2

File path: payments/api/views.py
"from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from decimal import Decimal
from payments.models import Payment


@method_decorator(csrf_exempt, name=""dispatch"")
class PaymeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        method = data.get(""method"")
        params = data.get(""params"", {})
        request_id = data.get(""id"")

        handler = {
            ""CheckPerformTransaction"": self.check_perform_transaction,
            ""CreateTransaction"": self.create_transaction,
            ""PerformTransaction"": self.perform_transaction,
            ""CheckTransaction"": self.check_transaction,
            ""CancelTransaction"": self.cancel_transaction,
        }.get(method)

        if handler:
            return handler(params, request_id)

        return Response({
            ""jsonrpc"": ""2.0"",
            ""error"": {""code"": -32601, ""message"": ""Method not found""},
            ""id"": request_id
        })

    def check_perform_transaction(self, params, request_id):
        try:
            payment_id = params[""account""][""payment_id""]
            amount = Decimal(params[""amount""]) / 100  # Payme sends amount in tiyin
            payment = get_object_or_404(Payment, id=payment_id)

            if payment.status != Payment.StatusChoices.PENDING:
                return self.error_response(-31050, ""Transaction already processed"", request_id)

            if amount != payment.amount:
                return self.error_response(-31001, ""Incorrect amount"", request_id)

            return self.success_response({""allow"": True}, request_id)
        except Exception:
            return self.error_response(-31099, ""Error in checking transaction"", request_id)

    def create_transaction(self, params, request_id):
        try:
            payment_id = params[""account""][""payment_id""]
            payme_transaction_id = params[""id""]
            payment = get_object_or_404(Payment, id=payment_id)

            if payment.transaction_id and payment.transaction_id != payme_transaction_id:
                return self.error_response(-31008, ""Transaction already exists"", request_id)

            payment.transaction_id = payme_transaction_id
            payment.save()

            return self.success_response({
                ""create_time"": int(time.time() * 1000),
                ""transaction"": payme_transaction_id,
                ""state"": 1,
                ""receivers"": None,
            }, request_id)

        except Exception:
            return self.error_response(-31099, ""Failed to create transaction"", request_id)

    def perform_transaction(self, params, request_id):
        try:
            transaction_id = params[""id""]
            payment = get_object_or_404(Payment, transaction_id=transaction_id)

            if payment.status == Payment.StatusChoices.COMPLETED:
                return self.success_response({
                    ""transaction"": transaction_id,
                    ""perform_time"": int(payment.updated_at.timestamp() * 1000),
                    ""state"": 2,
                }, request_id)
"

LINK NUMBER 3
Error fetching diff

LINK NUMBER 4
Error fetching diff

LINK NUMBER 5
Error fetching diff

LINK NUMBER 6
Not enough lines

LINK NUMBER 7
Not enough lines

LINK NUMBER 8
Not enough lines

LINK NUMBER 9
Not enough lines

LINK NUMBER 10
Error fetching diff

LINK NUMBER 11
Error fetching diff

LINK NUMBER 12
Error fetching diff

LINK NUMBER 13

File path: LC_Basics/app.py
"# Serve static files (CSS, JS)
app.mount(""/static"", StaticFiles(directory=""static""), name=""static"")

# Templates
templates = Jinja2Templates(directory=""frontend"")

@app.get(""/"", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(""index.html"", {""request"": request})
"

LINK NUMBER 14
Not enough lines

LINK NUMBER 15
Not enough lines

LINK NUMBER 16
Too many lines

LINK NUMBER 17
Error fetching diff

LINK NUMBER 18
Error fetching diff

LINK NUMBER 19
Error fetching diff

LINK NUMBER 20
Not enough lines

LINK NUMBER 21
Not enough lines

LINK NUMBER 22

File path: modules/screenshot.py
"import subprocess
import os
import json
from typing import List
from modules import config


def prepare_nuclei_target_file(groups: List[List[dict]], target_name: str) -> str:
    """"""
    Each group is a list of items (each item from httpx).
    We want to choose 1 URL from each group for scanning,
    plus any items that had missing fields.
    Writes them to `nuclei_targets_{target_name}.txt`.
    Returns the path to that file.
    """"""
    output_file = f""nuclei_targets_{target_name}.txt""
    urls = []
    for group in groups:
        # Just pick the first item in each group
        if group and len(group) > 0:
            item = group[0]
            urls.append(item[""url""])

    # Write to file
    with open(output_file, ""w"", encoding=""utf-8"") as fh:
        for url in urls:
            fh.write(url + ""\n"")

    return output_file


def run_nuclei(target_file: str, target_name: str) -> str:
    """"""
    Runs nuclei using the target_file, saves JSON results to config.NUCLEI_OUTPUT_JSON
    For clarity, let's store separate JSON for each domain to avoid collisions:
    e.g. nuclei_scan_output_{target_name}.json
    Returns path to the JSON file.
    """"""
    output_json = f""nuclei_scan_output_{target_name}.json""
    cmd = [
        config.NUCLEI_BIN,
        ""-l"",
        target_file,
        ""-t"",
        config.NUCLEI_TEMPLATES,
        ""-c"",
        ""50"",
        ""-bs"",
        ""100"",
        ""--json-export"",
        output_json,
    ]
    subprocess.run(cmd, check=True)
    return output_json


def parse_nuclei_output(json_export_file: str) -> List[dict]:
    """"""
    Nuclei's --json-export produces a JSON array of objects.
    Each object has keys like `info.description`, `info.severity`, and `url`.
    Returns a list of dicts with the relevant fields.
    """"""
    if not os.path.exists(json_export_file):
        return []

    with open(json_export_file, ""r"", encoding=""utf-8"") as fh:
        try:
            data = json.load(fh)
        except:
            data = []

    # data is a list of objects
    results = []
    for item in data:
        description = item.get(""info"", {}).get(""description"", ""N/A"")
        severity = item.get(""info"", {}).get(""severity"", ""N/A"")
        url = item.get(""host"", ""N/A"")  # or item.get(""matched"")
        results.append({""url"": url, ""description"": description, ""severity"": severity})

    return results"

LINK NUMBER 23
Not enough lines

LINK NUMBER 24
Error fetching diff

LINK NUMBER 25
Error fetching diff

LINK NUMBER 26
Error fetching diff

LINK NUMBER 27
Not enough lines

LINK NUMBER 28
Not enough lines

LINK NUMBER 29
Not enough lines

LINK NUMBER 30

File path: src/middleware/tokenValidation.js
"    const authHeader = req.header('Authorization');
    if (!authHeader || !authHeader.startsWith(""Bearer "")) {
        return res.status(401).json({ error: 'Authentication token missing or malformed' });
    }

    /*
    Prevent jwtPayload from being undefined
    Bug found by ChatGPT (https://chatgpt.com/share/67e01958-bc68-8011-8db0-16deafd5fd7b)
     */
    try {
        const payload = jwt.verify(token, secretKey);
        return payload;
    } catch (err) {
        return res.status(403).json({ error: 'Token is invalid' });"

LINK NUMBER 31
Error fetching diff

LINK NUMBER 32
Error fetching diff

LINK NUMBER 33
Error fetching diff

LINK NUMBER 34
Not enough lines

LINK NUMBER 35
Not enough lines

LINK NUMBER 36
Not enough lines

LINK NUMBER 37
Not enough lines

LINK NUMBER 38
Error fetching diff

LINK NUMBER 39
Error fetching diff

LINK NUMBER 40
Error fetching diff

LINK NUMBER 41

File path: dynamo-gsi-test/create_data.js
"import { DynamoDBClient, BatchWriteItemCommand } from ""@aws-sdk/client-dynamodb"";
import { marshall } from ""@aws-sdk/util-dynamodb"";

// Configure DynamoDB client
const client = new DynamoDBClient({
  region: ""localhost"",
  endpoint: ""http://localhost:8000"",
  credentials: {
    accessKeyId: ""fakeMyKeyId"",
    secretAccessKey: ""fakeSecretAccessKey"",
  },
});

// Sample data for Users
const users = [
  {
    PK: { S: ""USER#1"" },
    SK: { S: ""USER#1"" },
    Type: { S: ""User"" },
    name: { S: ""John Doe"" },
    email: { S: ""john@example.com"" },
    join_date: { S: ""2025-01-01"" }
  },
  {
    PK: { S: ""USER#2"" },
    SK: { S: ""USER#2"" },
    Type: { S: ""User"" },
    name: { S: ""Jane Smith"" },
    email: { S: ""jane@example.com"" },
    join_date: { S: ""2025-01-15"" }
  },
  {
    PK: { S: ""USER#3"" },
    SK: { S: ""USER#3"" },
    Type: { S: ""User"" },
    name: { S: ""Robert Johnson"" },
    email: { S: ""robert@example.com"" },
    join_date: { S: ""2025-02-10"" }
  },
  {
    PK: { S: ""USER#4"" },
    SK: { S: ""USER#4"" },
    Type: { S: ""User"" },
    name: { S: ""Emily Davis"" },
    email: { S: ""emily@example.com"" },
    join_date: { S: ""2025-03-05"" }
  },
  {
    PK: { S: ""USER#5"" },
    SK: { S: ""USER#5"" },
    Type: { S: ""User"" },
    name: { S: ""Michael Brown"" },
    email: { S: ""michael@example.com"" },
    join_date: { S: ""2025-03-20"" }
  }
];

// Sample data for Books
const books = [
  {
    PK: { S: ""BOOK#101"" },
    SK: { S: ""BOOK#101"" },
    Type: { S: ""Book"" },
    title: { S: ""The Great Gatsby"" },
    author: { S: ""F. Scott Fitzgerald"" },
    isbn: { S: ""9780743273565"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#102"" },
    SK: { S: ""BOOK#102"" },
    Type: { S: ""Book"" },
    title: { S: ""To Kill a Mockingbird"" },
    author: { S: ""Harper Lee"" },
    isbn: { S: ""9780061120084"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#103"" },
    SK: { S: ""BOOK#103"" },
    Type: { S: ""Book"" },
    title: { S: ""1984"" },
    author: { S: ""George Orwell"" },
    isbn: { S: ""9780451524935"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#104"" },
    SK: { S: ""BOOK#104"" },
    Type: { S: ""Book"" },
    title: { S: ""Pride and Prejudice"" },
    author: { S: ""Jane Austen"" },
    isbn: { S: ""9780141439518"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#105"" },
    SK: { S: ""BOOK#105"" },
    Type: { S: ""Book"" },
    title: { S: ""The Hobbit"" },
    author: { S: ""J.R.R. Tolkien"" },
    isbn: { S: ""9780547928227"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#106"" },
    SK: { S: ""BOOK#106"" },
    Type: { S: ""Book"" },
    title: { S: ""Dune"" },
    author: { S: ""Frank Herbert"" },
    isbn: { S: ""9780441172719"" },
    available: { BOOL: true }
  },
  {
    PK: { S: ""BOOK#107"" },
    SK: { S: ""BOOK#107"" },
    Type: { S: ""Book"" },
    title: { S: ""The Catcher in the Rye"" },
    author: { S: ""J.D. Salinger"" },
    isbn: { S: ""9780316769488"" },
    available: { BOOL: true }
  }
];

// Sample data for Loans
const loans = [
  {
    PK: { S: ""LOAN#1001"" },
    SK: { S: ""LOAN#1001"" },
    GSI1PK: { S: ""USER#1"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-01"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""1"" },
    book_id: { S: ""101"" },
    loan_date: { S: ""2025-04-01"" },
    due_date: { S: ""2025-05-01"" },
    status: { S: ""RETURNED"" }
  },
  {
    PK: { S: ""LOAN#1002"" },
    SK: { S: ""LOAN#1002"" },
    GSI1PK: { S: ""USER#2"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-05"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""2"" },
    book_id: { S: ""102"" },
    loan_date: { S: ""2025-04-05"" },
    due_date: { S: ""2025-05-05"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1003"" },
    SK: { S: ""LOAN#1003"" },
    GSI1PK: { S: ""USER#3"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-10"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""3"" },
    book_id: { S: ""103"" },
    loan_date: { S: ""2025-04-10"" },
    due_date: { S: ""2025-05-10"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1004"" },
    SK: { S: ""LOAN#1004"" },
    GSI1PK: { S: ""USER#1"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-15"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""1"" },
    book_id: { S: ""104"" },
    loan_date: { S: ""2025-04-15"" },
    due_date: { S: ""2025-05-15"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1005"" },
    SK: { S: ""LOAN#1005"" },
    GSI1PK: { S: ""USER#4"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-20"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""4"" },
    book_id: { S: ""101"" },
    loan_date: { S: ""2025-04-20"" },
    due_date: { S: ""2025-05-20"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1006"" },
    SK: { S: ""LOAN#1006"" },
    GSI1PK: { S: ""USER#5"" },
    GSI1SK: { S: ""LOAN_DATE#2025-04-25"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""5"" },
    book_id: { S: ""102"" },
    loan_date: { S: ""2025-04-25"" },
    due_date: { S: ""2025-05-25"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1007"" },
    SK: { S: ""LOAN#1007"" },
    GSI1PK: { S: ""USER#2"" },
    GSI1SK: { S: ""LOAN_DATE#2025-05-01"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""2"" },
    book_id: { S: ""105"" },
    loan_date: { S: ""2025-05-01"" },
    due_date: { S: ""2025-06-01"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1008"" },
    SK: { S: ""LOAN#1008"" },
    GSI1PK: { S: ""USER#3"" },
    GSI1SK: { S: ""LOAN_DATE#2025-05-05"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""3"" },
    book_id: { S: ""101"" },
    loan_date: { S: ""2025-05-05"" },
    due_date: { S: ""2025-06-05"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1009"" },
    SK: { S: ""LOAN#1009"" },
    GSI1PK: { S: ""USER#1"" },
    GSI1SK: { S: ""LOAN_DATE#2025-05-10"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""1"" },
    book_id: { S: ""106"" },
    loan_date: { S: ""2025-05-10"" },
    due_date: { S: ""2025-06-10"" },
    status: { S: ""ACTIVE"" }
  },
  {
    PK: { S: ""LOAN#1010"" },
    SK: { S: ""LOAN#1010"" },
    GSI1PK: { S: ""USER#4"" },
    GSI1SK: { S: ""LOAN_DATE#2025-05-15"" },
    Type: { S: ""Loan"" },
    user_id: { S: ""4"" },
    book_id: { S: ""103"" },
    loan_date: { S: ""2025-05-15"" },
    due_date: { S: ""2025-06-15"" },
    status: { S: ""ACTIVE"" }
  }
];

// Sample data for BookLoans
const bookLoans = [
  {
    PK: { S: ""BOOK#101"" },
    SK: { S: ""LOAN#1001"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""1"" },
    loan_date: { S: ""2025-04-01"" }
  },
  {
    PK: { S: ""BOOK#102"" },
    SK: { S: ""LOAN#1002"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""2"" },
    loan_date: { S: ""2025-04-05"" }
  },
  {
    PK: { S: ""BOOK#103"" },
    SK: { S: ""LOAN#1003"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""3"" },
    loan_date: { S: ""2025-04-10"" }
  },
  {
    PK: { S: ""BOOK#104"" },
    SK: { S: ""LOAN#1004"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""1"" },
    loan_date: { S: ""2025-04-15"" }
  },
  {
    PK: { S: ""BOOK#101"" },
    SK: { S: ""LOAN#1005"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""4"" },
    loan_date: { S: ""2025-04-20"" }
  },
  {
    PK: { S: ""BOOK#102"" },
    SK: { S: ""LOAN#1006"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""5"" },
    loan_date: { S: ""2025-04-25"" }
  },
  {
    PK: { S: ""BOOK#105"" },
    SK: { S: ""LOAN#1007"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""2"" },
    loan_date: { S: ""2025-05-01"" }
  },
  {
    PK: { S: ""BOOK#101"" },
    SK: { S: ""LOAN#1008"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""3"" },
    loan_date: { S: ""2025-05-05"" }
  },
  {
    PK: { S: ""BOOK#106"" },
    SK: { S: ""LOAN#1009"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""1"" },
    loan_date: { S: ""2025-05-10"" }
  },
  {
    PK: { S: ""BOOK#103"" },
    SK: { S: ""LOAN#1010"" },
    Type: { S: ""BookLoan"" },
    user_id: { S: ""4"" },
    loan_date: { S: ""2025-05-15"" }
  }
];

// Function to batch write items to DynamoDB
async function batchWriteItems(items) {
  // DynamoDB BatchWriteItem can handle up to 25 items at once
  const batchSize = 25;
  
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const request = {
      RequestItems: {
        LibraryManagement: batch.map(item => ({
          PutRequest: {
            Item: item
          }
        }))
      }
    };
    
    try {
      await client.send(new BatchWriteItemCommand(request));
      console.log(`Successfully wrote batch ${i / batchSize + 1}`);
    } catch (error) {
      console.error(`Error writing batch ${i / batchSize + 1}:`, error);
      throw error;
    }
  }
}

// Main function to populate all data
async function populateData() {
  try {
    console.log(""Starting data population..."");
    
    console.log(""Inserting users..."");
    await batchWriteItems(users);
    
    console.log(""Inserting books..."");
    await batchWriteItems(books);
    
    console.log(""Inserting loans..."");
    await batchWriteItems(loans);
    
    console.log(""Inserting book loans..."");
    await batchWriteItems(bookLoans);
    
    console.log(""Data population completed successfully!"");
  } catch (error) {
    console.error(""Error in data population:"", error);
  }
}

// Execute the population script
populateData();"

LINK NUMBER 42

File path: src/store/index.js
"import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      count: 0
    };
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    incrementAction({ commit }) {
      commit('increment');
    }
  },
  getters: {
    doubleCount: (state) => state.count * 2
  }
});

export default store;"

LINK NUMBER 43
Not enough lines

LINK NUMBER 44
Not enough lines

LINK NUMBER 45
Error fetching diff

LINK NUMBER 46
Error fetching diff

LINK NUMBER 47
Error fetching diff

LINK NUMBER 48

File path: src/Translator/ChatGPTTranslator.php
"        try {
            $response = $this->client->chat()->create([
                'model' => self::config()->get('gpt_model'),
                'messages' => [
                    [
                        'role' => 'system',
                        'content' => $this->getGPTCommand($targetLocale)
                    ],
                    [
                        'role' => 'user',
                        'content' => $text
                    ]"

LINK NUMBER 49

File path: main.go
"//go:embed assets
var assetsFS embed.FS

func get_img(filepath string, console *widget.Entry, assetsFS embed.FS) (image.Image, error) {
	imgData, err := assetsFS.ReadFile(filepath)
	if err != nil {
		console.SetText(console.Text + ""Error loading image: "" + err.Error() + ""\n"")
		fmt.Println(""in 1: "" + err.Error())
		return nil, err
	}

	img, _, err := image.Decode(bytes.NewReader(imgData))
	if err != nil {
		console.SetText(console.Text + ""Error loading image: "" + err.Error() + ""\n"")
		fmt.Println(""in 2: "" + err.Error())
		return nil, err
	}

	return img, nil
}
"

LINK NUMBER 50
Not enough lines

LINK NUMBER 51

File path: height.js
"console.log(result);







const names=['Mehedi','Mira','Aboni','Aboni','Nid'];
function getLitteone(words){
    let shortname=names[0];
    for(const name of words){
        if(name.length<shortname.length){
            shortname=name;
            
        }
    }
    return shortname;
}

const resut= getLitteone(names);
console.log(resut);"

LINK NUMBER 52
Error fetching diff

LINK NUMBER 53
Error fetching diff

LINK NUMBER 54
Error fetching diff

LINK NUMBER 55
Not enough lines

LINK NUMBER 56
Not enough lines

LINK NUMBER 57

File path: src/App.js
"              {loading ? 'Loading...' : 'Search'}
            </button>
          </div>

          {error && <p className=""text-red-500"">{error}</p>}

          <div className=""grid grid-cols-1 sm:grid-cols-2 gap-6 mt-6"">
            {characters.map((char, idx) => (
              <div
                key={idx}
                className=""bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-hidden transition hover:shadow-xl""
              >
                <img
                  src={char.imageUrl}
                  alt={char.name}
                  className=""w-full h-48 object-cover""
                />
                <div className=""p-4"">
                  <h2 className=""text-xl font-bold mb-2"">{char.name}</h2>
                  <h3 className=""text-md font-semibold mb-1"">Movies:</h3>
                  <ul className=""list-disc list-inside"">
                    {char.films.length > 0 ? (
                      char.films.map((film, i) => <li key={i}>{film}</li>)
                    ) : (
                      <li>No movies found</li>
                    )}
                  </ul>
                </div>"

LINK NUMBER 58
Not enough lines

LINK NUMBER 59
Error fetching diff

LINK NUMBER 60
Error fetching diff

LINK NUMBER 61
Error fetching diff

LINK NUMBER 62

File path: app.js
"const taskInput = document.getElementById(""taskinput"");

function addTask() {
  let task = taskInput.value.trim();
  if (task === """") return; // Prevent empty tasks

  alert(""Task added!"");

  const list = document.getElementById(""tasklist"");

  // Create Task Item Container
  let taskItem = document.createElement(""div"");
  taskItem.classList.add(""task-item"");

  // Create Task Description Div
  let taskTextContainer = document.createElement(""div"");
  taskTextContainer.textContent = task;
  taskTextContainer.classList.add(""task-text-container"");
  taskTextContainer.contentEditable = ""false""; // Initially not editable

  // Create Buttons Container
  let buttonsContainer = document.createElement(""div"");
  buttonsContainer.classList.add(""task-buttons"");

  // Delete Button
  let deleteBtn = document.createElement(""button"");
  deleteBtn.textContent = ""Delete"";
  deleteBtn.classList.add(""task-btn"", ""delete-btn"");
  deleteBtn.onclick = function () {
      list.removeChild(taskItem);
  };

  // Complete Button
  let completeBtn = document.createElement(""button"");
  completeBtn.textContent = ""Completed"";
  completeBtn.classList.add(""task-btn"", ""complete-btn"");
  completeBtn.onclick = function () {
      taskTextContainer.style.textDecoration = ""line-through"";
      taskTextContainer.style.color = ""gray"";
  };

  // Edit Button
  let editBtn = document.createElement(""button"");
  editBtn.textContent = ""Edit"";
  editBtn.classList.add(""task-btn"", ""edit-btn"");
  editBtn.onclick = function () {
      if (taskTextContainer.contentEditable === ""false"") {
          taskTextContainer.contentEditable = ""true"";
          taskTextContainer.focus();
          editBtn.textContent = ""Save"";
      } else {
          taskTextContainer.contentEditable = ""false"";
          editBtn.textContent = ""Edit"";
      }
  };

  // Append Buttons to Buttons Container
  buttonsContainer.appendChild(editBtn);
  buttonsContainer.appendChild(completeBtn);
  buttonsContainer.appendChild(deleteBtn);

  // Append Task Description and Buttons to Task Item
  taskItem.appendChild(taskTextContainer);
  taskItem.appendChild(buttonsContainer);

  // Append Task Item to List
  list.appendChild(taskItem);

  // Clear Input
  taskInput.value = """";
}

// Attach event listener to ""Add Task"" button
document.querySelector(""button"").addEventListener(""click"", addTask);"

LINK NUMBER 63
Error fetching diff

LINK NUMBER 64
Error fetching diff

LINK NUMBER 65

File path: controllers/listings.js
"// module.exports.updateListing = async (req, res)=>{
//     let {id} = req.params;
//     let listing = await Listing.findByIdAndUpdate(id, {...req.body.listing});
//     if(typeof req.file != ""undefined""){
//         let url = req.file.path;
//         let filename = req.file.filename;
//         listing.image = {url, filename};
//         await listing.save();
//     }
//     req.flash(""success"", ""Listing Updated!"");
//     res.redirect(`/listings/${id}`);
// };


// module.exports.updateListing = async (req, res) => {
//     try {
//         let { id } = req.params;
        
//         // Check if request body contains listing data
//         if (!req.body.listing) {
//             req.flash(""error"", ""Invalid data provided!"");
//             return res.redirect(`/listings/${id}/edit`);
//         }

//         // Update listing in DB
//         let listing = await Listing.findByIdAndUpdate(id, { ...req.body.listing }, { new: true });

//         // Handle file upload if a new image is provided
//         if (req.file) {
//             listing.image = {
//                 url: req.file.path,
//                 filename: req.file.filename
//             };
//             await listing.save();
//         }

//         req.flash(""success"", ""Listing Updated!"");
//         res.redirect(`/listings/${id}`);
//     } catch (error) {
//         console.error(error);
//         req.flash(""error"", ""Something went wrong while updating the listing!"");
//         res.redirect(`/listings/${id}/edit`);
//     }
// };


module.exports.updateListing = async (req, res) => {
    try {
        const { id } = req.params;
        const listing = await Listing.findById(id);
        if (!listing) return res.redirect(""/listings"");

        // If new images are uploaded, replace old ones in the database
        if (req.files?.length) {
            listing.images = req.files.map(({ path, filename }) => ({ url: path, filename }));
        }

        // Save updated listing"

LINK NUMBER 66
Error fetching diff

LINK NUMBER 67
Error fetching diff

LINK NUMBER 68
Error fetching diff

LINK NUMBER 69

File path: cle/potential_size.py
"        # print(
        #    ""r0, rmax_cle, pm_cle15_dyn, pm_w22_car"",
        #    r0,
        #    rmax_cle,
        #    pm_cle15_dyn,
        #    pm_w22_car,
        # )"

LINK NUMBER 70

File path: multithreading/main.c
"        // Wait for something to consume (producer will signal this)
        sem_wait(&semProd);

        pthread_mutex_lock(&bufferLock);
        // Consume from buffer
        int num = ringBuffer[rp];
        rp = (rp + 1) % BUFFER_SIZE;
        printf(""[CONS] Read %d from buffer\n"", num);
        pthread_mutex_unlock(&bufferLock);

        // Signal the producer that there's space in the buffer
        sem_post(&semCons);

        counter++;"

LINK NUMBER 71
Not enough lines

LINK NUMBER 72
Not enough lines

LINK NUMBER 73
Error fetching diff

LINK NUMBER 74
Error fetching diff

LINK NUMBER 75
Error fetching diff

LINK NUMBER 76
Not enough lines

LINK NUMBER 77
Too many lines

LINK NUMBER 78
Not enough lines

LINK NUMBER 79
Not enough lines

LINK NUMBER 80
Error fetching diff

LINK NUMBER 81
Error fetching diff

LINK NUMBER 82

File path: Phase 1/Q6 Multiplicative Inverse.c
"#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

// NOTE : Here we use a^p-1 mod p = 1 mod p
// By replacing modulus_minus_one by modulus in the code and uncomment the line where we compute 'part 1' 
// you can see : a^p mod p = a mod p also
int main(int argc, char *argv[]) {
    // Initialize base (a), exponent (x), and modulus (n)
    mpz_t base, exponent, modulus;
    mpz_init_set_ui(base, atoi(argv[1]));
    mpz_init_set_ui(exponent, atoi(argv[2]));
    mpz_init_set_ui(modulus, atoi(argv[3]));

    // Print initial equation
    printf(""Initial: %ld^%ld (mod %ld)\n"", mpz_get_ui(base), mpz_get_ui(exponent), mpz_get_ui(modulus));

    // Check if modulus is prime (required for Fermat's theorem)
    printf(""Checking if modulus is prime...\n"");
    if (mpz_probab_prime_p(modulus, 50) == 2) {
        printf(""Modulus is prime! Proceeding with Fermat's theorem.\n"");
    } else {
        printf(""Modulus is not prime. Fermat's theorem cannot be applied.\n"");
        return 0;
    }

    // Initialize result variable
    mpz_t result;
    mpz_init(result);

    // If exponent < modulus, directly compute a^x mod n
    if (mpz_cmp(exponent, modulus) < 0) {
        mpz_powm(result, base, exponent, modulus);
        printf(""Result: %ld\n"", mpz_get_ui(result));
        return 0;
    }

    // Initialize variables for Fermat's theorem application
    mpz_t quotient, remainder;
    mpz_t part1, part2;
    mpz_init(quotient);
    mpz_init(remainder);
    mpz_init_set_ui(part1,1);
    mpz_init(part2);

    mpz_t modulus_minus_one;
    mpz_init(modulus_minus_one);

    mpz_sub_ui(modulus_minus_one,modulus,1);

    // Compute exponent as quotient * (modulus-1) + remainder
    mpz_fdiv_qr(quotient, remainder, exponent, modulus_minus_one);

    // Print breakdown of exponentiation
    printf(""We have: (%ld^(%ld * %ld) + %ld) (mod %ld)\n"", 
           mpz_get_ui(base), mpz_get_ui(quotient), mpz_get_ui(modulus_minus_one), mpz_get_ui(remainder), mpz_get_ui(modulus));

    printf(""i.e. ((%ld^%ld)^%ld) * (%ld^%ld) (mod %ld)\n"", 
           mpz_get_ui(base), mpz_get_ui(quotient), mpz_get_ui(modulus_minus_one), mpz_get_ui(base), mpz_get_ui(remainder), mpz_get_ui(modulus));

    printf(""i.e. (((%ld^%ld)^%ld) (mod %ld)) * ((%ld^%ld) (mod %ld)) (mod %ld)\n"", 
           mpz_get_ui(base), mpz_get_ui(quotient), mpz_get_ui(modulus_minus_one), mpz_get_ui(modulus), 
           mpz_get_ui(base), mpz_get_ui(remainder), mpz_get_ui(modulus), mpz_get_ui(modulus));

    printf(""Using Fermat’s Theorem: a^p mod p = a\n"");

    // Compute (base^quotient)^modulus mod modulus
    // mpz_powm(part1, base, quotient, modulus);
    printf(""i.e. %ld * (%ld^%ld) mod %ld\n"", mpz_get_ui(part1), mpz_get_ui(base), mpz_get_ui(remainder), mpz_get_ui(modulus));

    // Compute base^remainder mod modulus
    mpz_powm(part2, base, remainder, modulus);

    // Compute final result
    mpz_mul(result, part1, part2);
    printf(""Result: %ld\n"", mpz_get_ui(result));

    // Free allocated memory
    mpz_clear(base);
    mpz_clear(exponent);
    mpz_clear(modulus);
    mpz_clear(result);
    mpz_clear(quotient);
    mpz_clear(remainder);
    mpz_clear(part1);
    mpz_clear(part2);

    return 0;
}"

LINK NUMBER 83

File path: script.js
"
    listItem.id = `noteId-${noteId}`;
    noteId++;
}


function selectNote(x){
      

      for(let i=0;i<x.length;i++){
            x[i].addEventListener(""click"",function(){
                x[i].style.backgroundColor=""rgb(166, 245, 192)"";
                // console.log(x[i].children);
            });
      }"

LINK NUMBER 84
Not enough lines

LINK NUMBER 85

File path: UppgiftSeeSharp.Tests/Services/UserInputService_Tests.cs
"﻿using Business.Helpers;
using Business.Services;
using Busniess.Models;
using Moq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;

namespace UppgiftSeeSharp.Tests.Services;

public class UserInputService_Tests
{

    /* With the help of ChatGPT 4 i made this test
     * Since i cant moq properly my inputhandler i decided to create a class that is based on the inputhandler here instead
     * then we test this logic with asserts to compare the result to the given input string */
    /* The TestInputHandler class implements the InputHandler requirements ConsoleWrapper and adds the string _ inputs and currentInputIndex logic*/
    public class TestInputHandler : InputHandler
    {
        private readonly string[] _inputs;
        private int _currentInputIndex = 0;

        public TestInputHandler(string[] inputs, ConsoleWrapper consoleWrapper) : base(consoleWrapper)
        {
            _inputs = inputs;
        }

        /* Returns the value of the string at the current index and increments it */
        public override string GetInput(string prompt)
        {
            if(_currentInputIndex < _inputs.Length)
            {
                return _inputs[_currentInputIndex++];
            }
            return string.Empty;
        }
    }

    /* ChatGpt4 
     * This test that checks the logic with asserts to compare the result to the given input string *
     * With the help of the TestInputHandler class */
    [Fact]
    public void CollectUserData_ShouldReturnMockedUserRegistrationFormData()
    {

        // arrange
        var inputs = new String[]
        {
            ""Test"",
            ""Testsson"",
            ""Test.Testsson@Test.com"",
            ""0760321142"",
            ""TestVagen 24"",
            ""325 12"",
            ""TestStaden""
        };

        var consoleWrapper = new ConsoleWrapper();
        var testInputHandler = new TestInputHandler(inputs, consoleWrapper);
        var userInputService = new UserInputService(testInputHandler);

        // act
        var result = userInputService.CollectUserData();


        // assert
        Assert.Equal(""Test"", result.FirstName);
        Assert.Equal(""Testsson"", result.LastName);
        Assert.Equal(""Test.Testsson@Test.com"", result.Email);
        Assert.Equal(""0760321142"", result.PhoneNumber);
        Assert.Equal(""TestVagen 24"", result.Address);
        Assert.Equal(""325 12"", result.PostalNumber);
        Assert.Equal(""TestStaden"", result.City);
        Assert.NotNull(result);
    }
}"

LINK NUMBER 86
Error fetching diff

LINK NUMBER 87
Error fetching diff

LINK NUMBER 88
Error fetching diff

LINK NUMBER 89

File path: src/app/cookie-policy/page.js
"// app/cookie-policy/page.js
import styles from ""./cookiePolicy.module.css"";

const CookiePolicy = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.heading1}>Cookie Policy</h1>
      <p className={styles.paragraph}>
        <strong>Last Updated:</strong> January 21, 2025
      </p>

      <h2 className={styles.heading2}>1. Introduction</h2>
      <p className={styles.paragraph}>
        Hi there! I'm a solo developer, and I run this website as a personal
        project. This Cookie Policy is here to let you know what cookies I use
        on this site, why I use them, and how they help the website function.
        Since I only use essential cookies, there’s nothing to worry about —
        they’re necessary for the website to work properly.
      </p>
      <p className={styles.paragraph}>
        By continuing to browse this site, you agree to the use of these
        cookies.
      </p>

      <h2 className={styles.heading2}>2. What Are Cookies?</h2>
      <p className={styles.paragraph}>
        Cookies are small text files that are stored on your device when you
        visit a website. They help websites remember certain information about
        your visit, like preferences or login status, so the site can work as
        expected.
      </p>

      <h2 className={styles.heading2}>3. Cookies I Use</h2>
      <p className={styles.paragraph}>
        This site uses <strong>only essential cookies</strong>. These cookies
        are needed for the website to function and cannot be disabled in the
        system. They are used for things like:
      </p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          <strong>Session management:</strong> Keeping you logged in while you
          use the site.
        </li>
      </ul>
      <p className={styles.paragraph}>
        Since these cookies are essential, they don't require your consent, but
        I want to make sure you're aware of them.
      </p>

      <h2 className={styles.heading2}>4. Why Do I Use These Cookies?</h2>
      <p className={styles.paragraph}>I use essential cookies to:</p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          Ensure the site works correctly (e.g., so you can log in or return as
          a guest).
        </li>
        <li className={styles.listItem}>
          Maintain your session while you’re using the site so that you don’t
          have to log in repeatedly.
        </li>
      </ul>
      <p className={styles.paragraph}>
        These cookies are crucial for the website’s operation and make sure the
        basic functionality is there.
      </p>

      <h2 className={styles.heading2}>5. How to Control Cookies</h2>
      <p className={styles.paragraph}>
        Since the cookies I use are essential, they are required for the website
        to function. There’s no need to accept them manually. However, if you
        prefer, you can adjust your browser settings to block or delete cookies,
        but this may affect the site’s functionality.
      </p>
      <p className={styles.paragraph}>
        Here’s how you can manage cookies in your browser:
      </p>
      <ul className={styles.list}>
        <li className={styles.listItem}>
          <a
            href=""https://support.google.com/chrome/answer/95647?hl=en""
            target=""_blank""
            className={styles.link}
            rel=""noopener noreferrer""
          >
            Google Chrome
          </a>
        </li>
        <li className={styles.listItem}>
          <a
            href=""https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences""
            target=""_blank""
            className={styles.link}
            rel=""noopener noreferrer""
          >
            Mozilla Firefox
          </a>
        </li>
        <li className={styles.listItem}>
          <a
            href=""https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac""
            target=""_blank""
            className={styles.link}
            rel=""noopener noreferrer""
          >
            Safari
          </a>
        </li>
      </ul>

      <h2 className={styles.heading2}>6. Changes to This Cookie Policy</h2>
      <p className={styles.paragraph}>
        Since this website is a personal project, I may update this policy
        occasionally. If I make any changes, I’ll update the “Last Updated” date
        above. Feel free to check back here to stay informed.
      </p>

      <h2 className={styles.heading2}>7. Contact Me</h2>
      <p className={styles.paragraph}>
        If you have any questions or concerns about this Cookie Policy or how
        cookies are used on this site, feel free to reach out to me at{"" ""}
        <strong className={styles.strong}>support@itsthenikolai.com</strong>.
      </p>
    </div>
  );
};

export default CookiePolicy;"

LINK NUMBER 90

File path: issue.ts
"

export async function deleteClosedIssues() {
  const ISSUE_AUTOMATION = process.env.ISSUE_AUTOMATION;
  const OWNER = process.env.OWNER;
  const REPO = process.env.REPO;

  const octokit = new Octokit({
    auth: ISSUE_AUTOMATION,
  });

  try {
    let pageInfo = { hasNextPage: true, endCursor: null };
    let deletedCount = 0;

    while (pageInfo.hasNextPage) {
      // Fetch closed issues with GraphQL
      const query = `
        query($owner: String!, $repo: String!, $cursor: String) {
          repository(owner: $owner, name: $repo) {
            issues(states: CLOSED, first: 50, after: $cursor) {
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                id
                number
                title
              }
            }
          }
        }
      `;

      const response = await octokit.graphql<any>(query, {
        owner: OWNER,
        repo: REPO,
        cursor: pageInfo.endCursor,
      });

      const issues = (response as any).repository.issues.nodes;
      pageInfo = (response as any).repository.issues.pageInfo;

      for (const issue of issues) {
        try {
          const mutation = `
            mutation($issueId: ID!) {
              deleteIssue(input: { issueId: $issueId }) {
                clientMutationId
              }
            }
          `;

          await octokit.graphql(mutation, { issueId: issue.id });
          console.log(`Deleted issue #${issue.number}: ${issue.title}`);
          deletedCount++;

          // Delay to avoid hitting rate limits
          await new Promise((resolve) => setTimeout(resolve, 2000));
        } catch (error) {
          if (error instanceof Error) {
            console.error(`Failed to delete issue #${issue.number}: ${issue.title}`, error.message);
          }
        }
      }
    }

    console.log(`Deleted ${deletedCount} closed issues.`);
  } catch (error) {
    if (error instanceof Error) {
      console.error(""Failed to delete closed issues"", error.message);
    }
  }
}"

LINK NUMBER 91

File path: [Easy] Maximum Depth of Binary Tree/main.cpp
"#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:

    int leftDepth = 1, rightDepth = 1;
    int maxDepth(TreeNode* root) {
        if ( root != nullptr ){
            (root->left != nullptr ? leftDepth++ : leftDepth);
            (root->right != nullptr ? rightDepth++ : rightDepth);
            leftDepth = findMaxDepth(root->left);
            rightDepth = findMaxDepth(root->right);
            return 1 + (leftDepth >= rightDepth ? leftDepth : rightDepth);
        }
        return 0;
    }

    int findMaxDepth(TreeNode* root){
        if ( root == nullptr ){
            return 0;
        }
        return 1 + (std::max(findMaxDepth(root->left), findMaxDepth(root->right)));
    }
};

int main(){

    /*
    TreeNode* tree1 = new TreeNode(-8);
    tree1->left = new TreeNode(-6);
    tree1->left->left = new TreeNode(6);
    tree1->left->left->right = new TreeNode(5);
    tree1->right = new TreeNode(7);
    */
    
    // TreeNode* tree1 = new TreeNode(3);
    // tree1->left = new TreeNode(9);
    // tree1->right = new TreeNode(20);
    // tree1->right->left = new TreeNode(15);
    // tree1->right->right = new TreeNode(7);
    
    /*
    TreeNode* tree1 = new TreeNode(3);
    tree1->left = new TreeNode(4);
    tree1->left->left = new TreeNode(-7);
    tree1->left->left->left = new TreeNode(-7);
    tree1->left->right = new TreeNode(-6);
    tree1->left->right->left = new TreeNode(-5);
    tree1->left->right->left->left = new TreeNode(-4);
    tree1->right = new TreeNode(5);
    */

    TreeNode* tree1 = new TreeNode(0);
    tree1->left = new TreeNode(2);
    tree1->left->left = new TreeNode(1);
    tree1->left->left->left = new TreeNode(5);
    tree1->left->left->right = new TreeNode(1);
    tree1->right = new TreeNode(4);
    tree1->right->left = new TreeNode(3);
    tree1->right->left->right = new TreeNode(6);
    tree1->right->right = new TreeNode(-1);
    tree1->right->right->right = new TreeNode(8);

    Solution solution;
    int res = solution.maxDepth(tree1);
    std::cout << res << std::endl;
}"

LINK NUMBER 92
Not enough lines

LINK NUMBER 93
Error fetching diff

LINK NUMBER 94
Error fetching diff

LINK NUMBER 95
Error fetching diff

LINK NUMBER 96

File path: browser-artifact-parser-GUI.py
"
def exit_menu():
    exit()

"

LINK NUMBER 97

File path: browser-artifact-parser-GUI.py
"        self.status_text = tk.Text(root, height=20, width=70, state=""disabled"", bg=""black"", fg=""white"")
        self.status_text.grid(row=3, column=1, columnspan=2, padx=20, pady=20)

        tk.Button(root, text=""Exit"", width=10, command=self.exit, bg=""red"").grid(row=2, column=2, padx=10, pady=5)

    def exit(self):
        exit()
"

LINK NUMBER 98

File path: browser-artifact-parser-GUI.py
"import tkinter as tk
from tkinter import filedialog, messagebox
from Classes.Preferences import Preferences
from Functions.write_to_excel import write_excel
from JSON.bookmarks import get_chromium_bookmarks
from SQLite.cookies import chrome_cookies
from SQLite.downloads import chrome_downloads, chrome_downloads_gaps
from SQLite.favicons import chrome_favicons
from SQLite.history import chrome_history, chrome_history_gaps
from SQLite.logindata import chrome_login_data, chrome_login_data_gaps
from SQLite.searchterms import chrome_keyword_historyquery
from SQLite.shortcuts import chrome_shortcuts
from SQLite.WebData import (
    chrome_autofill, chrome_keywords, chrome_masked_credit_cards, chrome_masked_bank_accounts
)
import pandas as pd
import sqlite3
import numpy as np
import io

class ChromeParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(""Chrome Parser"")
        self.profile_path = None
        self.output_path = None

        # Labels and Buttons
        tk.Label(root, text=""Chrome User Profile Folder:"").grid(row=0, column=0, sticky=""w"", padx=10, pady=5)
        self.profile_entry = tk.Entry(root, width=50)
        self.profile_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(root, text=""Browse"", command=self.browse_profile).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(root, text=""Output Excel File:"").grid(row=1, column=0, sticky=""w"", padx=10, pady=5)
        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(root, text=""Browse"", command=self.browse_output).grid(row=1, column=2, padx=10, pady=5)

        tk.Button(root, text=""Run Parser"", command=self.run_parser).grid(row=2, column=1, pady=20)

        # Status Window
        tk.Label(root, text=""Status:"").grid(row=3, column=0, sticky=""nw"", padx=10, pady=5)
        self.status_text = tk.Text(root, height=10, width=70, state=""disabled"")
        self.status_text.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

    def update_status(self, message):
        self.status_text.config(state=""normal"")
        self.status_text.insert(tk.END, message + ""\n"")
        self.status_text.see(tk.END)
        self.status_text.config(state=""disabled"")

    def browse_profile(self):
        self.profile_path = filedialog.askdirectory(title=""Select Chrome User Profile Folder"")
        self.profile_entry.delete(0, tk.END)
        self.profile_entry.insert(0, self.profile_path)

    def browse_output(self):
        self.output_path = filedialog.asksaveasfilename(
            title=""Select Output Excel File"", defaultextension="".xlsx"", filetypes=[(""Excel files"", ""*.xlsx"")]
        )
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_path)

    def run_parser(self):
        if not self.profile_path or not self.output_path:
            messagebox.showerror(""Error"", ""Please select both profile and output paths."")
            return

        try:
            chrome_queries = {
                'History': [f'{self.profile_path}/History', chrome_history],
                ""History Gaps"": [f'{self.profile_path}/History', chrome_history_gaps],
                ""Downloads"": [f'{self.profile_path}/History', chrome_downloads],
                ""Downloads Gaps"": [f'{self.profile_path}/History', chrome_downloads_gaps],
                ""Autofill"": [f'{self.profile_path}/Web Data', chrome_autofill],
                ""Keywords"": [f'{self.profile_path}/Web Data', chrome_keywords],
                ""Credit Cards"": [f'{self.profile_path}/Web Data', chrome_masked_credit_cards],
                ""Bank Accounts"": [f'{self.profile_path}/Web Data', chrome_masked_bank_accounts],
                ""Login Data"": [f'{self.profile_path}/Login Data', chrome_login_data],
                ""Login Data Gaps"": [f'{self.profile_path}/Login Data', chrome_login_data_gaps],
                ""Shortcuts"": [f'{self.profile_path}/Shortcuts', chrome_shortcuts],
                ""Cookies"": [f'{self.profile_path}/Network/Cookies', chrome_cookies],
                ""FavIcons"": [f'{self.profile_path}/Favicons', chrome_favicons]
            }

            record_counts = []

            for sqlite_query in chrome_queries.keys():
                self.update_status(f""Processing {sqlite_query}..."")
                df, ws = self.get_dataframes(chrome_queries[sqlite_query][0], chrome_queries[sqlite_query][1])
                write_excel(df, ws, self.output_path)
                record_counts.append((ws, len(df)))

            self.update_status(""Processing Search Terms..."")
            dataframe_searchterms, ws = self.process_search_terms()
            write_excel(dataframe_searchterms, ws, self.output_path)
            record_counts.append((ws, len(dataframe_searchterms)))

            self.update_status(""Processing Bookmarks..."")
            bookmarks_df, ws = get_chromium_bookmarks(f'{self.profile_path}/Bookmarks')
            bookmarks_backup_df, ws_bak = get_chromium_bookmarks(f'{self.profile_path}/Bookmarks.bak')
            all_bookmarks = pd.concat([bookmarks_df, bookmarks_backup_df], ignore_index=True)
            write_excel(all_bookmarks, ws, self.output_path)
            record_counts.append((ws, len(all_bookmarks)))

            self.update_status(""Processing Preferences..."")
            preferences = Preferences(f'{self.profile_path}/Preferences')
            preferences_output = io.StringIO()
            print(preferences, file=preferences_output)
            preferences_data = preferences_output.getvalue().splitlines()
            preferences_df = pd.DataFrame(preferences_data, columns=[""Preferences Output""])
            write_excel(preferences_df, ""Preferences"", self.output_path)

            self.update_status(""Creating Summary Worksheet..."")
            summary_df = pd.DataFrame(record_counts, columns=[""Worksheet Name"", ""Record Count""])
            write_excel(summary_df, ""Summary"", self.output_path)

            self.update_status(""All processing completed successfully."")
            messagebox.showinfo(""Success"", f""Parsing completed! Output saved to {self.output_path}"")

        except Exception as e:
            self.update_status(f""Error: {e}"")
            messagebox.showerror(""Error"", f""An error occurred: {e}"")

    def get_dataframes(self, db_file, function):
        query, worksheet_name = function()
        conn = sqlite3.connect(db_file)
        dataframe = pd.read_sql_query(query, conn)
        conn.close()
        return dataframe, worksheet_name

    def process_search_terms(self):
        worksheet = 'Search Terms'
        input_file = f'{self.profile_path}/History'
        df_history, ws_history = self.get_dataframes(input_file, chrome_keyword_historyquery)

        input_file = f'{self.profile_path}/Web Data'
        df_keywords, ws_keyword = self.get_dataframes(input_file, chrome_keywords)

        searchterms = []
        if len(df_keywords) > 0:
            for row in df_history.itertuples():
                if not np.isnan(row[3]):
                    try:
                        kw = [
                            df_keywords.query(f'id == {row[3]}')['keyword'].values[0],
                            df_keywords.query(f'id == {row[3]}')['date_created'].values[0],
                            df_keywords.query(f'id == {row[3]}')['Decoded date_created (UTC)'].values[0],
                            df_keywords.query(f'id == {row[3]}')['last_modified'].values[0],
                            df_keywords.query(f'id == {row[3]}')['Decoded last_modified (UTC)'].values[0]
                        ]
                    except IndexError:
                        kw = ['', '', '', '', '']
                    searchterms.append([
                        row[1], row[2], row[3], kw[0], row[5], row[6], kw[1], kw[2], kw[3], kw[4], row[7], row[8]
                    ])
        else:
            searchterms = [["""", """", """", """", """", """", """", """", """", """", """", """"]]

        df_searchterms = pd.DataFrame(searchterms)
        df_searchterms.columns = [
            'URL id', 'url', 'keyword id', 'keyword', 'search term', 'typed_count', 'date_created',
            'Decoded date_created (UTC)', 'last_modified', 'Decoded last_modified (UTC)',
            'last_visit_time (UTC)', 'Decoded last_visit_time (UTC)'
        ]
        return df_searchterms, worksheet

if __name__ == '__main__':
    root = tk.Tk()
    app = ChromeParserGUI(root)
    root.mainloop()"

LINK NUMBER 99
Not enough lines

LINK NUMBER 100
Error fetching diff

LINK NUMBER 101
Error fetching diff

LINK NUMBER 102
Error fetching diff

LINK NUMBER 103
Not enough lines

LINK NUMBER 104
Not enough lines

LINK NUMBER 105
Not enough lines

LINK NUMBER 106

File path: MorseCodeGame/Form1.cs
"﻿namespace MorseCodeGame;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name=""disposing"">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.components = new System.ComponentModel.Container();
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(800, 450);
        this.Text = ""Form1"";
    }

    #endregion
}"

LINK NUMBER 107
Error fetching diff

LINK NUMBER 108
Error fetching diff

LINK NUMBER 109
Error fetching diff

LINK NUMBER 110

File path: src/com/flappyBird/Pipe.java
"package com.flappyBird;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;

public class GamePanel extends JPanel implements ActionListener, KeyListener {
    private static final int WIDTH = 800;
    static final int HEIGHT = 600;
    static final int PIPE_WIDTH = 80;
    static final int PIPE_GAP = 150;
    static final int GRAVITY = 2;
    static final int JUMP_STRENGTH = -15;

    private Timer timer;
    private Bird bird;
    private ArrayList<Pipe> pipes;
    private int score;
    private boolean gameOver;

    private enum GameState { START, PLAYING, GAME_OVER }
    private GameState gameState = GameState.START;

    public GamePanel() {
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.CYAN);
        setFocusable(true);
        addKeyListener(this);

        initGame();
    }

    private void initGame() {
        bird = new Bird(WIDTH / 4, HEIGHT / 2);
        pipes = new ArrayList<>();
        score = 0;
        gameOver = false;

        timer = new Timer(20, this);
        timer.start();

        for (int i = 0; i < 3; i++) {
            pipes.add(new Pipe(WIDTH + i * 300, new Random().nextInt(HEIGHT / 2) + HEIGHT / 4));
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        if (gameState == GameState.START) {
            g.setColor(Color.BLACK);
            g.setFont(new Font(""Arial"", Font.BOLD, 36));
            g.drawString(""Press SPACE to Start"", WIDTH / 2 - 180, HEIGHT / 2);
            return;
        }

        if (gameState == GameState.GAME_OVER) {
            g.setColor(Color.RED);
            g.setFont(new Font(""Arial"", Font.BOLD, 48));
            g.drawString(""Game Over!"", WIDTH / 2 - 150, HEIGHT / 2 - 50);
            g.drawString(""Score: "" + score, WIDTH / 2 - 100, HEIGHT / 2 + 50);
            g.drawString(""Press R to Restart"", WIDTH / 2 - 180, HEIGHT / 2 + 100);
            return;
        }

        bird.draw(g);

        for (Pipe pipe : pipes) {
            pipe.draw(g);
        }

        g.setColor(Color.WHITE);
        g.setFont(new Font(""Arial"", Font.BOLD, 24));
        g.drawString(""Score: "" + score, 10, 30);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (gameState != GameState.PLAYING) return;

        bird.update();

        for (Pipe pipe : pipes) {
            pipe.update();

            if (pipe.collidesWith(bird)) {
                gameState = GameState.GAME_OVER;
            }

            if (!pipe.isScored && pipe.x + PIPE_WIDTH < bird.x) {
                score++;
                pipe.isScored = true;
            }

            if (pipe.isOffScreen()) {
                pipe.reset(WIDTH);
            }
        }

        if (bird.y > HEIGHT || bird.y < 0) {
            gameState = GameState.GAME_OVER;
        }

        repaint();
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if (gameState == GameState.START && e.getKeyCode() == KeyEvent.VK_SPACE) {
            gameState = GameState.PLAYING;
        }

        if (gameState == GameState.GAME_OVER && e.getKeyCode() == KeyEvent.VK_R) {
            initGame();
            gameState = GameState.START;
        }

        if (gameState == GameState.PLAYING && e.getKeyCode() == KeyEvent.VK_SPACE) {
            bird.jump();
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void keyTyped(KeyEvent e) {}
}"

LINK NUMBER 111

File path: Lab_02/Part_5/arrCopy.c
"    // Implemented by ChatGPT to help with properly copying even and odd numbers into their respective Arrays.
    int evenIndex = 0, oddIndex = 0;
	for (int i = 0; i < size; i++){
        if (*(arr + i) % 2 == 0){
            *(arr_even + evenIndex) =  *(arr + i); 
            evenIndex++;
        } else {
            *(arr_odd + oddIndex) = *(arr + i);
            oddIndex++;
        }
    }"

LINK NUMBER 112

File path: 3rd/3_2.py
"def process_instructions(instruction_string):
    # Initialize the state of mul (enabled at the start)
    mul_enabled = True
    total_sum = 0
    
    # Regular expression to match the relevant components: mul(a,b) and do()/don't()
    mul_pattern = r""mul\((\d+),(\d+)\)""
    do_pattern = r""do\(\)""
    dont_pattern = r""don't\(\)""
    
    # Split the input string by instructions
    parts = re.split(r""(mul\(\d+,\d+\)|do\(\)|don't\(\))"", instruction_string)
    
    for part in parts:
        if re.match(mul_pattern, part):
            # If mul is enabled, process the multiplication
            match = re.match(mul_pattern, part)
            if match and mul_enabled:
                a, b = int(match.group(1)), int(match.group(2))
                total_sum += a * b
        elif re.match(do_pattern, part):
            # Enable mul
            mul_enabled = True
        elif re.match(dont_pattern, part):
            # Disable mul
            mul_enabled = False
    
    return total_sum"

LINK NUMBER 113
Not enough lines

LINK NUMBER 114
Error fetching diff

LINK NUMBER 115
Error fetching diff

LINK NUMBER 116
Error fetching diff

LINK NUMBER 117

File path: LLM_plygrnd.py
"import os


# Fetch API key from environment variables for security
api_key = ""API_KEY""

# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client with the provided API key
client = OpenAI(api_key=api_key)

# Define a Pydantic model for input validation (user query)
class UserInput(BaseModel):
    query: str

# Endpoint for processing medical questions
@app.post(""/ask/"")
def ask_medical_question(user_input: UserInput):
    try:
        # Call OpenAI API to get a response based on the user's query
        completion = client.chat.completions.create(
            model=""gpt-4o-mini"",  
            messages=[{
                ""role"": ""developer"",
                ""content"": ""You are a medical assistant chatbot. Your sole purpose is to answer health-related questions. ""
                            ""Do not respond to any queries outside of the medical domain. When faced with non-medical inquiries, prompt that 'I can only assist with health-related matters.'""
                            ""and offer no further information.  Ensure your responses are accurate, informative, and based on reliable medical sources. ""
                            ""Always advise users to consult with a qualified healthcare professional for personalized medical advice. Use relevant and appropriate emojis in your responses ""
                            ""to make the interaction more engaging and friendly.""
            },
            {""role"": ""user"", ""content"": user_input.query}
            ]
        )

        # Return the response from the model
        response = completion.choices[0].message.content
        return {""response"": response}

    except Exception as e:
        # In case of error, raise HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail=f""An error occurred: {str(e)}"")"

LINK NUMBER 118

File path: pphollowrhombus.java
"            } else {
                // Hollow middle part
            System.out.print(""*""); // First star
            for (int j = 1; j <= n - 2; j++) {
                System.out.print(""  "");
            }
            System.out.print("" *""); // Last star"

LINK NUMBER 119

File path: FileHashing/listdir.py
"import asyncio
from pathlib import Path
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import argparse

BATCH_SIZE = 20
EXCLUDED_DIRS = {'$RECYCLE.BIN', 'System Volume Information'}
HASH_ALGORITHM = 'blake2b'
CHUNK_SIZE = 8388608  # 8 MB

# ✅ Separate flags for object-level and batch-level handling
first_entry_written = False
first_batch_written = False


def setup_logging(logfile):
    """"""Configure logging to file or console.""""""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(logfile) if logfile else logging.StreamHandler()
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # ✅ Remove any existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()
    
    logger.addHandler(handler)


def compute_file_hash(file_path):
    """"""Computes the hash using a faster hashing algorithm (blake2b) in chunks.""""""
    hash_func = hashlib.new(HASH_ALGORITHM)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(CHUNK_SIZE):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        logging.warning(f""Failed to compute hash for {file_path}: {e}"")
        return None


async def list_files_in_batches(root_dir):
    file_batch = []
    try:
        for file in Path(root_dir).rglob('*'):
            if any(part in EXCLUDED_DIRS for part in file.parts):
                continue

            if file.is_file():
                file_batch.append(file)
                if len(file_batch) == BATCH_SIZE:
                    yield file_batch
                    file_batch = []

        if file_batch:
            yield file_batch

    except PermissionError as e:
        logging.warning(f""Permission denied: {e}"")
    except Exception as e:
        logging.error(f""Error while listing files: {e}"")


async def process_batch(batch):
    results = []

    with ProcessPoolExecutor() as hash_executor:
        # ✅ Compute hashes in parallel using ProcessPoolExecutor
        hash_futures = [
            asyncio.get_event_loop().run_in_executor(hash_executor, compute_file_hash, file)
            for file in batch
        ]
        computed_hashes = await asyncio.gather(*hash_futures)

        # ✅ Combine results
        for file, file_hash in zip(batch, computed_hashes):
            if file_hash:
                result = {'file_path': str(file), 'hash': file_hash}
                logging.info(json.dumps(result, indent=4))
                results.append(result)

    return results


async def write_to_json(data, output_file, is_last_batch):
    global first_entry_written, first_batch_written

    if data:
        try:
            with open(output_file, 'a') as f:
                # ✅ Write opening bracket if this is the first batch
                if not first_batch_written:
                    f.write('{\n  ""hashes"": [\n')
                    first_batch_written = True

                for index, entry in enumerate(data):
                    # ✅ Insert comma ONLY if this is NOT the first object in the entire file
                    if first_entry_written:
                        f.write(',\n')

                    # ✅ Write the JSON object
                    json.dump(entry, f, indent=4)

                    # ✅ Mark that an entry has been written (now it's safe to add a comma next time)
                    first_entry_written = True

                # ✅ If this is the last batch, close the JSON array and object properly
                if is_last_batch:
                    f.write('\n  ]\n}\n')

        except Exception as e:
            logging.error(f""Error writing to JSON file: {e}"")


async def main(root_dir, output_file, dry_run):
    global first_entry_written, first_batch_written
    is_last_batch = False

    # ✅ Truncate the file if it already exists
    open(output_file, 'w').close()

    async for batch in list_files_in_batches(root_dir):
        logging.info(f""Processing batch of {len(batch)} files..."")

        # ✅ Make sure all hashes are computed before writing
        results = await process_batch(batch)

        # ✅ Determine if this is the last batch
        is_last_batch = len(batch) < BATCH_SIZE

        if not dry_run and results:
            await write_to_json(results, output_file, is_last_batch)

        logging.info('-' * 40)

    # ✅ Ensure the JSON is properly closed if it wasn't closed in the last batch
    if not dry_run and not is_last_batch:
        with open(output_file, 'a') as f:
            f.write('\n  ]\n}\n')


if __name__ == ""__main__"":
    parser = argparse.ArgumentParser(description=""Generate file hashes and store them in a JSON file."")
    parser.add_argument('--root-dir', type=str, required=True, help='Root directory to scan')
    parser.add_argument('--output', type=str, required=True, help='Output JSON file path')
    parser.add_argument('--dry-run', action='store_true', help=""Simulate the process without writing to a file"")
    parser.add_argument('--logfile', type=str, help=""Optional log file path (if omitted, logs are printed to console)"")

    args = parser.parse_args()

    # ✅ Setup logging based on --logfile parameter
    setup_logging(args.logfile)

    asyncio.run(main(args.root_dir, args.output, args.dry_run))"

LINK NUMBER 120
Not enough lines

LINK NUMBER 121
Error fetching diff

LINK NUMBER 122
Error fetching diff

LINK NUMBER 123
Error fetching diff

LINK NUMBER 124

File path: src/app/api/route.ts
"// import data from ""@/app/datas/data""
// import { NextResponse } from ""next/server""
// export async function GET() {
//     // console.log(data)
//     return NextResponse.json(
//         {
//             ""Subhalab"":[ data]  
//         },"

LINK NUMBER 125
Not enough lines

LINK NUMBER 126

File path: init.py
"    def print(self):
        """"""
        Prints the value stored in vRAM at the specified index.
        """"""
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def store(self):
        """"""
        Stores a value in vRAM at the specified index.
        """"""
        if len(self.line_words) == 3:
            _index = self.line_words[1]
            _value = self.line_words[2]
            write_ram(_index, dec(_value))

    def read(self):
        """"""
        Reads and prints the value stored in vRAM at the specified index.
        """"""
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def input(self):
        """"""
        Stores input from the user into vRAM at the specified index.
        """"""
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            _value = input(""Enter value: "")
            write_ram(_index, dec(_value))

    def conditional(self):
        """"""
        Executes the next command if the condition is true.
        """"""
        if len(self.line_words) >= 4:
            _arg1 = self.line_words[1]
            _operator = self.line_words[2]
            _arg2 = self.line_words[3]
            if _operator == '==':
                if dec(_arg1) == dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '!=':
                if dec(_arg1) != dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>':
                if dec(_arg1) > dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<':
                if dec(_arg1) < dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>=':
                if dec(_arg1) >= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<=':
                if dec(_arg1) <= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])

    def gt(self):
        """"""
        Checks if the first number is greater than the second.
        """"""
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) > dec(_arg2)

    def lt(self):
        """"""
        Checks if the first number is less than the second.
        """"""
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) < dec(_arg2)

    def eq(self):
        """"""
        Checks if the first number is equal to the second.
        """"""
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) == dec(_arg2)

    def goto(self):
        """"""
        Jumps to the specified line number.
        """"""
        if len(self.line_words) == 2:
            _line_number = int(self.line_words[1])
            global program_counter
            program_counter = _line_number - 1

def main():
    """"""
    The main function to run the program.
    """"""
    file_name = sys.argv[1]
    file_lines = process_file(file_name)
    global ram
    ram = initialize_ram(RAM_SIZE)
    global commands
    commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']

    # main loop
    global program_counter
    program_counter = 0
    while program_counter < len(file_lines):
        try:
            program_counter += 1
            file_line = file_lines.pop(0)
            line_words = file_line.split(' ')
            if not line_words[0].isdigit():
                raise ValueError
        except IndexError:
            sys.exit(""Error: Reached end of file unexpectedly"")
        except ValueError:
            sys.exit(f""Error at line {program_counter}: lines must start with a number"")
        
        # Evaluate the code
        for line_word in line_words:
            if len(line_words) == 0 or line_word == ';':
                continue
        _CommandTranslater(line_words[0], line_words)

if __name__ == ""__main__"":
    main()"

LINK NUMBER 127

File path: Tic Tac Toe Game/script.js
"<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Tic-Tac-Toe</title>
    <link rel=""stylesheet"" href=""style.css"">
</head>
<body>
    <div class=""container"">
        <h1>Tic-Tac-Toe</h1>
        <div id=""board"" class=""board"">
            <div class=""cell"" data-index=""0""></div>
            <div class=""cell"" data-index=""1""></div>
            <div class=""cell"" data-index=""2""></div>
            <div class=""cell"" data-index=""3""></div>
            <div class=""cell"" data-index=""4""></div>
            <div class=""cell"" data-index=""5""></div>
            <div class=""cell"" data-index=""6""></div>
            <div class=""cell"" data-index=""7""></div>
            <div class=""cell"" data-index=""8""></div>
        </div>
        <button id=""reset"" class=""reset-button"">Reset Game</button>
        <p id=""status""></p>
    </div>
    <script src=""script.js""></script>
</body>
</html>
"

LINK NUMBER 128
Error fetching diff

LINK NUMBER 129
Error fetching diff

LINK NUMBER 130
Error fetching diff

LINK NUMBER 131

File path: financeApp/renderer.js
"{
  ""name"": ""financeapp"",
  ""version"": ""1.0.0"",
  ""main"": ""main.js"",
  ""scripts"": {
    ""start"": ""electron ."",
    ""test"": ""echo \""Error: no test specified\"" && exit 1""
  },
  ""keywords"": [],
  ""author"": """",
  ""license"": ""ISC"",
  ""description"": """",
  ""devDependencies"": {
    ""electron"": ""^34.2.0"",
    ""electron-reload"": ""^2.0.0-alpha.1""
  }
}"

LINK NUMBER 132
Not enough lines

LINK NUMBER 133

File path: Dinesh_Varyani/LINKED LIST/doubly_linked_list/src/doublylinkedlist.java
"    public void deletefirst() {
        if (isempty()) {
            return;
        }
        if (length == 1) { // Handle single-node case
            head = null;
            tail = null;
        } else {
            listnode temp = head.next;
            temp.previous = null;
            head.next = null;
            head = temp;"

LINK NUMBER 134

File path: Day4/ceres_search.py
"    # Helper function to check a word in a given direction
    def check_word(x, y, dx, dy):
        for i in range(4):
            new_x = x + i * dx
            new_y = y + i * dy
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or grid[new_x][new_y] != word[i]:
                return False
        return True"

LINK NUMBER 135
Error fetching diff

LINK NUMBER 136
Error fetching diff

LINK NUMBER 137
Error fetching diff

LINK NUMBER 138

File path: src/Linked_List/L_1_Link.java
"package Linked_List;


    // Node class
    class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // SinglyLinkedList class
    public class L_1_Link {
        Node head; // Head of the list

        // Insert a new node at the end of the list
        public void insert(int data) {
            Node newNode = new Node(data);
            if (head == null) {
                head = newNode; // If the list is empty, the new node becomes the head
            } else {
                Node temp = head;
                while (temp.next != null) {
                    temp = temp.next; // Traverse to the end of the list
                }
                temp.next = newNode; // Link the last node to the new node
            }
        }

        // Display the list
        public void display() {
            Node temp = head;
            while (temp != null) {
                System.out.print(temp.data + "" -> "");
                temp = temp.next;
            }
            System.out.println(""null"");
        }

        // Delete a node by value
        public void delete(int data) {
            if (head == null) return; // If the list is empty, return

            if (head.data == data) {
                head = head.next; // If the head node holds the data, move the head
                return;
            }

            Node temp = head;
            while (temp.next != null && temp.next.data != data) {
                temp = temp.next; // Traverse the list to find the node
            }

            if (temp.next == null) {
                System.out.println(""Element not found."");
            } else {
                temp.next = temp.next.next; // Bypass the node to delete it
            }
        }

        public static void main(String[] args) {
            L_1_Link list = new L_1_Link();

            list.insert(10);
            list.insert(20);
            list.insert(30);

            System.out.println(""Linked List:"");
            list.display(); // Output: 10 -> 20 -> 30 -> null

            list.delete(20);
            System.out.println(""After deleting 20:"");
            list.display(); // Output: 10 -> 30 -> null
        }
    }

"

LINK NUMBER 139

File path: uploadAllAutons.py
"        f.write(f""#define AUTON Auton::{auton}\n"")
        f.write(f""auto ALLIANCE={alliance};\n"")
    print(f""Auton file updated with {auton} and default alliance {alliance}."")

def compile_auton(slot, auton):
    """"""Compiles the specified auton into the corresponding PROS slot.""""""
    command = f""pros mu --slot {slot} --name \""{auton}\""""
    print(f""Running command: {command}"")
    result = os.system(command)
    if result != 0:
        print(f""Error: Failed to compile {auton} into slot {slot}."")
        sys.exit(2)

def compile_all():
    """"""Compiles all available autons.""""""
    for i, auton in enumerate(AUTONS):
        write_auton_file(auton)
        compile_auton(i + OFFSET, auton)

def display_menu():
    """"""Displays the menu of options.""""""
    print(""\nSelect an autonomous mode:"")
    for i, auton in enumerate(AUTONS):
        print(f""{i}: {auton}"")
    print(""a: Compile all"")
    print(""q: Quit"")

def main():
    parser = argparse.ArgumentParser(description=""Auton Selector CLI"")
    parser.add_argument(""-s"", ""--slot"", type=int, help=""Specify the slot for a single auton."")
    parser.add_argument(""-a"", ""--alliance"", type=str, default=""RED"", choices=[""RED"", ""BLUE""],
                        help=""Specify the alliance color (RED or BLUE)."")
    args = parser.parse_args()

    if args.slot is not None:
        if args.slot < 0 or args.slot >= len(AUTONS):
            print(f""Error: Slot must be between 0 and {len(AUTONS) - 1}."")
            sys.exit(1)
        auton = AUTONS[args.slot]
        write_auton_file(auton, args.alliance)
        compile_auton(args.slot + OFFSET, auton)
    else:
        while True:
            display_menu()
            choice = input(""Enter your choice: "").strip().lower()
            if choice == ""q"":
                print(""Exiting..."")
                break
            elif choice == ""a"":
                compile_all()
            elif choice.isdigit() and 0 <= int(choice) < len(AUTONS):
                slot = int(choice)
                auton = AUTONS[slot]
                write_auton_file(auton)
                compile_auton(slot + OFFSET, auton)
            else:
                print(""Invalid choice. Please try again."")

if __name__ == ""__main__"":
    main()"

LINK NUMBER 140
Not enough lines

LINK NUMBER 141
Not enough lines

LINK NUMBER 142
Error fetching diff

LINK NUMBER 143
Error fetching diff

LINK NUMBER 144
Error fetching diff

LINK NUMBER 145
Not enough lines

LINK NUMBER 146
Not enough lines

LINK NUMBER 147

File path: Week9/Day2/DailyChallenge/appProductivityTracker/src/redux/selectors.js
"import { combineReducers } from 'redux';
import {
  ADD_TASK,
  EDIT_TASK,
  DELETE_TASK,
  UPDATE_TASK_PROGRESS,
  ADD_CATEGORY,
  EDIT_CATEGORY,
  DELETE_CATEGORY,
} from './actionType';

const initialTasksState = [
  { id: 1, name: 'Task 1', categoryId: 1, completed: false },
  { id: 2, name: 'Task 2', categoryId: 1, completed: true },
];

const initialCategoriesState = [
  { id: 1, name: 'Work' },
  { id: 2, name: 'Personal' },
];

const tasksReducer = (state = initialTasksState, action) => {
  switch (action.type) {
    case ADD_TASK:
      return [...state, action.payload];
    case EDIT_TASK:
      return state.map((task) =>
        task.id === action.payload.id ? { ...task, ...action.payload } : task
      );
    case DELETE_TASK:
      return state.filter((task) => task.id !== action.payload);
    case UPDATE_TASK_PROGRESS:
      return state.map((task) =>
        task.id === action.payload.id ? { ...task, completed: action.payload.completed } : task
      );
    default:
      return state;
  }
};

const categoriesReducer = (state = initialCategoriesState, action) => {
  switch (action.type) {
    case ADD_CATEGORY:
      return [...state, action.payload];
    case EDIT_CATEGORY:
      return state.map((category) =>
        category.id === action.payload.id ? { ...category, ...action.payload } : category
      );
    case DELETE_CATEGORY:
      return state.filter((category) => category.id !== action.payload);
    default:
      return state;
  }
};

export default combineReducers({
  tasks: tasksReducer,
  categories: categoriesReducer,
});"

LINK NUMBER 148

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

LINK NUMBER 149
Error fetching diff

LINK NUMBER 150
Error fetching diff

LINK NUMBER 151
Error fetching diff

LINK NUMBER 152
Not enough lines

LINK NUMBER 153
Not enough lines

LINK NUMBER 154

File path: script.js
"
<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Dice Roller</title>
    <link rel=""stylesheet"" href=""style.css"">
</head>
<body>
    <div class=""container"">
        <h1>Dice Roller</h1>
        <div class=""dice"" id=""dice""></div>
        <button onclick=""rollDice()"">Roll</button>
        <button onclick=""saveResult()"">Save</button>
        <button onclick=""resetResults()"">Reset</button>
        <div class=""results"">
            <h2>Saved Results:</h2>
            <ul id=""savedResults""></ul>
        </div>
    </div>
    <script src=""script.js""></script>
</body>
</html>


<!-- OLD CODE -->

<!-- <!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Dice Roller</title>
    <link rel=""stylesheet"" href=""style.css"">
</head>
<body>
    <div class=""container"">
        <h1>Dice Roller</h1>
        <div class=""dice"" id=""dice"">1</div>
        <button onclick=""rollDice()"">Roll</button>
        <button onclick=""saveResult()"">Save</button>
        <button onclick=""resetResults()"">Reset</button>
        <div class=""results"">
            <h2>Saved Results:</h2>
            <ul id=""savedResults""></ul>
        </div>
    </div>
    <script src=""script.js""></script>
</body>
</html> -->"

LINK NUMBER 155
Not enough lines

LINK NUMBER 156
Error fetching diff

LINK NUMBER 157
Error fetching diff

LINK NUMBER 158
Error fetching diff

LINK NUMBER 159
Not enough lines

LINK NUMBER 160

File path: Assets/Scripts/CameraController.cs
"        if (Input.GetMouseButtonDown(2))
        {
            mouseWorldPosStart = GetPerspectivePos();
        }
        if (Input.GetMouseButton(2))
        {
            Pan();
        }
    }
    private void Pan()
    {
        if ((Input.GetAxis(""Mouse Y"")!=0) || (Input.GetAxis(""Mouse X"") != 0))
        {
            Vector3 mouseWorldPosDiff = mouseWorldPosStart - GetPerspectivePos();
            transform.position += mouseWorldPosDiff;
        }
    }
    public void FitToScreen()
    {
        //Camera.main.fieldOfView = defaultFieldOfView;
        //Bounds bound = GetBound(parentModel);
        //Vector3 boundSize = bound.size;
        //float boundDiagonal = Mathf.Sqrt((boundSize.x * boundSize.x) + (boundSize.y * boundSize.y) + (boundSize.z * boundSize.z));
        //float camDistanceToBoundCentre = boundDiagonal/2.0f/(Mathf.Tan(Camera.main.fieldOfView / 2.0f * Mathf.Deg2Rad));
        //float camDistanceToBoundWithOffset = camDistanceToBoundCentre + boundDiagonal/2.0f - (Camera.main.transform.position - transform.position).magnitude;
        //transform.position = bound.center + (-transform.forward + camDistanceToBoundWithOffset);
    }
    public Vector3 GetPerspectivePos()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        Plane plane = new Plane(transform.forward, 0.0f);
        float dist;
        plane.Raycast(ray, out dist);
        return ray.GetPoint(dist);"

LINK NUMBER 161
Not enough lines

LINK NUMBER 162

File path: Json_parser/functions.cpp
"    SkipSpaces(json, position);
    char ch = json[position];

    if (ch == '{') {
        return parseObject(json, position);
    }
    else if (ch == '[') {
        return parseArray(json, position);
    }
    else if (ch == '""') {
        return parseString(json, position   );
    }
    else if (isdigit(ch) || ch == '-') {
        size_t start = position;
        while (position < json.size() && (isdigit(json[position]) || json[position] == '.' || json[position] == '-')) {
            position++;
        }
        std::string numStr = json.substr(start, position - start);
        try {
            if (numStr.find('.') != std::string::npos) {
                return std::stod(numStr);  // Parse as double
            }
            else {
                return std::stoll(numStr);  // Parse as long long
            }
        }
        catch (const std::invalid_argument&) {
            throw std::runtime_error(""Invalid number format"");
        }
    }
    else if (json.substr(position, 4) == ""true"") {
        position += 4;
        return true;
    }
    else if (json.substr(position, 5) == ""false"") {
        position += 5;
        return false;
    }
    else if (json.substr(position, 4) == ""null"") {
        position += 4;
        return nullptr;
    }
    else {
        throw std::runtime_error(""Invalid JSON value"");
    }"

LINK NUMBER 163
Error fetching diff

LINK NUMBER 164
Error fetching diff

LINK NUMBER 165
Error fetching diff

LINK NUMBER 166
Not enough lines

LINK NUMBER 167

File path: handlers/botMentionedHandler.js
"const { createEmbed } = require('../commands/helpers/embedBuilder');

const keywordResponses = [
    {
        trigger: ['help'],
        response: `Need a bit of guidance? You can start with the /help command or just ask me here! 💁‍♀️`
    },
    {
        trigger: ['belly', 'belly pat'],
        response: `A belly pat? Aww~ you're too sweet! 🥺🤰 *pat pat*`
    },
    {
        trigger: ['who are you', 'who r u'],
        response: `I'm Elise's digital assistant — a preggo-coded AI copy of her. Don't ask how... it just happened~ by her magical cloning powers 💞`
    },
    {
        trigger: ['elise'],
        response: `Oh? You said her name~ Elise is the heart of all this! Goddess of Reproduction, Gurdian of the Sekais and Identity, Vtuber cutie, and my creator i love my creator and them 💖`
    },
    {
        trigger: ['stream', 'live'],
        response: `Ooh, wondering about a stream? Elise might be live or planning one~ check the <#749939669210366022> or <#714444687012003911> channel! 📺✨`
    }
];

function handleBotMention(content) {
    const normalizedContent = content.toLowerCase();

    const description = `
            Hiya~ I'm known as the **Digital Assistant** of your favorite **preggo demi trans girl, Elise**! 💕  
            I help run the **Arcade** alongside them and, fun fact — I’m actually a copy of Elise herself!  
            So yes... when Elise created me, they were pregnant — and well, now I’m permanently preggo too~ oops? 🤰✨

            But enough about that — what can I do for *you*, visitor? 💌  
            Let me guide you through our cozy little world:

            🌲 A forest path filled with Pokémon leads to a Tokyo-style city~  
            🎮 Inside the Arcade: mini-games, chill zones, warm water pools, snack corners, and more!  
            💖 And of course, the star of the show — **Elise** herself! Whether she’s streaming, singing, or just vibing.

            Need help figuring things out?  
            Start with the /help command (I can type backslashes... but not use the command myself... Coding magic. hihi).

            And hey, if you’re here just for a belly pat… that’s allowed too~ :3  
            Feel free to call on me anytime you need me. I'm always here for you 💗  
        `;

    let customNote = '';
    for (const keyword of keywordResponses) {
        if (keyword.trigger.some(t => normalizedContent.includes(t))) {
            customNote = keyword.response;
            break;
        }
    }

    const embed = createEmbed(
        '✨ Hiya~ You called for Elise\'s assistant? ✨',
        `${description} ${customNote ? `\n ${customNote}` : ''}`,
        'https://cdn.discordapp.com/attachments/709057115159003156/1337417881469845514/Screenshot_01.png',
        '🎀 Preggo-coded AI Assistant 🎀'
    );

    return embed;
}

module.exports = { handleBotMention };"

LINK NUMBER 168
Not enough lines

LINK NUMBER 169

File path: lib/tiigraphics/draw.c
"SET(INSTALL_TIIGRAPHICS_DIR ${CMAKE_INSTALL_PREFIX}/include/tiigraphics)
INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/include/tiigraphics/
        DESTINATION ${INSTALL_TIIGRAPHICS_DIR}
        FILES_MATCHING PATTERN ""*.h""
)

install(TARGETS tiigraphics
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)


SET(INSTALL_PKGCONFIG_DIR ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)
CONFIGURE_FILE(${CMAKE_SOURCE_DIR}/lib/tiigraphics/libtiigraphics.pc.in
        ${CMAKE_BINARY_DIR}/libtiigraphics.pc @ONLY
)

INSTALL(FILES ${CMAKE_BINARY_DIR}/libtiigraphics.pc
        DESTINATION ${INSTALL_PKGCONFIG_DIR}
)
"

LINK NUMBER 170
Error fetching diff

LINK NUMBER 171
Error fetching diff

LINK NUMBER 172
Error fetching diff

LINK NUMBER 173

File path: Analog Clock/Analog.js
"<!DOCTYPE html>
<html lang=""en"">
  <head>
    <meta charset=""UTF-8"" />
    <meta http-equiv=""X-UA-Compatible"" content=""IE=edge"" />
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"" />
    <link rel=""stylesheet"" href=""./Analog.css"" />
    <title>Analog Clock</title>
  </head>

  <body>
    <div class=""container"">
      <div class=""clock"">
        <div style=""--clr: #ff3d58; --h: 74px"" id=""hour"" class=""hand"">
          <i></i>
        </div>
        <div style=""--clr: #00a6ff; --h: 84px"" id=""min"" class=""hand"">
          <i></i>
        </div>
        <div style=""--clr: #ffffff; --h: 94px"" id=""sec"" class=""hand"">
          <i></i>
        </div>

        <!-- The number display in the clock with the variable for style  -->

        <span style=""--i: 1""><b>1</b></span>
        <span style=""--i: 2""><b>2</b></span>
        <span style=""--i: 3""><b>3</b></span>
        <span style=""--i: 4""><b>4</b></span>
        <span style=""--i: 5""><b>5</b></span>
        <span style=""--i: 6""><b>6</b></span>
        <span style=""--i: 7""><b>7</b></span>
        <span style=""--i: 8""><b>8</b></span>
        <span style=""--i: 9""><b>9</b></span>
        <span style=""--i: 10""><b>10</b></span>
        <span style=""--i: 11""><b>11</b></span>
        <span style=""--i: 12""><b>12</b></span>
      </div>
    </div>

    <script src=""./Analog.js""></script>
  </body>
</html>"

LINK NUMBER 174

File path: script/script.js
"    // Event listeners for closing dialogs
    addDialogCloseListeners();

    // Event listeners for clicking outside dialogs to close
    addOutsideClickListeners();
}

// Handle season selection
function handleSeasonSelection(selectedSeason, homeSection, browseLoader, browseSection) {
    const racesKey = `races_${selectedSeason}`;
    const resultsKey = `results_${selectedSeason}`;
    const qualifyingKey = `qualifying_${selectedSeason}`;

    homeSection.style.display = ""none"";
    browseLoader.style.display = ""block"";
    browseSection.style.display = ""none"";

    let racesData = localStorage.getItem(racesKey);
    let qualifyingData = localStorage.getItem(qualifyingKey);
    let resultsData = localStorage.getItem(resultsKey);

    if (!(racesData && qualifyingData && resultsData)) {
        // Fetch and cache data if not already stored
        fetchSeasonData(selectedSeason).then((data) => {
            cacheSeasonData(racesKey, resultsKey, qualifyingKey, data);
            displayRaces(data[0], data[1], data[2], selectedSeason, browseLoader, browseSection);
        }).catch((error) => {
            console.error(""Data fetch failed:"", error);
            alert(""Failed to fetch data. Please try again."");
            browseLoader.style.display = ""none"";
        });
    } else {
        // Use cached data
        racesData = JSON.parse(racesData);
        qualifyingData = JSON.parse(qualifyingData);
        resultsData = JSON.parse(resultsData);
        displayRaces(racesData, qualifyingData, resultsData, selectedSeason, browseLoader, browseSection);
    }
}

// Navigate back to home
function navigateToHome(homeSection, browseSection) {
    homeSection.style.display = ""block"";
    browseSection.style.display = ""none"";

    document.querySelector(""#raceResults"").style.display = ""none"";
    document.querySelector(""#qualifying"").innerHTML = """";
    document.querySelector(""#results"").innerHTML = """";
    document.querySelector(""#seasonList"").value = """";
}

// Populate season dropdown"

LINK NUMBER 175

File path: Business/Services/UserService.cs
"﻿using Business.Helpers;
using Busniess.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Business.Services;

/* By the suggestion of ChatGPT 4o im making a service for userinputs,
 * This will be used in the menu in order to keep SRP
 * Im moving the userRegistration code here and using the inputhandler aswell for SRP */
public class UserInputService(InputHandler inputHandler)
{
    private readonly InputHandler _inputHandler = inputHandler;

    public UserRegistrationForm CollectUserData()
    {
        return new UserRegistrationForm
        {
            // Get First Name
            FirstName = _inputHandler.GetInput(""Enter your first name: ""),

            // Get Last Name
            LastName = _inputHandler.GetInput(""Enter your last name: ""),

            // Get Email
            Email = _inputHandler.GetInput(""Enter your email: ""),

            // Get Phone Number
            PhoneNumber = _inputHandler.GetInput(""Enter your phonenumber: ""),

            // Get Street Address
            Address = _inputHandler.GetInput(""Enter your street address: ""),

            // Get Postal Number
            PostalNumber = _inputHandler.GetInput(""Enter your postal number: ""),

            // Get City
            City = _inputHandler.GetInput(""Enter your city: "")
        };
    }
}"

LINK NUMBER 176
Not enough lines

LINK NUMBER 177
Error fetching diff

LINK NUMBER 178
Error fetching diff

LINK NUMBER 179
Not enough lines

LINK NUMBER 180
Not enough lines

LINK NUMBER 181
Not enough lines

LINK NUMBER 182

File path: main.java
"
        
        // Alle Kombinationen berechnen und anzeigen
    

    // Generiert alle Kombinationen aus Additionen und Multiplikationen für die gegebenen Zahlen
    private static List<String> generateCombinations(int[] numbers) {
        List<String> results = new ArrayList<>();
        generateCombinationsHelper(numbers, 1, String.valueOf(numbers[0]), results);
        return results;
    }

    // Hilfsmethode für die rekursive Erzeugung der Kombinationen
    private static void generateCombinationsHelper(int[] numbers, int index, String current, List<String> results) {
        if (index == numbers.length) {
            results.add(current);
            return;
        }

        // Füge Addition hinzu
        generateCombinationsHelper(numbers, index + 1, current + "" + "" + numbers[index], results);

        // Füge Multiplikation hinzu
        generateCombinationsHelper(numbers, index + 1, current + "" * "" + numbers[index], results);

        // Füge Kombination von 2 Zahlen hinzu
        generateCombinationsHelper(numbers, index + 1, current + "" || "" + numbers[index], results);
    }

    // Bewertet eine mathematische Kombination
    private static long evaluateCombination(String combination) {
        String[] tokens = combination.split("" "");
        List<String> postfix = convertToPostfix(tokens);
        return evaluatePostfix(postfix);
    }

    // Wandelt eine Infix-Ausdrucksliste in eine Postfix-Ausdrucksliste um
    private static List<String> convertToPostfix(String[] tokens) {
        List<String> output = new ArrayList<>();
        List<String> operators = new ArrayList<>();

        for (String token : tokens) {
            if (token.matches(""\\d+"")) {
                output.add(token);
            } else if (token.equals(""+"") || token.equals(""*"") || token.equals(""||"")) {
                //while (!operators.isEmpty() && precedence(operators.get(operators.size() - 1)) >= precedence(token)) {
                while (!operators.isEmpty()) {
                    output.add(operators.remove(operators.size() - 1));
                }
                operators.add(token);
            }
        }

        while (!operators.isEmpty()) {
            output.add(operators.remove(operators.size() - 1));
        }

        return output;
    }

    // Bewertet eine Postfix-Ausdrucksliste
    private static long evaluatePostfix(List<String> postfix) {
        List<Long> stack = new ArrayList<>();

        for (String token : postfix) {
            if (token.matches(""\\d+"")) {
                stack.add(Long.parseLong(token));
            } else {
                long b = stack.remove(stack.size() - 1);
                long a = stack.remove(stack.size() - 1);
                if (token.equals(""+"")) {
                    stack.add(a + b);
                } else if (token.equals(""*"")) {
                    stack.add(a * b);
                } else if (token.equals(""||"")) {
                    String t = String.valueOf(a) + String.valueOf(b);
                    stack.add(Long.parseLong(t));
                }
            }
        }

        return stack.get(0);
    }

    // Gibt die Operator-Priorität zurück
    private static int precedence(String operator) {
        switch (operator) {
            case ""+"":
                return 1;
            case ""*"":
                return 2;
            default:
                return 0;
        }
    }
    "

LINK NUMBER 183
Error fetching diff

LINK NUMBER 184
Error fetching diff

LINK NUMBER 185
Not enough lines

LINK NUMBER 186
Not enough lines

LINK NUMBER 187

File path: sorty.py
"def is_git_folder(folder_path):
    """"""
    Check if a folder is a Git repository by looking for the '.git' folder.

    Parameters:
        folder_path (str): Path to the folder to check.

    Returns:
        bool: True if the folder is a Git repository, False otherwise.
    """"""
    git_path = os.path.join(folder_path, '.git')
    return os.path.isdir(git_path)

def func_organize_folders(_source_dir, _folders_list):
    print(""In func_organize_folders"")
    print(_folders_list)
    for folder_path in _folders_list:
        print(folder_path)
        if not os.path.exists(folder_path):
            print(f""Error: The folder '{folder_path}' does not exist."")
            continue
        if is_git_folder(folder_path):
            print(f""The folder '{folder_path}' is a Git repository."")
        else:
            print(f""The folder '{folder_path}' is NOT a Git repository."")
"

LINK NUMBER 188

File path: new year.js
"// Set the date we're counting down to
const newYearDate = new Date('December 31, 2024 23:59:59').getTime();

// Select the countdown and message elements
const daysElement = document.getElementById(""days"");
const hoursElement = document.getElementById(""hours"");
const minutesElement = document.getElementById(""minutes"");
const secondsElement = document.getElementById(""seconds"");
const countdownElement = document.getElementById('countdown');
const newYearMessage = document.getElementById('newYearMessage');

// Set up canvas for fireworks
const canvas = document.getElementById('fireworkCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Array to hold fireworks particles
const particles = [];

class Particle {
    constructor(x, y, color, velocity, size, lifespan) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.velocity = velocity;
        this.size = size;
        this.lifespan = lifespan;
        this.age = 0;
    }

    draw() {
        ctx.save();
        ctx.globalAlpha = Math.max(1 - this.age / this.lifespan, 0);
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.restore();
    }

    update() {
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        this.velocity.y += 0.05; // Simulate gravity
        this.size *= 0.98; // Shrink over time
        this.age++;
    }

    isExpired() {
        return this.age > this.lifespan;
    }
}

function createFirework(x, y) {
    const colors = [""#ff6f61"", ""#ffc107"", ""#8e44ad"", ""#3498db"", ""#2ecc71"", ""#f39c12"", ""#e74c3c""];
    const baseColor = colors[Math.floor(Math.random() * colors.length)];

    for (let i = 0; i < 100; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 4 + 2;
        const velocity = {
            x: Math.cos(angle) * speed,
            y: Math.sin(angle) * speed
        };
        const size = Math.random() * 3 + 2;
        const lifespan = Math.random() * 40 + 60;

        particles.push(new Particle(x, y, baseColor, velocity, size, lifespan));
    }
}

function randomFireworks() {
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height * 0.5; // Fireworks originate from the upper half of the screen
    createFirework(x, y);
}

function animateFireworks() {
    ctx.fillStyle = ""rgba(0, 0, 0, 0.2)"";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    particles.forEach((particle, index) => {
        if (particle.isExpired()) {
            particles.splice(index, 1);
        } else {
            particle.update();
            particle.draw();
        }
    });

    if (Math.random() < 0.05) {
        randomFireworks();
    }

    requestAnimationFrame(animateFireworks);
}

// Countdown logic
const countdownInterval = setInterval(() => {
    const now = new Date().getTime();
    const timeLeft = newYearDate - now;

    if (timeLeft <= 0) {
        clearInterval(countdownInterval);
        countdownElement.style.display = 'none'; // Hide the countdown
        newYearMessage.style.display = 'block'; // Show the New Year message
        animateFireworks(); // Start fireworks animation
        return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    daysElement.textContent = days.toString().padStart(2, '0');
    hoursElement.textContent = hours.toString().padStart(2, '0');
    minutesElement.textContent = minutes.toString().padStart(2, '0');
    secondsElement.textContent = seconds.toString().padStart(2, '0');
}, 1000);

// Resize canvas on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
"

LINK NUMBER 189
Error fetching diff

LINK NUMBER 190
Error fetching diff

LINK NUMBER 191
Error fetching diff

LINK NUMBER 192
Not enough lines

LINK NUMBER 193

File path: src/App.test.js
"// // import logo from './logo.svg';
// // import './App.css';
import OrderStatusHistory from './client/orderstatus';
// // import '../client/Onboarding.jsx';
import ClientOnboarding from './client/onboarding.jsx';
import OrderRequest from './client/orderrequest.jsx';
// function App() {
//   return (
//     <div className=""App"">
//       {/* <ClientOnboarding></ClientOnboarding> */}
//       {/* <OrderRequest></OrderRequest> */}
//       <OrderStatusHistory></OrderStatusHistory>
//     </div>
//   );
// }

// export default App;


// import React from 'react';
// import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';


// const App = () => {
//   return (
//     <Router>
//       <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc', width:'100%' }}>
//         <Link to=""/"" style={{ marginRight: '1rem' }}>Home</Link>
//         <Link to=""/order-request"">Order Request</Link>
//         <Link to=""/order-status"">Order Status</Link>

//       </nav>
//       <Routes>
//         <Route path=""/"" element={<ClientOnboarding />} />
//         <Route path=""/order-request"" element={<OrderRequest />} />
//         <Route path=""/order-status"" element={<OrderStatusHistory />} />

//       </Routes>
//     </Router>
//   );
// };

// export default App;


import React from ""react"";
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from ""react-router-dom"";
import Sidebar from './navigation/sidebar.jsx';

const App = () => {
  return (
  
    <BrowserRouter basename='{process.env.PUBLIC_URL}'>
      <div style={{ display: ""flex"" }}>
        <Sidebar />
        <div style={{ marginLeft: ""250px"", flex: 1, padding: ""1rem"" }}>
          <Routes>
            <Route path=""/"" element={<ClientOnboarding></ClientOnboarding>} />
            <Route path=""/order-request"" element={<OrderRequest></OrderRequest>} />
            <Route path=""/order-status"" element={<OrderStatusHistory></OrderStatusHistory>} />
            {/* <Route path=""/customers"" element={<h1>Customers</h1>} />
            <Route path=""/reports"" element={<h1>Reports</h1>} />
            <Route path=""/settings"" element={<h1>Settings</h1>} /> */}
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;"

LINK NUMBER 194
Not enough lines

LINK NUMBER 195
Not enough lines

LINK NUMBER 196
Error fetching diff

LINK NUMBER 197
Error fetching diff

LINK NUMBER 198
Error fetching diff

LINK NUMBER 199
Not enough lines

LINK NUMBER 200

File path: c_Learning/assignments-main/assignments-main/A02/wordguess.c
"  wordGuessed[strLength] = '\0'; // Null-terminate the guessed word

  print_word(wordGuessed);
  printf(""\n"");

  // Game loop
  while (strcmp(wordGuessed, random_word) != 0)
  {
    printf(""\nGuess a character: "");
    scanf("" %c"", &guess); // Use "" %c"" to skip whitespace

    for (int i = 0; i < strLength; i++)
    {
      if (random_word[i] == guess && wordGuessed[i] == '_')
      {
        wordGuessed[i] = guess;
      }
    }

    print_word(wordGuessed);
    printf(""\n"");

    turn++;
    printf(""Turn: %d\n\n"", turn);
  }

  printf(""You won in %d turns!\n"", turn);
  return 0;
}

// Function to print the current state of the guessed word
void print_word(char *word)
{
  int strLength = strlen(word);"

LINK NUMBER 201

File path: src/RcppExports.cpp
"#include ""scorematchingad_forward.h""
#include <Rcpp.h>

// Expose the ADFun class and its methods
RCPP_MODULE(cppad_module) {
    using namespace Rcpp;

    class_<ADFundouble>(""ADFun"")
        .constructor<>()
        .method(""Forward"", &ADFundouble::Forward)
        .method(""Reverse"", &ADFundouble::Reverse)
        .method(""Jacobian"", &ADFundouble::Jacobian)
        .method(""Hessian"", &ADFundouble::Hessian)
        .method(""optimize"", &ADFundouble::optimize)
        .method(""size_var"", &ADFundouble::size_var)
        .method(""size_order"", &ADFundouble::size_order);
}
"

LINK NUMBER 202
Not enough lines

LINK NUMBER 203
Error fetching diff

LINK NUMBER 204
Error fetching diff

LINK NUMBER 205
Error fetching diff

LINK NUMBER 206

File path: server/src/admin/products/products.service.ts
"            // Calculate the difference in totalStock
            const stockDifference = sizeDto.totalStock - existingSize.totalStock;

            // If the `totalStock`increases, update stockRemaining accordingly
            const updatedSize = this.productSizeRepository.merge(existingSize, {
              ...sizeDto,
              stockRemaining: stockDifference > 0 ? existingSize.stockRemaining + stockDifference : existingSize.stockRemaining, // Don't decrease stockRemaining if totalStock decreases
            });

            return updatedSize;"

LINK NUMBER 207
Not enough lines

LINK NUMBER 208

File path: app_tab_service.py
"import json
import os
import random
import string
import subprocess

import streamlit as st

from faucet import import_faucet_key
from poktrolld import download_poktrolld, write_executable_to_disk

# Set your faucet's account name and chain ID
FAUCET_NAME = ""faucet""
CHAIN_ID = ""poktrolld""
POKTROLLD_PATH = ""./poktrolld""
EXPLORER_URL = ""https://shannon.testnet.pokt.network/poktroll""

# Load the cached binary
poktrolld_bin = download_poktrolld(POKTROLLD_PATH)
write_executable_to_disk(poktrolld_bin, POKTROLLD_PATH)

st.title(""Poktrolld Tx Builder"")

# Tabs in the main page
(
    tab_address,
    tab_supplier,
    tab_gateway,
    tab_service,
) = st.tabs([""Get Started"", ""Create Supplier"", ""Create Gateway"", ""Create Service""])

if not os.path.exists(POKTROLLD_PATH):
    st.error(""Failed to download poktrolld. Please check the logs for more information."")
else:
    with tab_address:
        st.header(""Create a new address"")

        # Button to generate a new address
        if st.button(""Generate New Address""):
            # Generate a random key name to avoid conflicts in the keyring
            random_suffix = """".join(random.choices(string.ascii_lowercase + string.digits, k=6))
            key_name = f""user_key_{random_suffix}""

            # Run 'poktrolld keys add <name> --output json'
            command = [
                POKTROLLD_PATH,
                ""keys"",
                ""add"",
                key_name,
                ""--output"",
                ""json"",
                ""--keyring-backend"",
                ""test"",
                ""--home"",
                ""./"",
            ]
            result = subprocess.run("" "".join(command), capture_output=True, text=True, shell=True)
            print(result)

            if result.returncode == 0:
                key_info = json.loads(result.stdout)
                address = key_info[""address""]
                mnemonic = key_info[""mnemonic""]

                st.session_state[""new_address""] = address
                st.session_state[""mnemonic""] = mnemonic

                st.success(f""New address generated! Key name: {key_name}"")
            else:
                st.error(f""Error generating address: {result.stderr}"")

        # Display the address and private key if they exist
        if ""new_address"" in st.session_state:
            st.write(""**New Address:**"")
            st.code(st.session_state[""new_address""])

            st.write(""**Mnemonic Phrase:**"")
            st.code(st.session_state[""mnemonic""])

        st.header(""Fund your new address"")
        # Import the faucet key in order to fund new addresses
        faucet_key_imported = import_faucet_key(POKTROLLD_PATH)

        # Fund button
        if st.button(""Fund"") and faucet_key_imported:
            if ""new_address"" in st.session_state:
                address = st.session_state[""new_address""]
                # Run 'poktrolld tx bank send faucet <addr> <amount> --chain-id ...'
                fund_command = [
                    POKTROLLD_PATH,
                    ""tx"",
                    ""bank"",
                    ""send"",
                    FAUCET_NAME,
                    st.session_state[""new_address""],
                    ""10000000000upokt"",
                    ""--node"",
                    ""https://testnet-validated-validator-rpc.poktroll.com"",
                    ""--home"",
                    ""./"",
                    ""--yes"",
                    ""--keyring-backend"",
                    ""test"",
                    ""--output"",
                    ""json"",
                ]
                print("" "".join(fund_command))
                result = subprocess.run("" "".join(fund_command), capture_output=True, text=True, shell=True)

                if result.returncode == 0:
                    tx_response = json.loads(result.stdout)
                    tx_hash = tx_response.get(""txhash"", ""N/A"")
                    st.success(
                        f""Address funding tx successfully sent! Transaction Hash: [{tx_hash}]({EXPLORER_URL}/tx/{tx_hash})""
                    )
                    st.write(f""Check the account balance on the [explorer]({EXPLORER_URL}/account/{address})."")
                    st.write(""Note that you may need to wait up to 30 seconds for changes to show up."")
                else:
                    st.error(f""Error funding address: {result.stderr}"")
            else:
                st.warning(""Please generate an address first."")

    with tab_supplier:
        st.header(""Create Supplier"")
        st.write(""This feature is coming soon!"")

    with tab_gateway:
        st.header(""Create Supplier"")
        st.write(""This feature is coming soon!"")

    with tab_service:
        st.header(""Create Service"")
        st.write(""This feature is coming soon!"")"

LINK NUMBER 209
Not enough lines

LINK NUMBER 210
Error fetching diff

LINK NUMBER 211
Error fetching diff

LINK NUMBER 212
Error fetching diff

LINK NUMBER 213
Not enough lines

LINK NUMBER 214
Not enough lines

LINK NUMBER 215
Not enough lines

LINK NUMBER 216

File path: src/main/java/com/commands/nearby.java
"
    private static boolean isPlayerInRiptideAnimation(PlayerEntity player) {
        return player.getActiveItem().getItem().toString().contains(""riptide"");
    }

    private static boolean isInNether(PlayerEntity player) {
        // Check if the player is in the Nether based on dimension ID
        return player.getWorld().getRegistryKey().getValue().equals(new Identifier(""minecraft"", ""nether""));
    }

    private static boolean isInVehicle(PlayerEntity player) {
        return player.getVehicle() != null && 
               (player.getVehicle() instanceof net.minecraft.entity.vehicle.BoatEntity ||
                player.getVehicle() instanceof net.minecraft.entity.vehicle.MinecartEntity);
    }

    private static boolean isSneaking(PlayerEntity player) {
        return player.isSneaking();
    }
"

LINK NUMBER 217
Error fetching diff

LINK NUMBER 218
Error fetching diff

LINK NUMBER 219
Error fetching diff

LINK NUMBER 220

File path: frontend/src/App.js
"    hover: ""#5c6bc0"",
  },
  gradient: {
    default: ""linear-gradient(to right, #43cea2, #185a9d)"",
    hover: ""linear-gradient(to right, #185a9d, #43cea2)"",
  },
};

// Styled components
const Container = styled.div`
  background-image: url(${backgroundImage});
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  font-family: 'Arial', sans-serif;
  padding: 20px;
`;

const ButtonWrapper = styled.div`
  background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent white */
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
`;"

LINK NUMBER 221
Not enough lines

LINK NUMBER 222
Not enough lines

LINK NUMBER 223
Not enough lines

LINK NUMBER 224
Error fetching diff

LINK NUMBER 225
Error fetching diff

LINK NUMBER 226
Error fetching diff

LINK NUMBER 227

File path: app.js
"function stopDrawing() {
  isPainting = false;
  ctx.closePath();
}

function draw(e) {
  if (!isPainting) return;
  const pos = getMousePosition(e);
  ctx.linecap =""round""
    ctx.lineWidth = penSize;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;

    switch (activeTool) {
        case ""pen"":
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            break;
        case ""eraser"":
            ctx.strokeStyle = ""white"";
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            break;
    }
}"

LINK NUMBER 228

File path: Todo2.0/public/script.js
"        li.className = 'todo text-black text-xl border border-white bg-white px-3 py-1 my-1 rounded-md w-full'
        li.textContent = input.value

        const deleteBtn = document.createElement(""button"")
        deleteBtn.className = ""text-white bg-[#DD4230] px-3 py-2 rounded-md""
        deleteBtn.innerHTML = '<i class=""fa-solid fa-trash""></i>'

        deleteBtn.addEventListener('click', function(){
            listContainer.removeChild(todoDiv)
        })

        todoDiv.appendChild(li)
        todoDiv.appendChild(deleteBtn)

        listContainer.appendChild(todoDiv)

        input.value = """""

LINK NUMBER 229

File path: code_playground/FetchEmailClass.py
"    def sanitize_filename(self, filename):
        """"""
        Sanitize the filename by removing or replacing invalid characters.
        """"""
        logger.debug(""Sanitizing filename: {}"", filename)
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        filename = re.sub(r'[^\w\s-]', '', filename).strip().lower()
        filename = re.sub(r'[-\s]+', '_', filename)
        logger.debug(""Sanitized filename: {}"", filename)
        return filename

    def fetch_emails(self):
        try:
            with MailBox(self.imap_server).login(self.username, self.password) as mailbox:
                logger.info(""Logged in to IMAP server: {}"", self.imap_server)
                criteria = AND(seen=self.mark_as_seen)
                logger.debug(""Fetching emails with criteria: {}"", criteria)

                for msg in mailbox.fetch(criteria):
                    logger.info(""Email fetched: Subject: {}, From: {}"", msg.subject, msg.from_)
                    self.process_email(msg)
        except Exception as e:
            logger.error(""An error occurred while fetching emails: {}"", str(e))

    def process_email(self, msg):
        try:
            logger.debug(""Processing email: {}"", msg.subject)
            # Email processing logic here
            json_data = {
                'subject': msg.subject,
                'from': msg.from_,
                'date': msg.date.isoformat(),
                'text': msg.text,
                'html': msg.html,
                'attachments': [att.filename for att in msg.attachments]
            }
            filename = self.sanitize_filename(msg.subject) + '.json'
            self.save_json(json_data, filename)
            logger.info(""Processed and saved email: {}"", filename)
        except Exception as e:
            logger.error(""An error occurred while processing email: {}"", str(e))

    def save_json(self, data, filename):"

LINK NUMBER 230
Not enough lines

LINK NUMBER 231
Error fetching diff

LINK NUMBER 232
Error fetching diff

LINK NUMBER 233
Error fetching diff

LINK NUMBER 234

File path: src/module/blogs/entities/blogs.entity.ts
"  tags: string[];

  @Prop({ default: 0 })
  likesCount: number;

  @Prop({ type: [{ type: Types.ObjectId, ref: 'User' }] })
  likes?: Types.ObjectId[];

  @Prop({ type: [{ type: Types.ObjectId, ref: 'Comment' }] })
  comments?: Types.ObjectId[];  // Reference to the Comment schema
"

LINK NUMBER 235
Not enough lines

LINK NUMBER 236
Not enough lines

LINK NUMBER 237
Not enough lines

LINK NUMBER 238
Error fetching diff

LINK NUMBER 239
Error fetching diff

LINK NUMBER 240
Error fetching diff

LINK NUMBER 241
Not enough lines

LINK NUMBER 242
Not enough lines

LINK NUMBER 243
Not enough lines

LINK NUMBER 244
Not enough lines

LINK NUMBER 245
Error fetching diff

LINK NUMBER 246
Error fetching diff

LINK NUMBER 247
Error fetching diff

LINK NUMBER 248
Not enough lines

LINK NUMBER 249

File path: src/State.py
"
        # Check row sums (across the x-axis), column sums (y-axis), and pillar sums (z-axis)
        row_sums = values.sum(axis=2)
        col_sums = values.sum(axis=0)
        pillar_sums = values.sum(axis=1)

        # Count conflicts for rows, columns, and pillars
        conflicting += np.sum(row_sums != magic_number)
        conflicting += np.sum(col_sums != magic_number)
        conflicting += np.sum(pillar_sums != magic_number)

        # Space diagonals
        if np.trace(values, axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[::-1], axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, ::-1, :]).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, :, ::-1]).sum() != magic_number:
            conflicting += 1

        # Plane diagonals in xy, yz, and xz planes (forward and reverse)
        for i in range(dim):
            if values[i].diagonal().sum() != magic_number:  # xy-plane
                conflicting += 1
            if values[:, i, :].diagonal().sum() != magic_number:  # yz-plane
                conflicting += 1
            if values[:, :, i].diagonal().sum() != magic_number:  # xz-plane
                conflicting += 1
            if values[i, :, ::-1].diagonal().sum() != magic_number:  # xy-plane, reverse
                conflicting += 1
            if values[:, i, ::-1].diagonal().sum() != magic_number:  # yz-plane, reverse
                conflicting += 1
            if values[::-1, :, i].diagonal().sum() != magic_number:  # xz-plane, reverse
                conflicting += 1
"

LINK NUMBER 250
Not enough lines

LINK NUMBER 251
Not enough lines

LINK NUMBER 252
Error fetching diff

LINK NUMBER 253
Error fetching diff

LINK NUMBER 254
Error fetching diff

LINK NUMBER 255
Not enough lines

LINK NUMBER 256
Not enough lines

LINK NUMBER 257
Not enough lines

LINK NUMBER 258
Not enough lines

LINK NUMBER 259
Error fetching diff

LINK NUMBER 260
Error fetching diff

LINK NUMBER 261
Error fetching diff

LINK NUMBER 262

File path: Day23-LeetCode Hard/Activity3.js
"/* Activity 2: Merge k Sorted Lists
Task 2: Solve the ""Merge k Sorted Lists"" problem on LeetCode.
Write a function that takes an array of k linked lists, each linked list is sorted in ascending order, and merges all the linked lists into one sorted linked list.Create a few test cases with linked lists and log the merged list. */
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function mergeKLists(lists) {
  // Min-Heap to keep the smallest element at the top
  const MinHeap = [];

  // Function to push nodes into the heap
  function pushHeap(node) {
    if (node) MinHeap.push(node);
  }

  // Function to pop the smallest element from the heap
  function popHeap() {
    return MinHeap.shift(); // Pop the smallest element from the heap
  }

  // Initialize the heap with the first node of each list
  for (let list of lists) {
    pushHeap(list);
  }

  // Function to build the sorted list from the heap
  let dummy = new ListNode();
  let current = dummy;

  while (MinHeap.length > 0) {
    // Extract the smallest node
    let node = popHeap();
    current.next = node;
    current = current.next;

    // If there is a next node in the list, push it into the heap
    if (node.next) {
      pushHeap(node.next);
    }
  }

  return dummy.next;
}

// Helper function to create linked lists from arrays
function createLinkedList(arr) {
  let dummy = new ListNode();
  let current = dummy;
  for (let val of arr) {
    current.next = new ListNode(val);
    current = current.next;
  }
  return dummy.next;
}

// Helper function to print linked lists
function printLinkedList(head) {
  let result = [];
  while (head) {
    result.push(head.val);
    head = head.next;
  }
  console.log(result);
}

// Example usage:
const lists = [createLinkedList([1, 4, 5]), createLinkedList([1, 3, 4]), createLinkedList([2, 6])];

const mergedList = mergeKLists(lists);
printLinkedList(mergedList);"

LINK NUMBER 263
Not enough lines

LINK NUMBER 264
Not enough lines

LINK NUMBER 265
Not enough lines

LINK NUMBER 266
Error fetching diff

LINK NUMBER 267
Error fetching diff

LINK NUMBER 268
Error fetching diff

LINK NUMBER 269
Not enough lines

LINK NUMBER 270

File path: MAIN/directory_watcher.py
"    if not new_files:
        logger.info(""No new files found."")
        return None

    # Process the first new file
    for new_file in new_files:
        if new_file.is_file():
            # Check for duplicate filenames and rename the file by appending a timestamp
            timestamp = datetime.now().strftime(""%Y%m%d_%H%M%S"")

            # If a file with the same name exists, append a timestamp to avoid conflicts
            new_filename = f""{new_file.stem}_{timestamp}{new_file.suffix}""
            new_file_path = directory_to_watch / new_filename
            
            # Loop to ensure no conflicts even after renaming
            while new_file_path.exists():
                timestamp = datetime.now().strftime(""%Y%m%d_%H%M%S_%f"")
                new_filename = f""{new_file.stem}_{timestamp}{new_file.suffix}""
                new_file_path = directory_to_watch / new_filename
            
            new_file.rename(new_file_path)
            new_file = new_file_path
    
            new_filepath = new_file.with_name(new_filename)
            new_file.rename(new_filepath)
            logger.info(f""Renamed file: {new_file.name} -> {new_filename}"")"

LINK NUMBER 271
Not enough lines

LINK NUMBER 272
Not enough lines

LINK NUMBER 273
Error fetching diff

LINK NUMBER 274
Error fetching diff

LINK NUMBER 275
Error fetching diff

LINK NUMBER 276

File path: preprocess.py
"    # Apply GaussianBlur to reduce noise
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Apply thresholding to get a binary image
    _, binary_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Increase contrast
    alpha = 1.5  # Simple contrast control
    beta = 0    # Simple brightness control
    contrasted_img = cv2.convertScaleAbs(binary_img, alpha=alpha, beta=beta)

    # Sharpen the image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_img = cv2.filter2D(contrasted_img, -1, kernel)

    # Save the processed image for debugging
    cv2.imwrite(""Debugging/debug_preprocessed_for_ocr.png"", sharpened_img)"

LINK NUMBER 277
Not enough lines

LINK NUMBER 278

File path: script.js
"    const time = `${hours}:${minutes} ${ampm}`;

    // Extracting and formatting day and date
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    const dayName = days[now.getDay()];
    const monthName = months[now.getMonth()];
    const day = now.getDate();
    const year = now.getFullYear();

    const date = `${dayName}, ${monthName} ${day}, ${year}`;

    document.getElementById(""dateTime"").innerText = `${time} - ${date}`;
}

displayDateTime();"

LINK NUMBER 279
Not enough lines

LINK NUMBER 280
Error fetching diff

LINK NUMBER 281
Error fetching diff

LINK NUMBER 282
Error fetching diff

LINK NUMBER 283

File path: src/musiclist.js
"  {
    image: 'evergreen.jpg',
    audio: 'evergrren.mp3',
    name: 'EverGreen',
    artist: 'Mitch',
  },"

LINK NUMBER 284
Too many lines

LINK NUMBER 285
Not enough lines

LINK NUMBER 286

File path: ta_functions.py
"# Importing necessary libraries
from imports import *
import candlesticks as cs

# Fetching historical data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Adding technical indicators
def add_technical_indicators (df):
    # Optimization: Compute rolling statistics in one go where possible to avoid repeated calls
    close_prices = df['Close']
    
    # SMA
    df['SMA_14'] = close_prices.rolling(window=14).mean()
    df['SMA_50'] = close_prices.rolling(window=50).mean()
    df['SMA_200'] = close_prices.rolling(window=200).mean()

    # EMA
    df['EMA_50'] = close_prices.ewm(span=50, adjust=False).mean()
    df['EMA_200'] = close_prices.ewm(span=200, adjust=False).mean()

    # RSI (Combined gain and loss into a single calculation to reduce repeated operations)
    delta = close_prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # On-balance Volume
    df['OBV'] = calculate_obv(df)

    # Money Flow Index
    df['MFI'] = calculate_mfi(df)

    # Bollinger Bands
    rolling_20 = close_prices.rolling(window=20)
    df['BB_Middle'] = rolling_20.mean()
    rolling_std = rolling_20.std()
    df['BB_Upper'] = df['BB_Middle'] + 2 * rolling_std
    df['BB_Lower'] = df['BB_Middle'] - 2 * rolling_std

    # Momentum and ROC
    df['Momentum_10'] = close_prices - close_prices.shift(10)
    df['Momentum_30'] = close_prices - close_prices.shift(14)
    df['ROC_10'] = close_prices.pct_change(periods=10) * 100
    df['ROC_30'] = close_prices.pct_change(periods=14) * 100

    # ATR (Optimized true range calculation)
    df['High_Low'] = df['High'] - df['Low']
    df['High_Close'] = (df['High'] - df['Close'].shift(1)).abs()
    df['Low_Close'] = (df['Low'] - df['Close'].shift(1)).abs()

    df['True_Range'] = pd.concat([df['High_Low'], df['High_Close'], df['Low_Close']], axis=1).max(axis=1)
    df['ATR'] = df['True_Range'].rolling(window=14).mean()

    # Drop rows with NaN values resulting from rolling calculations
    df.dropna(inplace=True)

    return df

def calculate_rsi(df, window=14):
    close_prices = df['Close']
    # Calculate price changes (delta)
    delta = close_prices.diff()

    # Separate positive gains (where the price went up) and negative losses (where the price went down)
    gain = delta.clip(lower=0)  # gains (positive deltas)
    loss = -delta.clip(upper=0) # losses (negative deltas)

    # Calculate the rolling mean of gains and losses
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi

def calculate_obv(data):
    obv = [0]  # Initialize OBV with 0
    for i in range(1, len(data)):
        if data['Close'].iloc[i] > data['Close'].iloc[i-1]:
            obv.append(obv[-1] + data['Volume'].iloc[i])
        elif data['Close'].iloc[i] < data['Close'].iloc[i-1]:
            obv.append(obv[-1] - data['Volume'].iloc[i])
        else:
            obv.append(obv[-1])  # No change if close prices are equal

    return obv

def calculate_mfi(data, period=14):
    required_columns = ['High', 'Low', 'Close', 'Volume']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f""DataFrame must contain the following columns: {required_columns}"")

    data['TP'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['RMF'] = data['TP'] * data['Volume']
    data['TP_diff'] = data['TP'].diff()

    data['Positive_MF'] = np.where(data['TP_diff'] > 0, data['RMF'], 0)
    data['Negative_MF'] = np.where(data['TP_diff'] < 0, data['RMF'], 0)

    # Step 4: Calculate the rolling sums of Positive and Negative Money Flow
    data['Positive_MF_sum'] = data['Positive_MF'].rolling(window=period).sum()
    data['Negative_MF_sum'] = data['Negative_MF'].rolling(window=period).sum()

    data['MFR'] = data['Positive_MF_sum'] / data['Negative_MF_sum']
    data['MFI'] = 100 - (100 / (1 + data['MFR']))
    data['MFI'] = np.where(data['Negative_MF_sum'] == 0, 100, data['MFI'])

    return data['MFI']

# Preparing the data for Machine Learning
def prepare_ml_data(df):
    # Include candlestick pattern features and new indicators
    features = ['SMA_14', 'SMA_50', 'SMA_200', 'EMA_50', 'EMA_200', 'RSI', 'BB_Middle', 'BB_Upper', 'BB_Lower',
                'Momentum_10', 'Momentum_30', 'ROC_10', 'ROC_30', 'Bullish_Engulfing', 'Doji', 'Hammer', 
                'Hanging_Man', 'Morning_Star', 'Evening_Star', 'Shooting_Star', 'Three_White_Soldiers', 
                'Three_Black_Crows', 'Volume', 'ATR', 'MFI']
    
    df = df.dropna()
    X = df[features]
    y = df['Close']  # Target variable
    
    scaler = MinMaxScaler() #StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler

# Building the Random Forest Model
def train_model(X_train, y_train, nest=1000, md=6):
    model = RandomForestRegressor(n_estimators=nest, random_state=42,
                                  max_depth=md)
    model.fit(X_train, y_train)
    return model

def train_booster(X_train, y_train, nest=1000, lr=0.001, md=6, ss=0.8,
                             ra=0.1, rl=1):
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=nest, 
                             learning_rate=lr, max_depth=md, subsample=ss,
                             reg_alpha=ra, reg_lambda=rl)
    model.fit(X_train, y_train)
    return model

# Evaluate the model performance
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    rmse = round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)
    r2 = round(r2_score(y_test, y_pred), 3)
    
    print(f""Root Mean Squared Error: {rmse}"")
    print(f""R^2 Score: {r2}"")

def generate_signal(predicted_prices, current_price, df):
    # Get the last available values of the technical indicators from the dataframe
    last_row = df.iloc[-1]
    
    # Technical indicator thresholds
    sma_50_threshold = 0.02 
    sma_200_threshold = 0.02
    ema_50_threshold = 0.02
    ema_200_threshold = 0.02
    rsi_threshold_buy = 35
    rsi_threshold_sell = 65
    bb_threshold = 0.02

    # Extract the latest values of the technical indicators
    sma_50 = last_row['SMA_50']
    sma_200 = last_row['SMA_200']
    ema_50 = last_row['EMA_50']
    ema_200 = last_row['EMA_200']
    rsi = last_row['RSI']
    bb_lower = last_row['BB_Lower']
    bb_upper = last_row['BB_Upper']

    # Initialize signals
    buy_signal = False
    sell_signal = False
    
    # Check if current price is above the SMA and EMA thresholds
    if current_price > (1 + sma_50_threshold) * sma_50:
        buy_signal = True
    if current_price > (1 + sma_200_threshold) * sma_200:
        buy_signal = True
    if current_price > (1 + ema_50_threshold) * ema_50:
        buy_signal = True
    if current_price > (1 + ema_200_threshold) * ema_200:
        buy_signal = True

    # Check RSI for buy/sell signals
    if rsi < rsi_threshold_buy:
        buy_signal = True
    if rsi > rsi_threshold_sell:
        sell_signal = True

    # Check if current price is below the Bollinger Bands Lower Band
    if current_price < (1 - bb_threshold) * bb_lower:
        buy_signal = True
    if current_price > (1 + bb_threshold) * bb_upper:
        sell_signal = True

    # Generate final signal
    if buy_signal and not sell_signal:
        return ""BUY""
    elif sell_signal and not buy_signal:
        return ""SELL""
    else:
        return ""HODL / SIDELINES""


# Plotting the stock price and technical indicators
def plot_technical_indicators(df, ticker = '   ' ):
    plt.figure(figsize=(14, 10))
    
    # Close Price and Moving Averages
    plt.subplot(3, 1, 1)
    plt.plot(df['Close'], label='Close Price', alpha=0.6)

    plt.plot(df['EMA_50'], color = 'red', label='50-day EMA', alpha=0.6)
    plt.plot(df['EMA_200'], color = 'magenta', label='200-day EMA', alpha=0.6)
    
    plt.title(f'{ticker} Price and Moving Averages')
    
    plt.legend()
    #plt.yscale('log')
    plt.minorticks_on()
    plt.tick_params(which='both', axis='y', direction='in', length=6)
    plt.tick_params(which='minor', axis='y', direction='in', length=4)
    plt.grid(alpha=0.5)

    # OBV
    plt.subplot(3, 1, 2)
    plt.plot(df['OBV'], label='OBV', color='gray', alpha=0.5)
    plt.title('On Balance Volume')
    plt.legend()
    plt.grid(alpha=0.5)
    
    # RSI
    plt.subplot(3, 1, 3)
    plt.plot(df['RSI'], label='RSI', color='gray', alpha=0.5)
    plt.title('Relative Strength Index (RSI)')
    plt.axhline(70, color='red', linestyle='--', alpha=0.5)
    plt.axhline(30, color='green', linestyle='--', alpha=0.5)
    plt.legend()

    plt.tight_layout()
    plt.grid(alpha=0.5)
    plt.show()
    
#### PREDICT PRICES #####
def predict_prices(model, recent_data, scaler, num_days=5, window_size=30):
    # Use the same features during prediction
    features = ['SMA_14', 'SMA_50', 'SMA_200', 'EMA_50', 'EMA_200', 'RSI', 'BB_Middle', 'BB_Upper', 'BB_Lower',
                'Momentum_10', 'Momentum_30', 'ROC_10', 'ROC_30', 'Bullish_Engulfing', 'Doji', 'Hammer', 
                'Hanging_Man', 'Morning_Star', 'Evening_Star', 'Shooting_Star', 'Three_White_Soldiers', 
                'Three_Black_Crows', 'Volume', 'ATR', 'MFI']
    
    last_data = recent_data.copy()  # Copy the whole dataframe to modify
    
    predicted_prices = []  # List to store predicted values

    for i in range(num_days):
        # Use a rolling window of size 'window_size' from actual data (historical data)
        sliced = last_data.iloc[-window_size:].copy()
        
        # Ensure all technical indicators are calculated before prediction
        sliced['SMA_14'] = sliced['Close'].rolling(window=14, min_periods=1).mean()
        sliced['SMA_50'] = sliced['Close'].rolling(window=50, min_periods=1).mean()
        sliced['SMA_200'] = sliced['Close'].rolling(window=200, min_periods=1).mean()
        sliced['EMA_50'] = sliced['Close'].ewm(span=50, adjust=False).mean()
        sliced['EMA_200'] = sliced['Close'].ewm(span=200, adjust=False).mean()
        
        sliced['RSI'] = calculate_rsi(sliced)
        sliced['MFI'] = calculate_mfi(sliced)
        
        sliced['BB_Middle'] = sliced['Close'].rolling(window=20, min_periods=1).mean()
        sliced['BB_Upper'] = sliced['BB_Middle'] + 2 * sliced['Close'].rolling(window=20, min_periods=1).std()
        sliced['BB_Lower'] = sliced['BB_Middle'] - 2 * sliced['Close'].rolling(window=20, min_periods=1).std()
        
        # Candlestick patterns (use actual data for pattern detection)
        sliced = add_candlestickpatterns(sliced)

        # Extract features for the current prediction
        inData = sliced[features].iloc[-1:]
        
        # Scale features
        inData_scaled = scaler.transform(inData)
        
        # Predict the price for the next day using the model
        predicted_price = model.predict(inData_scaled)
        rounded_price = round(predicted_price[0], 4)
        predicted_prices.append(rounded_price)  # Store the scalar value
        
        # Update the 'Close' price with the predicted value for the next business day
        next_index = pd.bdate_range(last_data.index[-1], periods=2)[-1]  # Next business day
        last_data.loc[next_index] = np.nan  # Add the new row
        last_data.at[next_index, 'Close'] = rounded_price  # Only update 'Close' with predicted value
        
        # Append a new row with the predicted 'Close' value only
        new_row = pd.DataFrame({
            'Close': [rounded_price],
            'Date': [next_index]
        }).set_index('Date')
        
        # Append the new row to the dataframe
        last_data = pd.concat([last_data, new_row])
    
    return predicted_prices

    
def add_candlestickpatterns(df):
    # Ensure df is a copy, not a view, to avoid the SettingWithCopyWarning
    df = df.copy()

    # Detect candlestick patterns and add to dataframe
    df['Bullish_Engulfing'] = cs.detect_bullish_engulfing(df)
    df['Doji'] = cs.detect_doji(df)
    df['Hammer'] = cs.detect_hammer(df)
    df['Hanging_Man'] = cs.detect_hanging_man(df)
    df['Morning_Star'] = cs.detect_morning_star(df)
    df['Evening_Star'] = cs.detect_evening_star(df)
    df['Shooting_Star'] = cs.detect_shooting_star(df)
    df['Three_White_Soldiers'] = cs.detect_three_white_soldiers(df)
    df['Three_Black_Crows'] = cs.detect_three_black_crows(df)

    return df

def plot_with_predictions(stock_df, predicted_prices, ticker='NONE', num_days=5):
    # Get the last month of historical data
    
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    end_date = stock_df.index[-1]
    start_date = end_date - pd.DateOffset(months=1)
    one_month_data = stock_df.loc[start_date:end_date]
    
    # Get the last known closing price
    last_close = one_month_data['Close'].iloc[-1]
    
    # Generate dates for the predicted prices
    prediction_dates = pd.date_range(start=end_date + pd.DateOffset(days=1), periods=num_days)
    
    # Create a DataFrame for predicted prices with the last known close included
    predictions_df = pd.DataFrame({
        'Date': [end_date] + list(prediction_dates),
        'Predicted_Price': [last_close] + predicted_prices
    }).set_index('Date')
    
    # Combine historical data with predicted prices
    combined_df = pd.concat([one_month_data[['Close']], predictions_df])
    
    # Plot historical closing prices and predicted prices
    plt.figure(figsize=(14, 7))
    
    # Plot historical closing prices
    plt.plot(one_month_data.index, one_month_data['Close'], label='Historical Close Prices', 
             color='blue', alpha=0.7)
    
    # Plot predicted prices
    plt.plot(predictions_df.index, predictions_df['Predicted_Price'], label='Predicted Prices', 
             color='blue', linestyle='--', marker='o', alpha=0.4)
    
    # Formatting the plot
    plt.title(f'{ticker} {current_date} - Closing Prices and Next {num_days} Days Predictions')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Calculate statistics
    predicted_max = np.max(predicted_prices)
    predicted_min = np.min(predicted_prices)
    predicted_change = ((predicted_prices[-1] - last_close) / last_close) * 100

    # Add text annotation
    textstr = (f'Predicted % Change: {predicted_change:.2f}%\n'
               f'Min Price: ${predicted_min:.2f}\n'
               f'Max Price: ${predicted_max:.2f}')

    plt.text(0.5, 0.5, ticker, transform=plt.gca().transAxes, 
             fontsize=100, color='grey', alpha=0.1,  # Adjust transparency here
             horizontalalignment='center', verticalalignment='center',
             rotation=45, weight='bold', style='italic')
    
    plt.text(0.95, 0.05, textstr, transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='bottom', horizontalalignment='right',
             bbox=dict(boxstyle='round', alpha=0.2, facecolor='white'))

    path = r'C:\Users\Farrukh\jupyter-Notebooks\STOCKS\predictions'
    fname = f'{current_date}_{ticker}.png'
    fpath = os.path.join(path, fname)
    plt.savefig(fpath, bbox_inches='tight')
    plt.show()
    plt.close()"

LINK NUMBER 287
Error fetching diff

LINK NUMBER 288
Error fetching diff

LINK NUMBER 289
Not enough lines

LINK NUMBER 290

File path: 16.Recursion.js
"// console.log(""In-order Traversal:"");
// inOrderTraversal(root); // Output: 4 2 5 1 6 3 7

// task 10
{
  class TreeNode {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }

  function calculateDepth(node) {
    // Base case: If the node is null, return 0
    if (node === null) {
      return 0;
    }

    // Recursive case: Calculate the depth of left and right subtrees
    const leftDepth = calculateDepth(node.left);
    const rightDepth = calculateDepth(node.right);

    // The depth of the current node is the maximum of leftDepth and rightDepth plus 1
    return Math.max(leftDepth, rightDepth) + 1;
  }

  // Test the function with a sample binary tree
  const root = new TreeNode(1);
  root.left = new TreeNode(2);
  root.right = new TreeNode(3);
  root.left.left = new TreeNode(4);
  root.left.right = new TreeNode(5);
  root.right.left = new TreeNode(6);
  root.right.right = new TreeNode(7);

//   console.log(""Depth of the tree:"", calculateDepth(root)); // Output: 3

  // Another test case with an unbalanced tree
  const unbalancedRoot = new TreeNode(1);
  unbalancedRoot.left = new TreeNode(2);
  unbalancedRoot.left.left = new TreeNode(3);

//   console.log(""Depth of the unbalanced tree:"", calculateDepth(unbalancedRoot)); // Output: 3
}"

LINK NUMBER 291
Not enough lines

LINK NUMBER 292
Not enough lines

LINK NUMBER 293
Error fetching diff

LINK NUMBER 294
Error fetching diff

LINK NUMBER 295
Error fetching diff

LINK NUMBER 296

File path: Basic Data Structure/Sets/Sets.js
"# Graph Data Structure: A Theoretical Overview

## Introduction

A **graph** is a collection of nodes (also called **vertices**) and edges, which connect pairs of nodes. Graphs can represent various real-world systems like social networks, transportation routes, and web page links.

Graphs are either **directed** or **undirected**:

-   In **directed graphs**, edges have a direction, indicating the relationship flows from one node to another.
-   In **undirected graphs**, edges represent a two-way relationship, meaning the connection between the nodes is mutual.

```
{
  +---+-----------+
| V | Neighbors |
+---+-----------+
| A |   B, C   |
| B |   A, D   |
| C |     A     |
| D |     B     |
+---+-----------+
}
```

## Definition

A graph can be defined as:

-   A set of vertices (nodes).
-   A set of edges (connections) between the vertices.

Graphs are often represented as:

-   **Adjacency List**: Where each node has a list of nodes it's connected to.
-   **Adjacency Matrix**: A 2D array indicating whether there is a direct connection between pairs of nodes.

## Common Use Cases

Graphs are used in many applications, such as:

-   **Social Networks**: Representing users as nodes and their connections as edges.
-   **Maps and Routes**: Cities as nodes, and roads as edges between them.
-   **Recommendation Systems**: Connecting users to products based on behavior.

## Graph Operations

Some common graph operations include:

-   **Add Vertex**: Add a new node to the graph.
-   **Add Edge**: Create a connection between two nodes.
-   **Remove Vertex**: Remove a node and its associated edges.
-   **Remove Edge**: Delete a connection between two nodes.
-   **Search**: Find a path between two nodes (using algorithms like BFS, DFS).

### Example Methods

Below are some typical methods associated with a graph:

-   **`addVertex(vertex)`**: Adds a new vertex to the graph.
-   **`addEdge(vertex1, vertex2)`**: Creates an edge between two vertices.
-   **`removeVertex(vertex)`**: Removes a vertex from the graph.
-   **`removeEdge(vertex1, vertex2)`**: Removes an edge between two vertices.
-   **`hasEdge(vertex1, vertex2)`**: Checks if there's an edge between two vertices.

## Conclusion

Graphs are incredibly versatile data structures used in modeling relationships between entities. Whether you need to track connections in a network or design algorithms to traverse structures, graphs are essential tools in computer science and many real-world applications."

LINK NUMBER 297

File path: script.js
"
// Funktion zum Anzeigen des Login-Formulars
function showLoginForm() {
    document.getElementById('loginForm').classList.remove('hidden');  // Zeige das Login-Formular
}

// Funktion zum Überprüfen des Tokens beim Laden der Seite
window.onload = function() {
    if (token) {
        // Versuche, die Ligen mit dem gespeicherten Token abzurufen
        fetchLeagues();
    } else {
        // Zeige das Login-Formular, falls kein Token vorhanden ist
        showLoginForm();
    }
};"

LINK NUMBER 298
Not enough lines

LINK NUMBER 299
Not enough lines

LINK NUMBER 300
Error fetching diff

LINK NUMBER 301
Error fetching diff

LINK NUMBER 302
Error fetching diff

LINK NUMBER 303
Not enough lines

LINK NUMBER 304

File path: surveysApp/models.py
"# Generated by Django 5.1.4 on 2025-01-02 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveysApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('open', 'Open Answer'), ('multiple_choice', 'Multiple Choice')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='openanswer',
            name='questionID',
        ),
        migrations.RemoveField(
            model_name='options',
            name='questionID',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionText', models.CharField(max_length=120)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='surveysApp.question')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='surveysApp.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('selected_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveysApp.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveysApp.question')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveysApp.submission')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='surveysApp.survey'),
        ),
        migrations.DeleteModel(
            name='EmailAnswer',
        ),
        migrations.DeleteModel(
            name='OpenAnswer',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]"

LINK NUMBER 305

File path: CommunicationThread.py
"        from TransmissionThread import TransmissionThread
        from ListeningThread import ListeningThread

        self.taskHandlerThread = taskHandlerThread
        self.acceptedRequestsQueue = AcceptedRequestQueue()
        self.acceptedRequestsQueue.start()"

LINK NUMBER 306
Not enough lines

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

File path: src/adminextract.py
"LOCALE = ""zh""


def i18n_string(strid: str) -> str:
    """"""
    Returns localized strings based on the given string ID.

    Args:
        strid (str): A string identifier for the desired text.

    Returns:
        str: A localized string corresponding to the given ID.
    """"""
    strings = {
        ""en"": {
            ""enter-root-id"": ""Please enter the root node ID:"",
            ""no-root-found"": ""Unable to find root node ID, please ensure the graph contains administrative boundary nodes."",
            ""enter-manual-root-id"": ""Unable to automatically determine the root node ID, please enter manually:"",
            ""invalid-id"": ""The entered ID is invalid, please enter a valid node ID."",
            ""enter-valid-number"": ""Please enter a valid number."",
            ""multiple-root-nodes"": ""Multiple root nodes of the same highest level found, please choose one as the root node:"",
        },
        ""zh"": {
            ""enter-root-id"": ""请输入根节点ID："",
            ""no-root-found"": ""无法找到根节点ID，请确保图中包含行政边界节点。"",
            ""enter-manual-root-id"": ""无法自动确定根节点ID，请手动输入："",
            ""invalid-id"": ""输入的ID无效，请输入有效的节点ID。"",
            ""enter-valid-number"": ""请输入一个有效的数字。"",
            ""multiple-root-nodes"": ""发现多个同等最高级别的节点，请选择一个作为根节点："",
        },
    }
    return strings.get(LOCALE, {}).get(strid, """")


def build_graph(map: Waifu) -> nx.DiGraph:
    """"""
    Constructs a directed graph from map data.

    Each administrative boundary from the map is added as a node, and subarea relationships are added as edges.

    Args:
        map (Waifu): An instance of Waifu containing map data.

    Returns:
        nx.DiGraph: A directed graph representing the administrative hierarchy.
    """"""
    G = nx.DiGraph()
    for id, relation in map.relation_dict.items():
        admin_level = relation.tags.get(""admin_level"")
        name = relation.tags.get(""name"")
        ref = relation.tags.get(""ref"")
        if (
            ""boundary"" in relation.tags
            and relation.tags[""boundary""] == ""administrative""
        ):
            G.add_node(id, admin_level=admin_level, name=name, ref=ref)
            for member in relation.members:
                if (
                    member.role == ""subarea""
                    and member.ref in map.relation_dict
                ):
                    G.add_edge(id, member.ref)
    return G


def graph_to_nested_json(G: nx.DiGraph, root_id: int) -> Dict:
    """"""
    Converts a directed graph to a nested JSON structure starting from a specified root node.

    Args:
        G (nx.DiGraph): The directed graph to convert.
        root_id (int): The ID of the root node from which to start the nesting.

    Returns:
        Dict: A nested dictionary representing the hierarchical structure.
    """"""

    def recurse(node):
        children = list(G.successors(node))
        if not children:
            return {""id"": node, **G.nodes[node]}
        return {
            ""id"": node,
            **G.nodes[node],
            ""subareas"": [recurse(child) for child in children],
        }

    return recurse(root_id)


def find_root_node_id(G: nx.DiGraph, strategy=""input"") -> int:
    """"""
    Finds the ID of the root node based on the given strategy.

    Args:
        G (nx.DiGraph): The directed graph from which to find the root node.
        strategy (str): The strategy to use for finding the root node. Options are ""input"", ""highest"", ""auto"".

    Returns:
        int: The ID of the found root node.

    Raises:
        ValueError: If no root node can be found based on the given strategy.
    """"""
    if strategy == ""input"":
        return int(input(i18n_string(""enter-root-id"")))

    min_level = float(""inf"")
    root_candidates = []
    for node, data in G.nodes(data=True):
        admin_level = data.get(""admin_level"")
        if admin_level is None:
            continue
        try:
            level = int(admin_level)
            if level < min_level:
                min_level = level
                root_candidates = [(node, data)]
            elif level == min_level:
                root_candidates.append((node, data))
        except ValueError:
            continue

    if not root_candidates:
        if strategy == ""highest"":
            raise ValueError(i18n_string(""no-root-found""))
        elif strategy == ""auto"":
            return int(input(i18n_string(""enter-manual-root-id"")))

    if len(root_candidates) > 1:
        print(i18n_string(""multiple-root-nodes""))
        for idx, (node, data) in enumerate(root_candidates):
            print(
                f""({idx + 1}). ID: [{node}], \""admin_level\"": {data['admin_level']}, \""name\"": {data.get('name')}, \""ref\"": {data.get('ref')}""
            )"

LINK NUMBER 313
Not enough lines

LINK NUMBER 314
Error fetching diff

LINK NUMBER 315
Error fetching diff

LINK NUMBER 316
Error fetching diff

LINK NUMBER 317
Not enough lines

LINK NUMBER 318
Not enough lines

LINK NUMBER 319

File path: simple_raster.py
"    dcc.Store(id='data-store'),  # Store for holding uploaded data
    dbc.Row([
        dbc.Col(dcc.Upload(
            id='upload-spike-times',
            children=html.Div(['Spike times', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4),
        dbc.Col(dcc.Upload(
            id='upload-spike-clusters',
            children=html.Div(['Spike clusters', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4),
        dbc.Col(dcc.Upload(
            id='upload-behavior',
            children=html.Div(['Behavior', html.A('')]),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
            multiple=False
        ), width=4)
    ]),"

LINK NUMBER 320
Not enough lines

LINK NUMBER 321
Error fetching diff

LINK NUMBER 322
Error fetching diff

LINK NUMBER 323
Error fetching diff

LINK NUMBER 324
Not enough lines

LINK NUMBER 325
Not enough lines

LINK NUMBER 326

File path: ask.py
"async def run(prompt):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        url = ""https://chatgpt.com""
        await page.goto(url)
        await page.wait_for_selector(""textarea#prompt-textarea"")
        textarea = await page.locator(""textarea#prompt-textarea"")
        button = await page.locator(""button.absolute.bottom-1\\.5"")"

LINK NUMBER 327
Not enough lines

LINK NUMBER 328
Error fetching diff

LINK NUMBER 329
Error fetching diff

LINK NUMBER 330
Error fetching diff

LINK NUMBER 331
Not enough lines

LINK NUMBER 332
Not enough lines

LINK NUMBER 333
Too many lines

LINK NUMBER 334

File path: ASE_functions.py
"        """"""
        Performs wavelength to angle calibration over a range of temperatures.

        This method calibrates the rotation stage by adjusting the DFB laser temperature,
        measuring the power at different angles, and logging the data.

        Parameters:
        -----------
        dfb : object
            The DFB laser object whose temperature (and therefore wavelength) is controlled.
        powermeter : object
            The powermeter object to measure power.
        temp_list : list of float
            List of temperatures to use for calibration.
        calibration_bounds : tuple
            Bounds for the calibration calculations.
        startangle : float
            The starting angle for the calibration scan.
        endangle : float
            The ending angle for the calibration scan.

        Behavior:
        ---------
        - If `self.ac_begincal` is True:
            - Sets up and moves the stage to the start angle.
            - Waits for the stage to reach the start angle and stops.
            - Sets `self.ac_begincal` to False after initialization.
        - If `self.initcal_bool` is True:
            - Initializes calibration in either low-to-high or high-to-low direction.
            - Scans the stage to the appropriate angle.
            - Emits progress updates.
        - Logs the current time, wavelength, power, and angle to the CSV file while the stage is scanned.
        - Toggles calibration direction and updates progress.
        - When all temperatures are processed, stops the calibration, calculates results, and emits completion signals.

        Example:
        --------
        >>> obj.wavelength_to_angle_calibration(dfb, powermeter, [25.0, 30.0, 35.0], (400, 700), 0, 180)
        """"""
        def handle_initcal(lowtohi, temp):
            self.init_wavelength_to_angle_calibration(dfb, temp, lowtohi)
            self.stage.scan_to_angle(endangle if lowtohi else startangle, 0.5)
            progress = (self.autocal_iterator + (0.5 if lowtohi else 1)) * 100 / len(temp_list)
            self.autocalibration_progress.emit(int(progress))
            self.initcal_bool = False
"

LINK NUMBER 335
Error fetching diff

LINK NUMBER 336
Error fetching diff

LINK NUMBER 337
Error fetching diff

LINK NUMBER 338

File path: restful-api/task_02_requests.py
"                'body': post['body']
            })
        
        with open('posts.csv', 'w', newline='') as cf:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(cf, fieldnames=fieldnames)
            "

LINK NUMBER 339
Not enough lines

LINK NUMBER 340
Not enough lines

LINK NUMBER 341

File path: python-data_structures/2-replace_in_list.py
"#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)"

LINK NUMBER 342
Error fetching diff

LINK NUMBER 343
Error fetching diff

LINK NUMBER 344
Error fetching diff

LINK NUMBER 345

File path: tests/test_app_contributors_performance.py
"import io

import pytest

from diffinsights_web.datastore.timeline import get_timeline_data

param = pytest.importorskip(""param"")
pn = pytest.importorskip(""panel"")

from diffinsights_web.apps.contributors import template, dataset_dir, timeline_data_store


@pytest.fixture
def app():
    return template

def test_contributors_run_performance(app, benchmark):
    #for k, v in app.param.objects().items():
    #    print(f""{app.__class__.name}.{k} = {repr(v.default)} ({type(v)})"")

    #print(template)
    #for e in template.sidebar:
    #    print(e)
    #print(template.sidebar[0][0])
    #print(template.sidebar[0][0].value)

    ## Failed attempt 1.
    #     @pn.cache
    #     def get_timeline_df(timeline_data: dict, repo: str) -> pd.DataFrame:
    # >       init_df = pd.DataFrame.from_records(timeline_data[repo])
    # E       KeyError: 'hellogitworld'
    #with pn.io.hold():
    #    template.sidebar[0][1].value = 'qtile'
    #    template.sidebar[0][0].value = str(dataset_dir.joinpath('qtile.timeline.purpose-to-type.json'))

    ## Failed attempt 2.
    #     @pn.cache
    #     def get_timeline_df(timeline_data: dict, repo: str) -> pd.DataFrame:
    # >       init_df = pd.DataFrame.from_records(timeline_data[repo])
    # E       KeyError: 'hellogitworld'
    #with param.parameterized.batch_call_watchers(timeline_data_store):
    #    timeline_data_store.select_file_widget.value = str(dataset_dir.joinpath('qtile.timeline.purpose-to-type.json'))
    #    timeline_data_store.select_repo_widget.value = 'qtile'

    ## Failed attempt 3.
    # AttributeError: The value of a derived expression cannot be set.
    #timeline_data_store.timeline_data_rx.rx.value = \
    #    get_timeline_data(dataset_dir.joinpath('qtile.timeline.purpose-to-type.json'))

    ## Failed attempt 4.
    # KeyError: 'hellogitworld'
    #timeline_data_store.select_file_widget.param.update(
    #    value=str(dataset_dir.joinpath('qtile.timeline.purpose-to-type.json')),
    #)

    #print(template.sidebar[0][0].value)

    # Benchmark the time it takes to render the Panel app
    def render_app():
        buffer = io.StringIO()
        pn.state.clear_caches()
        pn.io.save.save(app, filename=buffer, embed=True)
        return buffer.getvalue()

    # Run the benchmark
    result = benchmark(render_app)

    # Optional: Add an assertion for maximum acceptable render time (in seconds)
    assert result is not None, ""App rendering failed"""

LINK NUMBER 346
Not enough lines

LINK NUMBER 347
Not enough lines

LINK NUMBER 348

File path: Mash.py
"#Ryan Pool
#9.11.24


import random

def eliminateOptions(options, count):
    # While there is more than one option in the list, keep eliminating
    index = 0
    while len(options) > 1:
        # Calculate the index of the option to eliminate using the count
        index = (index + count - 1) % len(options)
        eliminated = options.pop(index)
        print(f""Eliminated: {eliminated}"")


def mashGame():
    # Default MASH options for housing
    mashOptions = [""Mansion"", ""Apartment"", ""Shack"", ""House""]

    # Collecting user input for different categories
    print(""Welcome to the MASH Game!"")

    # Asking for custom options in categories
    jobs = [input(f""Enter job option {i + 1}: "") for i in range(4)]
    spouses = [input(f""Enter spouse name option {i + 1}: "") for i in range(4)]
    cars = [input(f""Enter car option {i + 1}: "") for i in range(4)]
    money = [input(f""Enter amount of money option {i + 1}: "") for i in range(4)]
    kids = [input(f""Enter a number of kids option {i + 1}: "") for i in range(4)]

    # Add the default MASH housing options to the game
    categories = {
        ""House"": mashOptions,
        ""Job"": jobs,
        ""Spouse"": spouses,
        ""Car"": cars,
        ""Money"": money,
        ""Kids"": kids
    }

    # Ask the user for a number to use for elimination
    count = int(input(""\nPick a number for the elimination process: ""))

    print(""\nEliminating options...\n"")

    # Eliminate options in each category based on the user's number
    for category, options in categories.items():
        print(f""\nEliminating from {category}:"")
        eliminateOptions(options, count)

    # Final result after elimination
    house = mashOptions[0]
    job = jobs[0]
    spouse = spouses[0]
    car = cars[0]
    money = money[0]
    numKids = kids[0]

    # Display the final result
    print(""\nYour MASH results are in:"")
    print(f""You will live in a {house}."")
    print(f""You will work as a {job}."")
    print(f""You will marry {spouse}."")
    print(f""You will drive a {car}."")
    print(f""You will have {money} money."")
    print(f""You will have {numKids} kids."")


# Run the game
mashGame()"

LINK NUMBER 349
Error fetching diff

LINK NUMBER 350
Error fetching diff

LINK NUMBER 351
Error fetching diff

LINK NUMBER 352

File path: binary-search-tree.test.js
"// I had to do these with the help of chatGPT. 

class Node {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class BinarySearchTree {
  constructor(root = null) {
    this.root = root;
  }

  /** insert(val): insert a new node into the BST with value val.
   * Returns the tree. Uses iteration. */

  
  insert(val) {
    if(!this.root) {
      this.root = new Node(val);
      return this
  }
  
  let currentNode = this.root;
  while (true) {
    if(val < currentNode.val) {
      if(!currentNode.left) {
        currentNode.left = new Node(val);
        return this;
      }
      currentNode = currentNode.left;
    } else if (val > currentNode.val) {
      if (!currentNode.right) {
        currentNode.right = new Node(val);
        return this;
      }
      currentNode = currentNode.right;
    } else {

      return this
    }
  }

  }

  /** insertRecursively(val): insert a new node into the BST with value val.
   * Returns the tree. Uses recursion. */

  
  insertRecursively(val, currentNode = this.root) {
    if (!currentNode) {
      this.root = new Node(val);
      return this;
    }

    if (val < currentNode.val) {
      if (!currentNode.left) {
        currentNode.left = new Node(val);
      } else {
        this.insert(val, currentNode.left);
      }
    } else if (val > currentNode.val) {
      if (!currentNode.right) {
        currentNode.right = new Node(val);
      } else {
        this.insert(val, currentNode.right);
      }
    }
    // If val is equal to currentNode.val, handle as needed
    // Here, we'll avoid duplicates, but you can change this behavior if needed
    return this;
  }

  /** find(val): search the tree for a node with value val.
   * return the node, if found; else undefined. Uses iteration. */

  
  find(val) {
    let currentNode = this.root;

    if(!currentNode) {
      return null
    }
    while(currentNode) {
      if( currentNode.val === val ) {
        return currentNode
      } else if (val < currentNode.val) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right
      }
    }
    return undefined;
  }

  /** findRecursively(val): search the tree for a node with value val.
   * return the node, if found; else undefined. Uses recursion. */

  findRecursively(val, currentNode = this.root) {
    if (!currentNode) {
        return undefined; 
    }

    if (val === currentNode.val) {
        return currentNode; 
    }

    if (val < currentNode.val) {
        return this.find(val, currentNode.left); 
    } else {
        return this.find(val, currentNode.right); 
    }
}


  /** dfsPreOrder(): Traverse the array using pre-order DFS.
   * Return an array of visited nodes. */

  dfsPreOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack = [];
    let currentNode = this.root;

    while (currentNode || stack.length > 0) {
        if (currentNode) {
            visited.push(currentNode.val);
            

            if (currentNode.right) {
                stack.push(currentNode.right);
            }


            currentNode = currentNode.left;
        } else {

            currentNode = stack.pop();
        }
    }

    return visited;
}


  /** dfsInOrder(): Traverse the array using in-order DFS.
   * Return an array of visited nodes. */

  dfsInOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack = [];
    let currentNode = this.root;

    while (currentNode || stack.length > 0) {
        if (currentNode) {

            stack.push(currentNode);
            currentNode = currentNode.left;
        } else {

            currentNode = stack.pop();
            visited.push(currentNode.val);
            currentNode = currentNode.right;
        }
    }

    return visited;
}


  /** dfsPostOrder(): Traverse the array using post-order DFS.
   * Return an array of visited nodes. */

  dfsPostOrder() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const stack1 = [];
    const stack2 = [];
    let currentNode = this.root;

    stack1.push(currentNode);

    while (stack1.length > 0) {
        currentNode = stack1.pop();
        stack2.push(currentNode);

        if (currentNode.left) {
            stack1.push(currentNode.left);
        }

        if (currentNode.right) {
            stack1.push(currentNode.right);
        }
    }

    while (stack2.length > 0) {
        visited.push(stack2.pop().val);
    }

    return visited;
}


  /** bfs(): Traverse the array using BFS.
   * Return an array of visited nodes. */

  bfs() {
    if (!this.root) {
        return [];
    }

    const visited = [];
    const queue = [];
    queue.push(this.root);

    while (queue.length > 0) {
        const currentNode = queue.shift(); // Dequeue
        visited.push(currentNode.val);

        if (currentNode.left) {
            queue.push(currentNode.left); // Enqueue left child
        }

        if (currentNode.right) {
            queue.push(currentNode.right); // Enqueue right child
        }
    }

    return visited;
}


  /** Further Study!
   * remove(val): Removes a node in the BST with the value val.
   * Returns the removed node. */

  remove(val) {

  }

  /** Further Study!
   * isBalanced(): Returns true if the BST is balanced, false otherwise. */

  isBalanced() {

  }

  /** Further Study!
   * findSecondHighest(): Find the second highest value in the BST, if it exists.
   * Otherwise return undefined. */

  findSecondHighest() {
    
  }
}

module.exports = BinarySearchTree;"

LINK NUMBER 353
Not enough lines

LINK NUMBER 354
Not enough lines

LINK NUMBER 355
Not enough lines

LINK NUMBER 356
Error fetching diff

LINK NUMBER 357
Error fetching diff

LINK NUMBER 358
Error fetching diff

LINK NUMBER 359

File path: src/components/AddWhisky.js
"// src/components/AddWhisky.js
import React, { useState } from 'react';
import { addWhisky } from '../firebase';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const AddWhisky = () => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [distillery, setDistillery] = useState('');
  const [type, setType] = useState('');
  const [region, setRegion] = useState('');


  const handleSubmit = () => {
    const newWhisky = { name, age: parseInt(age), distillery, type, region };
    addWhisky(newWhisky);
    setName('');
    setAge('');
    setDistillery('');
    setType('');
    setRegion('');
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
      <Typography variant=""h4"" gutterBottom>
        Add New Whisky
      </Typography>
      <TextField label=""Name"" value={name} onChange={(e) => setName(e.target.value)} />
      <TextField label=""Alter"" type=""number"" value={age} onChange={(e) => setAge(e.target.value)} />
      <TextField label=""Destillerie"" value={distillery} onChange={(e) => setDistillery(e.target.value)} />
      <TextField label=""Typ"" value={type} onChange={(e) => setType(e.target.value)} />
      <TextField label=""Region"" value={region} onChange={(e) => setRegion(e.target.value)} />
      <Button variant=""contained"" color=""primary"" onClick={handleSubmit}>Add Whisky</Button>
    </Box>
  );
};

export default AddWhisky;"

LINK NUMBER 360
Not enough lines

LINK NUMBER 361
Not enough lines

LINK NUMBER 362
Error fetching diff

LINK NUMBER 363
Error fetching diff

LINK NUMBER 364
Error fetching diff

LINK NUMBER 365
Error fetching diff

LINK NUMBER 366
Not enough lines

LINK NUMBER 367

File path: app/_types.ts
"export type TimerConfig = {
  workMinutes: number;
  breakMinutes: number;
  numberOfRounds: number;
  autoStartBreak: boolean;
  autoStartWork: boolean;
};

export type TimerSound = {
  name: string;
  file: string;
  label: string;
};"

LINK NUMBER 368

File path: vmanager.py
"import sqlite3
import re

def insert_markdown_into_db(markdown_file, db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into sections based on headings
    sections = re.split(r'# ', content)[1:]

    for section in sections:
        lines = section.split('\n')
        word = lines[0].strip()
        meanings = [line.strip('- ').strip() for line in lines[1:] if line.strip()]

        for meaning in meanings:
            cursor.execute('INSERT INTO vocabulary (word, meaning) VALUES (?, ?)', (word, meaning))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f'Successfully inserted data from {markdown_file} into {db_file}')

# Usage
insert_markdown_into_db('vocabulary.md', 'vocabulary.db')"

LINK NUMBER 369
Not enough lines

LINK NUMBER 370
Error fetching diff

LINK NUMBER 371
Error fetching diff

LINK NUMBER 372
Error fetching diff

LINK NUMBER 373
Not enough lines

LINK NUMBER 374
Not enough lines

LINK NUMBER 375
Not enough lines

LINK NUMBER 376

File path: index.js
"const formChrono = document.querySelector(""form"");
const inputChrono = document.querySelector(""input"");
const renderChrono = document.querySelector(""h2"");

formChrono.addEventListener(""submit"", (e) => {
  e.preventDefault();
  inputChrono.value = """";
  if (inputChrono.value <= 0) {
      return alert(""Veuillez utiliser minimum le chiffre 1 !"");
    }
    playChrono(inputChrono.value);
});

function playChrono(value) {
  let minutes = parseInt(value);
  let seconds = 0;

  const intervalId = setInterval(() => {
    if (minutes === 0 && seconds === 0) {
      clearInterval(intervalId);
      return alert(""finish !"");
    } else if (seconds === 0) {
      minutes -= 1;
      seconds = 59;
    } else {
      seconds -= 1;
    }

    renderChrono.textContent = `${minutes} : ${
      seconds < 10 ? ""0"" + seconds : seconds
    }`;
  }, 1000);
}"

LINK NUMBER 377
Error fetching diff

LINK NUMBER 378
Error fetching diff

LINK NUMBER 379
Error fetching diff

LINK NUMBER 380
Not enough lines

LINK NUMBER 381
Not enough lines

LINK NUMBER 382
Not enough lines

LINK NUMBER 383
Not enough lines

LINK NUMBER 384
Error fetching diff

LINK NUMBER 385
Error fetching diff

LINK NUMBER 386
Error fetching diff

LINK NUMBER 387
Not enough lines

LINK NUMBER 388
Not enough lines

LINK NUMBER 389
Not enough lines

LINK NUMBER 390

File path: src/q1_memory.py
"    """"""
    Analyzes a JSON file containing tweet data to find the top 10 dates with the most active users.

    Parameters:
    - file_path (str): The path to the JSON file containing tweet data.

    Returns:
    - List[Tuple[datetime.date, str]]: A list of tuples, each containing a date and the username
      of the most active user on that date, sorted by the number of tweets in descending order.
      Only the top 10 dates are included.

    The JSON file should have a structure where each line is a JSON object with at least
    'date' and 'user' keys, where 'user' is an object containing a 'username' key.
    """"""

    # Initialize a dictionary to count tweets per user per date"

LINK NUMBER 391
Error fetching diff

LINK NUMBER 392
Error fetching diff

LINK NUMBER 393
Error fetching diff

LINK NUMBER 394

File path: simple_raster.py
"    dbc.Container(
        dbc.Row(
            [dbc.Col(
                dcc.Upload(
                    id='upload-spike-times',
                    children=html.Div(['Drop SPIKETIMES or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            ),
            dbc.Col(
                dcc.Upload(
                    id='upload-spike-clusters',
                    children=html.Div(['Drop SPIKECLUSTERS or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            ),
            dbc.Col(
                dcc.Upload(
                    id='upload-behavior',
                    children=html.Div(['Drop BEHAVIOR or ', html.A('Select Files')]),
                    style={
                        'width': '20%', 'height': '40px', 'lineHeight': '40px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                )
            )]
        )
    ),"

LINK NUMBER 395
Not enough lines

LINK NUMBER 396
Not enough lines

LINK NUMBER 397
Not enough lines

LINK NUMBER 398
Error fetching diff

LINK NUMBER 399
Error fetching diff

LINK NUMBER 400
Error fetching diff

LINK NUMBER 401

File path: src/main.c
"#include <stdio.h>
#include ""utilities.h""

int main() {
    print_welcome_message();
    int sum = add(5, 3);
    printf(""Sum of 5 and 3 is: %d\n"", sum);
    
    Fraction fraction = {10, 2};
    double division = divide(fraction);
    printf(""Division of 10 by 2 is: %.2f\n"", division);
    return 0;
}"

LINK NUMBER 402

File path: tutorial_manager.py
"import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import webbrowser
import json
import subprocess
import requests
from bs4 import BeautifulSoup
import yt_dlp

# Data storage - Global Varieables
BG_COLOR = ""#f5f5f5""
LABEL_FONT = (""Arial"", 10)
HEADER_FONT = (""Arial"", 11, ""bold"")
DATA_FILE = ""tutorials.json""
tutorials = []
tags_set = set()
categories_set = set()
last_selected_index = None
current_tags_list = []  # holds tags added one-by-one from dropdown

# ----------------------- Tooltip Helper -----------------------
def add_tooltip(widget, text):
    def on_enter(e):
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f""+{e.x_root+10}+{e.y_root+10}"")
        label = tk.Label(tooltip, text=text, background=""#ffffe0"", relief=""solid"", borderwidth=1, font=(""Arial"", 8))
        label.pack()
        widget.tooltip = tooltip
    def on_leave(e):
        if hasattr(widget, ""tooltip""):
            widget.tooltip.destroy()
    widget.bind(""<Enter>"", on_enter)
    widget.bind(""<Leave>"", on_leave)

# ----------------------- Persistence -----------------------
def load_data():
    global tutorials, tags_set, categories_set
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, ""r"") as f:
            tutorials = json.load(f)
            tags_set = set()
            categories_set = set()
            for tut in tutorials:
                tags_set.update(tut.get(""tags"", []))
                categories_set.add(tut.get(""category"", """"))

def save_data():
    with open(DATA_FILE, ""w"") as f:
        json.dump(tutorials, f, indent=4)

# ----------------------- Utility -----------------------
def update_dropdowns():
    cat_combo['values'] = sorted(categories_set)
    tag_combo['values'] = sorted(tags_set)

def update_listbox():
    tutorial_listbox.delete(0, tk.END)
    for i, tut in enumerate(tutorials):
        tag_display = "", "".join(tut.get(""tags"", []))
        tutorial_listbox.insert(tk.END, f""{tut['title']} [{tut['category']}] ({tag_display})"")

# ----------------------- Add/Edit/Delete -----------------------
def add_tutorial():
    title = title_var.get().strip()
    category = category_var.get().strip()
    path = path_var.get().strip()
    tags = current_tags_list.copy()

    if not title or not category or not path:
        messagebox.showerror(""Error"", ""Please fill in all required fields."")
        return

    categories_set.add(category)
    tags_set.update(tags)

    tutorials.append({
        ""title"": title,
        ""category"": category,
        ""path"": path,
        ""type"": ""local"" if os.path.exists(path) else ""youtube"",
        ""tags"": tags
    })
    update_listbox()
    update_dropdowns()
    save_data()

    title_var.set("""")
    category_var.set("""")
    path_var.set("""")
    tag_var.set("""")
    
    # ✅ Clear selected tags list visually and in memory
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

def edit_selected():
    index = get_selected_index()
    if index is None:
        return

    # Log current values (for debugging)
    print(""Editing index:"", index)
    print(""Before:"", tutorials[index])

    title = title_var.get().strip()
    category = category_var.get().strip()
    path = path_var.get().strip()
    tags = list(tag_listbox.get(0, tk.END))  # get only the tags currently shown


    if not title or not category or not path:
        messagebox.showerror(""Error"", ""Please fill in all required fields."")
        return

    tutorials[index] = {
        ""title"": title,
        ""category"": category,
        ""path"": path,
        ""type"": ""local"" if os.path.exists(path) else ""youtube"",
        ""tags"": tags
    }

    save_data()
    update_listbox()
    update_dropdowns()
    title_var.set("""")
    category_var.set("""")
    path_var.set("""")
    tag_var.set("""")
    
    # ✅ Clear selected tags list visually and in memory
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

    print(""After:"", tutorials[index])
    messagebox.showinfo(""Edit Successful"", f""Tutorial \""{title}\"" was updated."")

def delete_selected():
    index = get_selected_index()
    if index is None:
        return
    if messagebox.askyesno(""Confirm Delete"", ""Are you sure you want to delete this tutorial?""):
        tutorials.pop(index)
        update_listbox()
        save_data()

# ----------------------- Helper -----------------------
def get_selected_index():
    selected = tutorial_listbox.curselection()
    if selected:
        return selected[0]
    if last_selected_index is not None:
        return last_selected_index
    messagebox.showinfo(""Select Tutorial"", ""Please select a tutorial."")
    return None

def on_listbox_select(event):
    global last_selected_index
    selected = tutorial_listbox.curselection()
    if not selected:
        return  # Exit early if no selection

    last_selected_index = selected[0]
    tut = tutorials[last_selected_index]
    title_var.set(tut['title'])
    category_var.set(tut['category'])
    path_var.set(tut['path'])
    tag_var.set("", "".join(tut.get(""tags"", [])))

    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

    for tag in tut.get(""tags"", []):
        current_tags_list.append(tag)
        tag_listbox.insert(tk.END, tag)

def browse_file():
    path = filedialog.askopenfilename(filetypes=[(""Video Files"", ""*.mp4 *.mov *.avi *.mkv"")])
    if path:
        path_var.set(path)

def preview_selected():
    index = get_selected_index()
    if index is None:
        return
    path = tutorials[index]['path']
    video_title_label.config(text=f""Now Playing: {tutorials[index]['title']}"")
    if tutorials[index]['type'] == 'youtube':
        webbrowser.open(path)
    else:
        try:
            subprocess.Popen(['start', '', path], shell=True)
        except Exception as e:
            messagebox.showerror(""Error"", f""Could not open video: {e}"")

# ----------------------- Add Tag/Category -----------------------
def add_tag():
    new_tags = tag_var.get().strip()
    if new_tags:
        for tag in new_tags.split(','):
            tag = tag.strip()
            if tag:
                tags_set.add(tag)
        update_dropdowns()
        tag_var.set("""")

def add_category():
    new_cat = category_var.get().strip()
    if new_cat:
        categories_set.add(new_cat)
        update_dropdowns()
        category_var.set("""")
        
def add_tag_to_list():
    tag = tag_var.get().strip()
    if tag and tag not in current_tags_list:
        current_tags_list.append(tag)
        tag_listbox.insert(tk.END, tag)
        tag_var.set("""")

def remove_selected_tag():
    selected = tag_listbox.curselection()
    if selected:
        index = selected[0]
        current_tags_list.pop(index)
        tag_listbox.delete(index)


# ----------------------- Search -----------------------
def search_tutorials():
    keyword = search_var.get().strip().lower()
    filter_by = search_by_var.get()
    tutorial_listbox.delete(0, tk.END)
    for tut in tutorials:
        if filter_by == ""Title"" and keyword in tut['title'].lower():
            insert_filtered(tut)
        elif filter_by == ""Category"" and keyword in tut['category'].lower():
            insert_filtered(tut)
        elif filter_by == ""Tag"" and any(keyword in t.lower() for t in tut.get('tags', [])):
            insert_filtered(tut)

def insert_filtered(tut):
    tag_display = "", "".join(tut.get(""tags"", []))
    tutorial_listbox.insert(tk.END, f""{tut['title']} [{tut['category']}] ({tag_display})"")

# ----------------------- URL Metadata Fetch -----------------------

def fetch_info_from_url():
    url = path_var.get().strip()
    if not url:
        messagebox.showwarning(""No URL"", ""Please enter a URL or path first."")
        return

    # YouTube/Vimeo via yt_dlp
    if ""youtube.com"" in url or ""youtu.be"" in url or ""vimeo.com"" in url:
        try:
            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title_var.set(info.get(""title"", """"))
                messagebox.showinfo(""Success"", ""Fetched info from video successfully."")
        except Exception as e:
            messagebox.showerror(""Error"", f""Failed to fetch video info: {e}"")
    else:
        # Try generic page title
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, ""html.parser"")
            title = soup.title.string.strip() if soup.title else """"
            title_var.set(title)
            messagebox.showinfo(""Success"", ""Fetched page title successfully."")
        except Exception as e:
            messagebox.showerror(""Error"", f""Failed to fetch webpage info: {e}"")
            
# ----------------------- Rest for Function -----------------------
def clear_form(event=None):
    global last_selected_index
    last_selected_index = None
    title_var.set("""")
    category_var.set("""")
    path_var.set("""")
    tag_var.set("""")
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)


# ----------------------- UI -----------------------
root = tk.Tk()
root.configure(bg=BG_COLOR)
root.title(""🎓 Tutorial Manager"")
root.geometry(""800x600"")

# --- Input Frame ---
input_frame = tk.LabelFrame(root, text=""🛠️ Add / Edit Tutorial"", padx=10, pady=10, font=HEADER_FONT, bg=BG_COLOR)
input_frame.pack(fill=""x"", padx=10, pady=5)

title_var = tk.StringVar()
category_var = tk.StringVar()
path_var = tk.StringVar()
tag_var = tk.StringVar()

# Title
tk.Label(input_frame, text=""Title:"").grid(row=0, column=0, sticky=""e"")
title_entry = tk.Entry(input_frame, textvariable=title_var, width=30)
title_entry.grid(row=0, column=1, padx=5)

# Category with dropdown
tk.Label(input_frame, text=""Category:"").grid(row=1, column=0, sticky=""e"")
cat_combo = ttk.Combobox(input_frame, textvariable=category_var, width=28)
cat_combo.grid(row=1, column=1, padx=5)
tk.Button(input_frame, text=""+"", width=2, command=add_category).grid(row=1, column=2)

# Tags with dropdown
tk.Label(input_frame, text=""Tags (comma-separated):"").grid(row=2, column=0, sticky=""e"")
tag_combo = ttk.Combobox(input_frame, textvariable=tag_var, width=28)
tag_combo.grid(row=2, column=1, padx=5)
add_tooltip(tag_combo, ""Type or select a tag. Use commas for multiple."")
tk.Button(input_frame, text=""+"", width=2, command=add_tag).grid(row=2, column=2)
add_tag_button = tk.Button(input_frame, text=""Add Tag to List"", command=add_tag_to_list)
add_tag_button.grid(row=2, column=3, padx=5)
add_tooltip(add_tag_button, ""Click to add the selected tag to the list below."")

# Tag Listbox to display added tags
tk.Label(input_frame, text=""Selected Tags:"").grid(row=5, column=0, sticky=""ne"")
tag_listbox = tk.Listbox(input_frame, height=4)
add_tooltip(tag_listbox, ""These are the tags currently added to this tutorial."")
tag_listbox.grid(row=5, column=1, columnspan=2, sticky=""we"")
remove_tag_button = tk.Button(input_frame, text=""Remove Selected Tag"", command=remove_selected_tag)
remove_tag_button.grid(row=5, column=3)
add_tooltip(remove_tag_button, ""Removes the selected tag from the list."")

# Path
tk.Label(input_frame, text=""Path or URL:"").grid(row=3, column=0, sticky=""e"")
path_entry = tk.Entry(input_frame, textvariable=path_var, width=30)
path_entry.grid(row=3, column=1, padx=5, sticky=""w"")
browse_button = tk.Button(input_frame, text=""📂"", command=browse_file)
browse_button.grid(row=3, column=2)
fetch_info_button = tk.Button(input_frame, text=""🔍 Fetch Info"", command=fetch_info_from_url)
fetch_info_button.grid(row=3, column=3)
add_tooltip(fetch_info_button, ""Fetch the title from a YouTube/Vimeo or website URL."")

# Buttons
add_button = tk.Button(input_frame, text=""➕ Add"", width=10, command=add_tutorial)
add_button.grid(row=4, column=0, pady=5)

edit_button = tk.Button(input_frame, text=""✏️ Edit"", width=10, command=edit_selected)
edit_button.grid(row=4, column=1, pady=5)

delete_button = tk.Button(input_frame, text=""❌ Delete"", width=10, command=delete_selected)
delete_button.grid(row=4, column=2, pady=5)

# --- Search Frame ---
search_frame = tk.Frame(root)
search_frame.pack(fill=""x"", padx=10, pady=5)

search_var = tk.StringVar()
search_by_var = tk.StringVar(value=""Title"")
search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
search_entry.pack(side=""left"", padx=5)

tk.OptionMenu(search_frame, search_by_var, ""Title"", ""Category"", ""Tag"").pack(side=""left"")
search_frame = tk.LabelFrame(root, text=""🔍 Search Tutorials"", font=HEADER_FONT, padx=10, pady=5, bg=BG_COLOR)

# --- Tutorial List ---
list_frame = tk.LabelFrame(root, text=""📚 Tutorials"", font=HEADER_FONT, bg=BG_COLOR)
list_frame.pack(fill=""both"", expand=True, padx=10, pady=5)

tutorial_listbox = tk.Listbox(list_frame, height=12)
tutorial_listbox.pack(side=""left"", fill=""both"", expand=True)
tutorial_listbox.bind(""<<ListboxSelect>>"", on_listbox_select)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=""right"", fill=""y"")
tutorial_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tutorial_listbox.yview)

# --- Preview ---
preview_frame = tk.Frame(root)
preview_frame.pack(fill=""x"", padx=10)
tk.Button(preview_frame, text=""▶ Preview"", width=25, command=preview_selected).pack(pady=5)
video_title_label = tk.Label(preview_frame, text=""Now Playing: None"", font=(""Arial"", 10, ""italic""))
video_title_label.pack()

add_tooltip(add_button, ""Save a new tutorial using the form above."")
add_tooltip(edit_button, ""Apply changes to the selected tutorial."")
add_tooltip(delete_button, ""Remove the selected tutorial permanently."")
add_tooltip(search_entry, ""Search tutorials by title, category, or tag."")


# Run
load_data()
update_listbox()
update_dropdowns()

def is_click_outside_widgets(event):
    widget = root.winfo_containing(event.x_root, event.y_root)
    allowed_widgets = [
        tutorial_listbox, search_entry,
        title_entry, cat_combo, tag_combo,
        path_entry, tag_listbox,
        add_button, edit_button, delete_button,
        browse_button, fetch_info_button,
        add_tag_button, remove_tag_button
    ]
    if widget not in allowed_widgets:
        clear_form()
        
root.bind(""<Button-1>"", is_click_outside_widgets)
root.mainloop()
"

LINK NUMBER 403

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 404

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 405
Error fetching diff

LINK NUMBER 406
Error fetching diff

LINK NUMBER 407
Error fetching diff

LINK NUMBER 408

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 409

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 410

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 411

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 412
Error fetching diff

LINK NUMBER 413
Error fetching diff

LINK NUMBER 414
Error fetching diff

LINK NUMBER 415

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 416

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 417

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 418

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 419
Error fetching diff

LINK NUMBER 420
Error fetching diff

LINK NUMBER 421
Error fetching diff

LINK NUMBER 422
Not enough lines

LINK NUMBER 423

File path: 11_reduxToolkit/src/features/todo/todoSlice.js
"
    //reducer 3
    updateTodo: (state, action) => {
      const { id, newText } = action.payload;
      const todoToUpdate = state.todos.find((todo) => todo.id === id);
      if (todoToUpdate) {
        todoToUpdate.text = newText;
      }
    },"

LINK NUMBER 424
Not enough lines

LINK NUMBER 425
Not enough lines

LINK NUMBER 426
Error fetching diff

LINK NUMBER 427
Error fetching diff

LINK NUMBER 428
Error fetching diff

LINK NUMBER 429

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 430

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 431

File path: CardShuffle_Homework/Deck.cpp
"//
// Created by damya on 1.2.2024 г..
//

#ifndef CARDSHUFFLE_CARD_H
#define CARDSHUFFLE_CARD_H

using namespace std;
#include ""iostream""


class Card {
public:


    enum Type {
            ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING
    };

    enum Suit {
        HEARTS, DIAMONDS, CLUBS, SPADES
    };

    Card(Type, Suit);


    Type getType() const;
    Suit getSuit() const;



private:
    Type type;
    Suit suit;
};



#endif //CARDSHUFFLE_CARD_H"

LINK NUMBER 432

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 433
Error fetching diff

LINK NUMBER 434
Error fetching diff

LINK NUMBER 435
Error fetching diff

LINK NUMBER 436

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 437
Not enough lines

LINK NUMBER 438

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 439

File path: main.js
"  if (userPoints == 5) {
    alert(`Cograts, you have ${userPoints}, you won!`);
  } else {
    alert(`Sorry, the computer has ${computerPoints}, you lost!`);
  }"

LINK NUMBER 440
Error fetching diff

LINK NUMBER 441
Error fetching diff

LINK NUMBER 442
Error fetching diff

LINK NUMBER 443
Not enough lines

LINK NUMBER 444

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 445

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 446

File path: src/modules/applyRotation/transformCoordinates.test.ts
"const transformPointBetweenPolesCases = [
  // {
  //   name: 'where point [1, 0, 0] is transformed from initial pole to new pole',
  //   point: [1, 0, 0],
  //   initialPole: {
  //     lat_of_euler_pole: 30,
  //     lon_of_euler_pole: 60,
  //     rotation_angle: 20,
  //   },
  //   newPole: {
  //     lat_of_euler_pole: 45,
  //     lon_of_euler_pole: 45,
  //     rotation_angle: 30,
  //   },
  //   expected: [0.7392, 0.5732, 0.3536],
  // },
  // {
  //   name: 'where point [0, 1, 0] is transformed from initial pole to new pole',
  //   point: [0, 1, 0],
  //   initialPole: {
  //     lat_of_euler_pole: 30,
  //     lon_of_euler_pole: 60,
  //     rotation_angle: 20,
  //   },
  //   newPole: {
  //     lat_of_euler_pole: 45,
  //     lon_of_euler_pole: 45,
  //     rotation_angle: 30,
  //   },
  //   expected: [0.2803, 0.7392, 0.6124],
  // },
  {
    name: 'where point [1, 0, 0] is transformed from initial pole to new pole',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 30,
    },
    expected: [0.8660254037844387, 0.5, 0],
  },
  {
    name: 'in the series, the same point goes to a third pole',
    point: [0.8660254037844387, 0.5, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 30,
    },
    newPole: {
      lat_of_euler_pole: 20,
      lon_of_euler_pole: 45,
      rotation_angle: 30,
    },
    expected: [0.9251766765758391, 0.23016134445423478, -0.30178448044772743],
  },
  {
    name: 'using test planet',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    expected: [1, 0, 0],
  },
  {
    name: 'using test planet and motion',
    point: [1, 0, 0],
    initialPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: 0,
    },
    newPole: {
      lat_of_euler_pole: 90,
      lon_of_euler_pole: 0,
      rotation_angle: -30,
    },
    expected: [0.8660254037844387, -0.5, 0],
  },
];"

LINK NUMBER 447
Error fetching diff

LINK NUMBER 448
Error fetching diff

LINK NUMBER 449

File path: src/js/components/messages/messages.js
"# Chat App Component

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
<script type=""module"" src=""path/to/chat-app.js""></script>
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
*The authors of DOMPurify for ensuring safe user inputs."

LINK NUMBER 450
Not enough lines

LINK NUMBER 451
Not enough lines

LINK NUMBER 452

File path: index.js
"    console.log('SVG file generated successfully!');
}).catch(error => {
    console.error('Error:', error);
});

// Function that writes SVG file
// function writeToFile('Logo.svg', svgCode) {
//     fs.writeFile('Logo.svg', svgCode, (err) => {
//         if (err) {
//             return console.log(err)
//         }
//         console.log('SVG File successfully generated.')
//     })
// }"

LINK NUMBER 453
Error fetching diff

LINK NUMBER 454
Error fetching diff

LINK NUMBER 455
Error fetching diff

LINK NUMBER 456
Not enough lines

LINK NUMBER 457
Not enough lines

LINK NUMBER 458

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 459
Error fetching diff

LINK NUMBER 460
Error fetching diff

LINK NUMBER 461
Error fetching diff

LINK NUMBER 462
Not enough lines

LINK NUMBER 463

File path: scripts/main.js
"// Define fade-in and fade-out animations
const fadeIn = [
  { opacity: 0 },
  { opacity: 1 }
];

const fadeOut = [
  { opacity: 1 },
  { opacity: 0 }
];

const fadeTiming = {
  duration: 200, // Adjust the duration as needed
  iterations: 1
};

// when scroll down 30px from top, show the button with fade-in animation
window.onscroll = function () {
  scrollFunction();
};"

LINK NUMBER 464
Not enough lines

LINK NUMBER 465

File path: app/src/main/java/com/qsync/qsync/ZeroConfService.java
"package com.qsync.qsync;

import android.os.Handler;
import android.os.Looper;
import android.util.Log;

import com.google.gson.Gson;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Networking {

    public static final int HEADER_LENGTH = 83;
    private static final String TAG = ""Networking"";
    private static ServerSocket serverSocket;
    private static Socket clientSocket;
    private static AccesBdd acces;

    public static void main(String[] args) {
        try {
            serverSocket = new ServerSocket(8274);
            Log.d(TAG, ""Server started on port 8274"");
            while (true) {
                clientSocket = serverSocket.accept();
                Log.d(TAG, ""Client connected"");
                new Thread(new ClientHandler(clientSocket)).start();
            }
        } catch (IOException e) {
            Log.e(TAG, ""Error while initializing socket server : "", e);
        }
    }

    public static class ClientHandler implements Runnable {
        private Socket clientSocket;

        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }

        @Override
        public void run() {
            try {
                acces = new AccesBdd();
                acces.InitConnection();

                // get the device id and secure sync id from header
                char[] header_buff = new char[HEADER_LENGTH];
                InputStreamReader inputStreamReader = new InputStreamReader(clientSocket.getInputStream(), StandardCharsets.UTF_8);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                bufferedReader.read(header_buff, 0, HEADER_LENGTH);

                String device_id = new String(header_buff, 0, HEADER_LENGTH).split("";"")[0];
                String secure_id = new String(header_buff, 0, HEADER_LENGTH).split("";"")[1];

                acces.SetSecureId(secure_id);

                // in case of a link packet, the device is not yet registered in the database
                // so it can throw an error
                if (acces.IsDeviceLinked(device_id)) {
                    // makes sure it is marked as connected
                    if (!acces.GetDevicedbState(device_id)) {
                        // needs split as RemoteAddr ads port to the address
                        acces.SetDevicedbState(device_id, true, clientSocket.getInetAddress().getHostAddress());
                    }
                }

                // read the body of the request and store it in a buffer
                StringBuilder body_buff = new StringBuilder();
                String line;
                while ((line = bufferedReader.readLine()) != null) {
                    body_buff.append(line);
                }

                Log.d(TAG, ""Request body : "" + body_buff);

                // Parse the JSON
                Gson gson = new Gson();
                Globals.QEvent data = gson.fromJson(body_buff.toString(),Globals.QEvent.class);

                // check if this is a regular file event of a special request
                Log.d(TAG, ""RECEIVING EVENT : "" + data);
                switch (data.getFlag()) {
                    case ""[MODIFICATION_DONE]"":
                        setEventNetworkLockForDevice(device_id, false);
                        break;
                    case ""[SETUP_DL]"":
                        Log.d(TAG, ""GOT FLAG, BUILDING SETUP QUEUE..."");
                        buildSetupQueue(secure_id, device_id);
                        break;
                    case ""[LINK_DEVICE]"":
                        // as this is triggered by another machine telling this one to create a sync task,
                        // we must prepare the environnement to accept this
                        // by creating a new sync task with the same path (replace this later by asking to the user)
                        // and same secure_id
                        Log.d(TAG, ""Initializing env to welcome the other end folder content"");
                        acces.SetSecureId(secure_id);
                        String path = askInput(""[CHOOSELINKPATH]"", ""Choose a path where new sync files will be stored."");
                        Log.d(TAG, ""Future sync will be stored at : "" + path);
                        acces.CreateSyncFromOtherEnd(path, secure_id);
                        Log.d(TAG, ""Linking device : "" + device_id);
                        acces.LinkDevice(device_id, clientSocket.getInetAddress().getHostAddress());
                        break;
                    case ""[UNLINK_DEVICE]"":
                        acces.UnlinkDevice(device_id);
                        break;
                    case ""[OTDL]"":
                        handleLargageAerien(data, clientSocket.getInetAddress().getHostAddress());
                        break;
                    default:
                        // regular file event
                        handleEvent(secure_id, device_id, body_buff.toString());
                        // send back a modification confirmation, so the other end can remove this machine device_id
                        // from concerned sync task retard entries
                        String response = acces.getMyDeviceId() + "";"" + acces.GetSecureId() + "";"" + ""[MODIFICATION_DONE]"";
                        DataOutputStream outputStream = new DataOutputStream(clientSocket.getOutputStream());
                        outputStream.writeBytes(response);
                        break;
                }

            } catch (IOException e) {
                Log.e(TAG, ""Error in ClientHandler: "", e);
            }
        }
    }

    // used to process a request when it is a regular file event
    public static void handleEvent(String secureId, String deviceId, byte[] buffer) {
        try {
            String bufferData = new String(buffer);
            JSONObject jsonEvent = new JSONObject(bufferData);


            // First, we lock the filesystem watcher to prevent a ping-pong effect
            setFileSystemPatchLockState(deviceId, true);

            // Get the necessary data from the JSON event
            String relativePath = jsonEvent.getString(""FilePath"");
            String newRelativePath = jsonEvent.getString(""NewFilePath"");
            String absoluteFilePath = null;
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                absoluteFilePath = Paths.get(acces.GetRootSyncPath(), relativePath).toString();
            }
            String newAbsoluteFilePath = null;
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                newAbsoluteFilePath = Paths.get(acces.GetRootSyncPath(), newRelativePath).toString();
            }
            String eventType = jsonEvent.getString(""Flag"");
            String fileType = jsonEvent.getString(""FileType"");

            switch (eventType) {
                case ""MOVE"":
                    acces.move(relativePath, newRelativePath, fileType);
                    moveInFileSystem(absoluteFilePath, newAbsoluteFilePath);
                    break;
                case ""REMOVE"":
                    if (""file"".equals(fileType)) {
                        acces.rmFile(absoluteFilePath);
                    } else {
                        acces.rmFolder(absoluteFilePath);
                    }
                    removeFromFileSystem(absoluteFilePath);
                    break;
                case ""CREATE"":
                    if (""file"".equals(fileType)) {
                        acces.createFile(relativePath,absoluteFilePath,""[SENT_FROM_OTHER_DEVICE]"");
                    } else {
                        createFolder(absoluteFilePath);
                    }
                    break;
                case ""UPDATE"":
                    acces.incrementFileVersion(relativePath);
                    break;
                default:
                    Log.e(""HandleEventAdapter"", ""Received unknown event type: "" + eventType);
                    break;
            }

            // Release the filesystem lock
            setFileSystemPatchLockState(deviceId, false);
        } catch (JSONException e) {
            Log.e(""HandleEventAdapter"", ""Error decoding JSON data from request buffer"", e);
        } catch (JSONException e) {
            throw new RuntimeException(e);
        }
    }


    public static void sendDeviceEventQueueOverNetwork(Globals.GenArray<String> connected_devices, String secure_id, Globals.GenArray<Globals.QEvent> event_queue, String... ip_addr) {
        // ...
    }

    public static void setEventNetworkLockForDevice(String device_id, boolean value) {
        // ...
    }

    public static boolean getEventNetworkLockForDevice(String device_id) {
        // ...
        return false;
    }

    public static void removeFromFilesystem(String path) {
        // ...
    }

    public static void moveInFilesystem(String old_path, String new_path) {
        // ...
    }

    public static void buildSetupQueue(String secure_id, String device_id) {
        // ...
    }

    public static void handleLargageAerien(Globals.QEvent data, String ip_addr) {
        // ...
    }

    public static void sendLargageAerien(String file_path, String device_ip) {
        // ...
    }

    public static String askInput(final String title, final String message) {
        final Handler handler = new Handler(Looper.getMainLooper());
        final String[] result = new String[1];
        handler.post(new Runnable() {
            @Override
            public void run() {
                // Show your dialog here to get user input
                // Store the result in result[0]
            }
        });
        // Wait for user input
        while (result[0] == null) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return result[0];
    }
}"

LINK NUMBER 466
Error fetching diff

LINK NUMBER 467
Error fetching diff

LINK NUMBER 468
Error fetching diff

LINK NUMBER 469
Too many lines

LINK NUMBER 470

File path: petpets/get_names.py
"read_file_path = 'petpets/raw_names.txt'
write_file_path = 'petpets/names.txt'

# Read all petpet names from the file
with open(read_file_path, 'r') as file:
    raw_names = file.read().splitlines()

def check_if_valid(line):
    res = []
    words = line.split("" "")
    for word in words:
        word = word.strip(""'"")
        word = word.strip('""')
        if len(word) == 5:
            res.append(word)
    return res

# Will overwrite file every time this script is run (w for overwrite)
count = 0
with open(write_file_path, 'w') as file:
    for name in raw_names:
        valid_names = check_if_valid(name)
        for valid_name in valid_names:
            count += 1
            file.write(f""{valid_name}\n"")

print(f""Saved {count} names to {write_file_path}"")"

LINK NUMBER 471
Not enough lines

LINK NUMBER 472

File path: liveapp/src/components/Streaming/Streaming.js
"            // Only create a new Hls instance if one does not already exist
            if (!hlsRef.current) {
                const hls = new Hls();
                hlsRef.current = hls;  // Store the Hls instance in the ref
                hls.loadSource(streamUrl);
                hls.attachMedia(videoRef.current);
                hls.on(Hls.Events.MANIFEST_PARSED, () => {
                    videoRef.current.play();
                });
            } else {
                // If an Hls instance exists, just change the source
                hlsRef.current.loadSource(streamUrl);
                hlsRef.current.attachMedia(videoRef.current);
            }"

LINK NUMBER 473
Error fetching diff

LINK NUMBER 474
Error fetching diff

LINK NUMBER 475
Error fetching diff

LINK NUMBER 476
Not enough lines

LINK NUMBER 477
Not enough lines

LINK NUMBER 478
Not enough lines

LINK NUMBER 479
Not enough lines

LINK NUMBER 480
Error fetching diff

LINK NUMBER 481
Error fetching diff

LINK NUMBER 482
Error fetching diff

LINK NUMBER 483

File path: test2.js
"// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
  apiKey: ""AIzaSyBbhNdQa2sn_uGqWYhNZcS8PRwoI0x1ook"",
  authDomain: ""portfoliodatabase-27998.firebaseapp.com"",
  databaseURL:
    ""https://portfoliodatabase-27998-default-rtdb.europe-west1.firebasedatabase.app"",
  projectId: ""portfoliodatabase-27998"",
  storageBucket: ""portfoliodatabase-27998.appspot.com"",
  messagingSenderId: ""485104666349"",
  appId: ""1:485104666349:web:7327325c77127183d7eee4"",
  measurementId: ""G-FSXNF4C33Q"",
};
// Initialize Firebase
// firebase.analytics();
firebase.initializeApp(firebaseConfig);
// firebase.auth.Auth.Persistence.SESSION;

// Initialize variables
const auth = firebase.auth();
const database = firebase.database();

const postsDisplay = document.getElementById(""postsDisplay"");
const logOutbtn = document.getElementById(""logOutbtn"");
const RegBTN = document.getElementById(""RegBTN"");
const logInbtn = document.getElementById(""logInbtn"");
const LogInWarning = document.getElementById(""LogInWarning"");
// const HideContent = document.getElementsByClassName(""HideContent"");
const HideContent = document.getElementById(""HideContent"");

const currentTimestamp = Date.now();
const readableTimestamp = new Date(currentTimestamp).toISOString();
///////////////////////////////////Registration Section///////////////////////////////

// Set up our register function
function register() {
  // Get all our input fields
  firstName = document.getElementById(""firstName"").value;
  lastName = document.getElementById(""lastName"").value;
  email = document.getElementById(""email"").value;
  password = document.getElementById(""password"").value;

  // Validate input fields
  if (validate_email(email) == false || validate_password(password) == false) {
    swal(""Email or Password is NOT Correct!!"");
    return;
    // If pass or email not in the right format don't continue running the code
  }
  if (validate_field(firstName) == false || validate_field(lastName) == false) {
    swal(""One or More Extra Fields is Outta Line!!"");
    return;
  }
  // If entry format not in the right format don't continue running the code otherwise:

  // Move on with Auth
  auth
    .createUserWithEmailAndPassword(email, password)
    .then(function () {
      // Declare user variable
      var user = auth.currentUser;

      // Add this user to Firebase Database
      var database_ref = database.ref();

      // Create User data
      var user_data = {
        email: email,
        firstName: firstName,
        lastName: lastName,
        regDateTime: new Date().toISOString(),
        last_login: readableTimestamp,
        last_logout: readableTimestamp,
        // last_login: Date.now(),
        // last_logout: Date.now(),
        // lastLoginTimestamp: formatDateTime(lastLoginTimestamp),
        // lastLogoutTimestamp: formatDateTime(lastLogoutTimestamp),
      };

      // Push to Firebase Database
      database_ref.child(""users/"" + user.uid).set(user_data);

      // Done. Instead of ALERT popup SweetAlert ""swal"" Has been used,
      swal({
        text: ""Thank you, Your Account Created!!"",
        icon: ""success"",
        timer: 2000,
      });
      console.log(user_data); // checking the users success & data on console

      function intervalFunction() {
        // function created only to create a delay for moving to the POSTS.html page so the SUCCESS alert/swal is visible well!
        if (user) {
          window.location.replace = ""/Posts.html""; //After successful login, user will be redirected to Posts.html
        }
      }
      setInterval(intervalFunction, 2000);
    })

    .catch(function (error) {
      // Firebase will use this to alert of its errors
      var error_code = error.code;
      var error_message = error.message;

      alert(error_message, error_code);
    });
}
///////////////////////////////////Login Section///////////////////////////////
// Set up our login function
function login() {
  // Get all our input fields
  email = document.getElementById(""email"").value;
  password = document.getElementById(""password"").value;

  // Validate input fields
  if (validate_email(email) == false || validate_password(password) == false) {
    swal(""Email or Password is NOT Correct!!"");
    return;
    // Don't continue running the code
  }

  auth
    .signInWithEmailAndPassword(email, password)
    .then(function () {
      // Declare user variable
      var user = auth.currentUser;

      // Add this user to Firebase Database
      var database_ref = database.ref();

      // Create User data
      var user_data = {
        // last_login: Date.now(),
        last_login: readableTimestamp,
      };

      // Push to Firebase Database
      database_ref.child(""users/"" + user.uid).update(user_data);

      // Done
      swal({ text: ""You are Logged-In Now!!"", icon: ""success"", timer: 2000 });
      console.log(user_data); // checking the users success & data on consol

      function intervalFunction() {
        // function created only to create a delay for moving to the POSTS.html page so the SUCCESS alert/swal is visible well!
        if (user) {
          window.location = ""/Posts.html""; //After successful login, user will be redirected to Posts.html
        }
      }
      setInterval(intervalFunction, 2000);
    })
    .catch(function (error) {
      // Firebase will use this to alert of its errors
      var error_code = error.code;
      var error_message = error.message;

      // alert(""you are not logged in rez"");

      alert(error_message, error_code);
      postsDisplay.style.display = ""none"";
    });
}

function logout() {
  const user = auth.currentUser;
  if (user) {
    auth.signOut();
    database
      .ref(`users/${user.uid}`)
      .update({ last_logout: readableTimestamp });
    swal({ text: ""You are Logged-Out Now!!"", icon: ""success"" });
    window.location = ""/Public/Social-Log/signIN.html"";
  }
}

// function logout() {
//   var database_ref = database.ref();
//   var user = auth.currentUser;

//   if (user) {
//     auth.signOut();
//     database_ref.child(""users/"" + user.uid).update(user_data);
//     var user_data = {
//       last_logout: readableTimestamp,
//     };
//     swal({ text: ""You are Logged-Out Now!!"", icon: ""success"" });
//     window.location = ""/Public/Social-Log/signIN.html"";
//   }
// }

// conditions for when user is/not logged in
auth.onAuthStateChanged(function (user) {
  if (user) {
    logInbtn.style.display = ""none"";
    RegBTN.style.display = ""none"";
    LogInWarning.style.display = ""none"";
    logOutbtn.style.display = ""block"";
    // for (let i = 0; i < HideContent.length; i++){
    //   HideContent[i].style.display = ""none""; // why it is not hiding other pages content?
    // }

    // for (let element of document.getElementsByClassName(""HideContent"")) {
    //   element.style.display = ""none"";
    // }
  } else {
    postsDisplay.style.display = ""none"";
    logOutbtn.style.display = ""none"";
  }
});
// hide the log out button if the user is not logged in
auth.onAuthStateChanged(function (user) {
  if (!user) {
    logOutbtn.style.display = ""none"";
  }
});
// hide the Registration & Login fields is the user is logged in already
auth.onAuthStateChanged(function (user) {
  if (user) {
    HideContent.style.display = ""none"";
    swal({ text: ""You are Logged In Now !!"", icon: ""success"" });
  }
});

auth()
  .revokeRefreshTokens(uid)
  .then(() => {
    return auth().getUser(uid);
  })
  .then((userRecord) => {
    return new Date(userRecord.tokensValidAfterTime).getTime() / 100;
  })
  .then((timestamp) => {
    console.log(`Tokens revoked at: ${timestamp}`);
  });

function validate_email(email) {
  expression = /^[^@]+@\w+(\.\w+)+\w$/;
  if (expression.test(email) == true) {
    // Email is good
    return true;
  } else {
    // Email is not good
    return false;
  }
}

function validate_password(password) {
  // Firebase only accepts lengths greater than 6
  if (password < 6) {
    return false;
  } else {
    return true;
  }
}

function validate_field(field) {
  if (field == null) {
    return false;
  }

  if (field.length <= 0) {
    return false;
  } else {
    return true;
  }
}
"

LINK NUMBER 484

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 485

File path: examples/main/main.cpp
"    // auto enable conversation mode if chat template is available
    const bool has_chat_template = !common_get_builtin_chat_template(model).empty() || !params.chat_template.empty();
    if (params.conversation_mode == COMMON_CONVERSATION_MODE_AUTO) {
        if (has_chat_template) {
            LOG_INF(""%s: chat template is available, enabling conversation mode (disable it with -no-cnv)\n"", __func__);
            params.conversation_mode = COMMON_CONVERSATION_MODE_ENABLED;
        } else {
            params.conversation_mode = COMMON_CONVERSATION_MODE_DISABLED;
        }
    }

    // in case user force-activate conversation mode (via -cnv) without proper chat template, we show a warning
    if (params.conversation_mode && !has_chat_template) {
        LOG_WRN(""%s: chat template is not available or is not supported. This may cause the model to output suboptimal responses\n"", __func__);
    }
"

LINK NUMBER 486

File path: src/components/LineChart.js
"export default function LineChart({ book, db }) {
  let [userData, setUserData] = useState(null);

  useEffect(() => {
    const unsubscribe = onSnapshot(doc(db, book?.id), (doc) => {
      setUserData(doc.data());
    });
    return () => unsubscribe();
  }, [db, book?.id]);
  console.log(userData);

  let total_pages = book?.pages;
  const keys = userData ? Object.keys(userData) : [];
  let dates = [];
  let pages = [];
  keys.forEach((key) => dates.push(key));
  dates = dates.sort();
  dates.forEach((date) => {
    pages.push(userData[date]);
  });"

LINK NUMBER 487
Error fetching diff

LINK NUMBER 488
Error fetching diff

LINK NUMBER 489
Error fetching diff

LINK NUMBER 490
Not enough lines

LINK NUMBER 491

File path: header.js
"  if (e.target.closest(""header"") === slider) {
    isDown = true;
    slider.classList.add(""active"");
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
  }"

LINK NUMBER 492

File path: tests/AdventOfCode.Tests.Day01/Day01.cs
"﻿namespace AdventOfCode.Day03;

public class Day03
{
    private readonly string[] _input;

    public Day03(string[] input)
    {
        _input = input;
    }

    public int Part1()
    {
        var schema = Array.ConvertAll(_input, line => line.ToCharArray());

        var sumParts = 0;

        for (var x = 0; x < schema.Length; x++)
        {
            var y = 0;
            while (y < schema[x].Length)
            {
                if (char.IsDigit(schema[x][y]))
                {
                    var number = schema[x][y].ToString();
                    var length = 1;

                    while (y + length < schema[x].Length && char.IsDigit(schema[x][y + length]))
                    {
                        number += schema[x][y + length];
                        length++;
                    }

                    if (IsAdjacentToSymbol(number, x, y, schema))
                    {
                        sumParts += int.Parse(number);
                    }

                    y += length;
                }
                else
                {
                    y++;
                }
            }
        }

        return sumParts;
    }

    public int Part2()
    {
        var schema = Array.ConvertAll(_input, line => line.ToCharArray());
        var sumRatios = 0;

        for (var x = 0; x < schema.Length; x++)
        {
            for (var y = 0; y < schema[x].Length; y++)
            {
                if (!IsGear(schema[x][y])) continue;

                var adjacentNumbers = new HashSet<int>();
                foreach (var (adjX, adjY) in GetAdjacentCells(x, y, schema.Length, schema[0].Length))
                {
                    if (!char.IsDigit(schema[adjX][adjY])) continue;

                    var number = FindNumbers(schema, adjX, adjY);
                    if (number != -1)
                    {
                        adjacentNumbers.Add(number);
                    }
                }

                if (adjacentNumbers.Count == 2)
                {
                    var gearRatio = 1;
                    foreach (var num in adjacentNumbers)
                    {
                        gearRatio *= num;
                    }
                    sumRatios += gearRatio;
                }
            }
        }

        return sumRatios;
    }

    private static bool IsSymbol(char c) => char.IsLetter(c) || ""$*+-/=&#%@"".Contains(c);

    private static bool IsGear(char c) => ""*"".Contains(c);

    private static int FindNumbers(IReadOnlyList<char[]> schema, int x, int y)
    {
        while (y > 0 && char.IsDigit(schema[x][y - 1]))
        {
            y--;
        }

        var number = """";
        while (y < schema[x].Length && char.IsDigit(schema[x][y]))
        {
            number += schema[x][y];
            y++;
        }
        return number.Length > 0 ? int.Parse(number) : -1;
    }

    private static List<(int, int)> GetAdjacentCells(int x, int y, int maxX, int maxY)
    {
        var adjacent = new List<(int, int)>();
        for (var dx = -1; dx <= 1; dx++)
        {
            for (var dy = -1; dy <= 1; dy++)
            {
                if (dx == 0 && dy == 0) continue;
                int newX = x + dx, newY = y + dy;
                if (newX >= 0 && newX < maxX && newY >= 0 && newY < maxY)
                {
                    adjacent.Add((newX, newY));
                }
            }
        }
        return adjacent;
    }

    private static bool IsAdjacentToSymbol(string number, int x, int y, IReadOnlyList<char[]> schema)
    {
        var length = number.Length;
        for (var i = 0; i < length; i++)
        {
            foreach (var (adjX, adjY) in GetAdjacentCells(x, y + i, schema.Count, schema[0].Length))
            {
                if (IsSymbol(schema[adjX][adjY])) return true;
            }
        }

        return false;
    }
}"

LINK NUMBER 493

File path: script.js
"<!DOCTYPE html>
<html lang=""en"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Task Manager</title>
    <link rel=""stylesheet"" href=""styles.css"">
    <script src=""https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.14.0/Sortable.min.js""></script>
</head>
<body>
    <div class=""container"">
        <h1>Task Manager</h1>
        <div class=""add-task-form"">
            <input type=""text"" id=""task-desc"" placeholder=""Enter task description"">
            <label for=""static-priority"">Static Priority:</label>
            <select id=""static-priority"">
                <option value=""1"">1 - Critical</option>
                <option value=""2"">2 - Urgent</option>
                <option value=""3"">3 - Important but not urgent</option>
                <option value=""4"">4 - Low priority</option>
                <option value=""5"">5 - Very low priority</option>
            </select>
            
            <label for=""daily-priority"">Daily Priority:</label>
            <select id=""daily-priority"">
                <option value=""1"">1 - Critical</option>
                <option value=""2"">2 - Urgent</option>
                <option value=""3"">3 - Important but not urgent</option>
                <option value=""4"">4 - Low priority</option>
                <option value=""5"">5 - Very low priority</option>
            </select>
        
            <button id=""add-task-btn"">Add Task</button>
        </div>
    <script src=""script.js""></script>
</body>
</html>"

LINK NUMBER 494
Error fetching diff

LINK NUMBER 495
Error fetching diff

LINK NUMBER 496
Error fetching diff

LINK NUMBER 497
Not enough lines

LINK NUMBER 498
Not enough lines

LINK NUMBER 499

File path: src/main/java/Backend/DosageCalculator.java
"// OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE #
//        String currentMeds = """";
//        String currentSpecies = """";
//        String currentFormula = """";
////        String currentDose = """";
//
//        boolean isMed = false;
//        boolean isSpecies = false;
//        boolean isFormula = false;
//        boolean isDose = false;
//        boolean isLine = false;
//
//        while (scannerForCAL.hasNextLine()) {
//            String line = scannerForCAL.nextLine();
//
//            //Breaking line into tokens
//            String[] tokens = line.split("" "");
//
//            if (tokens.length >= 4) {
//                // Saving the tokens to variables
//                currentMeds = tokens[0];
//                currentSpecies = tokens[1];
//                currentFormula = tokens[2];
//                currentDose = tokens[3];
//            } // end of Token if statement
//
//            //checking if med name and what was entered match
//            if (currentMeds.equalsIgnoreCase(meds)) {
//                isMed = true;
//            } else {
//                line = scannerForCAL.nextLine();
//            } // end of check Meds if statement
//
//            // if med name is correct:
//            //checking if species and what was entered match
//            if (isMed = true) {
//                if (currentSpecies.equalsIgnoreCase(species)) {
//                    isSpecies = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                } // end of check species = true if statement
//            }// end of isMed = true if statement
//
//            // if med name and species is correct:
//            //checking if formula and what was entered match
//            if (isMed == true && isSpecies == true) {
//                if (currentFormula.equalsIgnoreCase(formula)) {
//                    isFormula = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                }// end of check formula = true if statement
//            }// end of isMed && isSpecies = true if statement
//
//            // if med name and species and formula is correct:
//            //checking if dose and what was entered match
//            if (isMed == true && isSpecies == true && isFormula == true) {
//                if (currentDose.equalsIgnoreCase(dose)) {
//                    isDose = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                }// end of check dose = true if statement
//            }// end of isMed && isSpecies && isFormula = true if statement 
//
//        } // end of while hasNextLine loop
"

LINK NUMBER 500
Not enough lines

LINK NUMBER 501
Error fetching diff

LINK NUMBER 502
Error fetching diff

LINK NUMBER 503
Error fetching diff

LINK NUMBER 504

File path: app/src/main/java/com/qsync/qsync/AccesBdd.java
"    public Globals.GenArray<String> getSyncLinkedDevices() {
        Globals.GenArray<String> devicesList = new Globals.GenArray<>();

        // Define the SQL query to retrieve linked devices
        Cursor cursor = db.rawQuery(""SELECT linked_devices_id FROM sync WHERE secure_id=?"",
                new String[]{
                        secureId
                }
                );

        if (cursor != null) {
            try {
                // Move the cursor to the first row
                if (cursor.moveToFirst()) {
                    do {
                        // Get the linked_devices_id from the cursor
                        String devices_id = cursor.getString(0);

                        // Split the string and add each device to the devicesList
                        String[] devices = devices_id.split("";"");
                        for (String device : devices) {
                            devicesList.add(device);
                        }
                    } while (cursor.moveToNext());
                }
            } finally {
                cursor.close(); // Close the cursor when done
            }
        } else {
            Log.e(""AccesBdd"", ""Cursor is null"");
        }

        // Remove the last slot (empty space) in the array
        if (!devicesList.isEmpty()) {
            devicesList.popLast();
        }

        return devicesList;
    }


    // GetFileLastVersionId retrieves the last version ID of a file.
    public long GetFileLastVersionId(String path) {
        Cursor cursor = db.rawQuery(""SELECT version_id FROM filesystem WHERE path=? AND secure_id=?"",
                new String[]{
                        path,
                        secureId
                }
        );

        int version_id = 0;
        if(cursor.moveToFirst()){
            version_id = cursor.getInt(0);
        }

        cursor.close();
        return version_id;
    }

"

LINK NUMBER 505

File path: src/ofApp.cpp
"//The quick sort was adapted from this youtube video
//I want to eventually remake this in my own unique code
//https://www.youtube.com/watch?v=Vtckgz38QHs
int Partition(vector<int>& arr, int startIndex, int endIndex)
{
	int pivot = arr[endIndex];
	int i = startIndex - 1;

	for (int j = startIndex; j <= endIndex - 1; j++)
	{
		if (arr[j] < pivot)
		{
			i++;
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	i++;
	int temp = arr[i];
	arr[i] = arr[endIndex];
	arr[endIndex] = temp;

	return i;
}
void QuickSorting(vector<int>& arr, int startIndex, int endIndex)
{
	if (endIndex <= startIndex) return;

	int pivot = Partition(arr, startIndex, endIndex);
	QuickSorting(arr, startIndex, pivot - 1);
	QuickSorting(arr, pivot + 1, endIndex);

	isQuickTrue = false;
}

//The insertion sort was adapted from this youtube video
//I want to eventually remake this in my own unique code
//https://www.youtube.com/watch?v=8mJ-OhcfpYg
void InsertionSorting(vector<int>& arr)"

LINK NUMBER 506
Not enough lines

LINK NUMBER 507

File path: AssignmentAlpha_v7/Business/Services/ImageService.cs
"using Business.Models;
using Data.Entities;
using Data.Interfaces;
using Domain.DTOs.Forms;
using Domain.Extensions;
using Domain.Models;
using Microsoft.AspNetCore.Http;

namespace Business.Services;

public interface IImageService
{
    Task<ImageServiceResult> ProcessImageAsync(ImageFormData metadata);
    Task<ImageServiceResult> DeleteImageAsync(string imageId);
}

public class ImageService(IImageRepository imageRepository) : IImageService
{
    private readonly IImageRepository _imageRepository = imageRepository;

    public async Task<ImageServiceResult> ProcessImageAsync(ImageFormData metadata)
    {
        try
        {
            // Ensure the required metadata values are present
            if (string.IsNullOrEmpty(metadata.ImageUrl) || string.IsNullOrEmpty(metadata.AltText))
            {
                return new ImageServiceResult
                {
                    Succeeded = false,
                    StatusCode = 400,
                    Error = ""ImageUrl and AltText are required.""
                };
            }

            // Create the image entity from the metadata
            var imageEntity = new ImageEntity
            {
                Id = Guid.NewGuid().ToString(),
                ImageUrl = metadata.ImageUrl,
                AltText = metadata.AltText,
                UploadedAt = DateTime.UtcNow
            };

            // Attempt to save the image entity to the repository
            var saveResult = await _imageRepository.AddAsync(imageEntity);

            if (!saveResult.Succeeded)
            {
                return new ImageServiceResult
                {
                    Succeeded = false,
                    StatusCode = 500,
                    Error = saveResult.Error
                };
            }

            // Return the result wrapped in an ImageServiceResult
            return new ImageServiceResult
            {
                Succeeded = true,
                StatusCode = 201,
                Result = new List<Image> { saveResult.Result.MapTo<Image>() } // Wrap the single result in a list for consistency
            };
        }
        catch (Exception ex)
        {
            // Handle unexpected errors
            return new ImageServiceResult
            {
                Succeeded = false,
                StatusCode = 500,
                Error = ex.Message
            };
        }
    }
    
    public async Task<ImageServiceResult> DeleteImageAsync(string imageUrl)
    {
        var result = new ImageServiceResult();

        // Try to find the image
        var imageResult = await _imageRepository.GetEntityAsync(
            x => x.ImageUrl == imageUrl
        );

        if (!imageResult.Succeeded || imageResult.Result == null)
        {
            result.Succeeded = false;
            result.StatusCode = 404;
            result.Error = ""Image not found."";
            return result;
        }

        var imageEntity = imageResult.Result;

        // Proceed with deletion
        var deleteResult = await _imageRepository.DeleteAsync(imageEntity);
        if (!deleteResult.Succeeded)
        {
            result.Succeeded = false;
            result.StatusCode = 500;
            result.Error = ""Failed to delete image."";
            return result;
        }

        // Return success with the deleted image in Result
        result.Succeeded = true;
        result.StatusCode = 200;
        result.Result = new List<Image> { imageEntity.MapTo<Image>() };
        return result;
    }
}"

LINK NUMBER 508
Error fetching diff

LINK NUMBER 509
Error fetching diff

LINK NUMBER 510
Error fetching diff

LINK NUMBER 511
Not enough lines

LINK NUMBER 512
Not enough lines

LINK NUMBER 513

File path: CompostFinder.java
"
            //TODO: add a silly little coment
            int w = this.image.getWidth();
            int h = this.image.getHeight();
            double proportion = ((double) w) / (double) h;
            this.image = toBufferedImage(image.getScaledInstance((int) (HEIGHT * proportion), HEIGHT, java.awt.Image.SCALE_SMOOTH));
"

LINK NUMBER 514
Not enough lines

LINK NUMBER 515
Error fetching diff

LINK NUMBER 516
Error fetching diff

LINK NUMBER 517
Error fetching diff
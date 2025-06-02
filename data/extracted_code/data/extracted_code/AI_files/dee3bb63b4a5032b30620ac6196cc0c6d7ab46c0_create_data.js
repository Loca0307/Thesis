import { DynamoDBClient, BatchWriteItemCommand } from "@aws-sdk/client-dynamodb";
import { marshall } from "@aws-sdk/util-dynamodb";

// Configure DynamoDB client
const client = new DynamoDBClient({
  region: "localhost",
  endpoint: "http://localhost:8000",
  credentials: {
    accessKeyId: "fakeMyKeyId",
    secretAccessKey: "fakeSecretAccessKey",
  },
});

// Sample data for Users
const users = [
  {
    PK: { S: "USER#1" },
    SK: { S: "USER#1" },
    Type: { S: "User" },
    name: { S: "John Doe" },
    email: { S: "john@example.com" },
    join_date: { S: "2025-01-01" }
  },
  {
    PK: { S: "USER#2" },
    SK: { S: "USER#2" },
    Type: { S: "User" },
    name: { S: "Jane Smith" },
    email: { S: "jane@example.com" },
    join_date: { S: "2025-01-15" }
  },
  {
    PK: { S: "USER#3" },
    SK: { S: "USER#3" },
    Type: { S: "User" },
    name: { S: "Robert Johnson" },
    email: { S: "robert@example.com" },
    join_date: { S: "2025-02-10" }
  },
  {
    PK: { S: "USER#4" },
    SK: { S: "USER#4" },
    Type: { S: "User" },
    name: { S: "Emily Davis" },
    email: { S: "emily@example.com" },
    join_date: { S: "2025-03-05" }
  },
  {
    PK: { S: "USER#5" },
    SK: { S: "USER#5" },
    Type: { S: "User" },
    name: { S: "Michael Brown" },
    email: { S: "michael@example.com" },
    join_date: { S: "2025-03-20" }
  }
];

// Sample data for Books
const books = [
  {
    PK: { S: "BOOK#101" },
    SK: { S: "BOOK#101" },
    Type: { S: "Book" },
    title: { S: "The Great Gatsby" },
    author: { S: "F. Scott Fitzgerald" },
    isbn: { S: "9780743273565" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#102" },
    SK: { S: "BOOK#102" },
    Type: { S: "Book" },
    title: { S: "To Kill a Mockingbird" },
    author: { S: "Harper Lee" },
    isbn: { S: "9780061120084" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#103" },
    SK: { S: "BOOK#103" },
    Type: { S: "Book" },
    title: { S: "1984" },
    author: { S: "George Orwell" },
    isbn: { S: "9780451524935" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#104" },
    SK: { S: "BOOK#104" },
    Type: { S: "Book" },
    title: { S: "Pride and Prejudice" },
    author: { S: "Jane Austen" },
    isbn: { S: "9780141439518" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#105" },
    SK: { S: "BOOK#105" },
    Type: { S: "Book" },
    title: { S: "The Hobbit" },
    author: { S: "J.R.R. Tolkien" },
    isbn: { S: "9780547928227" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#106" },
    SK: { S: "BOOK#106" },
    Type: { S: "Book" },
    title: { S: "Dune" },
    author: { S: "Frank Herbert" },
    isbn: { S: "9780441172719" },
    available: { BOOL: true }
  },
  {
    PK: { S: "BOOK#107" },
    SK: { S: "BOOK#107" },
    Type: { S: "Book" },
    title: { S: "The Catcher in the Rye" },
    author: { S: "J.D. Salinger" },
    isbn: { S: "9780316769488" },
    available: { BOOL: true }
  }
];

// Sample data for Loans
const loans = [
  {
    PK: { S: "LOAN#1001" },
    SK: { S: "LOAN#1001" },
    GSI1PK: { S: "USER#1" },
    GSI1SK: { S: "LOAN_DATE#2025-04-01" },
    Type: { S: "Loan" },
    user_id: { S: "1" },
    book_id: { S: "101" },
    loan_date: { S: "2025-04-01" },
    due_date: { S: "2025-05-01" },
    status: { S: "RETURNED" }
  },
  {
    PK: { S: "LOAN#1002" },
    SK: { S: "LOAN#1002" },
    GSI1PK: { S: "USER#2" },
    GSI1SK: { S: "LOAN_DATE#2025-04-05" },
    Type: { S: "Loan" },
    user_id: { S: "2" },
    book_id: { S: "102" },
    loan_date: { S: "2025-04-05" },
    due_date: { S: "2025-05-05" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1003" },
    SK: { S: "LOAN#1003" },
    GSI1PK: { S: "USER#3" },
    GSI1SK: { S: "LOAN_DATE#2025-04-10" },
    Type: { S: "Loan" },
    user_id: { S: "3" },
    book_id: { S: "103" },
    loan_date: { S: "2025-04-10" },
    due_date: { S: "2025-05-10" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1004" },
    SK: { S: "LOAN#1004" },
    GSI1PK: { S: "USER#1" },
    GSI1SK: { S: "LOAN_DATE#2025-04-15" },
    Type: { S: "Loan" },
    user_id: { S: "1" },
    book_id: { S: "104" },
    loan_date: { S: "2025-04-15" },
    due_date: { S: "2025-05-15" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1005" },
    SK: { S: "LOAN#1005" },
    GSI1PK: { S: "USER#4" },
    GSI1SK: { S: "LOAN_DATE#2025-04-20" },
    Type: { S: "Loan" },
    user_id: { S: "4" },
    book_id: { S: "101" },
    loan_date: { S: "2025-04-20" },
    due_date: { S: "2025-05-20" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1006" },
    SK: { S: "LOAN#1006" },
    GSI1PK: { S: "USER#5" },
    GSI1SK: { S: "LOAN_DATE#2025-04-25" },
    Type: { S: "Loan" },
    user_id: { S: "5" },
    book_id: { S: "102" },
    loan_date: { S: "2025-04-25" },
    due_date: { S: "2025-05-25" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1007" },
    SK: { S: "LOAN#1007" },
    GSI1PK: { S: "USER#2" },
    GSI1SK: { S: "LOAN_DATE#2025-05-01" },
    Type: { S: "Loan" },
    user_id: { S: "2" },
    book_id: { S: "105" },
    loan_date: { S: "2025-05-01" },
    due_date: { S: "2025-06-01" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1008" },
    SK: { S: "LOAN#1008" },
    GSI1PK: { S: "USER#3" },
    GSI1SK: { S: "LOAN_DATE#2025-05-05" },
    Type: { S: "Loan" },
    user_id: { S: "3" },
    book_id: { S: "101" },
    loan_date: { S: "2025-05-05" },
    due_date: { S: "2025-06-05" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1009" },
    SK: { S: "LOAN#1009" },
    GSI1PK: { S: "USER#1" },
    GSI1SK: { S: "LOAN_DATE#2025-05-10" },
    Type: { S: "Loan" },
    user_id: { S: "1" },
    book_id: { S: "106" },
    loan_date: { S: "2025-05-10" },
    due_date: { S: "2025-06-10" },
    status: { S: "ACTIVE" }
  },
  {
    PK: { S: "LOAN#1010" },
    SK: { S: "LOAN#1010" },
    GSI1PK: { S: "USER#4" },
    GSI1SK: { S: "LOAN_DATE#2025-05-15" },
    Type: { S: "Loan" },
    user_id: { S: "4" },
    book_id: { S: "103" },
    loan_date: { S: "2025-05-15" },
    due_date: { S: "2025-06-15" },
    status: { S: "ACTIVE" }
  }
];

// Sample data for BookLoans
const bookLoans = [
  {
    PK: { S: "BOOK#101" },
    SK: { S: "LOAN#1001" },
    Type: { S: "BookLoan" },
    user_id: { S: "1" },
    loan_date: { S: "2025-04-01" }
  },
  {
    PK: { S: "BOOK#102" },
    SK: { S: "LOAN#1002" },
    Type: { S: "BookLoan" },
    user_id: { S: "2" },
    loan_date: { S: "2025-04-05" }
  },
  {
    PK: { S: "BOOK#103" },
    SK: { S: "LOAN#1003" },
    Type: { S: "BookLoan" },
    user_id: { S: "3" },
    loan_date: { S: "2025-04-10" }
  },
  {
    PK: { S: "BOOK#104" },
    SK: { S: "LOAN#1004" },
    Type: { S: "BookLoan" },
    user_id: { S: "1" },
    loan_date: { S: "2025-04-15" }
  },
  {
    PK: { S: "BOOK#101" },
    SK: { S: "LOAN#1005" },
    Type: { S: "BookLoan" },
    user_id: { S: "4" },
    loan_date: { S: "2025-04-20" }
  },
  {
    PK: { S: "BOOK#102" },
    SK: { S: "LOAN#1006" },
    Type: { S: "BookLoan" },
    user_id: { S: "5" },
    loan_date: { S: "2025-04-25" }
  },
  {
    PK: { S: "BOOK#105" },
    SK: { S: "LOAN#1007" },
    Type: { S: "BookLoan" },
    user_id: { S: "2" },
    loan_date: { S: "2025-05-01" }
  },
  {
    PK: { S: "BOOK#101" },
    SK: { S: "LOAN#1008" },
    Type: { S: "BookLoan" },
    user_id: { S: "3" },
    loan_date: { S: "2025-05-05" }
  },
  {
    PK: { S: "BOOK#106" },
    SK: { S: "LOAN#1009" },
    Type: { S: "BookLoan" },
    user_id: { S: "1" },
    loan_date: { S: "2025-05-10" }
  },
  {
    PK: { S: "BOOK#103" },
    SK: { S: "LOAN#1010" },
    Type: { S: "BookLoan" },
    user_id: { S: "4" },
    loan_date: { S: "2025-05-15" }
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
    console.log("Starting data population...");
    
    console.log("Inserting users...");
    await batchWriteItems(users);
    
    console.log("Inserting books...");
    await batchWriteItems(books);
    
    console.log("Inserting loans...");
    await batchWriteItems(loans);
    
    console.log("Inserting book loans...");
    await batchWriteItems(bookLoans);
    
    console.log("Data population completed successfully!");
  } catch (error) {
    console.error("Error in data population:", error);
  }
}

// Execute the population script
populateData();
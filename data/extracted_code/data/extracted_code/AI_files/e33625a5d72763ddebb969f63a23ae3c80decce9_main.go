name: CI Pipeline

on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Go
      uses: actions/setup-go@v3
      with:
        go-version: 1.21

    - name: Build
      run: |
        cd frontend
        go build

    - name: Run tests
      run: |
        cd frontend
        go test ./...
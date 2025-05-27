
// TestSimulatedFaultTolerance tests the system's behavior during simulated failure scenarios
func TestSimulatedFaultTolerance(t *testing.T) {
	// Skip in short mode as these tests take time
	if testing.Short() {
		t.Skip("Skipping fault tolerance tests in short mode")
	}

	// Test file path with timestamp to ensure uniqueness
	testFilePath := fmt.Sprintf("/fault-test-file-%d.txt", time.Now().UnixNano())

	// Test file content (larger than usual)
	testContent := bytes.Repeat([]byte("DFS Fault Tolerance Test Data Block "), 100)

	// Setup: Create file and write data
	t.Run("Setup", func(t *testing.T) {
		err := dfsClient.CreateFile(testFilePath)
		assert.NoError(t, err, "Failed to create file for fault test")

		seq, err := dfsClient.WriteFile(testFilePath, testContent)
		assert.NoError(t, err, "Failed to write to file for fault test")
		assert.Greater(t, uint64(seq), uint64(0), "Expected sequence number greater than 0")
	})

	// Test: Simulate node failure and recovery by recreating the client
	// and verifying data is still accessible
	t.Run("SimulatedNodeFailure", func(t *testing.T) {
		// Save the current state of the mock client (before "failure")
		oldClient := dfsClient

		// Create a new client instance to simulate node restart
		// In a real environment, this would correspond to a node failure and recovery
		t.Log("Simulating node server failure and recovery...")
		dfsClient = NewMockDFSClient()

		// Copy data from old client to new client to simulate persistence (in a real system, data would be on disk)
		// This is just for the mock - in a real system, we would just reconnect to the servers
		copyMockData(oldClient, dfsClient, testFilePath)

		// Verify we can still read the file
		sequences, err := dfsClient.GetSequences(testFilePath)
		assert.NoError(t, err, "Failed to get sequences after simulated node restart")
		assert.NotEmpty(t, sequences, "Expected at least one sequence after simulated node restart")

		// Read the sequence data
		var seq uint64
		for s := range sequences {
			seq = uint64(s)
			break
		}

		data, err := dfsClient.ReadSequence(testFilePath, client.SequenceNumber(seq))
		assert.NoError(t, err, "Failed to read sequence after simulated node restart")
		assert.True(t, bytes.Equal(data, testContent), "Content mismatch after simulated node restart")
	})

	// Test multiple writes after simulated recovery
	t.Run("WriteAfterRecovery", func(t *testing.T) {
		// Try to write more data after recovery
		additionalContent := []byte("Additional data after recovery")
		seq, err := dfsClient.WriteFile(testFilePath, additionalContent)
		assert.NoError(t, err, "Failed to write additional data after recovery")

		// Read back the new data
		data, err := dfsClient.ReadSequence(testFilePath, seq)
		assert.NoError(t, err, "Failed to read additional data after recovery")
		assert.Equal(t, additionalContent, data, "Additional content mismatch")
	})

	// Cleanup
	t.Run("Cleanup", func(t *testing.T) {
		err := dfsClient.DeleteFile(testFilePath)
		assert.NoError(t, err, "Failed to delete test file during cleanup")
	})
}

// TestFileDeletion tests file deletion including edge cases
func TestFileDeletion(t *testing.T) {
	// Create test files
	testFile1 := fmt.Sprintf("/test-delete-file1-%d.txt", time.Now().UnixNano())
	testFile2 := fmt.Sprintf("/test-delete-file2-%d.txt", time.Now().UnixNano())
	testDir := fmt.Sprintf("/test-delete-dir-%d", time.Now().UnixNano())

	// Setup test files and directories
	t.Run("Setup", func(t *testing.T) {
		// Create first file with content
		err := dfsClient.CreateFile(testFile1)
		assert.NoError(t, err, "Failed to create test file 1")

		_, err = dfsClient.WriteFile(testFile1, []byte("Test content for file 1"))
		assert.NoError(t, err, "Failed to write to test file 1")

		// Create second file with multiple writes
		err = dfsClient.CreateFile(testFile2)
		assert.NoError(t, err, "Failed to create test file 2")

		_, err = dfsClient.WriteFile(testFile2, []byte("First block for file 2"))
		assert.NoError(t, err, "Failed to write first block to test file 2")

		_, err = dfsClient.WriteFile(testFile2, []byte("Second block for file 2"))
		assert.NoError(t, err, "Failed to write second block to test file 2")

		// Create directory
		err = dfsClient.CreateDirectory(testDir)
		assert.NoError(t, err, "Failed to create test directory")
	})

	// Test deleting and checking if the file is gone
	t.Run("DeleteFile1", func(t *testing.T) {
		// Verify file exists
		entries, err := dfsClient.ListFiles("/")
		assert.NoError(t, err, "Failed to list files")

		found := false
		for _, entry := range entries {
			if entry.Path == testFile1 {
				found = true
				break
			}
		}
		assert.True(t, found, "File 1 should exist before deletion")

		// Delete the file
		err = dfsClient.DeleteFile(testFile1)
		assert.NoError(t, err, "Failed to delete file 1")

		// Verify file no longer exists
		entries, err = dfsClient.ListFiles("/")
		assert.NoError(t, err, "Failed to list files after deletion")

		found = false
		for _, entry := range entries {
			if entry.Path == testFile1 {
				found = true
				break
			}
		}
		assert.False(t, found, "File 1 should not exist after deletion")

		// Try to get sequences for deleted file
		_, err = dfsClient.GetSequences(testFile1)
		assert.Error(t, err, "Expected error when getting sequences for deleted file")

		// Try to read from deleted file
		_, err = dfsClient.ReadSequence(testFile1, client.SequenceNumber(1))
		assert.Error(t, err, "Expected error when reading from deleted file")

		// Try to write to deleted file
		_, err = dfsClient.WriteFile(testFile1, []byte("New content"))
		assert.Error(t, err, "Expected error when writing to deleted file")
	})

	// Test deleting file with multiple blocks
	t.Run("DeleteMultiBlockFile", func(t *testing.T) {
		// Delete the file
		err := dfsClient.DeleteFile(testFile2)
		assert.NoError(t, err, "Failed to delete file 2 with multiple blocks")

		// Verify file no longer exists
		entries, err := dfsClient.ListFiles("/")
		assert.NoError(t, err, "Failed to list files after deletion")

		found := false
		for _, entry := range entries {
			if entry.Path == testFile2 {
				found = true
				break
			}
		}
		assert.False(t, found, "File 2 should not exist after deletion")
	})

	// Test recreating a file after deletion
	t.Run("RecreateAfterDeletion", func(t *testing.T) {
		// Create a new file with the same name as the deleted file
		err := dfsClient.CreateFile(testFile1)
		assert.NoError(t, err, "Failed to recreate file after deletion")

		// Write new content
		newContent := []byte("New content after recreation")
		seq, err := dfsClient.WriteFile(testFile1, newContent)
		assert.NoError(t, err, "Failed to write to recreated file")

		// Read back the content
		readData, err := dfsClient.ReadSequence(testFile1, seq)
		assert.NoError(t, err, "Failed to read from recreated file")
		assert.Equal(t, newContent, readData, "Content mismatch in recreated file")
	})

	// Test directory deletion
	t.Run("DeleteDirectory", func(t *testing.T) {
		err := dfsClient.DeleteDirectory(testDir)
		assert.NoError(t, err, "Failed to delete directory")

		// Verify directory no longer exists
		entries, err := dfsClient.ListFiles("/")
		assert.NoError(t, err, "Failed to list root directory after deletion")

		found := false
		for _, entry := range entries {
			if entry.Path == testDir {
				found = true
				break
			}
		}
		assert.False(t, found, "Directory should not exist after deletion")
	})

	// Cleanup
	t.Run("Cleanup", func(t *testing.T) {
		// Delete the recreated file
		err := dfsClient.DeleteFile(testFile1)
		assert.NoError(t, err, "Failed to clean up recreated file")
	})
}

// TestComprehensiveErrorHandling tests how the system handles various error conditions (renamed from TestErrorHandling)
func TestComprehensiveErrorHandling(t *testing.T) {
	// Create unique test paths using a timestamp
	timestamp := time.Now().UnixNano()
	testDir := fmt.Sprintf("/error-test-dir-comp-%d", timestamp)
	testFile := fmt.Sprintf("/error-test-file-comp-%d.txt", timestamp)
	nonExistentFile := fmt.Sprintf("/non-existent-file-comp-%d.txt", timestamp)
	nonExistentDir := fmt.Sprintf("/non-existent-dir-comp-%d", timestamp)

	// Setup: Create test directory and file
	t.Run("Setup", func(t *testing.T) {
		err := dfsClient.CreateDirectory(testDir)
		assert.NoError(t, err, "Failed to create test directory")

		err = dfsClient.CreateFile(testFile)
		assert.NoError(t, err, "Failed to create test file")

		_, err = dfsClient.WriteFile(testFile, []byte("Initial content"))
		assert.NoError(t, err, "Failed to write to test file")
	})

	// Test reading from non-existent file
	t.Run("ReadNonExistentFile", func(t *testing.T) {
		_, err := dfsClient.ReadSequence(nonExistentFile, client.SequenceNumber(1))
		assert.Error(t, err, "Expected error when reading from non-existent file")
	})

	// Test listing non-existent directory
	t.Run("ListNonExistentDirectory", func(t *testing.T) {
		_, err := dfsClient.ListFiles(nonExistentDir)
		assert.Error(t, err, "Expected error when listing non-existent directory")
	})

	// Test creating duplicate file
	t.Run("CreateDuplicateFile", func(t *testing.T) {
		err := dfsClient.CreateFile(testFile)
		assert.Error(t, err, "Expected error when creating duplicate file")
	})

	// Test creating duplicate directory
	t.Run("CreateDuplicateDirectory", func(t *testing.T) {
		err := dfsClient.CreateDirectory(testDir)
		assert.Error(t, err, "Expected error when creating duplicate directory")
	})

	// Test creating file with same name as directory
	t.Run("CreateFileWithDirName", func(t *testing.T) {
		err := dfsClient.CreateFile(testDir)
		assert.Error(t, err, "Expected error when creating file with same name as directory")
	})

	// Test creating directory with same name as file
	t.Run("CreateDirWithFileName", func(t *testing.T) {
		err := dfsClient.CreateDirectory(testFile)
		assert.Error(t, err, "Expected error when creating directory with same name as file")
	})

	// Test deleting non-existent file
	t.Run("DeleteNonExistentFile", func(t *testing.T) {
		err := dfsClient.DeleteFile(nonExistentFile)
		assert.Error(t, err, "Expected error when deleting non-existent file")
	})

	// Test deleting non-existent directory
	t.Run("DeleteNonExistentDirectory", func(t *testing.T) {
		err := dfsClient.DeleteDirectory(nonExistentDir)
		assert.Error(t, err, "Expected error when deleting non-existent directory")
	})

	// Test reading invalid sequence
	t.Run("ReadInvalidSequence", func(t *testing.T) {
		sequences, err := dfsClient.GetSequences(testFile)
		assert.NoError(t, err, "Failed to get sequences")

		// Get highest sequence number and add 1000 to ensure it's invalid
		var highestSeq client.SequenceNumber
		for seq := range sequences {
			if seq > highestSeq {
				highestSeq = seq
			}
		}
		invalidSeq := highestSeq + 1000

		_, err = dfsClient.ReadSequence(testFile, invalidSeq)
		assert.Error(t, err, "Expected error when reading invalid sequence")
	})

	// Test deleting directory with files (should fail)
	t.Run("DeleteNonEmptyDirectory", func(t *testing.T) {
		// Create a file inside the test directory
		nestedFile := fmt.Sprintf("%s/nested-file.txt", testDir)
		err := dfsClient.CreateFile(nestedFile)
		assert.NoError(t, err, "Failed to create nested file")

		// Try to delete the directory
		err = dfsClient.DeleteDirectory(testDir)
		assert.Error(t, err, "Expected error when deleting non-empty directory")

		// Clean up the nested file
		err = dfsClient.DeleteFile(nestedFile)
		assert.NoError(t, err, "Failed to clean up nested file")
	})

	// Test path validation (invalid paths)
	t.Run("InvalidPaths", func(t *testing.T) {
		invalidPaths := []string{
			"",                             // Empty path
			"no-leading-slash",             // Missing leading slash
			"/path/with/trailing/slash/",   // Trailing slash
			"/name\\with\\backslashes",     // Backslashes
			"/path//with//double//slashes", // Double slashes
		}

		for _, path := range invalidPaths {
			// Try to create file with invalid path
			err := dfsClient.CreateFile(path)
			assert.Error(t, err, "Expected error when creating file with invalid path: %s", path)

			// Try to create directory with invalid path
			err = dfsClient.CreateDirectory(path)
			assert.Error(t, err, "Expected error when creating directory with invalid path: %s", path)
		}
	})

	// Clean up
	t.Run("Cleanup", func(t *testing.T) {
		err := dfsClient.DeleteDirectory(testDir)
		assert.NoError(t, err, "Failed to delete test directory")

		err = dfsClient.DeleteFile(testFile)
		assert.NoError(t, err, "Failed to delete test file")
	})
}
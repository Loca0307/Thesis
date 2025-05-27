const CLI_FILE_NAME = 'cli.sh'
const CLI_FOLDER_NAME = '.codacy'
const CLI_COMMAND = `${CLI_FOLDER_NAME}/${CLI_FILE_NAME}`

// Set a larger buffer size (10MB)
const MAX_BUFFER_SIZE = 1024 * 1024 * 10

const execAsync = (command: string) => {
  const workspacePath = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || ''

  return new Promise((resolve, reject) => {
    exec(
      `CODACY_CLI_V2_VERSION=1.0.0-main.232.a6a6368 ${command}`,
      {
        cwd: workspacePath,
        maxBuffer: MAX_BUFFER_SIZE, // To solve: stdout maxBuffer exceeded
      },
      (error, stdout, stderr) => {
        if (error) {
          reject(error)
          return
        }

        if (stderr && (!stdout || /error|fail|exception/i.test(stderr))) {
          reject(new Error(stderr))
          return
        }

        resolve({ stdout, stderr })
      }
    )
  })
}
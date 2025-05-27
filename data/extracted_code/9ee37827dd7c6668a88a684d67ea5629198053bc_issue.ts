

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
      console.error("Failed to delete closed issues", error.message);
    }
  }
}
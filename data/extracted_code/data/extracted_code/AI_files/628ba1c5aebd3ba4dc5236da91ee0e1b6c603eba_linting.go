		fmt.Printf(`[INFO] API spec linting results:
Usability: %d
Security: %d
Robustness: %d
Evolution: %d
Overall: %d
`+"\n",
			resp.ImpactScore.CategorizedSummary.Usability,
			resp.ImpactScore.CategorizedSummary.Security,
			resp.ImpactScore.CategorizedSummary.Robustness,
			resp.ImpactScore.CategorizedSummary.Evolution,
			resp.ImpactScore.CategorizedSummary.Overall,
		)

		fmt.Println("[INFO] API spec linting passed for", spec)
		fmt.Println("[DEBUG] Removing report file...")
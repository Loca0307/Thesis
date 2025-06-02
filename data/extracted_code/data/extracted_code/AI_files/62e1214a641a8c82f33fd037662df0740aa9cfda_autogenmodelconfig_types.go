// Model Configurations
// This had to be created because the autogen_api.ModelInfo JSON tags are not
// compatible with the kubernetes api.
type ModelInfo struct {
	// +optional
	Vision bool `json:"vision"`
	// +optional
	FunctionCalling bool `json:"functionCalling"`
	// +optional
	JSONOutput bool `json:"jsonOutput"`
	// +optional
	Family string `json:"family"`
	// +optional
	StructuredOutput bool `json:"structuredOutput"`
	// +optional
	MultipleSystemMessages bool `json:"multipleSystemMessages"`
}

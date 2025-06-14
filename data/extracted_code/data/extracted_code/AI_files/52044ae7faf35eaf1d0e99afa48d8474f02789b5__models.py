{
  "status": "Error",
  "violations": [
    {
      "rule_ids": ["python_design.html#python-client-connection-string"],
      "line_no": 10,
      "bad_code": "connection_string: Optional[str] = None,",
      "suggestion": "Remove the connection_string parameter from the constructor and implement a separate factory method (e.g. from_connection_string) to create the client using a connection string.",
      "comment": "The constructor must not accept a connection string; using a factory method for connection string support is required by the guidelines."
    },
    {
      "rule_ids": [
        "python_design.html#python-client-optional-arguments-keyword-only"
      ],
      "line_no": 30,
      "bad_code": "def analyze_from_url(",
      "suggestion": "Insert a '*' after the required positional parameters so that all optional parameters are keyword-only. For example:\n\n  def analyze_from_url(self, image_url: str, visual_features: List[VisualFeatures], *, gender_neutral_caption: Optional[bool] = ..., language: Optional[str] = ..., model_version: Optional[str] = ..., smart_crops_aspect_ratios: Optional[List[float]] = ..., **kwargs: Any) -> ImageAnalysisResult",
      "comment": "Optional operation\u2010specific parameters must be keyword-only."
    },
    {
      "rule_ids": ["python_design.html#python-client-same-name-sync-async"],
      "line_no": 53,
      "bad_code": "class azure.ai.vision.imageanalysis.aio.AsyncImageAnalysisClient(ImageAnalysisClient): implements AsyncContextManager",
      "suggestion": "Rename the async client to ImageAnalysisClient (i.e. without the 'Async' prefix) and keep it under the 'azure.ai.vision.imageanalysis.aio' namespace so that both sync and async clients share the same client name.",
      "comment": "Async and sync clients must share the same client name; adding an 'Async' prefix violates this guideline."
    },
    {
      "rule_ids": [
        "python_design.html#python-client-constructor-api-version-argument-1"
      ],
      "line_no": 54,
      "bad_code": "def __init__(\n        self, \n        endpoint: str, \n        credential: Union[AzureKeyCredential, AsyncTokenCredential], \n    ) -> None",
      "suggestion": "Add an optional keyword-only api_version parameter to the async client __init__ signature, for example: \n    def __init__(self, endpoint: str, credential: Union[AzureKeyCredential, AsyncTokenCredential], *, api_version: str = ..., **kwargs: Any) -> None",
      "comment": "The async client constructor is missing the optional api_version parameter required by the guidelines."
    },
    {
      "rule_ids": [
        "python_implementation.html#python-codestyle-static-methods"
      ],
      "line_no": 88,
      "bad_code": "@staticmethod",
      "suggestion": "Remove the staticmethod decorator and refactor send_request as an instance method or a module-level function.",
      "comment": "Static methods are discouraged; module-level functions or instance methods should be used instead."
    },
    {
      "rule_ids": ["python_implementation.html#python-codestyle-type-naming"],
      "line_no": 209,
      "bad_code": "class azure.ai.vision.imageanalysis.models.detectedPerson(MutableMapping[str, Any]):",
      "suggestion": "Rename the class to DetectedPerson (using PascalCase) to adhere to type naming conventions.",
      "comment": "Type names should be in PascalCase; 'detectedPerson' violates this guideline."
    },
    {
      "rule_ids": ["python_implementation.html#python-codestyle-properties"],
      "line_no": 411,
      "bad_code": "def get_result(self) -> ObjectsResult",
      "suggestion": "Replace the get_result/set_result methods with a property (with a getter and setter) to expose the result, for example, using @property and @result.setter.",
      "comment": "Simple getter and setter functions are discouraged; properties should be used instead."
    },
    {
      "rule_ids": ["python_implementation.html#python-codestyle-properties"],
      "line_no": 413,
      "bad_code": "def set_result(self, obj) -> None",
      "suggestion": "Replace the set_result method with a property setter (e.g., @result.setter def result(self, value): ...).",
      "comment": "Simple setter methods should be implemented as property setters."
    },
    {
      "rule_ids": ["python_design.html#python-models-async"],
      "line_no": 432,
      "bad_code": "class azure.ai.vision.imageanalysis.models.aio.PeopleResult(MutableMapping[str, Any]):",
      "suggestion": "Move PeopleResult to the common models namespace (azure.ai.vision.imageanalysis.models) instead of duplicating it in the aio sub-namespace.",
      "comment": "Models should not be duplicated between the root and aio namespaces."
    },
    {
      "rule_ids": ["python_design.html#python-models-enum-name-uppercase"],
      "line_no": 517,
      "bad_code": "tags = \"tags\"",
      "suggestion": "Rename the enum member to use UPPERCASE (e.g., TAGS = \"tags\") in accordance with the guidelines.",
      "comment": "Enum member names must be in UPPERCASE to comply with naming conventions."
    }
  ]
}
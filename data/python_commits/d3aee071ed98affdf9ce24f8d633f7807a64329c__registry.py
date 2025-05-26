# Ignore assets used within evaluations, where we specifically want type checks to
# fail (e.g. buggy code that the agent should fix)
ignore = [
    "re_bench/*/assets",
    "re_bench/imported_asset_files",
    "re_bench/tests/solutions",
]
include = ["."]
reportAssertAlwaysTrue = true
reportDeprecated = true
reportUnusedImport = true
reportWildcardImportFromLibrary = true
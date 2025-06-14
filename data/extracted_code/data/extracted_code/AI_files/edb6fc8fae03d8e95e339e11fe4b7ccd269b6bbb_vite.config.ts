{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.worker.tsbuildinfo",
    "types": [
      "vite/client",
      "@cloudflare/workers-types",
      "./worker-configuration.d.ts",
      "@cloudflare/vitest-pool-workers"
    ],
    "paths": {
      "#api/*": ["./api/*"]
    }
  },
  "include": ["scripts", "worker/**/*", "api", "tests/**/*", "types"]
}
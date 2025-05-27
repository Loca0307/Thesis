### Presigning packages

Not all data receivers will have an S3 bucket or ICAV2 project for us to dump data in.  

Therefore we also support the old-school presigned url method.  

We can use the following command to generate presigned urls in a script for the package

```bash
data-sharing-tool presign-package \
  --package-id pkg.12345678910
```

This will return a presigned url for a shell script that can be used to download the package.
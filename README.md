# FINRA Ref Resolver

A python API to resolve `$ref` pointers in json-schemas and inline them. Supports relative file paths in `$ref`.
This is particularly customized for FINRA API json schema.
Thanks for the original source at https://github.com/purukaushik/ref-resolver/blob/master/README.md

## Example code invocation

1. install required packages for ref_resolver.py
2. run main.py

## FINRA special notes
- U4Filing.json is included here and set as start point. You can change to any other base json schema.
- some $ref links need credentials to access. Put a hardcode mapping here. This may change in the future. 


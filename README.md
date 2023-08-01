## Requirements
 - \>= Python 3.8
 - pip

## Instructions

### Setup
1. Clone this project onto your local machine.
2. From the project root run `python -m build`
3. From the project root run `pip install .`
4. You may need to add your python installation to your PATH
    - `cd ~`
    - `vi .zshrc` or `vi .bash_profile`
    - add `export PATH=$PATH:<path/to/your/python>/bin`

### Running the CLI
```
 snyk_agg_fixes generate-issues-data \
 --orgid=<ORG_ID> \
 --api-token=<API_TOKEN> \
 --project=<PROJECT_ID>
 -d

```
Note: `-d` is optional. If omitted, the .snyk file will be output in the current working directory.
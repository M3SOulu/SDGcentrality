# Installation guide

This files contains instructions on how to install and run each tool used in the data gathering process.

## Code2DFD

Download `Code2DFD` from its official [repository](https://github.com/tuhh-softsec/code2DFD).

Data presented in this package/paper were generated with the [c65b4a](https://github.com/tuhh-softsec/code2DFD/tree/c65b4a081ed2ca1618319e5dabf9ecf590988059) version of the tool.

Install its dependencies from [requirements.txt](https://github.com/tuhh-softsec/code2DFD/blob/c65b4a081ed2ca1618319e5dabf9ecf590988059/requirements.txt) as 

```
python -m pip install -r requirements.txt
```

The tool can be executed as 

```
python -m code2DFD.py --repo_url PATH_TO_REPO
```

in the cloned directory, where `PATH_TO_REPO` is a path to the repository that should be analysed (either local path or full GitHub URL).

Optionally, it is possible to provide a commit hash to checkout and analyse a specific commit:

```
python -m code2DFD.py --repo_url PATH_TO_REPO --commit HASH
```

For an analysed project, the tool will generate a folder `code2DFD_output/REPO_NAME/COMMIT` with the results for a specific commit from a specific repo.

Such results folders are presented here in [raw_data/code2dfd](raw_data/code2dfd).

## Working with the package scripts
Install the following Python packages: `networkx`, `pandas`, `requests`.
If you want to replicate a specific tool, follow its instructions on how to properly set it up.


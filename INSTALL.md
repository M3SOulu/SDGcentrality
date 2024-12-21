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

## Understand by SciTools

Download and install Understand from the [official website](https://licensing.scitools.com/download).

The data in this package are generated using version `6.5.1201`.

Request an Educational/Academic license at the appropriate step.

Change the variable `UND_PATH` in the [understand script](Scripts/metrics_understand.py) to point to the `und` [cli tool](https://support.scitools.com/support/solutions/articles/70000582798-using-understand-from-the-command-line-with-und) on your system.

## Working with the package scripts
Install the following Python packages: `networkx`, `pandas`, `requests`.
If you want to replicate a specific tool, follow its instructions on how to properly set it up.


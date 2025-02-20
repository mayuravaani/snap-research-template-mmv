# Repository Template for Reproducible Research

**Click "Use this template"** at the top of the webpage on GitHub to create a new repository with the same folder structure. You can then add your own files and edit this README for your particular project.

- This simple project structure template repository is adapted from https://github.com/UtrechtUniversity/simple-python-template. 
- You can find a guide to getting set up with Git, and slides from a workshop on reproducible research, in the `doc/` folder.
- See [here](https://github.com/DenisMot/Python-minimal-install) for a useful guide to installing a minimal Python environment and setting up in VS Code and conda.
- For more detail on Git, see [this great free tutorial](https://swcarpentry.github.io/git-novice/) 
- If you plan to develop a package, check out the [template repository for a Python package](https://github.com/UtrechtUniversity/re-python-package).

## How to run this code 

*Update for your specific project*

### You will need

-   Git (configured: check with `git config --list` )

    -   `git config --global user.name "Your Name"`

    -   `git config --global user.email "you@example.com"`

    -   For complete instructions, see `doc/git_setup_guide.md`

-   Python (latest stable version, e.g., 3.10+)

-   An active GitHub account

-   A terminal or IDE of your choice (VS Code recommended)

### Clone this repository 

```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

### Change directory to this folder

```sh
cd YOUR-REPO-NAME
```

### Set up virtual environment
1. Create a virtual environment: `python -m venv venv`
2. Activate the environment:
    - Windows: `source venv/Scripts/activate`
    - Linux/macOS: `source venv/bin/activate` 
3. Install required packages: `pip install -r requirements.txt`
    - If you haven't yet set up this file, you can first install the required packages, then use `pip freeze > requirements.txt` to write all the dependencies (and their versions) to this file. *Note that this can be a bit overkill with the number of dependencies listed: see [here](https://calmcode.io/course/pip-tools/compile) for an improved method.*

### Execute code
*For example: change these based on your specific files, and add detail about what each step involves*
```
python scripts/01_get_data.py
python scripts/02_clean_data.py
python scripts/03_analysis.py
```

## Project Structure
*Recommended: change based on your specific files. For example, you may also want a `src/`, `models/` or `notebooks/` folder. (If you are inside `notebooks/` you will likely want to put `sys.path.append(os.path.abspath(".."))` at the start of your notebook, so that you can import funcs from `scripts/`*

```
.
├── README.md          <- Overview of the project, how to install and use 
├── LICENSE            <- License for open-source projects
│── CITATION.cff       <- Citation file for academic use
├── .gitignore         <- Files to ignore (e.g., __pycache__, logs, data)
├── requirements.txt   <- Dependencies (if using pip: use environment.yml if using conda)
├── venv               <- Virtual environment (git ignored)
├── data/              <- Data directory (typically ignored in version control)
│   ├── raw/           <- Raw input data (DO NOT MODIFY!)
│   └── processed/     <- Processed datasets
├── doc/               <- Written reports, papers, and documentation
│   ├── project_overview.md
│   ├── final_paper.pdf
├── outputs/           <- Outputs like figures, results, model
│   └── figs/          <- Plots and figures
└── scripts/           <- Your codes
    ├── utils.py       <- Functions used by multiple scripts
    ├── 01_get_data.py
    ├── 02_clean_data.py
    └── 03_analysis.py

```

## Share your software

1. Link Zenodo to your GitHub account
2. Use Zenodo to create a DOI for the current version of this repo
2. Use this DOI when creating a citation file for your repository using [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/#/)

## License

This project is licensed under the terms of the [MIT License](/LICENSE).

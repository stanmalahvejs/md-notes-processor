# md-notes-processor

A toolset for processing structured [Markdown](https://en.wikipedia.org/wiki/Markdown) notes in a Git repository.

Table of contents:

- [md-notes-processor](#md-notes-processor)
    - [Features](#features)
    - [Usage](#usage)
    - [Structure of the notes repository](#structure-of-the-notes-repository)
        - [Valid README.md file](#valid-readmemd-file)
            - [YAML frontmatter structure](#yaml-frontmatter-structure)
    - [Development docs](#development-docs)

## Features

This repository produces a Docker image, that contains:

- [markdownlint](https://github.com/DavidAnson/markdownlint)

## Usage

Run the dockerimage and mount the notes respository at the path '/notes' as following:
`docker run -v ./notes-repo:/notes stanmalahvejs/md-notes-processor:latest /scripts/lint-notes.py`

## Structure of the notes repository

- Every directory in the repository, that contains a `README.md` file, is a note. The repository itself is not a note.
- A valid note satisfies the following rules:
    - Contains a [valid README.md file](#valid-readmemd-file).
    - Directory name equals to the top-level heading in the `README.md` file in [Kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case).
        - For example, for the top-level heading `Common notes`, the directory name should be `common-notes`.
    - Does not contain any other `.md` files.
    - Can contain files of any different format (for example, CSV or JSON). File extension matches the file format whenever possible.
    - Can contain other notes.
    - Can contain subdirectories.

### Valid README.md file

- [markdownlint](https://github.com/DavidAnson/markdownlint) shows no violations in the file.
- Starts with a [YAML frontmatter](https://jekyllrb.com/docs/front-matter/) with specific [YAML frontmatter structure](#yaml-frontmatter-structure), followed by one empty line.
- The rest of the file is a free form markdown content of the note.
    - Internal links within the repository point to existing notes.

#### YAML frontmatter structure

- The frontmatter serves as data container for organizing notes into structured system of objects, that can be handled by the md-notes-processor.
- Mandatory fields:
    - `types` - list of string values. Denotes the types this note belongs to. Example values: `problem`, `task`.
  
## Development docs

See in [the separate file](docs/development.md).

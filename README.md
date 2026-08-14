# CryptoLabX

CryptoLabX is a semester-long, modular cryptanalysis toolkit developed for the
Week 1 foundation assignment.  This first version establishes the project
layout, a command-line foundation, reusable datasets, file handling, logging,
and basic text analysis.  It deliberately does **not** implement encryption,
decryption, or attack algorithms yet.

## Team members

| Name | Student ID | Contribution |
| --- | --- | --- |
| Rakshit Kumar Jain | 2024UCP1335 | Project coordination CLI and logging |
| Krishna Yadav | 2024UCP1417 | File analysis and datasets |


## Project structure

```text
CryptoLabX/
├── classical/       # Future classical ciphers (Caesar, Vigenere, etc.)
├── attacks/         # Future cryptanalytic attack implementations
├── math/            # Number-theory and mathematical helper functions
├── modern/          # Future modern cryptography modules
├── analysis/        # File and frequency-analysis utilities
├── datasets/        # Plain-text samples used for testing and analysis
├── outputs/         # Generated analysis results and future reports
├── docs/            # Project documentation
├── tests/           # Automated unit tests
├── utils/           # Shared helpers, including future logging support
├── main.py          # Menu-driven application entry point
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

## Week 1 functionality

The main program presents options for **Encrypt**, **Decrypt**, **Attack**,
**Analyze**, and **Exit**.  The first three options are placeholders for future
weeks.  Every menu selection should be recorded with its date and time in a
log file.

The file-analysis component is ready for the Analyze option.  It reads a UTF-8
text file and displays:

- total characters;
- total words;
- total lines;
- number of unique characters; and
- case-insensitive letter frequency.

It can also be run on its own while the main menu is being integrated:

```bash
python3 -m analysis.file_analyzer datasets/sample_message.txt
```

Example output:

```text
File analysis: sample_message.txt
Characters: 73
Words: 13
Lines: 2
Unique characters: 23
Letter frequency: a: 5, b: 2, c: 1, d: 1, e: 8, ...
```

Five starter text files are included in `datasets/`: `sample_message.txt`,
`english_paragraph.txt`, `short_story.txt`, `quotes.txt`, and
`mixed_content.txt`.  These are intentionally small and varied so they can be
used in later testing, cipher exercises, and frequency-analysis comparisons.

## Running and testing

Use Python 3.10 or newer.  No third-party package is required for the Week 1
file analyzer.

```bash
python3 -m unittest discover -s tests -v
python3 -m analysis.file_analyzer datasets/english_paragraph.txt
```

## Future modules

Later milestones will add classical cipher implementations, cryptanalytic
attacks, statistical visualizations, mathematical utilities, modern-crypto
experiments, and richer command-line workflows.  Each feature should remain in
its appropriate module with matching tests and documentation so CryptoLabX
stays maintainable as it grows.

## Collaboration workflow

Before starting work, update the shared branch.  Develop on a personal feature
branch, test locally, commit with a descriptive message, push the branch, and
open a pull request for review.  This preserves each member's contribution and
makes merging safer.

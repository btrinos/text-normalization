# text-normalization
Text Normalization Project

Certainly! Here's a README.md file for the `normalize.py` script:

---

# Text Normalization Project

This repository contains the `normalize.py` script which aims to normalize text from a given `.txt` file. The normalization process helps in converting text into a consistent and standardized format, making it easier for subsequent analyses, comparisons, or other text processing tasks.

## Features

- Convert all characters to lowercase.
- Remove punctuation.
- Remove extra whitespace (e.g., multiple spaces, tabs, newlines).
- Exclude numeral characters.
- Remove common stopwords (like "and", "the", "is").

## Dependencies

- Python 3
- NLTK library (Natural Language Toolkit)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/btrinos/text-normalization.git
   cd text-normalization
   ```

2. (Optional) It's a good practice to create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install nltk
   ```

4. Download the NLTK stopwords (you only need to do this once):
   ```python
   import nltk
   nltk.download('stopwords')
   ```

## Usage

1. Place the `.txt` file you want to normalize in the same directory as the `normalize.py` script.
2. Rename the file to `document.txt` or modify the script to read from your filename.
3. Run the script:
   ```
   python normalize.py
   ```

4. The normalized content will be saved in `normalized_document.txt`.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Any contributions, whether it's refining the algorithm, improving documentation, or adding features, are highly appreciated!

## License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

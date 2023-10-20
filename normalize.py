# Import necessary libraries
import string
import nltk
from nltk.corpus import stopwords

# References: 
# https://www.nltk.org/
# https://www.assemblyai.com/blog/word-error-rate/ (how to normalize text for processing)

# Download the stopwords from nltk (if not already downloaded).
# Uncomment the line below if running for the first time.
# nltk.download('stopwords')

# Create a set of English stopwords for easy lookup
stop_words = set(stopwords.words('english'))

# Convert the entire text to lowercase
def lowercase(text):
    return text.lower()

# Remove punctuation from the text using string's punctuation list
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Convert any sequence of whitespace characters (spaces, tabs, newlines) to a single space
def remove_extra_whitespace(text):
    return ' '.join(text.split())

# Remove all numeral/digit characters from the text
def remove_numerals(text):
    return ''.join([i for i in text if not i.isdigit()])

# Remove common words (stopwords) that might not add significant meaning
def remove_stopwords(text):
    words = text.split()
    return ' '.join([word for word in words if word not in stop_words])

# Main normalization function that combines all the above steps
def normalize_text(text):
    text = lowercase(text)
    text = remove_punctuation(text)
    text = remove_extra_whitespace(text)
    text = remove_numerals(text)
    text = remove_stopwords(text)
    return text

# Main execution function
def main():
    # Open and read the content of the original document
    with open('document.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize the content using the above-defined function
    normalized_content = normalize_text(content)

    # Write the normalized content to a new file
    with open('normalized_document.txt', 'w', encoding='utf-8') as f:
        f.write(normalized_content)

# Ensure the main function is executed only when the script is run directly (and not imported elsewhere)
if __name__ == '__main__':
    main()
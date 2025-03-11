# Text Summarization using TextRank and BART

## Overview
This repository provides a simple yet powerful text summarization tool that integrates both **extractive** and **abstractive** methods:

- **TextRank**: A graph-based extractive summarization algorithm that selects key sentences based on importance.
- **BART (Bidirectional and Auto-Regressive Transformer)**: An abstractive summarization model that rephrases and condenses text.

This tool enables users to input an article and receive a concise, well-structured summary through a graphical user interface (GUI).

---

## Features
- **Hybrid Summarization**: Combines TextRank for extractive summarization and BART for abstractive summarization.
- **User-Friendly GUI**: A simple interface for entering text and obtaining summaries.
- **Pre-trained Models**: Uses pre-trained embeddings (GloVe) and transformers (BART) for effective results.
- **Customizable Parameters**: Allows tuning of summarization settings.

---

## Installation & Setup
### Prerequisites
Ensure you have Python 3.7+ installed.

### Steps to Set Up the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/rohitpugazh/Text-Summarization-using-TextRank-BART.git
   cd Text-Summarization-using-TextRank-BART
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download GloVe Vectors** (for TextRank)
   - Download **Wikipedia 2014 + Gigaword 5 GloVe vectors** from [this link](https://nlp.stanford.edu/projects/glove/).
   - Place the downloaded file in the appropriate directory as specified in the project.

4. **Run the GUI**
   ```bash
   python gui.py
   ```
   The GUI will launch, allowing you to input text and generate summaries.

5. **(Optional) Run Summarization Script**
   If you prefer running the summarization without the GUI, use:
   ```bash
   python combinedsummary.py
   ```

---

## Usage
### GUI Mode
1. Launch `gui.py`.
2. Enter the text/article you want to summarize.
3. Click the **Summarize** button.
4. View the extracted and generated summary.

### Command Line Mode
1. Modify `combinedsummary.py` to include your input text.
2. Run the script to generate a summary.
3. The summarized text will be displayed in the console.

---

## File Structure
```
Text-Summarization-using-TextRank-BART/
│── gui.py                 # GUI application for summarization
│── combinedsummary.py     # Main script integrating TextRank and BART
│── requirements.txt       # Dependencies
│── utils.py               # Helper functions for text processing
│── models/                # Pre-trained models and embeddings
│── data/                  # Sample text files (if applicable)
│── README.md              # Project documentation
```

---

## Dependencies
- **Python 3.7+**
- **NLTK** (for TextRank processing)
- **Transformers** (for BART model)
- **Gensim**
- **Tkinter** (for GUI)
- **Torch** (for deep learning computations)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- **TextRank**: Inspired by the PageRank algorithm.
- **BART Model**: Provided by [Hugging Face](https://huggingface.co/facebook/bart-large-cnn).
- **GloVe Embeddings**: From Stanford NLP Group.

For any questions or issues, feel free to open an issue on GitHub.


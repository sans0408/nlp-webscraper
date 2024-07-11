import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, CFG, Nonterminal, ProbabilisticProduction
from tabulate import tabulate

def scrape_and_analyze(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ''.join([para.text for para in paragraphs])
        text = re.sub(r'\[[0-9]*\]', '', text)

        # Tokenize Text
        tokens = tokenize_text(text)

        # POS Tagging
        pos_tags = pos_tagging(text)

        # Frequency Distribution
        freq_dist = frequency_distribution(text)

        # Create Grammar
        grammar = create_grammar()

        # Encode and Decode Text
        encode_decode_text(text)

        # Format POS Tags and Frequency Distribution as HTML tables
        pos_table = format_table(tabulate(pos_tags, headers=['Token', 'POS'], tablefmt='html'))
        freq_table = format_table(tabulate([(word, freq, f"{(freq/sum(freq_dist.values()))*100:.2f}%") for word, freq in freq_dist.items()],
                                           headers=['Word', 'Count', 'Frequency %'], tablefmt='html'))

        return pos_table, freq_table, grammar
    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}", "", ""

def tokenize_text(text):
    nltk.download('punkt', quiet=True)
    return word_tokenize(text)

def pos_tagging(text):
    nltk.download('averaged_perceptron_tagger', quiet=True)
    tokens = word_tokenize(text)
    return pos_tag(tokens)

def frequency_distribution(text):
    tokens = word_tokenize(text)
    return nltk.FreqDist(tokens)

def create_grammar():
    S = Nonterminal('S')
    NP = Nonterminal('NP')
    VP = Nonterminal('VP')
    V = Nonterminal('V')
    Det = Nonterminal('Det')
    N = Nonterminal('N')

    # Define production rules with probabilities
    productions = [
        ProbabilisticProduction(S, [NP, VP], prob=1.0),
        ProbabilisticProduction(NP, [Det, N], prob=0.8),
        ProbabilisticProduction(NP, [N], prob=0.2),
        ProbabilisticProduction(VP, [V, NP], prob=1.0),
        ProbabilisticProduction(Det, ['the'], prob=0.6),
        ProbabilisticProduction(Det, ['a'], prob=0.4),
        ProbabilisticProduction(N, ['cat'], prob=0.3),
        ProbabilisticProduction(N, ['dog'], prob=0.7),
        ProbabilisticProduction(V, ['chased'], prob=1.0)
    ]

    grammar = CFG(S, productions)
    return '\n'.join([str(prod) for prod in grammar.productions()])

def encode_decode_text(text):
    encoded_text = text.encode('utf-8')

    decoded_text = encoded_text.decode('utf-8')
    if text == decoded_text:
        print("No changes detected between encoded and decoded text.")
    else:
        print("Warning: There are changes between encoded and decoded text!")

def format_table(table_html):
    styled_html = f'''
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: left;
        }}
        th {{
            background-color: rgba(0, 0, 0, 0.1);
        }}
        tr:nth-child(even) {{
            background-color: rgba(255, 255, 255, 0.1);
        }}
    </style>
    {table_html}
    '''
    return styled_html
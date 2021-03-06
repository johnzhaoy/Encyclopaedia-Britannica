# Uses Regular Expression to extracts TERMS (uppercase words)
import re


def extract_terms(vol):
    terms = []

    for index, row in vol.iterrows():
        f = open('txt/' + row['file_name'], 'r', encoding="utf8")
        content = f.read()
        terms_ing = []
        terms_ing = re.findall('[A-Z][A-Z]+', content)  # a TERMS should start from at least two uppercase words
        terms = terms + terms_ing
        f.close()

    df = pd.DataFrame(terms, columns=['TERMS'])
    df['Term_length'] = df['TERMS'].str.len()

    return df


# drop the TERMs shorter than 2 letters or longer than 15 letters
df_firstvol = df_firstvol[df_firstvol['Term_length'] > 2]
df_firstvol = df_firstvol[df_firstvol['Term_length'] <= 15]

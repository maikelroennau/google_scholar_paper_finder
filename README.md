# Google Scholar Paper Finder

An engine that searches for papers on Google Scholar based on keywords extracted from a text.

## Requeriments

- [rake-nltk](https://github.com/csurfer/rake-nltk)
- [TextRank](https://github.com/davidadamojr/TextRank)
- [Scholar](https://github.com/ckreibich/scholar.py) - already included and with a little change, just to return the results

## Components

- search.py: responsible for reading the text and extracting the keywords.
- scholar.py: responsible for searching on Google Scholar, developed by Christian Kreibich, avaliable at [repository](https://github.com/ckreibich/scholar.py)
- text.txt: simple text talking about deep learning. Should return related papers.

## Usage

`python search.py text.txt`

### Author

**Maikel Maciel Rönnau**  
*Computer Scientist  
maikel.ronnau@gmail.com  
[Linkedin](https://br.linkedin.com/in/maikelronnau) - [GitHub](https://github.com/maikelronnau)*

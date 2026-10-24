# Assignment 2

This project inspects and cleans two corrupted text datasets using Python.
Each script saves a random sample of 10 lines and its cleaned version before
processing the full dataset.

## Datasets

Both datasets mainly contain English text: movie dialogue and informal Twitter posts.

| Dataset | Original lines | Cleaned lines |
| --- | ---: | ---: |
| Movie corpus | 304,713 | 304,713 |
| Twitter corpus | 16,556 | 10,512 |

The Twitter dataset contains many lines consisting only of HTML, noise symbols,
or emoji. After cleaning, 6,044 lines become empty and are removed.

## Cleaning Methods

- Decode HTML entities such as `&amp;` using `html.unescape()`.
- Remove HTML tags using regular expressions.
- Remove URLs if present. No URLs matching `http://`, `https://`, or `www.` were detected in these input files.
- Remove standalone noise symbols such as `@`, `$`, `%`, and `^^`, and the `+++$+++` marker where present.
- Remove emoji from the Twitter dataset using the `emoji` package.
- Normalize whitespace and discard lines that become empty.

Ordinary punctuation, capitalization, hashtags, @accounts, dollar amounts,
and percentages are preserved to retain meaning. The scripts do not correct
spelling or remove duplicate lines.

## Files

| Files | Purpose |
| --- | --- |
| `clean_movie.py` | Clean the movie corpus. |
| `clean_twitter.py` | Clean the Twitter corpus, including emoji removal. |
| `corrupt_movie_corpus.txt`, `corrupt_twitter_corpus.txt` | Original input files. |
| `cleaned_movie_corpus.txt`, `cleaned_twitter_corpus.txt` | Cleaned full datasets. |
| `movie_sample_input.txt`, `twitter_sample_input.txt` | Random samples of 10 original lines. |
| `movie_sample_output.txt`, `twitter_sample_output.txt` | Corresponding cleaned sample lines. |

Sampling uses seed `42` so repeated runs select the same lines. Sample outputs
retain empty positions for comparison; only the full outputs discard empty lines.

## How to Run

Place both scripts and both original TXT files in the same folder. Run the
following commands from that folder:

```bash
uv add emoji
uv run clean_movie.py
uv run clean_twitter.py
```

For a cloned project with dependencies already declared, use `uv sync`
instead of `uv add emoji`.

Each script writes its sample files and cleaned output beside the script and
prints one line-count summary.

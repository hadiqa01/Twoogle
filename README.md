# Twoogle
***Twoogle*** is a Twitter **sentiment analysis** search engine for retrieving and classifying real-time COVID-19 vaccination-related tweets. The application is powered by [DistilBERT](https://arxiv.org/abs/1910.01108) fine-tuned on [Coronavirus Tweets Dataset](https://ieee-dataport.org/open-access/coronavirus-covid-19-tweets-dataset#files).

## Quick Start

Included in this repository is a large (> 250 MB) pre-trained model. This model was trained on a subset of the above dataset. First install the [Git Large File Storage](https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage) (Git LFS) extension to retrieve this model during cloning.

Once Git LFS is successfully installed, clone this repository and `cd` into the root folder:
> `git clone https://github.com/hadiqa01/Twoogle.git && cd Twoogle/`

Run the following commands (preferrably from a **Python virtual environment**):

> 1. `pip3 install --upgrade pip`
> 2. `pip3 install -r requirements.txt`
> 3. `python3 main.py`

Then go to the following address in your browser:
> `127.0.0.1:5000/`

The webpage is a simple interface that allows you to search for **real time** tweets using a query of your choice. <br>
For a query with multiple terms, we recommend that you explicitly concatenate the terms: <br>

<!-- ![Query Example](images/query_ex.png "Query Example") -->
<img src="images/query_ex.png" height="250" title="Query Example"/>

## Using Arbitrary Text

You can also try out the model using copied tweets or text of your choice. To do this, simply run `analyze.py` with a text string argument from the root folder of the repository (ensure Git LFS is already installed):

> `python3 analyze.py "Not sure what to think but perhaps the Moderna shots work."` <br>
> returns <br>
> `The sentiment for the text 'Not sure what to think but perhaps the Moderna shots work.' is POSITIVE with a probaility of 0.98905.`
> <br> <br>
> `python3 analyze.py "Does the J&J one-shot vaccine work at all? Asking for a friend."` <br>
> returns <br>
> `The sentiment for the text 'Does the J&J one-shot vaccine work at all? Asking for a friend.' is NEGATIVE with a probaility of 0.99597.`

**Note**: The example texts **do not** necessarily reflect the sentiments (no pun intended) of the team.

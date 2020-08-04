# MovieRecomendationSystem
Prabhat Kr. Singh
Servendra Singh
Sanal Mishra
Yash Kr. Singh(Team Leader)
Movie Recomendation System
<h1>WHAT IS THIS PROJECT?</h1>
Recommender System is a system that seeks to predict or filter preferences according to the user’s choices. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general.
Recommender systems produce a list of recommendations in any of the two ways –
Content-based filtering: Content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user’s preferences. It recommends items based on user’s past preferences(supervised learning).
Collaborative filtering: Collaborative filtering approaches build a model from user’s past behavior (i.e. items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that user may have an interest in(unsupervised learning).
<h1>Dependencies</h1>
Python >=3.5
pandas
numpy
scipy
scikit-learnThe sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction
Textblob
What is TextBlob?
TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
scikit-surprise
lightfmLightFM is a Python implementation of a number of popular recommendation algorithms for both implicit and explicit feedback. It also makes it possible to incorporate both item and user metadata into the traditional matrix factorization algorithms.
matplotlib
seabornWhat is Seaborn?
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
Pycharm
GIT
Github
<h1>WHY GIT & GITHUB?</h1>
Git is a version control system that lets you manage and keep track of your source code history.
GitHub is a cloud-based hosting service that lets you manage Git repositories. If you have open-source projects that use Git, then GitHub is designed to help you better manage them.
<h1>WHAT IS TKINTER</h1>
Python offers multiple options for developing GUI (Graphical User Interface).Out of all the GUI methods, tkinter is the most commonly used method.It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications.Creating a GUI using tkinter is an easy task.
<h1>Details about Dataset</h1>
We have used MovieLens dataset in order to build movie recommendation engine.
Types of dataset:-
The full dataset: This dataset consists of 26,000,000 ratings and 750,000 tag applications applied to 45,000 movies by 270,000 users. Includes tag genome data with 12 million relevance scores across 1,100 tags.
The small dataset: This dataset comprises of 100,000 ratings and 1,300 tag applications applied to 9,000 movies by 700 users.
<h1>Data description</h1>
It contains 100004 ratings and 1296 tag applications across 9125 movies. These data were created by 671 users between January 09, 1995 and October 16, 2016. This dataset was generated on October 17, 2016.
Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.
The data are contained in the following files:-
credits.csv
keywords.csv
links.csv
links_small.csv
movies_metadata.csv
ratings.csv
ratings_small.csv

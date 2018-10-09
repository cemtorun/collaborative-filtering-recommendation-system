# collaborative-filtering-recommendation-system

Recently, I’ve been really interested in being able to using predictive analytics to better understand user preferences and predict their preferences in the future. 

That is what this project aims to do!

So what is collaborative filtering? Collaborative filtering (CF) is a technique used by recommender systems.

In the newer, narrower sense, collaborative filtering is a method of making automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating). The underlying assumption of the collaborative filtering approach is that if a person A has the same opinion as a person B on an issue, A is more likely to have B's opinion on a different issue than that of a randomly chosen person.

The data set used was taken from MovieLens. It contains 100,000 ratings from a total of 1000 users on 1700 movies. 

I will be using the Surprise library. Surprise is a Python scikit building and analyzing recommender systems. For more about the library and its documentation vist: http://surpriselib.com.

Surprise is awesome because within a few lines we are able to do cross validation of the entire data set. Cross validation is when we take our training data and split it into "folds". To give an example, if we split the data in to four folds, we will use folds 1, 2, and 3, in the training set to train on the 4th fold that is also part of the training set. Then we would use folds 2-4 and train it on the 1st fold, etc. Then we average the error of the folds. We can then choose the model that provides us the lowest mean error. This allows us to test different models while also maximizing the size of the testing and training data sets.

Since the whole purpose of this project is to predict how a user will rate a movie given data on individuals who have watched that movie and similar movies like the given user, I will use root mean squared error (RMSE) and with mean squared error (MSE) to determine the difference.


Note: this was one of my first projects in the space so there was a similar walkthrough through a previous tutorial that I did myself learning how the individual did it and writing my own documentation and learning throughout the process.



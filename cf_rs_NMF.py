from surprise import Reader, Dataset
from surprise import NMF, evaluate

# creating the format for the dataset when given the user, item, rating and timestamp
data_reader = Reader(line_format="user item rating timestamp", sep="\t")

# store the data in the specific format created above
# u. data is the data we want
data = Dataset.load_from_file("./ml-100k/u.data", reader=data_reader)

# will be splitting the data into 5 folds for cross validation
data.split(n_folds=5)

# for this project I will be using the NMF algorithm
algorithm = NMF()
evaluate(algorithm, data, measures=["RMSE", "MAE"])

# train the whole data set now
training_set = data.build_full_trainset()
algorithm.train(training_set)

# set the specific user and movie I want to predict
user_id = str(200)
item_id = str(222)
actual_rating = 5

# see how it works!
print(algorithm.predict(user_id, item_id, actual_rating))

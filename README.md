# E2S-Price-and-Location-Predictor

### Hello
This is my machine learning model for which I created using a dataset (with more than 7500+ data enteries) from a B2B start-up Excess2Sell. The company takes in excess inventory from a member (seller) and finds a client (buyer) which requires those items and sells it to them with a slight hike on the selling price which has been initially set by the seller. These models helps in predicting the price in which the seller's item will be sold also in which part of the country it will be sold.

Thus I have created 2 models, first one being a price predictor and the second one being a location predictor, the description of the files present in the git are as follows:
* .joblib files are the final models which have been exported in the directory after having been tested in the Jupyter (these havent been shared in the git but when you run your jupyter file they should be available with ease)
* .ui file is the PyQt5 frontend which was deseigned in Qt Designer and E2S_GUI.py is its corresponding python file
* .ipynb file is the Jupyter file in which I have tested and created both the models
* gui_testing.py is the final py file in which I have bought together all the above GUI and models in one single run

**The dataset has not been added to the git, if anyone requires they can contact me directly for the needed.**

### The dataset contains of the following attributes:
* Seller State
* Seller Location
* Product Group
* Product Category
* Product Subcategory
* Product Offered
* Quantity
* Actual Price (of the product offered)
* Seller Price
* Buyer Price
* Buyer Location

### Prerequisites Required:
* Python 3.10
* Scikit-Learn
* Jupyter
* Qt Designer
* PyQt5
* Joblib
* Pandas
* NumPy
* VScode

#### Working of the Program: https://drive.google.com/file/d/1v3YJWjlkDnVe6b9xrfGggAn3f7vIL9VA/view?usp=sharing

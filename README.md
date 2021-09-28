Steps to get results of the analyses on the Airbnb dataset:

⦁	First the datasets need to be cleaned and so, the 'Calendar_Cleaning.py' ,'Review_Cleaning.py'  and 'Listings_Cleaning.py' files should be executed to clean Calendar, Review and Listings tables respectively.

⦁	After the files are cleaned, a connection is needed to be established between the Python file and SQL Server. For that SSMS i.e. SQL Server Management Studio should be installed and then cleaned tables should be uploaded in the database. Following this, 'connectionToSQL.py' file should be executed to set up the connection.

⦁	Total number of amenities are then found from amenities column of Listings table. Run the 'adding amenities.py' file for this purpose.

⦁	Some queries are then run to manipulate the tables for performing some visualizations and analysis. Some of the queries include joining the tables, fetching information like total number of listings and reviews in a neighborhood, etc., and then the generated output table needs to be saved in the CSV file format. For this, 'SqlToCsv.py' file should be executed.

⦁	Some visualizations are then performed to get some meaningful insights from the data. For this 'visualization.py' should be executed.
⦁	For the first application i.e. Boosting Reservations, a multivariate regression model has been built. 'Boosting Reservation.py' file should be executed to obtain the results of this application.

⦁	For the second application i.e. Price Prediction, first a KPrototype clustering model is built to get most preferred neighborhoods in each city. For this, 'KPrototype Clustering.py' file is to be executed. This program generates an Excel sheet which adds clusters to the Listings table.

⦁	To develop a price prediction model, few factors along with clusters are provided as input to the regression model. To get output of this model, 'price_prediction.py' file should be executed.

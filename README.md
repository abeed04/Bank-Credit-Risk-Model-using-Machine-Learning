<h1 align="center">Bank Credit Risk Model using Machine Learning</h1>
<h2 align="center">Introduction</h2>

<img  align="right" src="https://www.shutterstock.com/image-vector/credit-risk-word-cloud-collage-260nw-1167365344.jpg" />

- 👨‍💻This project implements a bank credit risk prediction model using a Decision Tree classifier built with Python's scikit-learn library. It also demonstrates the deployment of this model as a web application using Flask for user interaction.

-  🔭 Built robust credit risk models that go beyond traditional credit scoring methods in banks. This model 
  can analyze vast datasets of historical loan data, customer profiles, and relevant factors, leading to 
  more accurate predictions.

- ⚡This project demonstrates proficiency in machine learning, data analysis, data visualization, and model building for real-world financial applications.

pen_spark


<h3 align="left">Requirements</h3>

- Python 3.x
- pandas
- numpy
- Scikit-learn
- Flask

  
<h2 align="center">Data Cleaning and Feature Engineering</h2>

- Performed data cleaning techniques like finding Null values, Outliers, Imputations and then performed EDA over the data in google colab using python.

- In Feature engineering performed Chi square test, Anova test, VIF, Multicollinearity, Label Model seencoding, One hot encoding and Data wrangling by which some of the columns were removed which were not useful for further process of model building and finally we had 37 columns.

- After performing all necessary actions created a new csv file named 'Clean_Bank_Data' which was used further in deployment of model.

<h2 align="center">Training the Model</h2>
<img  align="right" height=330 width=430 src="https://www.krasamo.com/wp-content/uploads/0730Building-ML-Models.jpg" />



- To deploy this model we used pycharm platform and flask framework.
-  Loads the data from the CSV file "Clean_Bank_Data".
- Encode categorical features using LabelEncoder from scikit-learn.
- Split the data into training and testing sets (8:2).
- Random Forest Algorithm, Desicion tree algorithm and logistic regression algorithms were used on training data as it was a task of classification.
- Desicion Tree Algorithm gave the best results of classification report .

- Evaluate the model's performance on the testing set.

- Save the trained model using pickle as "model.pkl".
  
<h2 align="center">Deployment</h2>

-  To deploy this model we used pycharm platform and flask framework .
-  Run deploy.py to start the Flask application.. This script defines two routes:
-  1) Renders the index.html template (if provided).
   2) Handles user input, makes predictions using the loaded model, and displays the result (either in the template or directly).

<h2 align="center">Customization</h2>

- You can modify the model training (in main.py) to explore different machine learning algorithms, hyperparameter tuning, and feature engineering techniques.
- You can customize the Flask application (in deploy.py) to create a more user-friendly interface with forms and informative output.
- Consider using a templating engine like Jinja2 for more complex layouts in index.html.
- For production deployment, explore options like containerization with Docker or cloud platforms like Heroku.

<h2 align="center">Use Cases</h2>

-  Major use cases are a streamlined loan approval process, reduced risk of defaults, improved loan portfolio management, and personalized loan offers. 
-  Banks make more informed lending decisions, potentially reducing defaults and improving their overall risk profile.
-  Banks can segment their customer base based on predicted credit risk. This allows for targeted marketing campaigns, customized product offerings.
-  The model can be used to identify existing customers who might be at higher risk of defaulting on their loans or credit card payments in the future.
-  A credit risk model can be used to help banks meet these regulatory requirements and ensure responsible lending practices. 

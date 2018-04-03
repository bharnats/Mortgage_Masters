# Predicting Loan Grades with a Neural Network: A Machine Learning Pipeline 

### The Problem Domain
Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first apply for home loan, after that company validates the customer eligibility for loan.

Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents,Applicant Income, Co-Applicant Income, Loan Amount, Credit History and others.

### Disclaimer: 
Looking at the problem statement, it is silly that one would try to automate decision based on replication of pasts decisions instead of optimizing for business result - minimizing loan default or fraud rate. Well, but the objective here is to play around with Machine Learning and practice Data munging with Python.

The problem was hosted for Data hack Contest in Analytics Vidhya. The dataset can be downloaded from the challenge page or from the direct link to the same dataset (here)[].
### Required libraries

Anaconda Python distribution is used to install most of the Python packages we need.
This notebook uses several Python packages that come standard with the Anaconda Python distribution. The primary libraries that is used here are:
•	NumPy: Provides a fast numerical array structure and helper functions.
•	Pandas: Provides a DataFrame structure to store data in memory and work with it easily and efficiently.
•	scikit-learn: The essential Machine Learning package in Python.
•	Keras :A high-level neural networks API, written in Python and capable of running on top of TensorFlow, enabling fast experimentation.
•	matplotlib: Basic plotting library in Python; most other Python plotting libraries are built on top of it.
To make sure we have all of the packages needed, install them with conda:
conda install numpy pandas scikit-learn matplotlib keras 


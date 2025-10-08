# Agriculture-Data-Dashboard
Goal of this project is to build a user-interactive dashboard for Agricultural Data so we can analysis the trends and make data driven decisions for the future.

### Requirements:
   1. Python IDE (VS Code Recommended)
   2. Power BI
   3. MySQL

Note: If you want to see only the Dashboard, skip the steps below and go to the step 5

### Install dependencies from requirements.txt
Run the command below on your terminal.

            pip install -r requirements.txt

## Step 1: 
            
            Download the sample_data file from the above.
            
## Step 2:

            Open any Python IDE ( VS Code Recommended )
            Download agri.py file from above,
                
Make sure to put the path of the sample_data file in ( pd.read_csv(r"file_path") ).

## Step 3:    
Open any one of the Python files ( agri.ipnd recommended ) for easier reading of the code.
Here I have done the EDA( Exploratory Data Analysis ) part, like,
Make sure it doesn't have any null values.
Performed some Analysis of the data using Seaborn and matplotlib

## Step 4:
After done with the EDA part, we import the data into MySQL database using SQLAlchemy.

Open MySQL Workbench, download, and import the .sql file from above.

Here you can find SQL queries regarding the data for some crucial insights
            
Change the password type in MySQL to standard incase if you get a connection error. Below is a preview,

<img width="776" height="37" alt="pass 1" src="https://github.com/user-attachments/assets/dceffc9d-bc72-4761-bfb0-e8e685a8bc8d" />  

to  

<img width="797" height="33" alt="pass 2" src="https://github.com/user-attachments/assets/a2743feb-8064-487d-a304-0a7ad8869c87" />


## Step 5:
For the dashboard, you can paste the link below into any one of the browsers of your choice.

            https://app.powerbi.com/view?r=eyJrIjoiM2U1ZDA0OTktNzgxYi00OWFkLTljMTQtOWM3OTdlYzQ4N2M4IiwidCI6ImE4YWY5NGE1LThhZWQtNDdjOC1iNzFhLTVlZjM5MmY5OGE1NSJ9&embedImagePlaceholder=true

Feel free to contact me for the actual .ipbx file in case you have Power BI and wanna implement or modify anything in the dashboard.
Below is a preview of the dashboard,
<img width="1322" height="747" alt="powerbi" src="https://github.com/user-attachments/assets/7c59feb1-cb64-434d-a4cb-2f67b553ef63" />

If you wanna address any issues or improvements, feel free to raise them via GitHub.

Thanks!






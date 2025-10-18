{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\"> <h1 style=\"color:green; margin-bottom:20px\">Reviewers comment v1</h1>\n",
    "\n",
    "Hello Jermaine!\n",
    "\n",
    "I'm happy to review your project today 🙌\n",
    "\n",
    "My name is **Gerardo Flores** and you can find me on the HUB as https://hub.tripleten.com/u/dea170e1\n",
    "\n",
    "You can find my comments under the heading **«Review»**. I will categorize my comments in green, blue or red boxes like this:\n",
    "\n",
    "<div class=\"alert alert-success\">\n",
    "    <b>Success:</b> if everything is done successfully\n",
    "</div>\n",
    "<div class=\"alert alert-warning\">\n",
    "    <b>Remarks:</b> if I can give some recommendations or ways to improve the project\n",
    "</div>\n",
    "<div class=\"alert alert-danger\">\n",
    "    <b>Needs fixing:</b> if the block requires some corrections. Work cant be accepted with the red comments\n",
    "</div>\n",
    "\n",
    "Please don't remove my comments :) If you have any questions don't hesitate to respond to my comments in a different section. \n",
    "<div class=\"alert alert-info\"> <b>Student comments:</b> For example like this</div>    \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"border:solid red 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v1:</b>\n",
    "\n",
    "    \n",
    "<b>Overall Feedback</b>\n",
    "    \n",
    "Hello Jermaine,\n",
    "    \n",
    "You’ve submitted another project—great work! Your commitment to pushing through the challenges of this program is admirable.\n",
    "\n",
    "After reviewing your submission, I’ve returned it with some feedback to help you make the necessary improvements.\n",
    "    \n",
    "   \n",
    "You can find my more detailed notes within your project notebook in the `Reviewer's comment v1:` section.\n",
    "\n",
    "**🚧 Suggested Tweaks & Areas for Attention**\n",
    "\n",
    "- You should calculate the monthly revenue considering to round up the monthly Internet GB consumption to the next whole number.\n",
    "\n",
    "- Write explicitly your hypothesis.\n",
    "   \n",
    "Keep in mind that revisions are a normal and valuable part of the learning process. Use this feedback to refine your work and resubmit when you’re ready. I know you’re capable of great things, and I’m here to support you every step of the way. Keep going—you’re doing a great job! 🏄\n",
    "\n",
    "If you find yourself uncertain or in need of further insights, never hesitate to consult with your tutor or ask your questions here. We are here to guide and assist you."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"border:solid green 2px; padding: 20px\">\n",
    "<b>Reviewer's comment v2:</b>\n",
    "\n",
    "    \n",
    "<b>Overall Feedback</b>\n",
    "    \n",
    "Hello Jermaine,\n",
    "    \n",
    "You’ve submitted another project—great work! Your commitment to pushing through the challenges of this program is admirable.\n",
    "\n",
    "After reviewing your submission, it is approved.\n",
    "    \n",
    "   \n",
    "You can find my more detailed notes within your project notebook in the `Reviewer's comment v2:` section.\n",
    "\n",
    "If you find yourself uncertain or in need of further insights, never hesitate to consult with your tutor or ask your questions here. We are here to guide and assist you."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Which one is a better plan?\n",
    "\n",
    "You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.\n",
    "\n",
    "You are going to carry out a preliminary analysis of the plans based on a relatively small client selection. You'll have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Your job is to analyze the clients' behavior and determine which prepaid plan brings in more revenue."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v1</b>\n",
    " \n",
    "Great job keeping the additional information about the project goal! Additionally, you could add a short description of the tasks you plan to perform and the available data. This information could be helpful for the notebook reader.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[We've provided you with some commentary to guide your thinking as you complete this project. However, make sure to remove all the bracketed comments before submitting your project.]\n",
    "\n",
    "[Before you dive into analyzing your data, explain for yourself the purpose of the project and actions you plan to take.]\n",
    "\n",
    "[Please bear in mind that studying, amending, and analyzing data is an iterative process. It is normal to return to previous steps and correct/expand them to allow for further steps.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Initialization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loading all the libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import math\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import stats"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the data files into different DataFrames\n",
    "calls=pd.read_csv('/datasets/megaline_calls.csv')\n",
    "internet=pd.read_csv('/datasets/megaline_internet.csv')\n",
    "messages=pd.read_csv('/datasets/megaline_messages.csv')\n",
    "plans=pd.read_csv('/datasets/megaline_plans.csv')\n",
    "users=pd.read_csv('/datasets/megaline_users.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Prepare the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[The data for this project is split into several tables. Explore each one to get an initial understanding of the data. Do necessary corrections to each table if necessary.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plans"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2 entries, 0 to 1\n",
      "Data columns (total 8 columns):\n",
      " #   Column                 Non-Null Count  Dtype  \n",
      "---  ------                 --------------  -----  \n",
      " 0   messages_included      2 non-null      int64  \n",
      " 1   mb_per_month_included  2 non-null      int64  \n",
      " 2   minutes_included       2 non-null      int64  \n",
      " 3   usd_monthly_pay        2 non-null      int64  \n",
      " 4   usd_per_gb             2 non-null      int64  \n",
      " 5   usd_per_message        2 non-null      float64\n",
      " 6   usd_per_minute         2 non-null      float64\n",
      " 7   plan_name              2 non-null      object \n",
      "dtypes: float64(2), int64(5), object(1)\n",
      "memory usage: 256.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "# Print the general/summary information about the plans' DataFrame\n",
    "plans.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>messages_included</th>\n",
       "      <th>mb_per_month_included</th>\n",
       "      <th>minutes_included</th>\n",
       "      <th>usd_monthly_pay</th>\n",
       "      <th>usd_per_gb</th>\n",
       "      <th>usd_per_message</th>\n",
       "      <th>usd_per_minute</th>\n",
       "      <th>plan_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   messages_included  mb_per_month_included  minutes_included  \\\n",
       "0                 50                  15360               500   \n",
       "1               1000                  30720              3000   \n",
       "\n",
       "   usd_monthly_pay  usd_per_gb  usd_per_message  usd_per_minute plan_name  \n",
       "0               20          10             0.03            0.03      surf  \n",
       "1               70           7             0.01            0.01  ultimate  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print a sample of data for plans\n",
    "display(plans)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I observe that there are no issues with the above data sample."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false,
    "jupyter": {
     "outputs_hidden": false
    }
   },
   "source": [
    "## Fix data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Fix obvious issues with the data given the initial observations.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Enrich data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Add additional factors to the data if you believe they might be useful.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 500 entries, 0 to 499\n",
      "Data columns (total 8 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   user_id     500 non-null    int64 \n",
      " 1   first_name  500 non-null    object\n",
      " 2   last_name   500 non-null    object\n",
      " 3   age         500 non-null    int64 \n",
      " 4   city        500 non-null    object\n",
      " 5   reg_date    500 non-null    object\n",
      " 6   plan        500 non-null    object\n",
      " 7   churn_date  34 non-null     object\n",
      "dtypes: int64(2), object(6)\n",
      "memory usage: 31.4+ KB\n"
     ]
    }
   ],
   "source": [
    "# Print the general/summary information about the users' DataFrame\n",
    "users.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>age</th>\n",
       "      <th>city</th>\n",
       "      <th>reg_date</th>\n",
       "      <th>plan</th>\n",
       "      <th>churn_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>Anamaria</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>45</td>\n",
       "      <td>Atlanta-Sandy Springs-Roswell, GA MSA</td>\n",
       "      <td>2018-12-24</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>2018-08-13</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>Carlee</td>\n",
       "      <td>Hoffman</td>\n",
       "      <td>36</td>\n",
       "      <td>Las Vegas-Henderson-Paradise, NV MSA</td>\n",
       "      <td>2018-10-21</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>Reynaldo</td>\n",
       "      <td>Jenkins</td>\n",
       "      <td>52</td>\n",
       "      <td>Tulsa, OK MSA</td>\n",
       "      <td>2018-01-28</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>Leonila</td>\n",
       "      <td>Thompson</td>\n",
       "      <td>40</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>2018-05-23</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>495</th>\n",
       "      <td>1495</td>\n",
       "      <td>Fidel</td>\n",
       "      <td>Sharpe</td>\n",
       "      <td>67</td>\n",
       "      <td>New York-Newark-Jersey City, NY-NJ-PA MSA</td>\n",
       "      <td>2018-09-04</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>1496</td>\n",
       "      <td>Ariel</td>\n",
       "      <td>Shepherd</td>\n",
       "      <td>49</td>\n",
       "      <td>New Orleans-Metairie, LA MSA</td>\n",
       "      <td>2018-02-20</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>1497</td>\n",
       "      <td>Donte</td>\n",
       "      <td>Barrera</td>\n",
       "      <td>49</td>\n",
       "      <td>Los Angeles-Long Beach-Anaheim, CA MSA</td>\n",
       "      <td>2018-12-10</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>498</th>\n",
       "      <td>1498</td>\n",
       "      <td>Scot</td>\n",
       "      <td>Williamson</td>\n",
       "      <td>51</td>\n",
       "      <td>New York-Newark-Jersey City, NY-NJ-PA MSA</td>\n",
       "      <td>2018-02-04</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>499</th>\n",
       "      <td>1499</td>\n",
       "      <td>Shena</td>\n",
       "      <td>Dickson</td>\n",
       "      <td>37</td>\n",
       "      <td>Orlando-Kissimmee-Sanford, FL MSA</td>\n",
       "      <td>2018-05-06</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>500 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     user_id first_name   last_name  age  \\\n",
       "0       1000   Anamaria       Bauer   45   \n",
       "1       1001     Mickey   Wilkerson   28   \n",
       "2       1002     Carlee     Hoffman   36   \n",
       "3       1003   Reynaldo     Jenkins   52   \n",
       "4       1004    Leonila    Thompson   40   \n",
       "..       ...        ...         ...  ...   \n",
       "495     1495      Fidel      Sharpe   67   \n",
       "496     1496      Ariel    Shepherd   49   \n",
       "497     1497      Donte     Barrera   49   \n",
       "498     1498       Scot  Williamson   51   \n",
       "499     1499      Shena     Dickson   37   \n",
       "\n",
       "                                          city    reg_date      plan  \\\n",
       "0        Atlanta-Sandy Springs-Roswell, GA MSA  2018-12-24  ultimate   \n",
       "1              Seattle-Tacoma-Bellevue, WA MSA  2018-08-13      surf   \n",
       "2         Las Vegas-Henderson-Paradise, NV MSA  2018-10-21      surf   \n",
       "3                                Tulsa, OK MSA  2018-01-28      surf   \n",
       "4              Seattle-Tacoma-Bellevue, WA MSA  2018-05-23      surf   \n",
       "..                                         ...         ...       ...   \n",
       "495  New York-Newark-Jersey City, NY-NJ-PA MSA  2018-09-04      surf   \n",
       "496               New Orleans-Metairie, LA MSA  2018-02-20      surf   \n",
       "497     Los Angeles-Long Beach-Anaheim, CA MSA  2018-12-10  ultimate   \n",
       "498  New York-Newark-Jersey City, NY-NJ-PA MSA  2018-02-04      surf   \n",
       "499          Orlando-Kissimmee-Sanford, FL MSA  2018-05-06      surf   \n",
       "\n",
       "    churn_date  \n",
       "0          NaN  \n",
       "1          NaN  \n",
       "2          NaN  \n",
       "3          NaN  \n",
       "4          NaN  \n",
       "..         ...  \n",
       "495        NaN  \n",
       "496        NaN  \n",
       "497        NaN  \n",
       "498        NaN  \n",
       "499        NaN  \n",
       "\n",
       "[500 rows x 8 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print a sample of data for users\n",
    "display(users)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I have notice that reg_date & churn_date are objects that need conversion to date_time datatypes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fix Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Fix obvious issues with the data given the initial observations.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "users['reg_date']=pd.to_datetime(users['reg_date'])\n",
    "users['churn_date']=pd.to_datetime(users['churn_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>age</th>\n",
       "      <th>city</th>\n",
       "      <th>reg_date</th>\n",
       "      <th>plan</th>\n",
       "      <th>churn_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>Anamaria</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>45</td>\n",
       "      <td>Atlanta-Sandy Springs-Roswell, GA MSA</td>\n",
       "      <td>2018-12-24</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>2018-08-13</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1002</td>\n",
       "      <td>Carlee</td>\n",
       "      <td>Hoffman</td>\n",
       "      <td>36</td>\n",
       "      <td>Las Vegas-Henderson-Paradise, NV MSA</td>\n",
       "      <td>2018-10-21</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1003</td>\n",
       "      <td>Reynaldo</td>\n",
       "      <td>Jenkins</td>\n",
       "      <td>52</td>\n",
       "      <td>Tulsa, OK MSA</td>\n",
       "      <td>2018-01-28</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1004</td>\n",
       "      <td>Leonila</td>\n",
       "      <td>Thompson</td>\n",
       "      <td>40</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>2018-05-23</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id first_name  last_name  age                                   city  \\\n",
       "0     1000   Anamaria      Bauer   45  Atlanta-Sandy Springs-Roswell, GA MSA   \n",
       "1     1001     Mickey  Wilkerson   28        Seattle-Tacoma-Bellevue, WA MSA   \n",
       "2     1002     Carlee    Hoffman   36   Las Vegas-Henderson-Paradise, NV MSA   \n",
       "3     1003   Reynaldo    Jenkins   52                          Tulsa, OK MSA   \n",
       "4     1004    Leonila   Thompson   40        Seattle-Tacoma-Bellevue, WA MSA   \n",
       "\n",
       "    reg_date      plan churn_date  \n",
       "0 2018-12-24  ultimate        NaT  \n",
       "1 2018-08-13      surf        NaT  \n",
       "2 2018-10-21      surf        NaT  \n",
       "3 2018-01-28      surf        NaT  \n",
       "4 2018-05-23      surf        NaT  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(users.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Enrich Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Add additional factors to the data if you believe they might be useful.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Calls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 137735 entries, 0 to 137734\n",
      "Data columns (total 4 columns):\n",
      " #   Column     Non-Null Count   Dtype  \n",
      "---  ------     --------------   -----  \n",
      " 0   id         137735 non-null  object \n",
      " 1   user_id    137735 non-null  int64  \n",
      " 2   call_date  137735 non-null  object \n",
      " 3   duration   137735 non-null  float64\n",
      "dtypes: float64(1), int64(1), object(2)\n",
      "memory usage: 4.2+ MB\n"
     ]
    }
   ],
   "source": [
    "# Print the general/summary information about the calls' DataFrame\n",
    "calls.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>user_id</th>\n",
       "      <th>call_date</th>\n",
       "      <th>duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000_93</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>8.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000_145</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>13.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1000_247</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>14.48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000_309</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-28</td>\n",
       "      <td>5.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000_380</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-30</td>\n",
       "      <td>4.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137730</th>\n",
       "      <td>1499_199</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-11-21</td>\n",
       "      <td>8.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137731</th>\n",
       "      <td>1499_200</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-10-20</td>\n",
       "      <td>10.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137732</th>\n",
       "      <td>1499_201</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-09-21</td>\n",
       "      <td>8.12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137733</th>\n",
       "      <td>1499_202</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-10-10</td>\n",
       "      <td>0.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137734</th>\n",
       "      <td>1499_203</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-12-29</td>\n",
       "      <td>13.86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>137735 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              id  user_id   call_date  duration\n",
       "0        1000_93     1000  2018-12-27      8.52\n",
       "1       1000_145     1000  2018-12-27     13.66\n",
       "2       1000_247     1000  2018-12-27     14.48\n",
       "3       1000_309     1000  2018-12-28      5.76\n",
       "4       1000_380     1000  2018-12-30      4.22\n",
       "...          ...      ...         ...       ...\n",
       "137730  1499_199     1499  2018-11-21      8.72\n",
       "137731  1499_200     1499  2018-10-20     10.89\n",
       "137732  1499_201     1499  2018-09-21      8.12\n",
       "137733  1499_202     1499  2018-10-10      0.37\n",
       "137734  1499_203     1499  2018-12-29     13.86\n",
       "\n",
       "[137735 rows x 4 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print a sample of data for calls\n",
    "display(calls)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I have noticed that call_date are objects that need conversion to date_time datatypes. \n",
    "I have noticed that duration needs to be rounded up with ceil function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fix data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Fix obvious issues with the data given the initial observations.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "calls['call_date']=pd.to_datetime(calls['call_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Enrich data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "calls['duration']= calls['duration'].apply(math.ceil)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Add additional factors to the data if you believe they might be useful.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>user_id</th>\n",
       "      <th>call_date</th>\n",
       "      <th>duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000_93</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000_145</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1000_247</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000_309</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-28</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000_380</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-30</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         id  user_id  call_date  duration\n",
       "0   1000_93     1000 2018-12-27         9\n",
       "1  1000_145     1000 2018-12-27        14\n",
       "2  1000_247     1000 2018-12-27        15\n",
       "3  1000_309     1000 2018-12-28         6\n",
       "4  1000_380     1000 2018-12-30         5"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calls.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Messages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 76051 entries, 0 to 76050\n",
      "Data columns (total 3 columns):\n",
      " #   Column        Non-Null Count  Dtype \n",
      "---  ------        --------------  ----- \n",
      " 0   id            76051 non-null  object\n",
      " 1   user_id       76051 non-null  int64 \n",
      " 2   message_date  76051 non-null  object\n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 1.7+ MB\n"
     ]
    }
   ],
   "source": [
    "# Print the general/summary information about the messages' DataFrame\n",
    "messages.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>user_id</th>\n",
       "      <th>message_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000_125</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000_160</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1000_223</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000_251</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000_255</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76046</th>\n",
       "      <td>1497_526</td>\n",
       "      <td>1497</td>\n",
       "      <td>2018-12-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76047</th>\n",
       "      <td>1497_536</td>\n",
       "      <td>1497</td>\n",
       "      <td>2018-12-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76048</th>\n",
       "      <td>1497_547</td>\n",
       "      <td>1497</td>\n",
       "      <td>2018-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76049</th>\n",
       "      <td>1497_558</td>\n",
       "      <td>1497</td>\n",
       "      <td>2018-12-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76050</th>\n",
       "      <td>1497_613</td>\n",
       "      <td>1497</td>\n",
       "      <td>2018-12-23</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>76051 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             id  user_id message_date\n",
       "0      1000_125     1000   2018-12-27\n",
       "1      1000_160     1000   2018-12-31\n",
       "2      1000_223     1000   2018-12-31\n",
       "3      1000_251     1000   2018-12-27\n",
       "4      1000_255     1000   2018-12-26\n",
       "...         ...      ...          ...\n",
       "76046  1497_526     1497   2018-12-24\n",
       "76047  1497_536     1497   2018-12-24\n",
       "76048  1497_547     1497   2018-12-31\n",
       "76049  1497_558     1497   2018-12-24\n",
       "76050  1497_613     1497   2018-12-23\n",
       "\n",
       "[76051 rows x 3 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print a sample of data for messages\n",
    "display(messages)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I have noticed that message_date column needs to be converted to date_time datatype."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fix data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Fix obvious issues with the data given the initial observations.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "messages['message_date']=pd.to_datetime(messages['message_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Enrich data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Add additional factors to the data if you believe they might be useful.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Internet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 104825 entries, 0 to 104824\n",
      "Data columns (total 4 columns):\n",
      " #   Column        Non-Null Count   Dtype  \n",
      "---  ------        --------------   -----  \n",
      " 0   id            104825 non-null  object \n",
      " 1   user_id       104825 non-null  int64  \n",
      " 2   session_date  104825 non-null  object \n",
      " 3   mb_used       104825 non-null  float64\n",
      "dtypes: float64(1), int64(1), object(2)\n",
      "memory usage: 3.2+ MB\n"
     ]
    }
   ],
   "source": [
    "# Print the general/summary information about the internet DataFrame\n",
    "internet.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>user_id</th>\n",
       "      <th>session_date</th>\n",
       "      <th>mb_used</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000_13</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-29</td>\n",
       "      <td>89.86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000_204</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-31</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1000_379</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-28</td>\n",
       "      <td>660.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000_413</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-26</td>\n",
       "      <td>270.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000_442</td>\n",
       "      <td>1000</td>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>880.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104820</th>\n",
       "      <td>1499_215</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-10-20</td>\n",
       "      <td>218.06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104821</th>\n",
       "      <td>1499_216</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-12-30</td>\n",
       "      <td>304.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104822</th>\n",
       "      <td>1499_217</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-09-22</td>\n",
       "      <td>292.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104823</th>\n",
       "      <td>1499_218</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-12-07</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104824</th>\n",
       "      <td>1499_219</td>\n",
       "      <td>1499</td>\n",
       "      <td>2018-12-24</td>\n",
       "      <td>758.31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>104825 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              id  user_id session_date  mb_used\n",
       "0        1000_13     1000   2018-12-29    89.86\n",
       "1       1000_204     1000   2018-12-31     0.00\n",
       "2       1000_379     1000   2018-12-28   660.40\n",
       "3       1000_413     1000   2018-12-26   270.99\n",
       "4       1000_442     1000   2018-12-27   880.22\n",
       "...          ...      ...          ...      ...\n",
       "104820  1499_215     1499   2018-10-20   218.06\n",
       "104821  1499_216     1499   2018-12-30   304.72\n",
       "104822  1499_217     1499   2018-09-22   292.75\n",
       "104823  1499_218     1499   2018-12-07     0.00\n",
       "104824  1499_219     1499   2018-12-24   758.31\n",
       "\n",
       "[104825 rows x 4 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print a sample of data for the internet traffic\n",
    "display(internet)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "i noticed that the session_date column needs conversion to datetime datatype."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fix data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Fix obvious issues with the data given the initial observations.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "internet['session_date']= pd.to_datetime(internet['session_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Enrich data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Add additional factors to the data if you believe they might be useful.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v1</b>\n",
    " \n",
    "Great data overview and comments at each dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Study plan conditions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[It is critical to understand how the plans work, how users are charged based on their plan subscription. So, we suggest printing out the plan information to view their conditions once again.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>messages_included</th>\n",
       "      <th>mb_per_month_included</th>\n",
       "      <th>minutes_included</th>\n",
       "      <th>usd_monthly_pay</th>\n",
       "      <th>usd_per_gb</th>\n",
       "      <th>usd_per_message</th>\n",
       "      <th>usd_per_minute</th>\n",
       "      <th>plan_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   messages_included  mb_per_month_included  minutes_included  \\\n",
       "0                 50                  15360               500   \n",
       "1               1000                  30720              3000   \n",
       "\n",
       "   usd_monthly_pay  usd_per_gb  usd_per_message  usd_per_minute plan_name  \n",
       "0               20          10             0.03            0.03      surf  \n",
       "1               70           7             0.01            0.01  ultimate  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print out the plan conditions and make sure they are clear for you\n",
    "display(plans)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Aggregate data per user\n",
    "\n",
    "[Now, as the data is clean, aggregate data per user per period in order to have just one record per user per period. It should ease the further analysis a lot.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "calls = pd.read_csv('/datasets/megaline_calls.csv')\n",
    "calls['call_date'] = pd.to_datetime(calls['call_date'])\n",
    "calls['duration'] = calls['duration'].apply(math.ceil)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the number of calls made by each user per month. Save the result.\n",
    "calls['month']=calls['call_date'].dt.month\n",
    "calls.drop(columns='call_date',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "calls_agg =calls.groupby(['user_id','month'])['duration'].sum().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "calls_agg.columns=['user_id','month','calls_sum']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>calls_sum</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>315</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>393</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>426</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2253</th>\n",
       "      <td>1498</td>\n",
       "      <td>12</td>\n",
       "      <td>339</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2254</th>\n",
       "      <td>1499</td>\n",
       "      <td>9</td>\n",
       "      <td>346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2255</th>\n",
       "      <td>1499</td>\n",
       "      <td>10</td>\n",
       "      <td>385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2256</th>\n",
       "      <td>1499</td>\n",
       "      <td>11</td>\n",
       "      <td>308</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2257</th>\n",
       "      <td>1499</td>\n",
       "      <td>12</td>\n",
       "      <td>496</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2258 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  calls_sum\n",
       "0        1000     12        124\n",
       "1        1001      8        182\n",
       "2        1001      9        315\n",
       "3        1001     10        393\n",
       "4        1001     11        426\n",
       "...       ...    ...        ...\n",
       "2253     1498     12        339\n",
       "2254     1499      9        346\n",
       "2255     1499     10        385\n",
       "2256     1499     11        308\n",
       "2257     1499     12        496\n",
       "\n",
       "[2258 rows x 3 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calls_agg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the number of messages sent by each user per month. Save the result.\n",
    "messages['month']=messages['message_date'].dt.month\n",
    "messages_per_month=messages.groupby(['user_id','month']).count().reset_index()\n",
    "messages_per_month.drop(columns=['id'],inplace=True)\n",
    "messages_per_month.columns=['user_id','month','messages_count']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>messages_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1801</th>\n",
       "      <td>1496</td>\n",
       "      <td>9</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1802</th>\n",
       "      <td>1496</td>\n",
       "      <td>10</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1803</th>\n",
       "      <td>1496</td>\n",
       "      <td>11</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1804</th>\n",
       "      <td>1496</td>\n",
       "      <td>12</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1805</th>\n",
       "      <td>1497</td>\n",
       "      <td>12</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1806 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  messages_count\n",
       "0        1000     12              11\n",
       "1        1001      8              30\n",
       "2        1001      9              44\n",
       "3        1001     10              53\n",
       "4        1001     11              36\n",
       "...       ...    ...             ...\n",
       "1801     1496      9              21\n",
       "1802     1496     10              18\n",
       "1803     1496     11              13\n",
       "1804     1496     12              11\n",
       "1805     1497     12              50\n",
       "\n",
       "[1806 rows x 3 columns]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "messages_per_month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>internet_sum</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>1901.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>6919.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>13314.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>22330.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>18504.30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2272</th>\n",
       "      <td>1498</td>\n",
       "      <td>12</td>\n",
       "      <td>23137.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2273</th>\n",
       "      <td>1499</td>\n",
       "      <td>9</td>\n",
       "      <td>12984.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2274</th>\n",
       "      <td>1499</td>\n",
       "      <td>10</td>\n",
       "      <td>19492.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2275</th>\n",
       "      <td>1499</td>\n",
       "      <td>11</td>\n",
       "      <td>16813.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2276</th>\n",
       "      <td>1499</td>\n",
       "      <td>12</td>\n",
       "      <td>22059.21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2277 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  internet_sum\n",
       "0        1000     12       1901.47\n",
       "1        1001      8       6919.15\n",
       "2        1001      9      13314.82\n",
       "3        1001     10      22330.49\n",
       "4        1001     11      18504.30\n",
       "...       ...    ...           ...\n",
       "2272     1498     12      23137.69\n",
       "2273     1499      9      12984.76\n",
       "2274     1499     10      19492.43\n",
       "2275     1499     11      16813.83\n",
       "2276     1499     12      22059.21\n",
       "\n",
       "[2277 rows x 3 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the volume of internet traffic used by each user per month. Save the result.\n",
    "internet['month']=internet['session_date'].dt.month\n",
    "internet['md_used'] = internet['mb_used'].apply(math.ceil)\n",
    "internet_used_per_month= internet.groupby(['user_id','month'])['mb_used'].sum().reset_index()\n",
    "internet_used_per_month.columns=['user_id','month','internet_sum']\n",
    "internet_used_per_month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>internet_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2272</th>\n",
       "      <td>1498</td>\n",
       "      <td>12</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2273</th>\n",
       "      <td>1499</td>\n",
       "      <td>9</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2274</th>\n",
       "      <td>1499</td>\n",
       "      <td>10</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2275</th>\n",
       "      <td>1499</td>\n",
       "      <td>11</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2276</th>\n",
       "      <td>1499</td>\n",
       "      <td>12</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2277 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  internet_count\n",
       "0        1000     12               5\n",
       "1        1001      8              25\n",
       "2        1001      9              53\n",
       "3        1001     10              56\n",
       "4        1001     11              51\n",
       "...       ...    ...             ...\n",
       "2272     1498     12              65\n",
       "2273     1499      9              45\n",
       "2274     1499     10              61\n",
       "2275     1499     11              49\n",
       "2276     1499     12              65\n",
       "\n",
       "[2277 rows x 3 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "internet['month']=internet['session_date'].dt.month\n",
    "internet_used_per_month_count= internet.groupby(['user_id','month'])['mb_used'].count().reset_index()\n",
    "internet_used_per_month_count.columns=['user_id','month','internet_count']\n",
    "internet_used_per_month_count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Put the aggregate data together into one DataFrame so that one record in it would represent what an unique user consumed in a given month.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "unique_user_per_month = (calls_agg\n",
    ".merge(messages_per_month, on=['user_id', 'month'], how='outer')\n",
    ".merge(internet_used_per_month, on=['user_id', 'month'], how='outer')\n",
    ".merge(internet_used_per_month_count, on=['user_id','month'], how='outer'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>calls_sum</th>\n",
       "      <th>messages_count</th>\n",
       "      <th>internet_sum</th>\n",
       "      <th>internet_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>124.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>1901.47</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>182.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>6919.15</td>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>315.0</td>\n",
       "      <td>44.0</td>\n",
       "      <td>13314.82</td>\n",
       "      <td>53.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>393.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>22330.49</td>\n",
       "      <td>56.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>426.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>18504.30</td>\n",
       "      <td>51.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2288</th>\n",
       "      <td>1349</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>61.0</td>\n",
       "      <td>13039.91</td>\n",
       "      <td>27.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2289</th>\n",
       "      <td>1361</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1519.69</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2290</th>\n",
       "      <td>1482</td>\n",
       "      <td>10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2291</th>\n",
       "      <td>1108</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>233.17</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2292</th>\n",
       "      <td>1311</td>\n",
       "      <td>6</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1498.83</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2293 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  calls_sum  messages_count  internet_sum  internet_count\n",
       "0        1000     12      124.0            11.0       1901.47             5.0\n",
       "1        1001      8      182.0            30.0       6919.15            25.0\n",
       "2        1001      9      315.0            44.0      13314.82            53.0\n",
       "3        1001     10      393.0            53.0      22330.49            56.0\n",
       "4        1001     11      426.0            36.0      18504.30            51.0\n",
       "...       ...    ...        ...             ...           ...             ...\n",
       "2288     1349     12        NaN            61.0      13039.91            27.0\n",
       "2289     1361      5        NaN             2.0       1519.69             9.0\n",
       "2290     1482     10        NaN             2.0           NaN             NaN\n",
       "2291     1108     12        NaN             NaN        233.17             2.0\n",
       "2292     1311      6        NaN             NaN       1498.83             9.0\n",
       "\n",
       "[2293 rows x 6 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "unique_user_per_month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add the plan information\n",
    "user_revenue= unique_user_per_month.merge(users, on= 'user_id',how= 'left').merge(plans, left_on='plan', right_on='plan_name', how='left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "usage_columns = ['calls_sum', 'messages_count', 'internet_sum', 'internet_count']\n",
    "user_revenue[usage_columns] = user_revenue[usage_columns].fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>calls_sum</th>\n",
       "      <th>messages_count</th>\n",
       "      <th>internet_sum</th>\n",
       "      <th>internet_count</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>age</th>\n",
       "      <th>city</th>\n",
       "      <th>...</th>\n",
       "      <th>plan</th>\n",
       "      <th>churn_date</th>\n",
       "      <th>messages_included</th>\n",
       "      <th>mb_per_month_included</th>\n",
       "      <th>minutes_included</th>\n",
       "      <th>usd_monthly_pay</th>\n",
       "      <th>usd_per_gb</th>\n",
       "      <th>usd_per_message</th>\n",
       "      <th>usd_per_minute</th>\n",
       "      <th>plan_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>124.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>1901.47</td>\n",
       "      <td>5.0</td>\n",
       "      <td>Anamaria</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>45</td>\n",
       "      <td>Atlanta-Sandy Springs-Roswell, GA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaT</td>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>182.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>6919.15</td>\n",
       "      <td>25.0</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>315.0</td>\n",
       "      <td>44.0</td>\n",
       "      <td>13314.82</td>\n",
       "      <td>53.0</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>393.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>22330.49</td>\n",
       "      <td>56.0</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>426.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>18504.30</td>\n",
       "      <td>51.0</td>\n",
       "      <td>Mickey</td>\n",
       "      <td>Wilkerson</td>\n",
       "      <td>28</td>\n",
       "      <td>Seattle-Tacoma-Bellevue, WA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2288</th>\n",
       "      <td>1349</td>\n",
       "      <td>12</td>\n",
       "      <td>0.0</td>\n",
       "      <td>61.0</td>\n",
       "      <td>13039.91</td>\n",
       "      <td>27.0</td>\n",
       "      <td>Florentina</td>\n",
       "      <td>Diaz</td>\n",
       "      <td>69</td>\n",
       "      <td>Boston-Cambridge-Newton, MA-NH MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2289</th>\n",
       "      <td>1361</td>\n",
       "      <td>5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1519.69</td>\n",
       "      <td>9.0</td>\n",
       "      <td>Jacelyn</td>\n",
       "      <td>Hoffman</td>\n",
       "      <td>45</td>\n",
       "      <td>Birmingham-Hoover, AL MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>surf</td>\n",
       "      <td>NaT</td>\n",
       "      <td>50</td>\n",
       "      <td>15360</td>\n",
       "      <td>500</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.03</td>\n",
       "      <td>surf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2290</th>\n",
       "      <td>1482</td>\n",
       "      <td>10</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Armand</td>\n",
       "      <td>Glenn</td>\n",
       "      <td>70</td>\n",
       "      <td>New York-Newark-Jersey City, NY-NJ-PA MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaT</td>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2291</th>\n",
       "      <td>1108</td>\n",
       "      <td>12</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>233.17</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Porfirio</td>\n",
       "      <td>Kane</td>\n",
       "      <td>45</td>\n",
       "      <td>Salt Lake City, UT MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaT</td>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2292</th>\n",
       "      <td>1311</td>\n",
       "      <td>6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1498.83</td>\n",
       "      <td>9.0</td>\n",
       "      <td>Cherlyn</td>\n",
       "      <td>Saunders</td>\n",
       "      <td>69</td>\n",
       "      <td>Memphis, TN-MS-AR MSA</td>\n",
       "      <td>...</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>NaT</td>\n",
       "      <td>1000</td>\n",
       "      <td>30720</td>\n",
       "      <td>3000</td>\n",
       "      <td>70</td>\n",
       "      <td>7</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0.01</td>\n",
       "      <td>ultimate</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2293 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      user_id  month  calls_sum  messages_count  internet_sum  internet_count  \\\n",
       "0        1000     12      124.0            11.0       1901.47             5.0   \n",
       "1        1001      8      182.0            30.0       6919.15            25.0   \n",
       "2        1001      9      315.0            44.0      13314.82            53.0   \n",
       "3        1001     10      393.0            53.0      22330.49            56.0   \n",
       "4        1001     11      426.0            36.0      18504.30            51.0   \n",
       "...       ...    ...        ...             ...           ...             ...   \n",
       "2288     1349     12        0.0            61.0      13039.91            27.0   \n",
       "2289     1361      5        0.0             2.0       1519.69             9.0   \n",
       "2290     1482     10        0.0             2.0          0.00             0.0   \n",
       "2291     1108     12        0.0             0.0        233.17             2.0   \n",
       "2292     1311      6        0.0             0.0       1498.83             9.0   \n",
       "\n",
       "      first_name  last_name  age                                       city  \\\n",
       "0       Anamaria      Bauer   45      Atlanta-Sandy Springs-Roswell, GA MSA   \n",
       "1         Mickey  Wilkerson   28            Seattle-Tacoma-Bellevue, WA MSA   \n",
       "2         Mickey  Wilkerson   28            Seattle-Tacoma-Bellevue, WA MSA   \n",
       "3         Mickey  Wilkerson   28            Seattle-Tacoma-Bellevue, WA MSA   \n",
       "4         Mickey  Wilkerson   28            Seattle-Tacoma-Bellevue, WA MSA   \n",
       "...          ...        ...  ...                                        ...   \n",
       "2288  Florentina       Diaz   69         Boston-Cambridge-Newton, MA-NH MSA   \n",
       "2289     Jacelyn    Hoffman   45                  Birmingham-Hoover, AL MSA   \n",
       "2290      Armand      Glenn   70  New York-Newark-Jersey City, NY-NJ-PA MSA   \n",
       "2291    Porfirio       Kane   45                     Salt Lake City, UT MSA   \n",
       "2292     Cherlyn   Saunders   69                      Memphis, TN-MS-AR MSA   \n",
       "\n",
       "      ...      plan churn_date messages_included  mb_per_month_included  \\\n",
       "0     ...  ultimate        NaT              1000                  30720   \n",
       "1     ...      surf        NaT                50                  15360   \n",
       "2     ...      surf        NaT                50                  15360   \n",
       "3     ...      surf        NaT                50                  15360   \n",
       "4     ...      surf        NaT                50                  15360   \n",
       "...   ...       ...        ...               ...                    ...   \n",
       "2288  ...      surf        NaT                50                  15360   \n",
       "2289  ...      surf        NaT                50                  15360   \n",
       "2290  ...  ultimate        NaT              1000                  30720   \n",
       "2291  ...  ultimate        NaT              1000                  30720   \n",
       "2292  ...  ultimate        NaT              1000                  30720   \n",
       "\n",
       "      minutes_included  usd_monthly_pay  usd_per_gb  usd_per_message  \\\n",
       "0                 3000               70           7             0.01   \n",
       "1                  500               20          10             0.03   \n",
       "2                  500               20          10             0.03   \n",
       "3                  500               20          10             0.03   \n",
       "4                  500               20          10             0.03   \n",
       "...                ...              ...         ...              ...   \n",
       "2288               500               20          10             0.03   \n",
       "2289               500               20          10             0.03   \n",
       "2290              3000               70           7             0.01   \n",
       "2291              3000               70           7             0.01   \n",
       "2292              3000               70           7             0.01   \n",
       "\n",
       "      usd_per_minute  plan_name  \n",
       "0               0.01   ultimate  \n",
       "1               0.03       surf  \n",
       "2               0.03       surf  \n",
       "3               0.03       surf  \n",
       "4               0.03       surf  \n",
       "...              ...        ...  \n",
       "2288            0.03       surf  \n",
       "2289            0.03       surf  \n",
       "2290            0.01   ultimate  \n",
       "2291            0.01   ultimate  \n",
       "2292            0.01   ultimate  \n",
       "\n",
       "[2293 rows x 21 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_revenue"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v1:</b> </a>\n",
    "\n",
    "The revenue is well calculated; however, in order to maximize the revenue from each user without increasing their plan, you should round up the monthly Internet GB consumption to the next whole number (previously you did something similar for calls)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Calculate the monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan). N.B. This might not be as trivial as just a couple of lines given the plan conditions! So, it's okay to spend some time on it.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "user_revenue['call_overage'] = np.maximum(0, user_revenue['calls_sum'] - user_revenue['minutes_included']) * user_revenue['usd_per_minute']\n",
    "\n",
    "user_revenue['message_overage'] = np.maximum(0, user_revenue['messages_count'] - user_revenue['messages_included']) * user_revenue['usd_per_message']\n",
    "\n",
    "user_revenue['internet_overage'] = np.maximum(0, (user_revenue['internet_sum'] - user_revenue['mb_per_month_included']) / 1024) * user_revenue['usd_per_gb']\n",
    "\n",
    "user_revenue['monthly_revenue'] = user_revenue['usd_monthly_pay'] + user_revenue['call_overage'] + user_revenue['message_overage'] + user_revenue['internet_overage'\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>month</th>\n",
       "      <th>plan</th>\n",
       "      <th>calls_sum</th>\n",
       "      <th>messages_count</th>\n",
       "      <th>internet_sum</th>\n",
       "      <th>call_overage</th>\n",
       "      <th>message_overage</th>\n",
       "      <th>internet_overage</th>\n",
       "      <th>monthly_revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000</td>\n",
       "      <td>12</td>\n",
       "      <td>ultimate</td>\n",
       "      <td>124.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>1901.47</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>70.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1001</td>\n",
       "      <td>8</td>\n",
       "      <td>surf</td>\n",
       "      <td>182.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>6919.15</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1001</td>\n",
       "      <td>9</td>\n",
       "      <td>surf</td>\n",
       "      <td>315.0</td>\n",
       "      <td>44.0</td>\n",
       "      <td>13314.82</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1001</td>\n",
       "      <td>10</td>\n",
       "      <td>surf</td>\n",
       "      <td>393.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>22330.49</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.09</td>\n",
       "      <td>68.071191</td>\n",
       "      <td>88.161191</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1001</td>\n",
       "      <td>11</td>\n",
       "      <td>surf</td>\n",
       "      <td>426.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>18504.30</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>30.706055</td>\n",
       "      <td>50.706055</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1001</td>\n",
       "      <td>12</td>\n",
       "      <td>surf</td>\n",
       "      <td>412.0</td>\n",
       "      <td>44.0</td>\n",
       "      <td>19369.18</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>39.152148</td>\n",
       "      <td>59.152148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1002</td>\n",
       "      <td>10</td>\n",
       "      <td>surf</td>\n",
       "      <td>59.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>6552.01</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1002</td>\n",
       "      <td>11</td>\n",
       "      <td>surf</td>\n",
       "      <td>386.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>19345.08</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>38.916797</td>\n",
       "      <td>58.916797</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1002</td>\n",
       "      <td>12</td>\n",
       "      <td>surf</td>\n",
       "      <td>384.0</td>\n",
       "      <td>41.0</td>\n",
       "      <td>14396.24</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1003</td>\n",
       "      <td>12</td>\n",
       "      <td>surf</td>\n",
       "      <td>1104.0</td>\n",
       "      <td>50.0</td>\n",
       "      <td>27044.14</td>\n",
       "      <td>18.12</td>\n",
       "      <td>0.00</td>\n",
       "      <td>114.102930</td>\n",
       "      <td>152.222930</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  month      plan  calls_sum  messages_count  internet_sum  \\\n",
       "0     1000     12  ultimate      124.0            11.0       1901.47   \n",
       "1     1001      8      surf      182.0            30.0       6919.15   \n",
       "2     1001      9      surf      315.0            44.0      13314.82   \n",
       "3     1001     10      surf      393.0            53.0      22330.49   \n",
       "4     1001     11      surf      426.0            36.0      18504.30   \n",
       "5     1001     12      surf      412.0            44.0      19369.18   \n",
       "6     1002     10      surf       59.0            15.0       6552.01   \n",
       "7     1002     11      surf      386.0            32.0      19345.08   \n",
       "8     1002     12      surf      384.0            41.0      14396.24   \n",
       "9     1003     12      surf     1104.0            50.0      27044.14   \n",
       "\n",
       "   call_overage  message_overage  internet_overage  monthly_revenue  \n",
       "0          0.00             0.00          0.000000        70.000000  \n",
       "1          0.00             0.00          0.000000        20.000000  \n",
       "2          0.00             0.00          0.000000        20.000000  \n",
       "3          0.00             0.09         68.071191        88.161191  \n",
       "4          0.00             0.00         30.706055        50.706055  \n",
       "5          0.00             0.00         39.152148        59.152148  \n",
       "6          0.00             0.00          0.000000        20.000000  \n",
       "7          0.00             0.00         38.916797        58.916797  \n",
       "8          0.00             0.00          0.000000        20.000000  \n",
       "9         18.12             0.00        114.102930       152.222930  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sample_data = user_revenue[['user_id', 'month', 'plan', 'calls_sum', 'messages_count', 'internet_sum', \n",
    "                           'call_overage', 'message_overage', 'internet_overage', 'monthly_revenue']].head(10)\n",
    "display(sample_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v1</b>\n",
    " \n",
    "Well done!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Study user behaviour"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Calculate some useful descriptive statistics for the aggregated and merged data, which typically reveal an overall picture captured by the data. Draw useful plots to help the understanding. Given that the main task is to compare the plans and decide on which one is more profitable, the statistics and the plots should be calculated on a per-plan basis.]\n",
    "\n",
    "[There are relevant hints in the comments for Calls but they are not provided for Messages and Internet though the principle of statistical study is the same for them as for Calls.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Calls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAInCAYAAACSvmjBAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAABX3klEQVR4nO3de3zP9f//8ft75zEbwzbn04TlMFEMOR/KIlEOyUiphByiksIkpJyS+CQhTQ6R0sH5lEPOpySRDWUzh2xjbLO9fn/08/72bsNebHu/t92ul8v7cvF+PZ+v1+vxer2H933P1+v5shiGYQgAAAAAkGlO9i4AAAAAAHIbghQAAAAAmESQAgAAAACTCFIAAAAAYBJBCgAAAABMIkgBAAAAgEkEKQAAAAAwiSAFAAAAACYRpAAAAADAJIIUACDHjB49WhaLRRcuXLhj3/Lly6tXr17ZX9Q9uHk8/5bddffq1Uvly5fPtu3b27x582SxWLRnzx57lyIp488YACSCFIBc5uOPP5bFYlG9evXsXYrDKV++vCwWi1q2bJlh++zZs2WxWHLkS+q4ceO0YsWKbN3H3YiPj1d4eLhq1aolLy8veXp6qnr16nr99dd19uzZHK3l5mfx/PPPZ9g+YsQIa5/MBM+slJiYqNGjR2vTpk05ut+c1KtXL+v5tVgs8vb2Vq1atTRp0iQlJSXZuzwAuQBBCkCuEhERofLly2vXrl06ceKEvctxOB4eHtq4caNiYmLStUVERMjDwyNH6nDEIHXy5EkFBwfrnXfeUVBQkN577z19+OGHatasmebMmaOmTZvmeE0eHh5atmyZkpOT07V9+eWXGX5es2fP1rFjx7K1rsTERIWHh+fpICVJ7u7uWrBggRYsWKBx48bJ19dXQ4cOVc+ePe1dGoBcgCAFINeIjIzU9u3bNXnyZBUvXlwRERE5XkNaWpquX7+e4/vNrIYNG8rLy0uLFy+2Wf7nn3/qp59+UmhoqJ0qs68bN26oY8eOOnfunDZt2qQvv/xS/fr1U58+fTR9+nSdPHlSTz31VI7X9cgjjyg+Pl4//vijzfLt27crMjIyw8/L1dVV7u7uOVVinubi4qJnnnlGzzzzjPr376/169erbt26Wrx4cY6PUALIfQhSAHKNiIgIFSlSRKGhoXryySdtglRKSop8fX317LPPplsvPj5eHh4eGjp0qHVZUlKSRo0apcDAQLm7u6tMmTJ67bXX0l3SY7FY1L9/f0VEROj++++Xu7u7Vq1aJUn64IMP1KBBAxUtWlSenp6qU6eOvvrqq3T7v3btml555RUVK1ZMhQoVUvv27fXXX3/JYrFo9OjRNn3/+usv9e7dW/7+/nJ3d9f999+vzz77LNPnyMPDQx07dtTChQttln/55ZcqUqSI2rRpk+F6GzZs0MMPP6yCBQuqcOHCevzxx3X06FGbPjfvFTlx4oR69eqlwoULy8fHR88++6wSExNtztnVq1c1f/5862VT/71n6PLly7fdxn+dPHlSFotFU6ZMSde2fft2WSwWffnll7dcf9myZTp48KBGjBihRo0apWv39vbWu+++a33/008/6amnnlLZsmWtPx+DBw/WtWvXbrmPu1GqVCk1btw43ecVERGhGjVqqHr16unW+e89UlFRUbJYLPrggw/0ySefqFKlSnJ3d9eDDz6o3bt326zbtGnTDEfe/r3NqKgoFS9eXJIUHh5u/Qz//bP622+/6cknn5Svr688PDxUt25dffvttzbbTElJUXh4uCpXriwPDw8VLVpUjRo10tq1azN1bhITE/Xiiy+qaNGi8vb2VlhYmP7++29re8+ePVWsWDGlpKSkW7d169aqUqVKpvbzb05OTtbzExUVdct+c+fOVfPmzeXn5yd3d3cFBQVp5syZ6fqVL19ejz32mLZu3aqHHnpIHh4eqlixoj7//HPTtQFwPAQpALlGRESEOnbsKDc3N3Xr1k3Hjx+3flF0dXXVE088oRUrVqS7TGrFihVKSkpS165dJf0zqtS+fXt98MEHateunaZPn64OHTpoypQp6tKlS7r9btiwQYMHD1aXLl00bdo06xfOadOmqXbt2hozZozGjRsnFxcXPfXUU/r+++9t1u/Vq5emT5+utm3b6r333pOnp2eGIw3nzp1T/fr1tW7dOvXv31/Tpk1TYGCgnnvuOU2dOjXT5+npp5/Wrl279Mcff1iXLVy4UE8++aRcXV3T9V+3bp3atGmj2NhYjR49WkOGDNH27dvVsGHDDL9Mdu7cWQkJCRo/frw6d+6sefPmKTw83Nq+YMECubu76+GHH7ZeNvXiiy+a2sZ/VaxYUQ0bNsxwFDIiIkKFChXS448/fsv1b37J79Gjxy37/NvSpUuVmJiovn37avr06WrTpo2m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svZPS0tTjRo1NHny5Az3V6ZMGZv3//7t800//fST2rdvr8aNG+vjjz9WiRIl5Orqqrlz56abOCAz0tLSJEnPPPPMLaderlmzZqa3V69ePVWqVEmDBg1SZGTkXX0xvxVnZ+cMlxv//96V7NxGWFiYli5dqu3bt6tGjRr69ttv9fLLL8vJ6fa/F6xatar279+vM2fOpPt8/ys1NVWtWrXSpUuX9Prrr6tq1aoqWLCg/vrrL/Xq1cv6WWWl9u3by93dXT179lRSUpI6d+5sehuZOacWiyXDc3xzVPdObh770KFDbzlxyc1fEjRu3Fh//PGHvvnmG61Zs0affvqppkyZolmzZt3y2VlmBQUFqU6dOvriiy8UFhamL774Qm5ubpk+f87Ozrd87tqt/PHHH2rRooWqVq2qyZMnq0yZMnJzc9MPP/ygKVOmpPv5yIq/LwAcE0EKgMOLiIiQn59fhjdyL1++XF9//bVmzZolT09PNW7cWCVKlNDixYvVqFEjbdiwQSNGjLBZp1KlSjp48KBatGiR4ShNZixbtkweHh5avXq1zVTUc+fOtelXrlw5paWlKTIy0uY37P99Blbx4sVVqFAhpaammv5idyvdunXT2LFjVa1aNQUHB2fY5+blYxk9l+i3335TsWLFVLBgQdP7vtvzeiePPPKIder7evXqKTExMVOjD+3atdOXX36pL774QsOHD79t38OHD+v333/X/PnzbSaXyOxsc3fD09NTHTp00BdffKFHH31UxYoVy5b9FClSJMNLym6OTN50q8/v5kiNq6trpn5Ob86k+eyzz+rKlStq3LixRo8enakgdfz4ceulvJJ05coVRUdHq23btjb9wsLCNGTIEEVHR2vhwoUKDQ21ucQxq61cuVJJSUn69ttvbUab/ntJMIC8j0v7ADi0a9euafny5Xrsscf05JNPpnv1799fCQkJ1lnZnJyc9OSTT2rlypVasGCBbty4kW4mvs6dO+uvv/7S7NmzM9zffy9ly4izs7MsFovNb/KjoqLSPYT25m/tP/74Y5vl06dPT7e9Tp06admyZfrll1/S7e/8+fN3rOm/nn/+eY0aNUqTJk26ZZ8SJUooODhY8+fP1+XLl63Lf/nlF61Zsybdl9bMKliwoM32soqLi4u6deumJUuWaN68eapRo0amRuqefPJJ1ahRQ++++6527NiRrj0hIcEauG+OIPx7xMAwDE2bNi2LjiJjQ4cO1ahRo/T2229n2z4qVaqk3377zebn6eDBg9q2bZtNvwIFCkhSus/Qz89PTZs21f/+9z9FR0en2/6/t3vx4kWbNi8vLwUGBqZ7xMCtfPLJJzYzDs6cOVM3btzQo48+atOvW7duslgsGjhwoE6ePHnXs/VlVkY/H3Fxcel+iQIg72NECoBDu3kjefv27TNsr1+/vnWE4mZg6tKli6ZPn65Ro0apRo0aqlatms06PXr00JIlS/TSSy9p48aNatiwoVJTU/Xbb79pyZIlWr16terWrXvbukJDQzV58mQ98sgjevrppxUbG6sZM2YoMDDQ5j6QOnXqqFOnTpo6daouXryo+vXra/Pmzfr9998l2f7mf8KECdq4caPq1aunPn36KCgoSJcuXdK+ffu0bt06Xbp0ydS5K1euXLrnVGXk/fff16OPPqqQkBA999xzunbtmqZPny4fH59MrZ+ROnXqaN26dZo8ebJKliypChUqqF69ene1rf8KCwvThx9+qI0bN+q9997L1Dqurq5avny5WrZsqcaNG6tz585q2LChXF1ddeTIES1cuFBFihTRu+++q6pVq6pSpUoaOnSo/vrrL3l7e2vZsmXZfk9LrVq1bC5BzQ69e/fW5MmT1aZNGz333HOKjY3VrFmzdP/999tM9OHp6amgoCAtXrxY9913n3x9fVW9enVVr15dM2bMUKNGjVSjRg316dNHFStW1Llz57Rjxw79+eefOnjwoKR/Lrtr2rSp6tSpI19fX+3Zs0dfffWV+vfvn6lak5OT1aJFC3Xu3FnHjh3Txx9/rEaNGqX7t6B48eJ65JFHtHTpUhUuXDjbHzrdunVrubm5qV27dnrxxRd15coVzZ49W35+fhmGSwB5FyNSABxaRESEPDw81KpVqwzbnZycFBoaqlWrVll/A96gQQOVKVNGCQkJGT4XysnJSStWrNCECRN0+PBhDR06VOHh4dq9e7cGDhxonXTidpo3b645c+YoJiZGgwYN0pdffqn33ntPTzzxRLq+n3/+ufr166fvv/9er7/+upKTk60zC3p4eFj7+fv7a9euXXr22We1fPly67OkLl26lOnAcDdatmypVatWqWjRoho5cqQ++OAD1a9fX9u2bcvUzGcZmTx5surUqaO33npL3bp1y/BhpXerTp06uv/+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b7/V6dOnlZycbNM2efLkLCkMAAAAAByV6SC1fv16tW/fXhUrVtRvv/2m6tWrKyoqSoZh6IEHHsiOGgEAAADAoZiebGL48OEaOnSoDh8+LA8PDy1btkxnzpxRkyZN9NRTT2VHjQAAAADgUEwHqaNHjyosLEyS5OLiomvXrsnLy0tjxozRe++9l+UFAgAAAICjMR2kChYsaL0vqkSJEvrjjz+sbRcuXMi6ygAAAADAQZkOUvXr19fWrVslSW3bttWrr76qd999V71791b9+vVNbWv8+PF68MEHVahQIfn5+alDhw46duyYTZ/r16+rX79+Klq0qLy8vNSpUyedO3fOps/p06cVGhqqAgUKyM/PT8OGDdONGzfMHhoAAAAAZIrpySYmT56sK1euSJLCw8N15coVLV68WJUrVzY9Y9/mzZvVr18/Pfjgg7px44befPNNtW7dWr/++qsKFiwoSRo8eLC+//57LV26VD4+Purfv786duyobdu2SZJSU1MVGhqqgIAAbd++XdHR0QoLC5Orq6vGjRtn9vDuWvk3vr+n9aMmhGZRJQAAAACym6kglZqaqj///FM1a9aU9M9lfrNmzbrrna9atcrm/bx58+Tn56e9e/eqcePGiouL05w5c7Rw4UI1b95ckjR37lxVq1ZNP//8s+rXr681a9bo119/1bp16+Tv76/g4GC98847ev311zV69Gi5ubnddX0AAAAAkBFTl/Y5OzurdevW+vvvv7OlmLi4OEmSr6+vJGnv3r1KSUlRy5YtrX2qVq2qsmXLaseOHZKkHTt2qEaNGvL397f2adOmjeLj43XkyJEM95OUlKT4+HibFwAAAABklul7pKpXr66TJ09meSFpaWkaNGiQGjZsqOrVq0uSYmJi5ObmpsKFC9v09ff3V0xMjLXPv0PUzfabbRkZP368fHx8rK8yZcpk8dEAAAAAyMtMB6mxY8dq6NCh+u677xQdHZ1lIzv9+vXTL7/8okWLFt31NjJr+PDhiouLs77OnDmT7fsEAAAAkHeYnmyibdu2kqT27dvLYrFYlxuGIYvFotTUVNNF9O/fX9999522bNmi0qVLW5cHBAQoOTlZly9fthmVOnfunAICAqx9du3aZbO9m7P63ezzX+7u7nJ3dzddJwAAAABIdxGkNm7cmGU7NwxDAwYM0Ndff61NmzapQoUKNu116tSR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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Compare average duration of calls per each plan per each distinct month. Plot a bar plat to visualize it.\n",
    "\n",
    "avg_call_minutes = user_revenue.groupby(['plan', 'month'])['calls_sum'].mean().reset_index()\n",
    "avg_call_minutes_pivot = avg_call_minutes.pivot(index='month', columns='plan', values='calls_sum')\n",
    "avg_call_minutes_pivot.plot(kind='bar', figsize=(10, 6))\n",
    "plt.title('Average Monthly Call Minutes by Plan')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Average Call Minutes')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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vREfH6+JUomIiKgWqlMByMbGBlFRUfjxxx/x448/ws7ODl5eXjh16hQA4O7duygsLISVlZXKflZWViXWCT0rLy8PWVlZKg8iIiKqvzR6CayyXFxc4OLiIj3v0qULrl27hkWLFmHt2rVVHjcsLAxz585VR4lERERUB9SpM0Cl6dy5M65evQoAMDc3h1KpRHp6ukqf9PR0WFtblzlGaGgoMjMzpceNGzeqtWYiIiLSrDofgBITE2FjYwMA0NXVRceOHREbGyttLyoqQmxsLDw9PcscQ09PDyYmJioPIiIiqr80egksOztbOnsDAElJSUhMTESjRo3QrFkzhIaG4tatW1izZg0AIDIyEo6Ojmjbti1yc3Px3Xff4cCBA9i7d680RkhICPz9/dGpUyd07twZkZGRyMnJke4KIyIiItJoADp58iR69OghPQ8JCQEA+Pv7Izo6GqmpqUhJSZG25+fnY+rUqbh16xYMDQ3Rvn177N+/X2WMYcOG4c6dO5g1axbS0tLg7u6OmJiYEgujiYiISL4UQgih6SJqm6ysLJiamiIzM7NaLoeFbjsH35sLyty+vemMMreFDXZVez1ERET1QWV+f9f5NUBERERElcUARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESyo9EAdPjwYQwcOBC2trZQKBTYvn17uf23bduG3r17w8LCAiYmJvD09MSePXtU+syZMwcKhULl0apVq2qcBREREdU1Gg1AOTk5cHNzw7JlyyrU//Dhw+jduzd27dqFhIQE9OjRAwMHDsTp06dV+rVt2xapqanS48iRI9VRPhEREdVR2po8eL9+/dCvX78K94+MjFR5/sUXX2DHjh345Zdf0KFDB6ldW1sb1tbW6iqTiIiI6pk6vQaoqKgIjx49QqNGjVTar1y5AltbWzRv3hwjR45ESkqKhiok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OCIiIqLqUKU1QHv37sWePXvQtGlTlXZnZ2dcv35dLYURERERVZcqnQHKyclROfNT7P79+/xKCSIiIqr1qhSAunXrJn09BfDPd34VFRVhwYIFKp/sTERERFQbVekS2IIFC9CrVy+cPHkS+fn5mDFjBv7880/cv38fR48eVXeNRERERGpVpTNA7dq1w+XLl9G1a1cMGjQIOTk5GDx4ME6fPo0WLVqou0YiIiIitar0GaCCggL07dsXUVFR+PTTT6ujJiIiIqJqVekzQDo6Ojh79mx11EJERERUI6p0Cey9997D999/r+5aiIiIiGpElRZBP336FCtXrsT+/fvRsWPHEt8BFhERoZbiiIiIiKpDpQLQ33//DQcHB5w/fx6vvPIKAODy5csqfRQKhfqqIyIiIqoGlQpAzs7OSE1NxcGDBwH889UXS5YsgZWVVbUUR0RERFQdKrUG6Plve9+9ezdycnLUWhARERFRdavSIuhizwciIiIiorqgUgFIoVCUWOPDNT9ERERU11RqDZAQAgEBAdIXnubm5uLDDz8scRfYtm3b1FchERERkZpVKgD5+/urPH/vvffUWgwRERFRTahUAFq1alV11UFERERUY15qETQRERFRXcQARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREssMARERERLLDAERERESywwBEREREslMrAtCyZcvg4OAAfX19eHh44MSJE2X29fLykr6V/tlH//79pT4BAQEltvft27cmpkJERER1QKW+C6w6bN68GSEhIYiKioKHhwciIyPh4+ODS5cuwdLSskT/bdu2IT8/X3p+7949uLm5YciQISr9+vbtq/LdZcXfYE9ERESk8TNAERERGDduHAIDA9GmTRtERUXB0NAQK1euLLV/o0aNYG1tLT327dsHQ0PDEgFIT09PpV/Dhg1rYjpERERUB2g0AOXn5yMhIQHe3t5Sm5aWFry9vREfH1+hMb7//nsMHz4cRkZGKu1xcXGwtLSEi4sLxo8fj3v37qm1diIiIqq7NHoJ7O7duygsLISVlZVKu5WVFS5evPjC/U+cOIHz58/j+++/V2nv27cvBg8eDEdHR1y7dg2ffPIJ+vXrh/j4eCiVyhLj5OXlIS8vT3qelZVVxRkRERFRXaDxNUAv4/vvv4erqys6d+6s0j58+HDp/11d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hAkT4O7ujlatWuG7775DUVERYmNjVfrp6enB2tpaejRs2LAmpkNERER1gEYDUH5+PhISEuDt7S21aWlpwdvbG/Hx8RUa4/HjxygoKECjRo1U2uPi4mBpaQkXFxeMHz8e9+7dU2vtREREVHdpa/Lgd+/eRWFhIaysrFTarayscPHixQqN8dFHH8HW1lYlRPXt2xeDBw+Go6Mjrl27hk8++QT9+vVDfHw8lEpliTHy8vKQl5cnPc/KyqrijIiIiKgu0GgAellffvklNm3ahLi4OOjr60vtw4cPl/7f1dUV7du3R4sWLRAXF4devXqVGCcsLAxz586tkZqJiIhI8zR6Cczc3BxKpRLp6ekq7enp6bC2ti5334ULF+LLL7/E3r170b59+3L7Nm/eHObm5rh69Wqp20NDQ5GZmSk9bty4UbmJEBERUZ2i0QCkq6uLjh07qixgLl7Q7OnpWeZ+CxYswPz58xETE4NOnTq98Dg3b97EvXv3YGNjU+p2PT09mJiYqDyIiIio/tL4XWAhISH49ttvsXr1avz1118YP348cnJyEBgYCADw8/NDaGio1P+rr77CzJkzsXLlSjg4OCAtLQ1paWnIzs4GAGRnZ2P69On4/fffkZycjNjYWAwaNAhOTk7w8fHRyByJiIiodtH4GqBhw4bhzp07mDVrFtLS0uDu7o6YmBhpYXRKSgq0tP4vp61YsQL5+fl45513VMaZPXs25syZA6VSibNnz2L16tV4+PAhbG1t0adPH8yfPx96eno1OjciIiKqnTQegAAgKCgIQUFBpW6Li4tTeZ6cnFzuWAYGBtizZ4+aKiMiIqL6SOOXwIiIiIhqGgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREclOrQhAy5Ytg4ODA/T19eHh4YETJ06U23/r1q1o1aoV9PX14erqil27dqls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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Compare the number of minutes users of each plan require each month. Plot a histogram.\n",
    "avg_min = user_revenue.groupby(['plan','month'])['calls_sum'].sum().reset_index()\n",
    "for plan in avg_min['plan'].unique():\n",
    "    plt.hist(avg_min.loc[avg_min['plan'] == plan, 'calls_sum'],\n",
    "             bins=30,\n",
    "             alpha=0.6,\n",
    "             label=plan)\n",
    "plt.xlabel('Call Minutes')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Distribution of Call Minutes by Plan')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Calculate the mean and the variable of the call duration to reason on whether users on the different plans have different behaviours for their calls.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the mean and the variance of the monthly call duration\n",
    "monthly_calls = user_revenue.groupby(['user_id', 'month'])['calls_sum'].sum().reset_index()\n",
    "mean_duration = monthly_calls['calls_sum'].mean()\n",
    "variance_duration = monthly_calls['calls_sum'].var()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "429.2834714348016"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55847.17877118995"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "variance_duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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5ftfpTFUBgYGuHTpklrBEREREVU2Kg9K//TTT/Hrr7+WRixEREREFZLKY6jy8/Px22+/4ciRI2jdujVMTU0V6jU9MJ2IiIiovFM5oYqPj8f7778PALhx44ZCnUQi0UxURERERBWIyglVZGRkacRBREREVGGpPIaKiIiIiBSp3EPVuXPnEi/tHTt2TK2AiIiIiCoalRMq+TPy5PLy8hAXF4f4+PhSfWAxERERUXmlckIVHBxcZPncuXORmZmpdkBEREREFY3GxlB9+umn+O233zS1OiIiIqIKQ2MJVUxMjMLz84iIiIh0hcqX/Pr376+wLAgCEhMTcf78ecyaNUtjgRERERFVFConVBYWFgrLenp6aNiwIYKCguDl5aWxwIiIiIgqCpUTqg0bNpRGHEREREQVlsoJlSAIiI2Nxd27dyGRSFC3bl20bNmSj50hIiIinaVSQhUZGYlRo0bh3r17EAQBwKvn9zk5OeG3335Dx44dSyVIIiIiovJM6bv8bt26BR8fHzg6OiIkJATXrl3D1atXsWvXLtSuXRve3t64c+dOacZKREREVC4p3UO1YsUKuLm54ejRowrljRo1Qr9+/eDp6Yng4GCsXr1a40ESERERlWdK91AdP34ckydPLrJOIpFg8uTJiIyM1FRcRERERBWG0gnV/fv34eLiUmx9s2bNcO/ePY0ERURERFSRKJ1QZWZmokqVKsXWV6lSBdnZ2RoJioiIiKgiUekuv6tXryIpKanIuidPnmgkICIiIqKKRqWEqmvXruJ0Ca+TSCQQBIFzUREREZFOUjqhSkhIKM04iIiIiCospRMqBweH0oyDiIiIqMJSelA6ERERERWNCRURERGRmphQEREREamJCRURERGRmphQEREREalJqbv8WrVqpfQcUxcuXFArICIiIqKKRqmEqm/fvqUcBhEREVHFpVRCNWfOnNKOo1iPHj3CjBkzEBYWhuzsbDg7O2PDhg1o06YNAEAQBMyZMwc///wz0tLS0K5dO6xduxb169cX15GamoqJEydi37590NPTw4ABA7By5UqYmZlpa7eIiIioEinXY6iePXuGdu3awcDAAGFhYbh69SqWLVsGKysrsc2SJUuwatUqrFu3DmfOnIGpqSm6d++Oly9fim2GDh2KK1euICIiAvv378eJEycwZswYbewSERERVUJK9VBZWVkpPYYq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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a boxplot to visualize the distribution of the monthly call duration\n",
    "monthly_calls_with_plan = user_revenue.groupby(['user_id', 'month', 'plan'])['calls_sum'].sum().reset_index()\n",
    "\n",
    "monthly_calls_with_plan.boxplot(column='calls_sum', by='plan', grid=True, patch_artist=True)\n",
    "plt.title('Distribution of Monthly Call Duration by Plan')\n",
    "plt.suptitle('') \n",
    "\n",
    "plt.xlabel('Plan')\n",
    "plt.ylabel('Monthly Call Duration (minutes)')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate conclusions on how the users behave in terms of calling. Is their behaviour different between the plans?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "there are no major behavior differences between users in terms of calls. The only main behavior difference i notice is with in the frequency of calls. As the call minutes increase up toward 80000 the frequency in ultimate plan users stops. This tells me that ultimate users aren't pushing up against there usage limits."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Messages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0kAAAInCAYAAABN8BLeAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAABVf0lEQVR4nO3dd3gUZf/+/XPTAymQQAglEJpApBqUKl1BkC5dqTc2QAERQZSugEqxIHgjgmKQjvWLSJeiAgkicks1EZCETgIEkpDM84dP9jdrAmRhs5vA+3UcexzONdfMfGYmwT0zM9dYDMMwBAAAAACQJLm5ugAAAAAAyEsISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAADglvr27Ss/P7/bXj48PFyPP/64Ayu6MxaLRePHj3d1GQDyKEISgDzlww8/lMViUZ06dVxdSp4THh4ui8WiFi1aZDt/3rx5slgsslgs2r17t5Ory98yj23mJyQkRA8//LBWr17tlO1nbvc///lPtvPHjBlj7XP27NlcqyM5OVnjx4/X5s2bc20buSkuLs7mPLq7u6t06dLq2LGjfv31V1eXByAfISQByFOioqIUHh6unTt36siRI64uJ8/x8fHRpk2blJCQkGVeVFSUfHx8XFDV3aFmzZpatGiRFi1apBEjRujkyZPq1KmT5s6d65Tt+/j4aOXKlUpNTc0y74svvnDKuU1OTtaECRPybUjK1KNHDy1atEiffPKJevbsqY0bN6pu3boEJQA5RkgCkGfExsZqx44dmjFjhooWLaqoqCin15CRkaFr1645fbs51aBBA/n5+Wnp0qU27SdOnNDWrVvVpk0bF1WW/5UsWVJPPvmknnzySY0cOVLbt29XwYIFNXPmzDte97Vr15SRkXHTPq1atVJSUpLWrFlj075jxw7FxsZybu3wwAMP6Mknn1SfPn00depUff7550pJSdGcOXNcXRqAfIKQBCDPiIqKUuHChdWmTRs98cQTNiEpLS1NQUFB6tevX5blkpKS5OPjoxEjRljbUlJSNG7cOFWoUEHe3t4KCwvTyJEjlZKSYrOsxWLR4MGDFRUVpfvvv1/e3t76/vvvJUnvvPOO6tevr+DgYPn6+ioyMlIrVqzIsv2rV6/qhRdeUJEiReTv76927drp77//zvaZh7///lv9+/dXsWLF5O3trfvvv1+ffPJJjo+Rj4+POnXqpMWLF9u0f/HFFypcuLBatmyZ7XIHDhzQE088oaCgIPn4+Kh27dr6+uuvbfqkpaVpwoQJqlixonx8fBQcHKyGDRtq3bp11j4JCQnq16+fSpUqJW9vbxUvXlzt27dXXFyctc9XX32lNm3aqESJEvL29lb58uU1adIkpaenZ6lr9uzZKleunHx9ffXQQw9p69atatKkiZo0aWLTL6fnc926dWrYsKEKFSokPz8/VapUSa+++mpODm0WoaGhqlKlimJjY61tOTl/mzdvlsVi0ZIlS/Taa6+pZMmSKlCggJKSkm66vZIlS6pRo0ZZzm1UVJSqVaumqlWrZrvc8uXLFRkZKV9fXxUpUkRPPvmk/v77b5s+mc8T/f333+rQoYP8/PxUtGhRjRgxwnpe4uLiVLRoUUnShAkTrLesZfczfKN15MQPP/ygmjVrysfHRxEREVq1apV13p9//imLxZJtMN2xY4csFou++OKLHG8rU7NmzSTJ5lz+219//aXnn39elSpVkq+vr4KDg9WlSxebn21JWrhwoSwWi7Zv367hw4eraNGiKliwoDp27KgzZ87YXRuAvMnD1QUAQKaoqCh16tRJXl5e6tGjh+bMmaNdu3bpwQcflKenpzp27KhVq1bpo48+kpeXl3W5L7/8UikpKerevbukf64GtWvXTtu2bdPTTz+tKlWqaN++fZo5c6YOHTqkL7/80ma7Gzdu1LJlyzR48GAVKVJE4eHhkqR3331X7dq1U69evZSamqolS5aoS5cu+vbbb23+qt+3b18tW7ZMTz31lOrWrastW7Zk+1f/U6dOqW7dutZgVrRoUa1Zs0YDBgxQUlKShg4dmqPj1LNnTz366KM6evSoypcvL0lavHixnnjiCXl6embpv3//fjVo0EAlS5bUqFGjVLBgQS1btkwdOnTQypUr1bFjR0nS+PHjNWXKFP3nP//RQw89pKSkJO3evVsxMTF65JFHJEmdO3fW/v37NWTIEIWHh+v06dNat26djh07Zj1uCxculJ+fn4YPHy4/Pz9t3LhRY8eOVVJSkt5++21rXXPmzNHgwYP18MMPa9iwYYqLi1OHDh1UuHBhlSpVytovp+dz//79evzxx1W9enVNnDhR3t7eOnLkiLZv356j4/pvaWlpOn78uIKDgyXZf/4mTZokLy8vjRgxQikpKTY/szfSs2dPvfjii7p8+bL8/Px0/fp1LV++XMOHD8/2CufChQvVr18/Pfjgg5oyZYpOnTqld999V9u3b9eePXtUqFAha9/09HS1bNlSderU0TvvvKP169dr+vTpKl++vJ577jkVLVpUc+bM0XPPPaeOHTuqU6dOkqTq1avneB23cvjwYXXr1k3PPvus+vTpowULFqhLly76/vvv9cgjj6hcuXJq0KCBoqKiNGzYMJtlo6Ki5O/vr/bt299yO/929OhRSbKey+zs2rVLO3bsUPfu3VWqVCnFxcVpzpw5atKkif73v/+pQIECNv2HDBmiwoULa9y4cYqLi9OsWbM0ePDgLFd5AeRTBgDkAbt37zYkGevWrTMMwzAyMjKMUqVKGS+++KK1z9q1aw1JxjfffGOzbOvWrY1y5cpZpxctWmS4ubkZW7dutek3d+5cQ5Kxfft2a5skw83Nzdi/f3+WmpKTk22mU1NTjapVqxrNmjWztkVHRxuSjKFDh9r07du3ryHJGDdunLVtwIABRvHixY2zZ8/a9O3evbsRGBiYZXv/VqZMGaNNmzbG9evXjdDQUGPSpEmGYRjG//73P0OSsWXLFmPBggWGJGPXrl3W5Zo3b25Uq1bNuHbtmrUtIyPDqF+/vlGxYkVrW40aNYw2bdrccPsXLlwwJBlvv/32TevMbj+eeeYZo0CBAtYaUlJSjODgYOPBBx800tLSrP0WLlxoSDIaN25sbcvp+Zw5c6YhyThz5sxN68tOmTJljEcffdQ4c+aMcebMGWPv3r1G9+7dDUnGkCFDDMPI+fnbtGmTIckoV67cLc9pJknGoEGDjPPnzxteXl7GokWLDMMwjO+++86wWCxGXFycMW7cOJv9S01NNUJCQoyqVasaV69eta7r22+/NSQZY8eOtbb16dPHkGRMnDjRZru1atUyIiMjrdNnzpzJ8nNr7zpupEyZMoYkY+XKlda2xMREo3jx4katWrWsbR999JEhyfjjjz+sbampqUaRIkWMPn363HQbsbGxhiRjwoQJxpkzZ4yEhARj8+bNRq1atbJs+9/7md25+umnnwxJxmeffWZty/wda9GihZGRkWFtHzZsmOHu7m5cvHjxlscCQN7H7XYA8oSoqCgVK1ZMTZs2lfTPbXDdunXTkiVLrLfyNGvWTEWKFLH5S+2FCxe0bt06devWzdq2fPlyValSRZUrV9bZs2etn8xbbjZt2mSz7caNGysiIiJLTb6+vjbbSUxM1MMPP6yYmBhre+atec8//7zNskOGDLGZNgxDK1euVNu2bWUYhk1dLVu2VGJios16b8bd3V1du3a13nYUFRWlsLAwPfzww1n6nj9/Xhs3blTXrl116dIl6zbPnTunli1b6vDhw9ZbswoVKqT9+/fr8OHD2W7X19dXXl5e2rx5sy5cuHDD+szHLXObDz/8sJKTk3XgwAFJ0u7du3Xu3DkNHDhQHh7/76aGXr16qXDhwjbry+n5zLxq8tVXX93y+Z/s/PDDDypatKiKFi2qGjVqaPny5Xrqqac0bdq02zp/ffr0sTkWOVG4cGG1atXKem4XL16s+vXrq0yZMln67t69W6dPn9bzzz9vM6hDmzZtVLlyZX333XdZlnn22Wdtph9++GH9+eefdtV4J+soUaKE9cqlJAUEBKh3797as2ePdTCSrl27ysfHx+Z227Vr1+rs2bN68sknc7SdcePGqWjRogoNDVWTJk109OhRTZs2zXp1LDvmc5WWlqZz586pQoUKKlSoULa/m08//bQsFot1+uGHH1Z6err++uuvHNUIIG8jJAFwufT0dC1ZskRNmzZVbGysjhw5oiNHjqhOnTo6deqUNmzYIEny8PBQ586d9dVXX1mfRVm1apXS0tJsQtLhw4e1f/9+6xfezM99990nSTp9+rTN9suWLZttXd9++63q1q0rHx8fBQUFWW9HSkxMtPb566+/5ObmlmUdFSpUsJk+c+aMLl68qP/+979Z6sp8zurfdd1Mz5499b///U979+7V4sWL1b17d5svbJmOHDkiwzD0+uuvZ9nuuHHjbLY7ceJEXbx4Uffdd5+qVauml19+Wb/99pt1Xd7e3po2bZrWrFmjYsWKqVGjRnrrrbeyjLS3f/9+dezYUYGBgQoICFDRokWtX24zj13mF8l/HycPDw/rbXuZcno+u3XrpgYNGug///mPihUrpu7du2vZsmU5Dkx16tTRunXrtH79eu3YsUNnz57VZ599Jl9f39s6fzf6ubqVnj17Wm9h/PLLL9WzZ89s+2Uew0qVKmWZV7ly5Sxf1n18fKzPHGUqXLjwTQPvv93pOipUqJDl5zTzPGY++1OoUCG1bdvW5tmsqKgolSxZ0hqMb+Xpp5/WunXrtGHDBkVHR+v06dMaOXLkTZe5evWqxo4dq7CwMHl7e6tIkSIqWrSoLl68aPM7n6l06dI205nh3p7jCSDv4pkkAC63ceNGxcfHa8mSJVqyZEmW+VFRUXr00UclSd27d9dHH32kNWvWqEOHDlq2bJkqV66sGjVqWPtnZGSoWrVqmjFjRrbbCwsLs5nO7q/9W7duVbt27dSoUSN9+OGHKl68uDw9PbVgwYIsD9bnROYX9cwRt7JjfvbjVurUqaPy5ctr6NChio2NveEX6cztjhgx4oaDOmQGlUaNGuno0aP66quv9MMPP+jjjz/WzJkzNXfuXOv7e4YOHaq2bdvqyy+/1Nq1a/X6669rypQp2rhxo2rVqqWLFy+qcePGCggI0MSJE1W+fHn5+PgoJiZGr7zyym1d4cnp+fT19dWPP/6oTZs26bvvvtP333+vpUuXqlmzZvrhhx/k7u5+0+0UKVLkhu+gup3zZ+9VpEzt2rWTt7e3+vTpo5SUFHXt2vW21vNvt9p/Z60jJ3r37q3ly5drx44dqlatmr7++ms9//zzcnPL2d92K1aseMNzeSNDhgzRggULNHToUNWrV0+BgYGyWCzq3r17tj+3NzoWhmHYtV0AeRMhCYDLRUVFKSQkRLNnz84yb9WqVVq9erXmzp0rX19fNWrUSMWLF9fSpUvVsGFDbdy4UWPGjLFZpnz58tq7d6+aN2+e7dWVnFi5cqV8fHy0du1aeXt7W9sXLFhg069MmTLKyMhQbGysKlasaG3/9zueihYtKn9/f6Wnp9v95e1GevToocmTJ6tKlSqqWbNmtn3KlSsnSfL09MzRdjNHEOzXr58uX76sRo0aafz48TYvOS1fvrxeeuklvfTSSzp8+LBq1qyp6dOn6/PPP9fmzZt17tw5rVq1So0aNbIu8+9RxTJvHzty5Ij1FktJun79uuLi4mwChz3n083NTc2bN1fz5s01Y8YMvfnmmxozZow2bdp0R8c9N87fjfj6+qpDhw76/PPP9dhjj6lIkSLZ9ss8hgcPHsxyheXgwYPZ3qJ3K7f7+5JTmVc2zds5dOiQJNlcQWzVqpX1NQB16tRRcnKynnrqqVytbcWKFerTp4+mT59ubbt27ZouXryYq9sFkDdxux0Al7p69apWrVqlxx9/XE888USWz+DBg3Xp0iXrcNVubm564okn9M0332jRokW6fv26za120j/PNPz999+aN29ettu7cuXKLetyd3eXxWKxGdo4Li4uy8h4mVdnPvzwQ5v2999/P8v6OnfurJUrV+r333/Psr3bGTr4P//5j8aNG2fzpe7fQkJC1KRJE3300UeKj4+/6XbPnTtnM8/Pz08VKlSw3tqYnJycZYS18uXLy9/f39on86/r5r+mp6amZjk+tWvXVnBwsObNm6fr169b26OiorLcrpTT83n+/Pks8zPD47+HCrdXbpy/mxkxYoTGjRun119//YZ9ateurZCQEM2dO9dm/9asWaM//vjjtt6rlDmCW24Fg5MnT2r16tXW6aSkJH322WeqWbOmQkNDre0eHh7q0aOHli1bpoULF6patWp2XWm9He7u7lmuAr3//vt2DW8O4O7BlSQALvX111/r0qVLateuXbbz69ata/2LcmYY6tatm95//32NGzdO1apVU5UqVWyWeeqpp7Rs2TI9++yz2rRpkxo0aKD09HQdOHBAy5Yt09q1a1W7du2b1tWmTRvNmDFDrVq1Us+ePXX69GnNnj1bFSpUsHlOJzIyUp07d9asWbN07tw56xDgmX8dN//FfOrUqdq0aZPq1KmjgQMHKiIiQufPn1dMTIzWr1+f7Zf8mylTpkyWd9hkZ/bs2WrYsKGqVaumgQMHqly5cjp16pR++uknnThxQnv37pUkRUREqEmTJoqMjFRQUJB2796tFStWaPDgwZL++Yt/8+bN1bVrV0VERMjDw0OrV6/WqVOnrMOv169fX4ULF1afPn30wgsvyGKxaNGiRVm+fHp5eWn8+PEaMmSImjVrpq5duyouLk4LFy5U+fLlbY5bTs/nxIkT9eOPP6pNmzYqU6aMTp8+rQ8//FClSpVSw4YN7Tq22XH0+buZGjVq2NxCmh1PT09NmzZN/fr1U+PGjdWjRw/rEODh4eFZhtDOCV9fX0VERGjp0qW67777FBQUpKpVq97wHU32uu+++zRgwADt2rVLxYoV0yeffKJTp05luUIr/XPL3XvvvadNmzZp2rRpDtn+zTz++ONatGiRAgMDFRERoZ9++knr16+/6bDhAO5irhpWDwAMwzDatm1r+Pj4GFeuXLlhn759+xqenp7WoZczMjKMsLAwQ5IxefLkbJdJTU01pk2bZtx///2Gt7e3UbhwYSMyMtKY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WLFimjdvnq5cuaJ+/frJ399fFSpU0Jo1a6zLpKena8CAASpbtqx8fX1VqVIlvfvuu9b548eP16effqqvvvpKFotFFotFmzdvliQdP35cXbt2VaFChRQUFKT27dsrLi7OEYcHAAAAuCOEpLvczp07JUnr169XfHy8Vq1adcO+n376qYoUKaKdO3dqyJAheu6559SlSxfVr19fMTExevTRR/XUU08pOTlZkpSRkaFSpUpp+fLl+t///qexY8fq1Vdf1bJlyyRJI0aMUNeuXdWqVSvFx8crPj5e9evXV1pamlq2bCl/f39t3bpV27dvl5+fn1q1aqXU1NTcPygAAADATRCS7nJFixaVJAUHBys0NFRBQUE37FujRg299tprqlixokaPHi0fHx8VKVJEAwcOVMWKFTV27FidO3dOv/32myTJ09NTEyZMUO3atVW2bFn16tVL/fr1s4YkPz8/+fr6ytvbW6GhoQoNDZWXl5eWLl2qjIwMffzxx6pWrZqqVKmiBQsW6NixY9YrTQAAAICr8EwSrKpXr279b3d3dwUHB6tatWrWtmLFikmSTp8+bW2bPXu2PvnkEx07dkxXr15VamqqzQAR2dm7d6+OHDkif39/m/Zr167p6NGjDtgTAAAA4PYRkvIhNze3LCPTpaWl3fF6PT09baYtFotNm8VikfTPbXaStGTJEo0YMULTp09XvXr15O/vr7ffflu//PLLTbdz+fJlRUZGKioqKsu8zCtfAAAAgKsQkvKhokWLKj4+3jqdlJSk2NjYbPt6eXlJ+meQBUfbvn276tevr+eff97a9u8rQV5eXlm2/cADD2jp0qUKCQlRQECAw+sCAAAA7gTPJOVDzZo106JFi7R161bt27dPffr0kbu7e7Z9Q0JC5Ovrq++//16nTp1SYqLj3slUsWJF7d69W2vXrtWhQ4f0+uuva9euXTZ9wsPD9dtvv+ngwYM6e/as0tLS1KtXLxUpUkTt27fX1q1bFRsbq82bN+uFF17QiRMnHFYfAAAAcDu4kpSdXHy5qyOMHj1asbGxevzxxxUYGKhJkybd8EqSh4eH3nvvPU2cOFFjx47Vww8/7LDBEZ555hnt2bNH3bp1k8ViUY8ePfT888/bDBM+cOBAbd68WbVr19bly5e1adMmNWnSRD/++KNeeeUVderUSZcuXVLJkiXVvHlzriwBAADA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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Compare the number of messages users of each plan tend to send each month\n",
    "avg_message_per_month = user_revenue.groupby(['plan', 'month'])['messages_count'].mean().reset_index()\n",
    "avg_message_per_month_pivot = avg_message_per_month.pivot(index='month', columns='plan', values='messages_count')\n",
    "avg_message_per_month_pivot.plot(kind='bar', figsize=(10, 6))\n",
    "plt.title('Average Messages Per Month by Plan')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Average Messages')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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bjp37iw9EgF4+gwplUqF77//nt8WTERERFpVro+lvv/+e3Tr1g3x8fHIycnB5MmTcebMGdy/fx8HDx7UdI1EREREpVauKzfNmjXDhQsX0KlTJwQEBCArKwv9+vXD8ePH0aBBA03XSERERFRqZb5yk5ubi549e2LJkiX44osvKqMmIiIionIr85UbfX19nDx5sjJqISIiIqqwcn0s9c477+DXX3/VdC1EREREFVauCcV5eXlYvnw59uzZg9atWxd6plR4eLhGiiMiIiIqqzKFmytXrsDFxQWnT59Gq1atAAAXLlxQ66NQKDRXHREREVEZlSncuLm5ISkpCTExMQCePm5hwYIFsLOzq5TiiIiIiMqqTHNunn/q944dO5CVlaXRgoiIiIgqolwTigs8H3aIiIiItK1M4UahUBSaU8M5NkRERFSdlGnOjRACQ4cOlR6O+eTJE4wcObLQ3VKbN2/WXIVEREREZVCmcBMcHKy2/M4772i0GCIiIqKKKlO4WbFiRWXVQURERKQRFZpQTERERFTdMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsMNwQERGRrDDcEBERkaww3BAREZGsaDXc7Nu3D3369IGjoyMUCgW2bt36wm1iY2PRqlUrKJVKNGzYEBEREZVeJxEREdUcWg03WVlZaNGiBRYuXFiq/levXoW/vz9effVVJCQkYNy4cRg+fDh27dpVyZUSERFRTaGnzYP36tULvXr1KnX/JUuWwNXVFXPmzAEAeHh44MCBA5g7dy78/Pwqq0wiIiKqQWrUnJu4uDj4+vqqtfn5+SEuLq7YbbKzs5GRkaH2IiIiIvnS6pWbskpOToadnZ1am52dHTIyMvD48WMYGRkV2iYsLAzTp0+vqhJLLfDm94Ub/6/2f//dZ37JO/i/sWqLh6/eV1veWndyqWto51q76A4vqgFA6OZTL9x/SUpTZ1HC+nk+/Y/nxqGQIs6hpJqL8ux5FDlWpRinCivHeRYo7fkW9fNSO9+qOM//r6w/o2dJ743yqsBYa4NWx6qcKlIzoL26XzY18b1VoEZduSmP0NBQpKenS68bN25ouyQiIiKqRDXqyo29vT1SUlLU2lJSUmBmZlbkVRsAUCqVUCqVVVEeERERVQM16sqNt7c3oqKi1NoiIyPh7e2tpYqIiIioutFquMnMzERCQgISEhIAPL3VOyEhAYmJiQCefqQUFBQk9R85ciSuXLmCyZMn49y5c1i0aBE2bNiA8ePHa6N8IiIiqoa0Gm7i4+PRsmVLtGzZEgAwYcIEtGzZElOmTAEAJCUlSUEHAFxdXfHXX38hMjISLVq0wJw5c/DLL7/wNnAiIiKSaHXOjY+PD4QQxa4v6tuHfXx8cPz48UqsioiIiGqyGjXnhoiIiOhFGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFYYboiIiEhWGG6IiIhIVhhuiIiISFaqRbhZuHAhXFxcYGhoiHbt2uHIkSPF9o2IiIBCoVB7GRoaVmG1REREVJ1pPdysX78eEyZMwNSpU3Hs2DG0aNECfn5+SE1NLXYbMzMzJCUlSa/r169XYcVERERUnWk93ISHh2PEiBEICQlBkyZNsGTJEhgbG2P58uXFbqNQKGBvby+97OzsqrBiIiIiqs60Gm5ycnJw9OhR+Pr6Sm06Ojrw9fVFXFxcsdtlZmbC2dkZTk5OCAgIwJkzZ4rtm52djYyMDLUXERERyZdWw83du3eRn59f6MqLnZ0dkpOTi9zG3d0dy5cvx7Zt27B69WqoVCp06NABN2/eLLJ/WFgYzM3NpZeTk5PGz4OIiIiqD61/LFVW3t7eCAoKgpeXF7p27YrNmzfDxsYGS5cuLbJ/aGgo0tPTpdeNGzequGIiIiKqSnraPLi1tTV0dXWRkpKi1p6SkgJ7e/tS7UNfXx8tW7bEpUuXilyvVCqhVCorXCsRERHVDFq9cmNgYIDWrVsjKipKalOpVIiKioK3t3ep9pGfn49Tp07BwcGhssokIiKiGkSrV24AYMKECQgODkabNm3Qtm1bzJs3D1lZWQgJCQEABAUFoU6dOggLCwMAzJgxA+3bt0fDhg2RlpaG2bNn4/r16xg+fLg2T4OIiIiqCa2Hm4EDB+LOnTuYMmUKkpOT4eXlhZ07d0qTjBMTE6Gj898FpgcPHmDEiBFITk6GpaUlWrdujUOHDqFJkybaOgUiIiKqRrQebgBg9OjRGD16dJHrYmNj1Zbnzp2LuXPnVkFVREREVBPVuLuliIiIiErCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESywnBDREREssJwQ0RERLLCcENERESyUi3CzcKFC+Hi4gJDQ0O0a9cOR44cKbH/xo0b0bhxYxgaGsLT0xPbt2+vokqJiIioutN6uFm/fj0mTJiAqVOn4tixY2jRogX8/PyQmppaZP9Dhw5h8ODBGDZsGI4fP47AwEAEBgbi9OnTVVw5ERERVUdaDzfh4eEYMWIEQkJC0KRJEyxZsgTGxsZYvnx5kf3nz5+Pnj17YtKkSfDw8MDMmTPRqlUr/PTTT1VcOREREVVHWg03OTk5OHr0KHx9faU2HR0d+Pr6Ii4ursht4uLi1PoDgJ+fX7H9iYiI6OWip82D3717F/n5+bCzs1Nrt7Ozw7lz54rcJjk5ucj+ycnJRfbPzs5Gdna2tJyeng4A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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "avg_message = user_revenue.groupby(['plan','month'])['messages_count'].sum().reset_index()\n",
    "\n",
    "for plan in avg_message['plan'].unique():\n",
    "    plt.hist( avg_message.loc[avg_message['plan'] == plan, 'messages_count'],\n",
    "              bins=30,\n",
    "              alpha=0.6,\n",
    "              label=plan)\n",
    "plt.xlabel('Message Counted')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Distribution of Messages by Plan')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "monthly_messages = user_revenue.groupby(['user_id', 'month'])['messages_count'].sum().reset_index()\n",
    "mess_mean_count = monthly_messages['messages_count'].mean()\n",
    "mess_variance_count = monthly_messages['messages_count'].var() \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33.166593981683384"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mess_mean_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1160.770663655758"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mess_variance_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAksAAAG9CAYAAAAFnjKbAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAABWf0lEQVR4nO3deVxU5f8+/mvYhh1EdkVAMRXFJTVwAVzYFE1EcskVTculvgZqaeWepolLamq9yy21DAkTN1AR0cSFssQtNdwBtwABZRnO7w9/Mx9H8MjYwAzM9Xw8fMjc555zXrOc4eKc+9wjEQRBABERERFVSk/TBRARERFpM4YlIiIiIhEMS0REREQiGJaIiIiIRDAsEREREYlgWCIiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCIYl0iqzZ8+GRCKpkW1169YN3bp1U9w+fPgwJBIJYmNja2T7o0aNgpubW41s61UVFBTgnXfegaOjIyQSCSZPnqzpkv4T+fvr/v37L+3r5uaGUaNGVX9R9J/U9H77Mhs2bIBEIsG1a9c0XQqpEcMSVRv5h4b8n7GxMZydnREcHIyvvvoKjx49Ust27ty5g9mzZ+PMmTNqWZ86aXNtVbFgwQJs2LAB48ePx+bNmzF8+PAX9nVzc4NEIkFAQECly7/99lvFe+H06dPVVTKAp3XHx8dX6zZUce3aNcVjnz9/fqV9hg4dColEAnNz8xqujqpCHrTl/0xNTeHp6YlPP/0U+fn5mi6PqhnDElW7uXPnYvPmzVizZg3ef/99AMDkyZPh5eWFv/76S6nvp59+isePH6u0/jt37mDOnDkqB5LExEQkJiaqdB9VidX27bff4tKlS9W6/f/q0KFD8PHxwaxZszBs2DC0b99etL+xsTGSk5ORnZ1dYdmWLVtgbGxcXaUq0bawJGdsbIxt27ZVaC8sLMTOnTtr7PmhV7dmzRps3rwZS5cuRfPmzfH5558jJCQE/JrVuo1hiapdr169MGzYMERGRmL69OnYv38/Dhw4gLt37+LNN99UCkcGBgbV/gujqKgIAGBkZAQjI6Nq3ZYYQ0NDSKVSjW2/Ku7evQtra+sq9+/SpQvMzc3x008/KbXfunULqampCA0NVXOFtUvv3r1x/vx5/Pnnn0rtO3fuRElJCQIDAzVUGVVVREQEhg0bhvfeew9xcXEIDw/H8ePHkZaWpunSqBoxLJFG9OjRA5999hmuX7+OH374QdFe2ZilpKQkdO3aFdbW1jA3N0ezZs0wY8YMAE/HK3Ts2BEAEBkZqThEvmHDBgBPxyW1atUK6enp8PPzg6mpqeK+z49ZkpPJZJgxYwYcHR1hZmaGN998Ezdv3lTq86LxLM+u82W1VTZmqbCwENHR0XBxcYFUKkWzZs2wZMmSCn+1SiQSTJo0CfHx8WjVqhWkUilatmyJffv2Vf6EP+fu3bsYM2YMHBwcYGxsjDZt2mDjxo2K5fJxIJmZmdi9e7ei9peNwzA2NkZ4eDi2bt2q1L5t2zbUq1cPwcHBld7v0KFD8PX1hZmZGaytrdGvXz9cuHBBqY/8vXHlyhWMGjUK1tbWsLKyQmRkpCIAy5+bwsJCbNy4UVH3869Vbm6u6Dqe988//0AikWDZsmUVlv3222+QSCSVHjF6XqdOneDu7l7h+dmyZQtCQkJgY2NT6f327t2reH4sLCwQGhqKc+fOKfXJzs5GZGQkGjZsCKlUCicnJ/Tr10/pNTt9+jSCg4Nha2sLExMTuLu7Y/To0UrrWbJkCTp37oz69evDxMQE7du3r3Q80OPHj/HBBx/A1tYWFhYWePPNN3H79m1IJBLMnj1bqe/t27cxevRoODg4KN6r33//fYV1rly5Ei1btoSpqSnq1auHDh06VHiuXuRl++2sWbNgaGiIe/fuVbjvuHHjYG1tjSdPnlRpW8/q0aMHACAzM/OFfXbu3InQ0FA4OztDKpWiSZMmmDdvHmQymVI/+efV+fPn0b17d5iamqJBgwZYvHixynWRejEskcbIx7+InQo7d+4c+vTpg+LiYsydOxcxMTF48803cezYMQBAixYtMHfuXABPP/A2b96MzZs3w8/PT7GOBw8eoFevXmjbti2WL1+O7t27i9b1+eefY/fu3fjoo4/wwQcfICkpCQEBASqfHqxKbc8SBAFvvvkmli1bhpCQECxduhTNmjXD1KlTERUVVaH/0aNHMWHCBAwePBiLFy/GkydPMGDAADx48EC0rsePH6Nbt27YvHkzhg4dii+//BJWVlYYNWoUVqxYoah98+bNsLW1Rdu2bRW129nZvfRxv/322zh58iSuXr2qaNu6dSsiIiJgaGhYof+BAwcQHByMu3fvYvbs2YiKisJvv/2GLl26VBrOBg4ciEePHmHhwoUYOHAgNmzYgDlz5iiWb968GVKpFL6+voq63333XZXW8bzGjRujS5cu2LJlS4VlW7ZsgYWFBfr16/fS5wYAhgwZgh9//FERgO/fv4/ExES8/fbblfbfvHkzQkNDYW5ujkWLFuGzzz7D+fPn0bVrV6XnZ8CAAfjll18QGRmJr7/+Gh988AEePXqEGzduAHgakIOCgnDt2jV8/PHHWLlyJYYOHVrhiMiKFSvQrl07zJ07FwsWLICBgQHeeust7N69W6nfqFGjsHLlSvTu3RuLFi2CiYlJpUcOc3Jy4OPjgwMHDmDSpElYsWIFPDw8MGbMGCxfvlzR79tvv8UHH3wAT09PLF++HHPmzEHbtm1x4sSJKj2vL9tvhw8fjrKysgpHPUtKShAbG4sBAwa80lFt+fu8fv36L+yzYcMGmJubIyoqCitWrED79u0xc+ZMfPzxxxX6/vvvvwgJCUGbNm0QExOD5s2b46OPPsLevXtVro3USCCqJuvXrxcACKdOnXphHysrK6Fdu3aK27NmzRKefVsuW7ZMACDcu3fvhes4deqUAEBYv359hWX+/v4CAGHt2rWVLvP391fcTk5OFgAIDRo0EPLz8xXt27dvFwAIK1asULS5uroKI0eOfOk6xWobOXKk4OrqqrgdHx8vABDmz5+v1C8iIkKQSCTClStXFG0ABCMjI6W2P//8UwAgrFy5ssK2nrV8+XIBgPDDDz8o2kpKSoROnToJ5ubmSo/d1dVVCA0NFV3f833LysoER0dHYd68eYIgCML58+cFAEJKSkql74m2bdsK9vb2woMHD5Qei56enjBixAhFm/y9MXr0aKXt9u/fX6hfv75Sm5mZWaWvjyrreP41XrdunQBAuHDhgqKtpKREsLW1rXRbz8rMzBQACF9++aWQkZEhABBSU1MFQRCE1atXC+bm5kJhYaEwcuRIwczMTHG/R48eCdbW1sLYsWOV1pednS1YWVkp2v/991/F+l/kl19+een+KAiCUFRUpHS7pKREaNWqldCjRw9FW3p6ugBAmDx5slLfUaNGCQCEWbNmKdrGjBkjODk5Cffv31fqO3jwYMHKykqxvX79+gktW7YUra0yquy3nTp1Ery9vZXuHxcXJwAQkpOTRbcjf+9cunRJuHfvnpCZmSmsW7dOkEqlgoODg1BYWCgIwv997mVmZiru+/xzKgiC8O677wqmpqbCkydPFG3yz6tNmzYp2oqLiwVHR0dhwIABVXo+qHrwyBJplLm5uehVcfLxMjt37kR5efkrbUMqlSIyMrLK/UeMGAELCwvF7YiICDg5OWHPnj2vtP2q2rNnD/T19fHBBx8otUdHR0MQhAp/WQYEBKBJkyaK261bt4alpSX++eefl27H0dERQ4YMUbQZGhrigw8+QEFBAVJSUv7T49DX18fAgQMVp6W2bNkCFxcX+Pr6VuiblZWFM2fOYNSoUUqnoFq3bo3AwMBKn/P33ntP6bavry8ePHig0hVJr7KOgQMHwtjYWOno0v79+3H//n0MGzasyttu2bIlWrdurXh+tm7din79+sHU1LRC36SkJOTm5mLIkCG4f/++4p++vj68vb2RnJwMADAxMYGRkREOHz6Mf//9t9LtyvelhIQElJaWvrA+ExMTxc///vsv8vLy4Ovri99//13RLj/dO2HCBKX7yi/gkBMEATt27EDfvn0hCILSYwgODkZeXp5ivdbW1rh16xZOnTr1wtrEVGW/HTFiBE6cOKF01FP+/vT396/Sdpo1awY7Ozu4u7vj3XffhYeHB3bv3l3p6yf37HP66NEj3L9/H76+vigqKsLFixeV+pqbmyu9n4yMjPDGG2+8dL+m6sWwRBpVUFCg9AH3vEGDBqFLly5455134ODggMGDB2P79u0qBacGDRqoNJC7adOmSrclEgk8PDyqfd6U69evw9nZucLz0aJFC8XyZzVq1KjCOurVq/fCX5bPbqdp06bQ01Pe/V+0nVfx9ttvKwYyb926FYMHD650/iz5tpo1a1ZhWYsWLXD//n0UFhYqtT//uOvVqwcAL33c/3Ud1tbW6Nu3r9IYmi1btqBBgwaKcStV9fbbb+Pnn3/GlStX8Ntvv73wFNzly5cBPB0XY2dnp/QvMTERd+/eBfD0D4JFixZh7969cHBwgJ+fHxYvXqx0VaK/vz8GDBiAOXPmwNbWFv369cP69etRXFystM2EhAT4+PjA2NgYNjY2sLOzw5o1a5CXl6foc/36dejp6cHd3V3pvh4eHkq37927h9zcXHzzzTcV6pf/ASN/DB999BHMzc3xxhtvoGnTppg4caLidHtVVGW/HTRoEKRSqSLw5uXlISEhQTFtQ1Xs2LEDSUlJOHz4MK5cuYKMjIyXXiV67tw59O/fH1ZWVrC0tISdnZ0iED37vAJAw4YNK9RSlf2aqpeBpgsg3XXr1i3k5eVV+IB9lomJCY4cOYLk5GTs3r0b+/btw08//YQePXogMTER+vr6L93Os3/VqcuLPlhlMlmValKHF21H0IJLmL29vdGkSRNMnjwZmZmZLwwDr0Idj/tV1zFixAj8/PPP+O233+Dl5YVff/0VEyZMqBA8X2bIkCGYPn06xo4di/r16yMoKKjSfvI/CjZv3gxHR8cKyw0M/u8jfPLkyejbty/i4+Oxf/9+fPbZZ1i4cCEOHTqEdu3aKSZuTEtLw65du7B//36MHj0aMTExSEtLg7m5OVJTU/Hmm2/Cz88PX3/9NZycnGBoaIj169dXeaB1ZfUPGzYMI0eOrLRP69atATwNx5cuXUJCQgL27duHHTt24Ouvv8bMmTNFx5Opol69eujTpw+2bNmCmTNnIjY2FsXFxSodGfTz84OtrW2V++fm5sLf3x+WlpaYO3cumjRpAmNjY/z+++/46KOPKvzhp837tS5jWCKN2bx5MwC88AopOT09PfTs2RM9e/bE0qVLsWDBAnzyySdITk5GQECA2mf8lv81LycIAq5cuaL4UAeefujm5uZWuO/169fRuHFjxW1VanN1dcWBAwfw6NEjpaNL8sP0rq6uVV7Xy7bz119/oby8XOmXvLq3M2TIEMyfPx8tWrRA27ZtX1gLgErnm7p48SJsbW1hZmam8raraxb4kJAQ2NnZYcuWLfD29kZRUZHoRJ0v0qhRI3Tp0gWHDx/G+PHjlULPs+SnWe3t7V842efz/aOjoxEdHY3Lly+jbdu2iImJUbri1MfHBz4+Pvj888+xdetWDB06FD/++CPeeecd7NixA8bGxti/f7/StBbr169X2o6rqyvKy8uRmZmpdETnypUrSv3s7OxgYWEBmUxWpfrNzMwwaNAgDBo0CCUlJQgPD8fnn3+O6dOnv3TwdVX2W+Bp4O3Xrx9OnTqFLVu2oF27dmjZsuVLa3tVhw8fxoMHDxAXF6d0cYfY1XOkfXgajjTi0KFDmDdvHtzd3TF06NAX9nv48GGFNvkvXvnpA/kv08rCy6vYtGmT0jiq2NhYZGVloVevXoq2Jk2aIC0tDSUlJYq2hISEClMMqFJb7969IZPJsGrVKqX2ZcuWQSKRKG3/v+jduzeys7OVrgoqKyvDypUrYW5uXuWxGy/zzjvvYNasWYiJiXlhHycnJ7Rt2xYbN25Ueo4yMjKQmJiI3r17v9K2zczM1PZ+eJaBgQGGDBmC7du3Y8OGDfDy8qrwy7iq5s+fj1mzZlUY5/Os4OBgWFpaYsGCBZWOM5JfBl9UVFThsvcmTZrAwsJCsZ/8+++/FY5OPL8v6evrQyKRKF3Sfu3atQoTfMr/wPn666+V2leuXKl0W19fHwMGDMCOHTuQkZHxwvoBVLiK08jICJ6enhAEQXSMlVxV9lvg6bxvtra2WLRoEVJSUlQ6qvQq5EeKnn3uS0pKKjx3pN14ZImq3d69e3Hx4kWUlZUhJycHhw4dQlJSElxdXfHrr7+K/sU4d+5cHDlyBKGhoXB1dcXdu3fx9ddfo2HDhujatSuAp78UrK2tsXbtWlhYWMDMzAze3t4VxlNUlY2NDbp27YrIyEjk5ORg+fLl8PDwwNixYxV93nnnHcTGxiIkJAQDBw7E1atX8cMPPygNuFa1tr59+6J79+745JNPcO3aNbRp0waJiYnYuXMnJk+eXGHdr2rcuHFYt24dRo0ahfT0dLi5uSE2NhbHjh3D8uXLRceQqcLV1bXCfDuV+fLLL9GrVy906tQJY8aMwePHj7Fy5UpYWVlV6f6Vad++PQ4cOIClS5fC2dkZ7u7u8Pb2fqV1PW/EiBH46quvkJycjEWLFr3yevz9/V8aTC0tLbFmzRoMHz4cr7/+OgYPHgw7OzvcuHEDu3fvRpcuXbBq1Sr8/fff6NmzJwYOHAhPT08YGBjgl19+QU5ODgYPHgwA2LhxI77++mv0798fTZo0waNHj/Dtt9/C0tJSEUpDQ0OxdOlShISE4O2338bdu3exevVqeHh4KM223759ewwYMADLly/HgwcP4OPjg5SUFPz9998AlI/sffHFF0hOToa3tzfGjh0LT09PPHz4EL///jsOHDig+IMoKCgIjo6O6NKlCxwcHHDhwgWsWrUKoaGhVXpPVmW/BZ5ezDB48GCsWrUK+vr6Shc6VIfOnTujXr16GDlyJD744ANIJBJs3ryZp9VqG41cg0c6QX4JrfyfkZGR4OjoKAQGBgorVqxQusxX7vmpAw4ePCj069dPcHZ2FoyMjARnZ2dhyJAhwt9//610v507dwqenp6CgYGB0qX6/v7+L7wc+UVTB2zbtk2YPn26YG9vL5iYmAihoaHC9evXK9w/JiZGaNCggSCVSoUuXboIp0+frrBOsdqenzpAEJ5eKv7hhx8Kzs7OgqGhodC0aVPhyy+/FMrLy5X6ARAmTpxYoaYXTWnwvJycHCEyMlKwtbUVjIyMBC8vr0qnN3iVqQPEvGg6iQMHDghdunQRTExMBEtLS6Fv377C+fPnlfrI3xvPTyNR2aXaFy9eFPz8/AQTExMBgOI5UWUdYs9ly5YtBT09PeHWrVuij1fu2akDxDw/dYBccnKyEBwcLFhZWQnGxsZCkyZNhFGjRgmnT58WBEEQ7t+/L0ycOFFo3ry5YGZmJlhZWQne3t7C9u3bFev4/fffhSFDhgiNGjUSpFKpYG9vL/Tp00exDrnvvvtOaNq0qSCVSoXmzZsL69evr7BfCoIgFBYWChMnThRsbGwEc3NzISwsTLh06ZIAQPjiiy+U+ubk5AgTJ04UXFxcBENDQ8HR0VHo2bOn8M033yj6rFu3TvDz8xPq168vSKVSoUmTJsLUqVOFvLw80edM1f1WEATh5MmTAgAhKChIdN3PetF753mVvZeOHTsm+Pj4CCYmJoKzs7Mwbdo0Yf/+/RWmLHjR51VlnxVUsySCwHhLRKSKdu3awcbGBgcPHtR0KVrlzJkzaNeuHX744QfR0+ua9ueff6Jt27bYtGnTK405I93DMUtERCo4ffo0zpw5gxEjRmi6FI2qbEb75cuXQ09P74Wz1GuLb7/9Fubm5ggPD9d0KVRLcMwSEVEVZGRkID09HTExMXBycsKgQYM0XZJGLV68GOnp6ejevTsMDAywd+9e7N27F+PGjYOLi4umy6vUrl27cP78eXzzzTeYNGnSK11pSbqJp+GIiKpg9uzZmDt3Lpo1a4a1a9eq7arB2iopKQlz5szB+fPnUVBQgEaNGmH48OH45JNPXjgVgqa5ubkhJycHwcHB2Lx5s9ouZqC6j2GJiIiISATHLBERERGJYFgiIiIiEqGdJ5ZrWHl5Oe7cuQMLC4tq+5oEIiIi0i6CIODRo0dwdnYW/Y5HhiUAd+7c0dqrN4iIiKh63bx5Ew0bNnzhcoYlQHFFxM2bN2FpaanhaqimlZaWIjExEUFBQTA0NNR0OURUg7j/67b8/Hy4uLi89MpIhiX83/cYWVpaMizpoNLSUpiamsLS0pIflkQ6hvs/AXjpEBwO8CYiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCIYlIiIiIhEMS0REREQiGJaIiIiIRDAsEREREYlgWCKdJpPJkJKSgiNHjiAlJQUymUzTJRERkZZhWCKdFRcXBw8PDwQGBmLp0qUIDAyEh4cH4uLiNF0aERFpEYYl0klxcXGIiIiAl5cXUlNTsW3bNqSmpsLLywsREREMTEREpMCwRDpHJpMhOjoaffr0QXx8PLy9vWFiYgJvb2/Ex8ejT58+mDJlCk/JERERAIYl0kGpqam4du0aZsyYAT095V1AT08P06dPR2ZmJlJTUzVUIRERaROGJdI5WVlZAIBWrVpVulzeLu9HRES6jWGJdI6TkxMAICMjo9Ll8nZ5PyIi0m0MS6RzfH194ebmhgULFqC8vFxpWXl5ORYuXAh3d3f4+vpqqEIiItImDEukc/T19RETE4OEhASEhYUhLS0Njx8/RlpaGsLCwpCQkIAlS5ZAX19f06USEZEWMNB0AUSaEB4ejtjYWERHR8PPz0/R7u7ujtjYWISHh2uwOiIi0iYMS6SzwsPD0a9fPyQnJ2Pv3r3o1asXunfvziNKRESkhGGJdJq+vj78/f1RWFgIf39/BiUiIqqAY5aIiIiIRDAsEREREYlgWCIiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCIYlIiIiIhEMS0REREQiGJaIiIiIRGg0LC1cuBAdO3aEhYUF7O3tERYWhkuXLin16datGyQSidK/9957T6nPjRs3EBoaClNTU9jb22Pq1KkoKyuryYdCREREdZRGv+4kJSUFEydORMeOHVFWVoYZM2YgKCgI58+fh5mZmaLf2LFjMXfuXMVtU1NTxc8ymQyhoaFwdHTEb7/9hqysLIwYMQKGhoZYsGBBjT4eIiIiqns0Gpb27dundHvDhg2wt7dHenq60jfBm5qawtHRsdJ1JCYm4vz58zhw4AAcHBzQtm1bzJs3Dx999BFmz54NIyOjan0MREREVLdp1Rfp5uXlAQBsbGyU2rds2YIffvgBjo6O6Nu3Lz777DPF0aXjx4/Dy8sLDg4Oiv7BwcEYP348zp07h3bt2lXYTnFxMYqLixW38/PzAQClpaUoLS1V++Mi7SZ/zfnaE+ke7v+6raqvu9aEpfLyckyePBldunRBq1atFO1vv/02XF1d4ezsjL/++gsfffQRLl26hLi4OABAdna2UlACoLidnZ1d6bYWLlyIOXPmVGhPTExUOsVHuiUpKUnTJRCRhnD/101FRUVV6qc1YWnixInIyMjA0aNHldrHjRun+NnLywtOTk7o2bMnrl69iiZNmrzStqZPn46oqCjF7fz8fLi4uCAoKAiWlpav9gCo1iotLUVSUhICAwNhaGio6XKIqAZx/9dt8jNLL6MVYWnSpElISEjAkSNH0LBhQ9G+3t7eAIArV66gSZMmcHR0xMmTJ5X65OTkAMALxzlJpVJIpdIK7YaGhtxZdBhffyLdxf1fN1X1Ndfo1AGCIGDSpEn45ZdfcOjQIbi7u7/0PmfOnAEAODk5AQA6deqEs2fP4u7du4o+SUlJsLS0hKenZ7XUTURERLpDo0eWJk6ciK1bt2Lnzp2wsLBQjDGysrKCiYkJrl69iq1bt6J3796oX78+/vrrL3z44Yfw8/ND69atAQBBQUHw9PTE8OHDsXjxYmRnZ+PTTz/FxIkTKz16RERERKQKjR5ZWrNmDfLy8tCtWzc4OTkp/v30008AACMjIxw4cABBQUFo3rw5oqOjMWDAAOzatUuxDn19fSQkJEBfXx+dOnXCsGHDMGLECKV5mYiIiIhelUaPLAmCILrcxcUFKSkpL12Pq6sr9uzZo66yiIiIiBT43XBEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRDpNJpMhJSUFR44cQUpKCmQymaZLIiIiLcOwRDorLi4OHh4eCAwMxNKlSxEYGAgPDw/ExcVpujQiItIiDEukk+Li4hAREQEvLy+kpqZi27ZtSE1NhZeXFyIiIhiYiIhIgWGJdI5MJkN0dDT69OmD+Ph4eHt7w8TEBN7e3oiPj0efPn0wZcoUnpIjIiIADEukg1JTU3Ht2jXMmDEDenrKu4Cenh6mT5+OzMxMpKamaqhCIiLSJgxLpHOysrIAAK1atap0ubxd3o+IiHQbwxLpHCcnJwBARkZGpcvl7fJ+RESk2xiWSOf4+vrCzc0NCxYsQHl5udKy8vJyLFy4EO7u7vD19dVQhUREpE0Ylkjn6OvrIyYmBgkJCQgLC0NaWhoeP36MtLQ0hIWFISEhAUuWLIG+vr6mSyUiIi1goOkCiDQhPDwcsbGxiI6Ohp+fn6Ld3d0dsbGxCA8P12B1RESkTRiWSGeFh4ejX79+SE5Oxt69e9GrVy90796dR5SIiEgJwxLpNH19ffj7+6OwsBD+/v4MSkREVAHHLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEqHRsLRw4UJ07NgRFhYWsLe3R1hYGC5duqTU58mTJ5g4cSLq168Pc3NzDBgwADk5OUp9bty4gdDQUJiamsLe3h5Tp05FWVlZTT4UIiIiqqM0GpZSUlIwceJEpKWlISkpCaWlpQgKCkJhYaGiz4cffohdu3bh559/RkpKCu7cuYPw8HDFcplMhtDQUJSUlOC3337Dxo0bsWHDBsycOVMTD4mIiIjqGANNbnzfvn1Ktzds2AB7e3ukp6fDz88PeXl5+O6777B161b06NEDALB+/Xq0aNECaWlp8PHxQWJiIs6fP48DBw7AwcEBbdu2xbx58/DRRx9h9uzZMDIy0sRDIyIiojpCo2HpeXl5eQAAGxsbAEB6ejpKS0sREBCg6NO8eXM0atQIx48fh4+PD44fPw4vLy84ODgo+gQHB2P8+PE4d+4c2rVrV2E7xcXFKC4uVtzOz88HAJSWlqK0tLRaHhtpL/lrzteeSPdw/9dtVX3dtSYslZeXY/LkyejSpQtatWoFAMjOzoaRkRGsra2V+jo4OCA7O1vR59mgJF8uX1aZhQsXYs6cORXaExMTYWpq+l8fCtVSSUlJmi6BiDSE+79uKioqqlI/rQlLEydOREZGBo4ePVrt25o+fTqioqIUt/Pz8+Hi4oKgoCBYWlpW+/ZJu5SWliIpKQmBgYEwNDTUdDlEVIO4/+s2+Zmll9GKsDRp0iQkJCTgyJEjaNiwoaLd0dERJSUlyM3NVTq6lJOTA0dHR0WfkydPKq1PfrWcvM/zpFIppFJphXZDQ0PuLDqMrz+R7uL+r5uq+ppr9Go4QRAwadIk/PLLLzh06BDc3d2Vlrdv3x6GhoY4ePCgou3SpUu4ceMGOnXqBADo1KkTzp49i7t37yr6JCUlwdLSEp6enjXzQIiIiKjO0uiRpYkTJ2Lr1q3YuXMnLCwsFGOMrKysYGJiAisrK4wZMwZRUVGwsbGBpaUl3n//fXTq1Ak+Pj4AgKCgIHh6emL48OFYvHgxsrOz8emnn2LixImVHj0iIiIiUoVGw9KaNWsAAN26dVNqX79+PUaNGgUAWLZsGfT09DBgwAAUFxcjODgYX3/9taKvvr4+EhISMH78eHTq1AlmZmYYOXIk5s6dW1MPg4iIiOowjYYlQRBe2sfY2BirV6/G6tWrX9jH1dUVe/bsUWdpRERERAD43XBEREREohiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCTiP4clmUyGM2fO4N9//1VHPUQ1SiaTISUlBUeOHEFKSgpkMpmmSyIiIi2jcliaPHkyvvvuOwBPf9H4+/vj9ddfh4uLCw4fPqzu+oiqTVxcHDw8PBAYGIilS5ciMDAQHh4eiIuL03RpRESkRVQOS7GxsWjTpg0AYNeuXcjMzMTFixfx4Ycf4pNPPlF7gUTVIS4uDhEREfDy8kJqaiq2bduG1NRUeHl5ISIigoGJiIgUVA5L9+/fh6OjIwBgz549eOutt/Daa69h9OjROHv2rNoLJFI3mUyG6Oho9OnTB/Hx8fD29oaJiQm8vb0RHx+PPn36YMqUKTwlR0REAF4hLDk4OOD8+fOQyWTYt28fAgMDAQBFRUXQ19dXe4FE6paamopr165hxowZ0NNT3gX09PQwffp0ZGZmIjU1VUMVEhGRNjFQ9Q6RkZEYOHAgnJycIJFIEBAQAAA4ceIEmjdvrvYCidQtKysLANCqVatKl8vb5f2IiEi3qRyWZs+ejVatWuHmzZt46623IJVKAQD6+vr4+OOP1V4gkbo5OTkBADIyMuDj41NheUZGhlI/IiLSbSqHJQCIiIgAADx58kTRNnLkSPVURFTNfH194ebmhgULFiA+Pl5pWXl5ORYuXAh3d3f4+vpqpkAiItIqKo9ZkslkmDdvHho0aABzc3P8888/AIDPPvtMMaUAkTbT19dHTEwMEhISEBYWhrS0NDx+/BhpaWkICwtDQkIClixZwjF4REQE4BXC0ueff44NGzZg8eLFMDIyUrS3atUK//vf/9RaHFF1CQ8PR2xsLM6ePQs/Pz8MGTIEfn5+yMjIQGxsLMLDwzVdIhERaQmVw9KmTZvwzTffYOjQoUp/ebdp0wYXL15Ua3FE1Sk8PBxXrlxBUlISoqKikJSUhMuXLzMoERGREpXHLN2+fRseHh4V2svLy1FaWqqWoohqir6+Pvz9/VFYWAh/f3+eeiMiogpUPrLk6elZ6fwzsbGxaNeunVqKIiIiItIWKh9ZmjlzJkaOHInbt2+jvLwccXFxuHTpEjZt2oSEhITqqJGIiIhIY1Q+stSvXz/s2rULBw4cgJmZGWbOnIkLFy5g165ditm8iYiIiOqKV5pnydfXF0lJSequhajGyWQypKSk4MiRIzAzM0P37t05bomIiJSofGSJqK6Ii4uDh4cHAgMDsXTpUgQGBsLDwwNxcXGaLo2IiLSIymGpXr16sLGxqfCvfv36aNCgAfz9/bF+/frqqJVIbeLi4hAREQEvLy+kpqZi27ZtSE1NhZeXFyIiIhiYiHTAs0eWU1JSIJPJNF0SaSmJIAiCKndYtmwZPv/8c/Tq1QtvvPEGAODkyZPYt28fPvzwQ2RmZmLz5s1YuXIlxo4dWy1Fq1t+fj6srKyQl5cHS0tLTZdD1Uwmk8HDwwNeXl6Ij4+HTCbDnj170Lt3b+jr6yMsLAwZGRm4fPkyT8kR1VFxcXGIjo7GtWvXFG1ubm6IiYnhXGs6pKq//1Ues3T06FHMnz8f7733nlL7unXrkJiYiB07dqB169b46quvak1YIt2SmpqKa9euYdu2bdDT01P6a1JPTw/Tp09H586dkZqaim7dummuUCKqFvIjy3369MHmzZtx69YtNGzYEIsXL0ZERARn8acKVD4Nt3//fgQEBFRo79mzJ/bv3w8A6N27t+I744i0TVZWFoCnX9FT2WH4Vq1aKfUjorpDJpMhOjoaffr0QXx8PLy9vWFiYgJvb2/Ex8ejT58+mDJlCk/JkRKVw5KNjQ127dpVoX3Xrl2wsbEBABQWFsLCwuK/V0dUDZycnAAAq1atqnSA96pVq5T6EVHdIT+yPGPGDOjpKf8KlB9ZzszMrHTyZdJdKp+G++yzzzB+/HgkJycrxiydOnUKe/bswdq1awEASUlJ8Pf3V2+lRGri6+sLe3t7TJ8+vcJh+EWLFmHGjBmwt7eHr6+vpkslIjV79shyZXhkmSqjclgaO3YsPD09sWrVKsUVQ82aNUNKSgo6d+4MAIiOjlZvlURq9ux1DfKfVbzWgYhqIfkR44yMDPj4+FRYnpGRodSPCHiFq+HqIl4Np1sOHz6M7t27Y+HChVi3bp3S1TDu7u4YO3YsZsyYgeTkZA7wJqpjeDUsPauqv///06SUT548QX5+vtI/Im0nP7w+adIkXLlyBUlJSYiKikJSUhIuX76MSZMmKfUjorpDX18fMTExSEhIQFhYGNLS0vD48WOkpaUhLCwMCQkJWLJkCYMSKVH5NFxRURGmTZuG7du348GDBxWW8woC0nbPHobv2LFjheU8DE9Ut4WHhyM2NhbR0dHw8/NTtLu7u3PaAKqUyqfhJk6ciOTkZMybNw/Dhw/H6tWrcfv2baxbtw5ffPEFhg4dWl21VhuehtMt8sPwtra2uHfvHq5fv65Y5urqCjs7Ozx48ICH4YnqOJlMhuTkZOzduxe9evXid0PqoGqblHLXrl3YtGkTunXrhsjISPj6+sLDwwOurq7YsmVLrQxLpFv09fXx1ltv4csvv4SdnR0iIiLw8OFD2NjYICUlBadPn8bUqVP5oUlUx+nr68Pf3x+FhYXw9/fnPk8vpHJYevjwIRo3bgwAsLS0xMOHDwEAXbt2xfjx49VbHVE1kMlk+Pnnn+Hg4ICcnBzExsYqLXdwcEBsbCwWLlzID08iIlJ9gHfjxo2RmZkJAGjevDm2b98O4OkRJ2tra7UWR1Qd5JPS5eTkVLo8JyeHk9IREZGCykeWIiMj8eeff8Lf3x8ff/wx+vbti1WrVqG0tBRLly6tjhqJ1OrmzZuKn+3t7TF37lxIpVIUFxdj5syZuHv3boV+RFT3PPt1R2ZmZhyzRC/0n+dZun79OtLT0+Hh4YHWrVurq64axQHeuuXdd9/FN998A1NTU+Tl5UEQBMU8KxKJBFZWVigqKsK4ceOwbt06TZdLRNUgLi4O0dHRSvOsubm5ISYmhlfD6ZBqG+D9PFdXV1hZWfEUHNUa586dA/D0g7G4uBhTpkxBWloa9u3bhyVLlsDV1RUXLlxQ9COiuiUuLg4REREIDQ1FVFQU/v77b7z22mtITExEREQEpw+gClQ+srRo0SK4ublh0KBBAICBAwdix44dcHR0xJ49e9CmTZtqKbQ68ciSbunatSuOHTv20n5dunTB0aNHa6AiIqopz04dcv/+/QpHlmxtbTl1iA6pthm8165dCxcXFwBPvzA3KSlJMUfF1KlTX71iohrSr18/tfYjotpDfoFHeno6vLy8kJqaim3btiE1NRVeXl5IT0/nBR5UgcphKTs7WxGWEhISMHDgQAQFBWHatGk4deqU2gskUrdx48Ypfra1tcXkyZMxbtw4TJ48Gba2tpX2I6K64fbt2wCAkJAQ7NixA0+ePMGpU6fw5MkT7NixAyEhIUr9iIBXGLNUr1493Lx5Ey4uLti3bx/mz58P4Ok3tvOrTqg2+OSTTxQ/379/H8uXL39hv1WrVtVQVURUE+7duwfg6Sk3Dw8P3LhxAwCwdOlSNGrUCL1791bqRwS8wpGl8PBwvP322wgMDMSDBw/Qq1cvAMAff/wBDw8PldZ15MgR9O3bF87OzpBIJIiPj1daPmrUKEgkEqV/8tQv9/DhQwwdOhSWlpawtrbGmDFjUFBQoOrDIh1y+fJlAEDPnj0rXS5vl/cjorrDzs4OALBmzZoK04PcvHkTa9euVepHBLxCWFq2bBkmTZoET09PJCUlwdzcHMDTb2ifMGGCSusqLCxEmzZtsHr16hf2CQkJQVZWluLftm3blJYPHToU586dQ1JSEhISEnDkyBGePiFRTZs2BQAcPHgQxsbGSsuMjY1x8OBBpX5EVHc4Ojoqfn7++qZnbz/bj+g/z7OkLhKJBL/88gvCwsIUbaNGjUJubm6FI05yFy5cgKenJ06dOoUOHToAAPbt24fevXvj1q1bcHZ2rtK2eTWcbikoKICFhQWAp2G8d+/eikuH9+zZg3379gEAHj16pPhjgIjqhr179ypOtYnZs2eP4swJ1V3VNs/Sxo0bYWtri9DQUADAtGnT8M0338DT0xPbtm2Dq6vrq1ddicOHD8Pe3h716tVDjx49MH/+fNSvXx8AcPz4cVhbWyuCEgAEBARAT08PJ06cQP/+/StdZ3FxMYqLixW38/PzAQClpaUoLS1Va/2kfX777TfFz/v27VOEo8r6de/evabKIqIasGnTJsXP9vb2GDx4MJ48eQJjY2P8+OOPihn8N23ahICAAE2VSTWkqr/zVQ5LCxYswJo1awA8DSurV6/GsmXLkJCQgA8//BBxcXGqrvKFQkJCEB4eDnd3d1y9ehUzZsxAr169cPz4cejr6yM7Oxv29vZK9zEwMICNjQ2ys7NfuN6FCxdizpw5FdoTExNhamqqtvpJO23ZsqVK/f73v//h8ePH1VwNEdUk+RxrlpaWEAQBX331lWKZvb09LC0tkZ+fj2PHjmHPnj2aKpNqSFFRUZX6qRyWbt68qRjIHR8fjwEDBmDcuHHo0qULunXrpurqRA0ePFjxs5eXF1q3bo0mTZrg8OHDLxycWxXTp09HVFSU4nZ+fj5cXFwQFBTE03A64Pjx4wAAHx8fxMXFoWfPnrh16xYaNmyIgwcPon///jhx4gQaN25cpcP1RFR7zJgxAwBgY2ODc+fO4ciRI0hKSkJgYCD8/Pzg6emJ/Px8WFhYcP/XAfIzSy+jclgyNzfHgwcP0KhRIyQmJipCh7GxcbX/Fd64cWPY2triypUr6NmzJxwdHRWHTOXKysrw8OFD0cF5UqkUUqm0QruhoSEMDQ3VXjdpF/lVLufPn1ca13bhwgU4OzsrxjPZ2dnx/UBUx7Rp0wbnz5/HtWvXMHDgQHz00Ufo2LEjzMzMMHDgQFy/fl3Rj/t/3VfV11jlsBQYGIh33nkH7dq1w99//61I3ufOnYObm5uqq1PJrVu38ODBAzg5OQEAOnXqhNzcXKSnp6N9+/YAgEOHDqG8vBze3t7VWgvVXvIg/aK/KB49eqTUj4jqjsjISMVV1Xv37sXu3bsVy/T09JT6EcmpPHXA6tWr0alTJ9y7dw87duxQDLZOT0/HkCFDVFpXQUEBzpw5gzNnzgAAMjMzcebMGdy4cQMFBQWYOnUq0tLScO3aNRw8eBD9+vWDh4cHgoODAQAtWrRASEgIxo4di5MnT+LYsWOYNGkSBg8eXOUr4Uj3yN+z6upHRLVHjx49YGVlBQAoLy9XWia/bWVlhR49etR4baTFBA1KTk4WAFT4N3LkSKGoqEgICgoS7OzsBENDQ8HV1VUYO3askJ2drbSOBw8eCEOGDBHMzc0FS0tLITIyUnj06JFKdeTl5QkAhLy8PHU+PNJS7733nuK9ZmRkpPTek0qlip/fe+89TZdKRNVg6tSplf7ukf+bOnWqpkukGlLV3/+vNM9Samoq1q1bh3/++Qc///wzGjRogM2bN8Pd3R1du3b9j/Gt5nGeJd3SoUMHpKenAwB69+6Nxo0bK+ZZ+ueffxRXwLRv3x6nT5/WZKlEpGYymQweHh6wtbXFvXv3FGOUgKdfgWJra4sHDx7g8uXL0NfX12ClVBOqbZ6lHTt2YPjw4Rg6dCh+//13xXxFeXl5WLBgAS+1pFqjefPmSExMRFlZGYCnU0cYGBjgtddew99//63h6oioOqSmpuLatWvYtm0bOnbsiOTkZOzduxe9evVC9+7dcfLkSXTu3Bmpqalqv8Kbai+VxyzNnz8fa9euxbfffqs0irxLly74/fff1VocUXWQTzR38eJFBAQEoH///vDy8kL//v0REBCgCEqckI6o7snKygIAtGrVCvr6+vD394efnx/8/f2hr6+PVq1aKfUjAl7hyNKlS5fg5+dXod3Kygq5ubnqqImoWvXo0QOLFi0CAKXZu8+ePVuhHxHVLfKrqTMyMuDj41NheUZGhlI/IuAVjiw5OjriypUrFdqPHj2Kxo0bq6UooupU1XEIHK9AVPf4+vrCzc0NCxYsqPRquIULF8Ld3R2+vr4aqpC0kcphaezYsfh//+//4cSJE5BIJLhz5w62bNmCKVOmYPz48dVRI5Fa3blzR/GzsbGx0rJnbz/bj4jqBn19fcTExCAhIQFhYWFIS0vD48ePkZaWhrCwMCQkJGDJkiX8Y4mUqHwa7uOPP0Z5eTl69uyJoqIi+Pn5QSqVYsqUKXj//fero0YitTpx4gQAwNvbu8LVbqWlpXjjjTdw8uRJnDhxAsOHD9dEiUT0HxUVFeHixYuVLnNzc8PixYuxbNkypWElDRo0wOLFi+Hm5lbpGNzmzZvz+0N1lMphSSKR4JNPPsHUqVNx5coVFBQUwNPTE+bm5tVRH5HayWfLOHHiBEJDQxEUFITLly+jadOmSExMVMzo+wqzahCRlrh48aLimx2q6vbt25g6deoLl6enp+P111//r6VRLaRyWJIzMjKCp6enOmshqhFNmjRRaz8i0j7NmzdXzKcm5lJWLqJ+Poulb3mhmZP1S9dJuqnKYWn06NFV6vf999+/cjFENcHLywvA0y9U3r9/v9J3QxkYGEAqlaK4uFjRj4hqH1NT0yodBdK7/gDS1Mdo0aoN2rryK46oclUOSxs2bICrqyvatWvH0xNUq92/fx8AUFxcDAMDA7Rt2xbFxcWQSqXIyMhQTLQq70dERLqtymFp/Pjx2LZtGzIzMxEZGYlhw4bBxsamOmsjqhb29vYAAHNzc8WXOT9L3i7vR0REuq3KUwesXr0aWVlZmDZtGnbt2gUXFxcMHDgQ+/fv55EmqpUKCgpUaiciIt2k0jxLUqkUQ4YMQVJSEs6fP4+WLVtiwoQJcHNz4y8YqjWenT/JwMAA3bt3h5+fH7p37w4DA4NK+xERke565avh9PT0IJFIIAgCZDKZOmsiqlbHjh0D8PQ9XFZWhuTkZKXlenp6KC8vx7FjxzjPEhERqRaWiouLERcXh++//x5Hjx5Fnz59sGrVKoSEhEBPT+XJwIk0Qv4dcOXl5bC3t8fQoUNRWFgIMzMzbNmyBXfv3lXqR0REuq3KCWfChAlwcnLCF198gT59+uDmzZv4+eef0bt3bwYlqrU6dOiA0tJSXLt2DaWlpejQoYOmSyIiIi1T5SNLa9euRaNGjdC4cWOkpKQgJSWl0n5xcXFqK46oOsiv4tTT08OePXsU7YmJiYr28vJyXu1JREQAVAhLI0aMgEQiqc5aiGqEi4sLACi+cfz111+HiYkJHj9+jN9//13RLu9HRES6TaVJKYnqgsaNGyvdruwLMyvrR0REuomDjYiIiIhEMCyRzsnMzFT8/PzFCc/efrYfERHpLoYl0jnPjr2Tj0+q7DbH6BEREcCwRDqoY8eOau1HRER1m8ozeMsn7yOqreSTTsq9/vrrMDU1RVFRkdJg7+f7ERGRblI5LDk4OGDgwIEYPXo0unbtWh01EVWr569+e9HVcC9qJyIi3aLyabgffvgBDx8+RI8ePfDaa6/hiy++4BeOUq2SkZGh+NnIyAgeHh5wcnKCh4cHjIyMKu1HRES6S+WwFBYWhvj4eNy+fRvvvfcetm7dCldXV/Tp0wdxcXEoKyurjjqJ1MbCwkLxc0lJCa5cuYKsrCxcuXIFJSUllfYjIiLd9coDvO3s7BAVFYW//voLS5cuxYEDBxAREQFnZ2fMnDkTRUVF6qyTSG3s7OzU2o+IiOo2lccsyeXk5GDjxo3YsGEDrl+/joiICIwZMwa3bt3CokWLkJaWpviuLSJtYm9vr9Z+RERUt6kcluLi4rB+/Xrs378fnp6emDBhAoYNGwZra2tFn86dO6NFixbqrJNIbbKzs9Xaj4iI6jaVw1JkZCQGDx6MY8eOvXAeGmdnZ3zyySf/uTii6vDPP/+otR8REdVtKoelrKwsmJqaivYxMTHBrFmzXrkoouqUn5+v+FkikUAQhEpvP9uPiIh0V5XC0vO/NMR+iVhaWv63ioiqmZ2dHW7dugUASkHp+dsc4E1EREAVw5K1tfVLvydLEARIJBLIZDK1FEZUXQICAvDHH38AeDrPUufOnVFeXg49PT389ttviukDAgICNFkmERFpiSqFpeTk5Oqug6jGPHvEqKSkBIcPH35pPyIi0l1VCkv+/v7VXQdRjcnNzVVrPyIiqtteaZ6l3NxcnDx5Enfv3kV5ebnSshEjRqilMKLqoqf3f3OxGhsb48mTJ5XefrYfERHpLpXD0q5duzB06FAUFBTA0tJSaSyTRCJhWCKt161bN8yfPx/NmzfH48ePcf36dcUyR0dHGBsb4+LFi+jWrZvmiiQiIq2hcliKjo7G6NGjsWDBgpdOIUCkjbp16wZ7e3tcvHgRoaGhiIqKwuXLl9G0aVMkJiZi9+7dsLe3Z1giIiIArxCWbt++jQ8++IBBibReUVERLl68WOmyqVOnYtq0aThw4AB2796taDc2NoZEIsHUqVPx559/Vrhf8+bN+d4nItIxKoel4OBgnD59Go0bN66OeojU5uLFi2jfvr1on+LiYqXb8vFKU6dOrbR/eno6Xn/9dfUUSEREtUKVwtKvv/6q+Dk0NBRTp07F+fPn4eXlBUNDQ6W+b775pnorJHpFzZs3R3p6umgfmUyGXw+kYuXeM3i/V1u8GeALfX190XUSEZFuqVJYCgsLq9A2d+7cCm2clJK0iampaZWOAhnaN8bmvGYY8LYP2rrWr4HKiIioNqlSWHp+egAiIiIiXaHyRDKbNm2qMM4DeDoT8qZNm9RSFBEREZG2UDksRUZGIi8vr0L7o0ePEBkZqZaiiIiIiLSFymFJ/oW5z7t16xasrKzUUhQRERGRtqjy1AHt2rWDRCKBRCJBz549YWDwf3eVyWTIzMxESEhItRRJREREpClVDkvyK+LOnDmD4OBgmJubK5YZGRnBzc0NAwYMUHuBRERERJpU5bA0a9YsAICbmxsGDRoEY2PjaiuKiIiISFuoPGZp5MiRMDY2RklJCW7duoUbN24o/VPFkSNH0LdvXzg7O0MikSA+Pl5puSAImDlzJpycnGBiYoKAgABcvnxZqc/Dhw8xdOhQWFpawtraGmPGjEFBQYGqD4uIiIioUiqHpcuXL8PX1xcmJiZwdXWFu7s73N3d4ebmBnd3d5XWVVhYiDZt2mD16tWVLl+8eDG++uorrF27FidOnICZmRmCg4MVX0kBAEOHDsW5c+eQlJSEhIQEHDlyBOPGjVP1YRERERFVSuXvhhs1ahQMDAyQkJAAJyenSq+Mq6pevXqhV69elS4TBAHLly/Hp59+in79+gF4OseTg4MD4uPjMXjwYFy4cAH79u3DqVOn0KFDBwDAypUr0bt3byxZsgTOzs6vXBsRERER8Aph6cyZM0hPT6/278jKzMxEdnY2AgICFG1WVlbw9vbG8ePHMXjwYBw/fhzW1taKoAQAAQEB0NPTw4kTJ9C/f/9K111cXKw0sWZ+fj4AoLS0FKWlpdX0iEhblZWVKf7n60+kW7j/67aqvuYqhyVPT0/cv39f5YJUlZ2dDQBwcHBQandwcFAsy87Ohr29vdJyAwMD2NjYKPpUZuHChZgzZ06F9sTERJiamv7X0qmWuVkAAAZIS0vD7QxNV0NENYn7v24rKiqqUj+Vw9KiRYswbdo0LFiwAF5eXjA0NFRabmlpqeoqa9z06dMRFRWluJ2fnw8XFxcEBQXVivpJvf688RA4exo+Pj5o08hG0+UQUQ3i/q/b5GeWXkblsCQ/LdazZ0+ldvnM3jKZTNVVVsrR0REAkJOTAycnJ0V7Tk4O2rZtq+hz9+5dpfuVlZXh4cOHivtXRiqVQiqVVmg3NDSsEP6o7pNPsGpgYMDXn0jHcP/XbVV9zVUOS8nJySoX8yrc3d3h6OiIgwcPKsJRfn4+Tpw4gfHjxwMAOnXqhNzcXKSnp6N9+/YAgEOHDqG8vBze3t41UicRERHVbSqHJX9/f7VtvKCgAFeuXFHczszMxJkzZ2BjY4NGjRph8uTJmD9/Ppo2bQp3d3d89tlncHZ2Vswm3qJFC4SEhGDs2LFYu3YtSktLMWnSJAwePJhXwhEREZFaqByWACA3NxffffcdLly4AABo2bIlRo8erfIX6Z4+fRrdu3dX3JaPIxo5ciQ2bNiAadOmobCwEOPGjUNubi66du2Kffv2Kc0evmXLFkyaNAk9e/aEnp4eBgwYgK+++upVHhYRERFRBRJBEARV7nD69GkEBwfDxMQEb7zxBgDg1KlTePz4MRITE/H6669XS6HVKT8/H1ZWVsjLy+MAbx105voDhK1JQ/x4H7R1ra/pcoioBnH/121V/f2v8pGlDz/8EG+++Sa+/fZbxcC4srIyvPPOO5g8eTKOHDny6lUTERERaRmVw9Lp06eVghLw9CqCadOmKU0OSURERFQXqPzdcJaWlpV+Ye7NmzdhYWGhlqKIiIiItIXKYWnQoEEYM2YMfvrpJ9y8eRM3b97Ejz/+iHfeeQdDhgypjhqJiIiINEbl03BLliyBRCLBiBEjFN+pY2hoiPHjx+OLL75Qe4FEREREmqRyWDIyMsKKFSuwcOFCXL16FQDQpEkTfqcaERER1UmvNM8SAJiamsLLy0udtRARERFpnSqHpdGjR1ep3/fff//KxRARERFpmyqHpQ0bNsDV1RXt2rWDivNYEhEREdVaVQ5L48ePx7Zt25CZmYnIyEgMGzYMNjY21VkbERERkcZVeeqA1atXIysrC9OmTcOuXbvg4uKCgQMHYv/+/TzSRERERHWWSvMsSaVSDBkyBElJSTh//jxatmyJCRMmwM3NDQUFBdVVIxEREZHGqDwppeKOenqQSCQQBAEymUydNRERERFpDZXCUnFxMbZt24bAwEC89tprOHv2LFatWoUbN27A3Ny8umokIiIi0pgqD/CeMGECfvzxR7i4uGD06NHYtm0bbG1tq7M2IiIiIo2rclhau3YtGjVqhMaNGyMlJQUpKSmV9ouLi1NbcURERESaVuWwNGLECEgkkuqshYiIiEjrqDQpJREREZGueeWr4YiIiIh0AcMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJMNB0AURERKq4nfsY/xaWqGVdV+8VKv43MPjvvxLrmRmhgbXJf14PaReGJSIiqjVu5z5GjyWHUVxWrtb1RseeVct6pAZ6ODSlGwNTHcPTcEREVGv8W1ii9qCkTsVl5Wo76kXag2GJiIiISATDEhEREZEIhiUiIiIiEQxLRERERCIYloiIiIhEMCwRERERiWBYIiIiIhLBsEREREQkQqvD0uzZsyGRSJT+NW/eXLH8yZMnmDhxIurXrw9zc3MMGDAAOTk5GqyYiIiI6hqtDksA0LJlS2RlZSn+HT16VLHsww8/xK5du/Dzzz8jJSUFd+7cQXh4uAarJSIiorpG678bzsDAAI6OjhXa8/Ly8N1332Hr1q3o0aMHAGD9+vVo0aIF0tLS4OPjU9OlEhERUR2k9WHp8uXLcHZ2hrGxMTp16oSFCxeiUaNGSE9PR2lpKQICAhR9mzdvjkaNGuH48eOiYam4uBjFxcWK2/n5+QCA0tJSlJaWVt+DIa1UVlam+J+vP5F2k++v2oyfJbVHVV8nrQ5L3t7e2LBhA5o1a4asrCzMmTMHvr6+yMjIQHZ2NoyMjGBtba10HwcHB2RnZ4uud+HChZgzZ06F9sTERJiamqrzIVAtcLMAAAyQlpaG2xmaroaIxMj3V2129OhRXDfXdBVUFUVFRVXqp9XvuF69eil+bt26Nby9veHq6ort27fDxMTkldc7ffp0REVFKW7n5+fDxcUFQUFBsLS0/E81U+3z542HwNnT8PHxQZtGNpouh4hEnLuTjyVn0zRdhqiuXbuipTN/l9QG8jNLL6PVYel51tbWeO2113DlyhUEBgaipKQEubm5SkeXcnJyKh3j9CypVAqpVFqh3dDQEIaGhuoum7ScgYGB4n++/kTaTb6/ajN+ltQeVX2dtP9d94yCggJcvXoVw4cPR/v27WFoaIiDBw9iwIABAIBLly7hxo0b6NSpk4Yrpep2O/cx/i0sUcu6rt4rVPyvjg/iemZGaGD96kc+iYhIu2h1WJoyZQr69u0LV1dX3LlzB7NmzYK+vj6GDBkCKysrjBkzBlFRUbCxsYGlpSXef/99dOrUiVfC1XG3cx+jx5LDKC4rV+t6o2PPqmU9UgM9HJrSjYGJiKiO0OqwdOvWLQwZMgQPHjyAnZ0dunbtirS0NNjZ2QEAli1bBj09PQwYMADFxcUIDg7G119/reGqqbr9W1ii9qCkTsVl5fi3sIRhiYiojtDqsPTjjz+KLjc2Nsbq1auxevXqGqqIiIiIdI3Wz+BNREREpEkMS0REREQiGJaIiIiIRDAsEREREYlgWCIiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCIYlIiIiIhEMS0REREQiGJaIiIiIRDAsEREREYlgWCIiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCANNF0BERFRVxbIn0DO+rekyRBXLngCw0nQZpEYMS0REVGvcKbwOM/eVmi5D1J3CtmgPB02XQWrEsERERLWGs5krCjPf13QZopy7u2q6BFIzhiUiIqo1pPrGKH/SQNNliJLqG2u6BFIzDvAmIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQgO8KZah/OsEBFRTWJYolqH86wQEVFNYliiWofzrBARUU1iWKJah/OsEBFRTeIAbyIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSERERkQiGJSIiIiIRDEtEREREIhiWiIio1qhnZgSpgfb+6pIa6KGemZGmyyA1M9B0AURERFXVwNoEh6Z0w7+FJWpZ36WsPETHnkVMhBeaOVn95/XVMzNCA2sTNVRG2oRhiYiIapUG1iZqCyRlZWUAgCZ2ZmjV4L+HJaqbtPdYJhEREZEWqDNhafXq1XBzc4OxsTG8vb1x8uRJTZdEREREdUCdCEs//fQToqKiMGvWLPz+++9o06YNgoODcffuXU2XRtWAAzyJiKgm1YkxS0uXLsXYsWMRGRkJAFi7di12796N77//Hh9//LGGqyN14wBPIiKqSbU+LJWUlCA9PR3Tp09XtOnp6SEgIADHjx+v9D7FxcUoLi5W3M7PzwcAlJaWorS0tHoLJrWwNzOAvZn427eoqAiXLl166boeZ+WhOPsKHt82QlG5eFhq1qwZTE1NX7pOvo+INKuq+//f///+n3HGCCU56tn/qfao6md1rQ9L9+/fh0wmg4ODg1K7g4MDLl68WOl9Fi5ciDlz5lRoT0xM5I5Qh1y9ehXR0dFV7j9848v7xMTEoEmTJv+hKiKqCdz/qSqKioqq1K/Wh6VXMX36dERFRSlu5+fnw8XFBUFBQbC0tNRgZaRORUVF6Nq160v7FTwuxv7UUwj27QhzE6loX/5lSVQ7cP+nqpCfWXqZWh+WbG1toa+vj5ycHKX2nJwcODo6VnofqVQKqbTiTmFoaAhDQ8NqqZNqnpWVFd54442X9istLcWj3Ifw7ezD15+ojuD+T1VR1ddcey8pqiIjIyO0b98eBw8eVLSVl5fj4MGD6NSpkwYrIyIiorqg1h9ZAoCoqCiMHDkSHTp0wBtvvIHly5ejsLBQcXUcERER0auqE2Fp0KBBuHfvHmbOnIns7Gy0bdsW+/btqzDom4iIiEhVdSIsAcCkSZMwadIkTZdBREREdUytH7NEREREVJ0YloiIiIhEMCwRERERiWBYIiIiIhLBsEREREQkgmGJiIiISATDEhEREZEIhiUiIiIiEQxLRERERCLqzAze/4UgCACA/Px8DVdCmlBaWoqioiLk5+fzW8eJdAz3f90m/70vzwEvwrAE4NGjRwAAFxcXDVdCRERENe3Ro0ewsrJ64XKJ8LI4pQPKy8tx584dWFhYQCKRaLocqmH5+flwcXHBzZs3YWlpqelyiKgGcf/XbYIg4NGjR3B2doae3otHJvHIEgA9PT00bNhQ02WQhllaWvLDkkhHcf/XXWJHlOQ4wJuIiIhIBMMSERERkQiGJdJ5UqkUs2bNglQq1XQpRFTDuP9TVXCANxEREZEIHlkiIiIiEsGwRERERCSCYYmIiIhIBMMSURVdvHgRPj4+MDY2Rtu2bTVdDpHOkkgkiI+PF+0zatQohIWF1Ug9VPdxUkqiKpo1axbMzMxw6dIlmJuba7ocIgJw7do1uLu7448//lD6I2bFihUv/b4vdRg1ahRyc3NfGt6odmNYInqJkpISGBkZ4erVqwgNDYWrq6umSyKil6jKrMxEVcXTcFQnxcbGwsvLCyYmJqhfvz4CAgJQWFiIbt26YfLkyUp9w8LCMGrUKMVtNzc3zJs3DyNGjIClpSXGjRsHiUSC9PR0zJ07FxKJBLNnz67Rx0OkS9zc3LB8+XKltrZt21a637m7uwMA2rVrB4lEgm7dugGoeBquW7dueP/99zF58mTUq1cPDg4O+Pbbb1FYWIjIyEhYWFjAw8MDe/fuVdxHJpNhzJgxcHd3h4mJCZo1a4YVK1Yols+ePRsbN27Ezp07IZFIIJFIcPjwYQDAzZs3MXDgQFhbW8PGxgb9+vXDtWvX1PH0kAYwLFGdk5WVhSFDhmD06NG4cOECDh8+jPDwcJUOyS9ZsgRt2rTBH3/8gc8++wxZWVlo2bIloqOjkZWVhSlTplTjIyCiqjp58iQA4MCBA8jKykJcXNwL+27cuBG2trY4efIk3n//fYwfPx5vvfUWOnfujN9//x1BQUEYPnw4ioqKADz9kvWGDRvi559/xvnz5zFz5kzMmDED27dvBwBMmTIFAwcOREhICLKyspCVlYXOnTujtLQUwcHBsLCwQGpqKo4dOwZzc3OEhISgpKSk+p8UUjuehqM6JysrC2VlZQgPD1ecMvPy8lJpHT169EB0dLRSm4GBAczNzeHo6Ki2Wonov7GzswMA1K9f/6X7Zps2bfDpp58CAKZPn44vvvgCtra2GDt2LABg5syZWLNmDf766y/4+PjA0NAQc+bMUdzf3d0dx48fx/bt2zFw4ECYm5vDxMQExcXFStv+4YcfUF5ejv/973+QSCQAgPXr18Pa2hqHDx9GUFCQWp8Dqn4MS1TntGnTBj179oSXlxeCg4MRFBSEiIgI1KtXr8rr6NChQzVWSESa0Lp1a8XP+vr6qF+/vtIfUg4ODgCAu3fvKtpWr16N77//Hjdu3MDjx49RUlLy0qth//zzT1y5cgUWFhZK7U+ePMHVq1fV8EiopjEsUZ2jr6+PpKQk/Pbbb0hMTMTKlSvxySef4MSJE9DT06twOq60tLTCOszMzGqqXCJ6TlX3U1UZGhoq3ZZIJEpt8qNA5eXlAIAff/wRU6ZMQUxMDDp16gQLCwt8+eWXOHHihOh2CgoK0L59e2zZsqXCMvmRMKpdGJaoTpJIJOjSpQu6dOmCmTNnwtXVFb/88gvs7OyQlZWl6CeTyZCRkYHu3btrsFoietbz+2l+fj4yMzMr7WtkZATg6b6sbseOHUPnzp0xYcIERdvzR4aMjIwqbPv111/HTz/9BHt7e1haWqq9Lqp5HOBNdc6JEyewYMECnD59Gjdu3EBcXBzu3buHFi1aoEePHti9ezd2796NixcvYvz48cjNzdV0yUT0jB49emDz5s1ITU3F2bNnMXLkSOjr61fa197eHiYmJti3bx9ycnKQl5entjqaNm2K06dPY//+/fj777/x2Wef4dSpU0p93Nzc8Ndff+HSpUu4f/8+SktLMXToUNja2qJfv35ITU1FZmYmDh8+jA8++AC3bt1SW31UcxiWqM6xtLTEkSNH0Lt3b7z22mv49NNPERMTg169emH06NEYOXIkRowYAX9/fzRu3JhHlYi0zPTp0+Hv748+ffogNDQUYWFhaNKkSaV9DQwM8NVXX2HdunVwdnZGv3791FbHu+++i/DwcAwaNAje3t548OCB0lEmABg7diyaNWuGDh06wM7ODseOHYOpqSmOHDmCRo0aITw8HC1atMCYMWPw5MkTHmmqpSRCTUxxSkRERFRL8cgSERERkQiGJSIiIiIRDEtEREREIhiWiIiIiEQwLBERERGJYFgiIiIiEsGwRERERCSCYYmIiIhIBMMSEemEDRs2wNraWtNlEFEtxLBERHXGqFGjIJFIIJFIYGRkBA8PD8ydOxdlZWWaLo2IajEDTRdARKROISEhWL9+PYqLi7Fnzx5MnDgRhoaGcHJy0nRpRFRL8cgSEdUpUqkUjo6OcHV1xfjx4xEQEIBff/21Qr+rV6+iX79+cHBwgLm5OTp27IgDBw4o9XFzc8OCBQswevRoWFhYoFGjRvjmm29q6qEQkZZgWCKiOs3ExAQlJSUV2gsKCtC7d28cPHgQf/zxB0JCQtC3b1/cuHFDqV9MTAw6dOiAP/74AxMmTMD48eNx6dKlmiqfiLQAwxIR1UmCIODAgQPYv38/evToUWF5mzZt8O6776JVq1Zo2rQp5s2bhyZNmlQ4CtW7d29MmDABHh4e+Oijj2Bra4vk5OSaehhEpAUYloioTklISIC5uTmMjY3Rq1cvDBo0CLNnz67Qr6CgAFOmTEGLFi1gbW0Nc3NzXLhwocKRpdatWyt+lkgkcHR0xN27d6v7YRCRFuEAbyKqU7p37441a9bAyMgIzs7OMDCo/GNuypQpSEpKwpIlS+Dh4QETExNERERUOGVnaGiodFsikaC8vLza6ici7cOwRER1ipmZGTw8PF7a79ixYxg1ahT69+8P4OmRpmvXrlVzdURUG/E0HBHppKZNmyIuLg5nzpzBn3/+ibfffptHjIioUgxLRKSTli5dinr16qFz587o27cvgoOD8frrr2u6LCLSQhJBEARNF0FERESkrXhkiYiIiEgEwxIRERGRCIYlIiIiIhEMS0REREQiGJaIiIiIRDAsEREREYlgWCIiIiISwbBEREREJIJhiYiIiEgEwxIRERGRCIYlIiIiIhH/H7VaPgR9HknnAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "\n",
    "monthly_messages_with_plan = user_revenue.groupby(['user_id', 'month', 'plan'])['messages_count'].sum().reset_index()\n",
    "\n",
    "monthly_messages_with_plan.boxplot(column='messages_count', by='plan', grid=True, patch_artist=True)\n",
    "plt.title('Distribution of Monthly Messages by Plan')\n",
    "plt.suptitle('') \n",
    "plt.xlabel('Plan')\n",
    "plt.ylabel('Monthly Messages')\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Message usage statistics by plan:\n",
      "               mean        std  median  min    max\n",
      "plan                                              \n",
      "surf      31.159568  33.566717    24.0  0.0  266.0\n",
      "ultimate  37.551389  34.767179    30.0  0.0  166.0\n"
     ]
    }
   ],
   "source": [
    "message_stats = user_revenue.groupby('plan')['messages_count'].agg(['mean', 'std', 'median', 'min', 'max'])\n",
    "print(\"Message usage statistics by plan:\")\n",
    "print(message_stats)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate conclusions on how the users behave in terms of messaging. Is their behaviour different between the plans?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I've noticed that users on Ultimate Plan use slightly more messages per month than users on Surf Plan."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Internet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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o1GjRta27du3G5KMAQMG2Izt1q2bIckYM2aMta1Hjx5GSEiI8ffff9uMbd++veHr65vleDdy8uTJLPteu3atIckoWbJklv1cvnzZyMjIsGlLSEgw3N3djbFjx9q0SzL69euXZawk480337Rpnz17tiHJSEhIMAzDMM6ePWt4e3sbtWrVMi5dumQzNjMz86bndG1fq1atMk6ePGkcPXrUmDdvnhEQEGB4enoaf/75p5GYmGg4Ozsbr732ms22e/bsMVxcXGza69evb0gyZs2addPjXtO1a1ejYMGCN+wvWLCg0bVrV+t6lSpVjBYtWtx0n40bNzbCw8ONy5cvW9syMzONOnXqGGXKlMly7nXr1jWuXr2arXoB4G7AI4sAkIfExsYqKChIDRs2lPTPo4RPP/205s2bp4yMDEn/PL5WuHBhzZ8/37rdmTNnFBcXp6efftra9tVXX6l8+fIqV66c/v77b+ty7fG3tWvX2hy7fv36qlChQpaaPD09bY5z7tw5PfLII9qxY4e1/drjjc8//7zNti+88ILNumEY+uabb9SyZUsZhmFTV1RUlM6dO2ez39vVtWtXm7olyd3d3foeWUZGhk6dOiUvLy+VLVvWIce8Ji4uTufPn9eIESOyvINnsViytY/IyEgVKVJEoaGhat++vby8vPTtt9+qWLFiWrhwoTIzM9WuXTub6xccHKwyZcpk+b26u7tf9xFXR/Dz89O+fft08ODB6/afPn1aa9asUbt27XT+/HlrradOnVJUVJQOHjyov/76y2abXr16OfydPADISTyyCAB5REZGhubNm6eGDRvavCtUq1YtTZ48WatXr1aTJk3k4uKiNm3aaO7cuUpLS5O7u7sWLlyo9PR0m0B28OBB/frrrypSpMh1j3fixAmb9bCwsOuOW7JkicaPH6/4+Hibd8/+HS7++OMPOTk5ZdnHf2eHPHnypM6ePasPPvhAH3zwQbbquh3XO5fMzExNnz5d7777rhISEqwBV/r/jwI6wrXHCytVqnTb+5g5c6YeeOABubi4KCgoSGXLlrWGyYMHD8owDJUpU+a627q6utqsFytWzObR1jv179/72LFj9fjjj+uBBx5QpUqV1LRpU3Xu3Nk6+cqhQ4dkGIZeffVVvfrqq9fd34kTJ1SsWDHr+o3+OQSAuxWBDADyiDVr1igpKUnz5s3TvHnzsvTHxsaqSZMmkqT27dvr/fff17Jly9S6dWstWLBA5cqVU5UqVazjMzMzFR4erilTplz3eKGhoTbr/72jJEk//PCDWrVqpXr16undd99VSEiIXF1dNXv27NuaoCIzM1OS9Mwzz6hr167XHfPvmRRv1/XO5fXXX9err76q7t27a9y4cfL395eTk5MGDBhgretu8dBDD93wG2eZmZmyWCxatmzZde8k/ffdtutdixvx8PBQWlqaDMPIcjfPMAxdvnzZ5q5fvXr1dPjwYf3vf//TypUr9dFHH2nq1KmaNWuWevbsab2uQ4YMUVRU1HWP+d/Qbk+9AHA3IJABQB4RGxurwMBAzZw5M0vfwoUL9e2332rWrFny9PRUvXr1FBISovnz56tu3bpas2aNXnnlFZttSpUqpV27dqlx48bZflTuv7755ht5eHhoxYoVNt/Zmj17ts244sWLKzMzUwkJCTZ3bg4dOmQzrkiRIvL29lZGRoYiIyNvq6bb9fXXX6thw4b6+OOPbdrPnj2rwoULO+w4pUqVkiTt3bs3R74fV6pUKRmGobCwMD3wwAMO3Xfx4sV19epVHT58OEvthw4dUkZGhnW2yWuuzfr57LPPKjU1VfXq1VN0dLR69uypkiVLSvrnrl1u/74BILfwDhkA5AGXLl3SwoUL9dhjj+mpp57KsvTv31/nz5+3ThXu5OSkp556St99950+//xzXb161eZxRUlq166d/vrrL3344YfXPV52ZrBzdnaWxWKxebwvMTExywyN1+5+vPvuuzbt77zzTpb9tWnTRt9884327t2b5XjXvvWVE5ydnWUYhk3bV199leUdpjvVpEkTeXt7a8KECbp8+bJN33+PfzuefPJJOTs7KyYmJsv+DMPQqVOnbnvfzZo1kyTNmDEjS9+1vyi4NkZSlmN5eXmpdOnS1kdbAwMD1aBBA73//vtKSkrKss+c/H0DQG7hDhkA5AGLFy/W+fPn1apVq+v2165dW0WKFFFsbKw1eD399NN65513NGbMGIWHh6t8+fI223Tu3FkLFixQnz59tHbtWj388MPKyMjQ/v37tWDBAq1YseKGj8Vd06JFC02ZMkVNmzZVx44ddeLECc2cOVOlS5fW7t27reNq1KihNm3aaNq0aTp16pR12vvffvtNku17RxMnTtTatWtVq1Yt9erVSxUqVNDp06e1Y8cOrVq1SqdPn76ta3grjz32mMaOHatnn31WderU0Z49exQbG2u9i+MoPj4+mjp1qnr27KkHH3xQHTt2VKFChbRr1y5dvHhRn3766R3tv1SpUho/frxGjhypxMREtW7dWt7e3kpISNC3336r3r1723yLzh5Vq1ZVz549NX36dB08eNA6dX1cXJyWLl2qnj172jwWW6FCBTVo0EA1atSQv7+/tm3bpq+//lr9+/e3jpk5c6bq1q2r8PBw9erVSyVLltTx48e1ZcsW/fnnnzbfgQOAexGBDADygNjYWHl4eFj/APxfTk5OatGihWJjY3Xq1CkFBASoTp06Cg0N1dGjR7PcHbu2zaJFizR16lR99tln+vbbb1WgQAGVLFlSL730UrYed2vUqJE+/vhjTZw4UQMGDFBYWJjeeOMNJSYm2gQySfrss88UHBysL7/8Ut9++60iIyM1f/58lS1b1ua9o6CgIP30008aO3asFi5cqHfffVcBAQGqWLGi3njjDTuvXPa9/PLLunDhgubOnav58+erevXq+v777zVixAiHH6tHjx4KDAzUxIkTNW7cOLm6uqpcuXIaOHCgQ/Y/YsQIPfDAA5o6dapiYmIk/fNOYJMmTW4Y6rPr/fffV3h4uD755BONHDlSklS2bFm9/fbb6tevn83YF198UYsXL9bKlSuVlpam4sWLa/z48Ro6dKh1TIUKFbRt2zbFxMRozpw5OnXqlAIDA1WtWjWNHj36jmoFgLuBxXDE8w8AAOSA+Ph4VatWTV988YU6depkdjkAADgc75ABAO4Kly5dytI2bdo0OTk5qV69eiZUBABAzuORRQDAXWHSpEnavn27GjZsKBcXFy1btkzLli1T7969s0yxDwBAXsEjiwCAu0JcXJxiYmL0yy+/KDU1Vffff786d+6sV155RS4u/P0hACBvIpABAAAAgEl4hwwAAAAATEIgAwAAAACT8FC+g2RmZurYsWPy9va2+YApAAAAgPzFMAydP39eRYsWlZPTze+BEcgc5NixY8wCBgAAAMDq6NGjuu+++246hkDmIN7e3pL+ueg+Pj4mVwMAAADALCkpKQoNDbVmhJshkDnItccUfXx8CGQAAAAAsvUqE5N6AAAAAIBJCGQAAAAAYBICGQAAAACYhHfIcllGRobS09PNLgM34OrqKmdnZ7PLAAAAQD5BIMslhmEoOTlZZ8+e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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Compare the amount of internet traffic consumed by users per plan\n",
    "avg_int_traffic = user_revenue.groupby(['plan', 'month'])['internet_sum'].mean().reset_index()\n",
    "avg_int_traffic_pivot = avg_int_traffic.pivot(index='month', columns='plan', values='internet_sum')\n",
    "avg_int_traffic_pivot.plot(kind='bar', figsize=(10, 6))\n",
    "plt.title('Average Traffic Per User')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Average Internet Traffic')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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fPgw6tevX2ZfKysrpKWlKbSlpaWJP6ii/5bV53WhoaHIyMgQX3fv3lV2V4iIiKqEq6srunXrBmdnZ/Tv3x8//fQTnj59WqExPDw8Kqm66k+tAUgQBAQHB2Pbtm04dOgQHBwc3rhOu3btEBcXp9B24MABtGvXDgDg4OAAKysrhT6ZmZk4ffq02Od1urq6MDY2VngRERFVZ5qamjhw4AD27t2L5s2b47vvvoOTkxOSkpKgoaFR7FJYSU9OLu2OaylQawAaO3Ys1q1bh/Xr18PIyAipqalITU3FP//8I/bx9/dHaGio+H78+PGIjY3FggULcO3aNUyfPh1nz55FcHAwgJdPiJwwYQJmzZqFnTt34vLly/D394eNjQ369OlT1btIRERUaWQyGTp06ICIiAhcuHABOjo62LZtG8zNzZGSkiL2KywsxJUrV9RYafWj1jlAy5YtAwB06dJFoX3VqlXiTPXk5GRoaPwvp7Vv3x7r16/HV199hWnTpsHR0RHbt29XmDg9depUZGdn45NPPsGzZ8/QsWNHxMbG8hlARET0zjh9+jTi4uLg7e0NCwsLnD59Gg8fPkSzZs1gaGiIkJAQ7N69G40aNcLChQvx7NkzdZdcrag1AJVnpnp8fHyxtv79+6N///6lriOTyTBjxgzMmDHjbcojIiKqtoyNjXH06FFERUUhMzMTdnZ2WLBgAXx9fVFQUICLFy/C398fWlpamDhxIrp27arukquVavUgxOqish+EyLvAiIiqj7IerEfVzzv5IEQiIiKiqsAARERERJLDAERERESSwwBEREREksMARERERJLDAERERESSwwBEREREksMARERERJLDAERERESSwwBERET0jpLJZNi+fXuZfQIDAyX5ZeFq/S4wIiKiau238VW3rV6LK3X427dvw8HBARcuXICbm5vYvnjx4nJ9N+fbCgwMxLNnz94YyKoKAxAREZGEmZiYqLsEteAlMCIiohrK3t4eUVFRCm1ubm6YPn16sb4ODg4AgFatWkEmk6FLly4Ail8C69KlCz7//HNMmDABtWvXhqWlJX766SdkZ2cjKCgIRkZGaNy4Mfbu3SuuU1hYiBEjRsDBwQH6+vpwcnLC4sX/O6M1ffp0rF69Gjt27IBMJoNMJkN8fDwA4O7duxgwYABMTU1Rp04d9O7dG7dv31bF4SkTAxAREZEEnDlzBgBw8OBBpKSkYOvWraX2Xb16NczMzHDmzBl8/vnnGDNmDPr374/27dvj/Pnz8Pb2xrBhw5CTkwMAkMvlqF+/PjZv3oyrV68iLCwM06ZNw6ZNmwAAkydPxoABA9CjRw+kpKQgJSUF7du3R0FBAXx8fGBkZIRjx47hxIkTqFWrFnr06IH8/PxKPR4MQERERBJgbm4OAKhbty6srKxQp06dUvu6urriq6++gqOjI0JDQ6GnpwczMzOMGjUKjo6OCAsLw+PHj3Hp0iUAgLa2NiIiIuDh4QEHBwcMGTIEQUFBYgCqVasW9PX1oaurCysrK1hZWUFHRwcbN26EXC7H8uXL4ezsjGbNmmHVqlVITk4WzxBVFs4BIiIiIgUuLi7i/2tqaqJu3bpwdnYW2ywtLQEA6enpYtvSpUuxcuVKJCcn459//kF+fr7CZOuSXLx4EYmJiTAyMlJoz83Nxa1bt1SwJ6VjACIiIqqhNDQ0it3BVVBQ8NbjamtrK7yXyWQKbTKZDMDLS18AsGHDBkyePBkLFixAu3btYGRkhHnz5uH06dNlbicrKwvu7u74+eefiy0rOmNVWRiAiIiIaihzc3OkpKSI7zMzM5GUlFRiXx0dHQAvJyyr2okTJ9C+fXt89tlnYtvrZ3B0dHSKbbt169bYuHEjLCwsYGxsrPK6ysI5QERERDXU+++/j7Vr1+LYsWO4fPkyAgICoKmpWWJfCwsL6OvrIzY2FmlpacjIyFBZHY6Ojjh79iz27duHGzdu4Ouvv8Yff/yh0Mfe3h6XLl3C9evX8ejRIxQUFGDIkCEwMzND7969cezYMSQlJSE+Ph7jxo3DvXv3VFZfSRiAiIiIaqjQ0FB07twZH3zwAfz8/NCnTx80atSoxL5aWlpYsmQJfvjhB9jY2KB3794qq2P06NHo168fBg4cCE9PTzx+/FjhbBAAjBo1Ck5OTvDw8IC5uTlOnDgBAwMDHD16FA0aNEC/fv3QrFkzjBgxArm5uZV+RkgmVMXjH2uYzMxMmJiYICMjo1J+AKFbLyu9bmQ/5zd3IiKicsvNzUVSUhIcHBygp6en7nLoDcr6eVXk9zfPABEREZHkMAARERGR5DAAERERkeQwABEREZHkMAAREREBxR4oSNWTqn5ODEBERCRpRU84LvpiT6rein5Orz+tuqL4JGgiIpI0TU1NmJqait9rZWBgIH7VA1UfgiAgJycH6enpMDU1LfWBj+XFAERERJJnZWUFQPHLPal6MjU1FX9eb4MBiIiIJE8mk8Ha2hoWFhYq+TJRqhza2tpvfeanCAMQERHR/9PU1FTZL1iq3jgJmoiIiCRHrQHo6NGj6NWrF2xsbCCTybB9+/Yy+wcGBkImkxV7tWjRQuwzffr0YsubNm1ayXtCRERENYlaA1B2djZcXV2xdOnScvVfvHgxUlJSxNfdu3dRp04d9O/fX6FfixYtFPodP368MsonIiKiGkqtc4B8fX3h6+tb7v4mJiYwMTER32/fvh1Pnz5FUFCQQj8tLS2VzBAnIiKid1ONngO0YsUKeHl5wc7OTqH95s2bsLGxQcOGDTFkyBAkJyerqUIiIiKqjmrsXWAPHjzA3r17sX79eoV2T09PxMTEwMnJCSkpKYiIiECnTp1w5coVGBkZlThWXl4e8vLyxPeZmZmVWjsRERGpV40NQKtXr4apqSn69Omj0P7qJTUXFxd4enrCzs4OmzZtwogRI0ocKzIyEhEREZVZLhEREVUjNfISmCAIWLlyJYYNGwYdHZ0y+5qamqJJkyZITEwstU9oaCgyMjLE1927d1VdMhEREVUjNTIAHTlyBImJiaWe0XlVVlYWbt26BWtr61L76OrqwtjYWOFFRERE7y61BqCsrCwkJCQgISEBAJCUlISEhARx0nJoaCj8/f2LrbdixQp4enqiZcuWxZZNnjwZR44cwe3bt3Hy5En07dsXmpqaGDx4cKXuCxEREdUcap0DdPbsWXTt2lV8HxISAgAICAhATEwMUlJSit3BlZGRgV9//RWLFy8uccx79+5h8ODBePz4MczNzdGxY0f8/vvvMDc3r7wdISIiohpFrQGoS5cuEASh1OUxMTHF2kxMTJCTk1PqOhs2bFBFaURERPQOq5FzgIiIiIjeBgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERERSQ4DEBEREUkOAxARERFJDgMQERER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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "avg_usage = user_revenue.groupby(['plan','month'])['internet_sum'].sum().reset_index()\n",
    "for plan in avg_usage['plan'].unique():\n",
    "    plt.hist(avg_usage.loc[avg_usage['plan'] == plan, 'internet_sum'],\n",
    "             bins=30,\n",
    "             alpha=0.6,\n",
    "             label=plan)\n",
    "    \n",
    "plt.xlabel('Internet Used (MB)')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Distribution of Internet Usage by Plan')\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "monthly_usage = user_revenue.groupby(['user_id', 'month'])['internet_sum'].sum().reset_index()\n",
    "usage_mean= monthly_usage['internet_sum'].mean()\n",
    "usage_variance= monthly_usage['internet_sum'].var() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16764.39760575665"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "usage_mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "63476873.81347372"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "usage_variance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAl0AAAG9CAYAAAAvLsM0AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAA9hAAAPYQGoP6dpAABlGklEQVR4nO3dd1gU5/o38O+yLktzwQaIIqAYK/aI2AuwKhoJcizxRGwpBJOjWBJyEltyJFExGmM05Rw1iTE2QgxWREVUsGCJxhI1GiwUG6wCUnaf94/8dl5WUFmEXYTv57q8ZJ65d+ae3Z3de2eeeUYmhBAgIiIiokplYe4EiIiIiGoCFl1EREREJsCii4iIiMgEWHQRERERmQCLLiIiIiITYNFFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRMXMmTMHMpnMJOvq27cv+vbtK03v27cPMpkMmzZtMsn6x40bB3d3d5Osq7wePHiASZMmwdnZGTKZDFOmTDF3Ss9E//66ffv2U2Pd3d0xbty4yk+qmrh69SpkMhkWLVpk7lQA/P/9ed++feZOhaoQFl1Uba1evRoymUz6Z2VlBRcXF6jVanz++ee4f/9+hazn5s2bmDNnDk6ePFkhy6tIVTm3spg/fz5Wr16N0NBQfP/993j11VcfG+vu7g6ZTAZfX99S53/zzTfSe+HYsWOVlTKAv/OOiYmp1HUY42kF/eTJk032Y+N5V9rnygsvvIDJkycjIyPD3OlRFVfL3AkQVbZ58+bBw8MDhYWFSE9Px759+zBlyhQsXrwYW7ZsQbt27aTYDz74AO+9955Ry7958ybmzp0Ld3d3dOjQocyP27Vrl1HrKY8n5fbNN99Ap9NVeg7PYs+ePejWrRtmz55dpngrKyvs3bsX6enpcHZ2Npi3du1aWFlZ4eHDh5WRqoH58+cjODgYgYGBlb4uMg/958rDhw9x4MABrFixAtu2bcOZM2dgY2Nj7vSoiuKRLqr2Bg0ahH/+858YP348IiIisHPnTuzevRuZmZl46aWXkJeXJ8XWqlULVlZWlZpPbm4uAMDS0hKWlpaVuq4nUSgUUCqVZlt/WWRmZsLBwaHM8T169ICdnR3Wr19v0H79+nUkJiYiICCggjOkmkr/uTJp0iSsXr0aU6ZMwZUrV/DLL7+YOzWqwlh0UY3Uv39/fPjhh/jrr7/www8/SO2l9emKi4tDz5494eDgADs7O7Ro0QLvv/8+gL9P27z44osAgPHjx0unHFavXg3g735bbdu2RUpKCnr37g0bGxvpsY/26dLTarV4//334ezsDFtbW7z00ku4du2aQczj+vsUX+bTciutT1dOTg6mTZsGV1dXKJVKtGjRAosWLYIQwiBOJpNh8uTJiImJQdu2baFUKtGmTRvs2LGj9Cf8EZmZmZg4cSKcnJxgZWWF9u3bY82aNdJ8/emwK1euYOvWrVLuV69efeJyraysEBQUhB9//NGgfd26dahTpw7UanWpj9uzZw969eoFW1tbODg4YNiwYTh37pxBjP69cenSJYwbNw4ODg6wt7fH+PHjpUJa/9zk5ORgzZo1Ut6PvlZZWVlPXMaj/vzzT8hkMnz22Wcl5h06dAgymQzr1q174nNjrCe97wGgoKAAs2bNQufOnWFvbw9bW1v06tULe/fuLbGsO3fu4NVXX4VKpYKDgwNCQkJw6tQpg/ej3vnz5xEcHIy6devCysoKXbp0wZYtW4zK/bPPPoObmxusra3Rp08fnDlzRpq3atUqyGQynDhxosTj5s+fD7lcjhs3bhi1PuDvzxQAuHLlymNjEhMT8Y9//ANNmjSBUqmEq6srpk6davDDD/h737Szs8ONGzcQGBgIOzs7NGjQANOnT4dWqzU6N6o6WHRRjaXvH/Sk03y///47hgwZgvz8fMybNw9RUVF46aWXcPDgQQBAq1atMG/ePADA66+/ju+//x7ff/89evfuLS3jzp07GDRoEDp06IAlS5agX79+T8zrP//5D7Zu3Yp3330X77zzDuLi4uDr61vig/lpypJbcUIIvPTSS/jss88wcOBALF68GC1atMCMGTMQHh5eIv7AgQN46623MGrUKCxYsAAPHz7E8OHDcefOnSfmlZeXh759++L777/HmDFjsHDhQtjb22PcuHFYunSplPv333+P+vXro0OHDlLuDRo0eOp2v/LKKzhy5AguX74stf34448IDg6GQqEoEb97926o1WpkZmZizpw5CA8Px6FDh9CjR49Si7wRI0bg/v37iIyMxIgRI7B69WrMnTtXmv/9999DqVSiV69eUt5vvPGGUct4VNOmTdGjRw+sXbu2xLy1a9eidu3aGDZs2FOfm7J62vseADQaDb799lv07dsXn376KebMmYNbt25BrVYb9CHU6XQYOnQo1q1bh5CQEPznP/9BWloaQkJCSl1vt27dcO7cObz33nuIioqCra0tAgMD8fPPP5cp9++++w6ff/45wsLCEBERgTNnzqB///5Sf6vg4GBYW1s/9rns27cvGjVqZOQzBun9Vq9evcfGbNy4Ebm5uQgNDcWyZcugVquxbNkyjB07tkSsVquFWq1GvXr1sGjRIvTp0wdRUVH4+uuvjc6NqhBBVE2tWrVKABBHjx59bIy9vb3o2LGjND179mxRfLf47LPPBABx69atxy7j6NGjAoBYtWpViXl9+vQRAMTKlStLndenTx9peu/evQKAaNSokdBoNFL7hg0bBACxdOlSqc3NzU2EhIQ8dZlPyi0kJES4ublJ0zExMQKA+Pjjjw3igoODhUwmE5cuXZLaAAhLS0uDtlOnTgkAYtmyZSXWVdySJUsEAPHDDz9IbQUFBcLHx0fY2dkZbLubm5sICAh44vIejS0qKhLOzs7io48+EkIIcfbsWQFAJCQklPqe6NChg3B0dBR37twx2BYLCwsxduxYqU3/3pgwYYLBel9++WVRr149gzZbW9tSXx9jlvHoa/zVV18JAOLcuXNSW0FBgahfv36p6ypO/97auHFjqfPDwsKMft8XFRWJ/Px8g7Z79+4JJycng+3bvHmzACCWLFkitWm1WtG/f/8S780BAwYILy8v8fDhQ6lNp9OJ7t27i+bNmz9xG69cuSIACGtra3H9+nWp/fDhwwKAmDp1qtQ2evRo4eLiIrRardR2/Pjxx+4rxenfQ7t37xa3bt0S165dEz/99JOoV6+ewbr1z/nevXulx+bm5pZYXmRkpJDJZOKvv/6S2kJCQgQAMW/ePIPYjh07is6dOz8xP6raeKSLajQ7O7snXsWo70/0yy+/lLvTuVKpxPjx48scP3bsWNSuXVuaDg4ORsOGDbFt27Zyrb+stm3bBrlcjnfeecegfdq0aRBCYPv27Qbtvr6+aNasmTTdrl07qFQq/Pnnn09dj7OzM0aPHi21KRQKvPPOO3jw4AESEhKeaTvkcjlGjBghnW5bu3YtXF1d0atXrxKxaWlpOHnyJMaNG4e6desabIufn1+pz/mbb75pMN2rVy/cuXMHGo2mzDmWZxkjRoyAlZWVwRGanTt34vbt2/jnP/9Z5nWXRVne93K5XOqTqNPpcPfuXRQVFaFLly44fvy4FLdjxw4oFAq89tprUpuFhQXCwsIMlnf37l3s2bNHOgp4+/Zt3L59G3fu3IFarcbFixfLdNovMDDQ4EhV165d4e3tbfBajh07Fjdv3jQ4Fbp27VpYW1tj+PDhT10H8Pf7v0GDBnB1dcWoUaNgZ2eHn3/++YlHyaytraW/c3JycPv2bXTv3h1CiFJPd5b2Pnna/kVVG4suqtEePHhgUOA8auTIkejRowcmTZoEJycnjBo1Chs2bDCqAGvUqJFRHeabN29uMC2TyeDp6fnU/kzP6q+//oKLi0uJ56NVq1bS/OKaNGlSYhl16tTBvXv3nrqe5s2bw8LC8OPncespj1deeQVnz57FqVOn8OOPP2LUqFGlDomgX1eLFi1KzGvVqhVu376NnJwcg/ZHt7tOnToA8NTtftZlODg4YOjQoQb91dauXYtGjRpJ/YkqSlnf92vWrEG7du1gZWWFevXqoUGDBti6dSuys7OlmL/++gsNGzYscUWfp6enwfSlS5cghMCHH36IBg0aGPzTX72amZn51Nwf3X8A4IUXXjDYf/z8/NCwYUOpgNXpdFi3bh2GDRv2xM+D4pYvX464uDjs3bsXZ8+exZ9//vnYPoN6qampUoGv76fVp08fADB4zoC/+yc+ejq9LPsXVW0cMoJqrOvXryM7O7vEh39x1tbW2L9/P/bu3YutW7dix44dWL9+Pfr3749du3ZBLpc/dT3Ff91WlMeNqaTVasuUU0V43HrEI53uzcHb2xvNmjWTrih75ZVXKmzZFbHd5V3G2LFjsXHjRhw6dAheXl7YsmUL3nrrrRIF7KP0V+Q+rl9gbm6uwVW7ZXnf//DDDxg3bhwCAwMxY8YMODo6Qi6XIzIy0qA/XVnpC7rp06c/tnh50r5qDLlcjldeeQXffPMNvvzySxw8eBA3b9406ohh165d0aVLlzLHa7Va+Pn54e7du3j33XfRsmVL2Nra4saNGxg3blyJgtZU+zGZFosuqrG+//57AHjqr1MLCwsMGDAAAwYMwOLFizF//nz8+9//xt69e+Hr61vhg0pevHjRYFoIgUuXLhmMJ1anTh1kZWWVeOxff/2Fpk2bStPG5Obm5obdu3fj/v37Br/2z58/L82vCG5ubvjtt9+g0+kMioWKXs/o0aPx8ccfo1WrVo8dP02/rgsXLpSYd/78edSvXx+2trZGr7uyBhodOHAgGjRogLVr18Lb2xu5ublPHDBW70nbqW9/9Hl/2vt+06ZNaNq0KaKjow2299Ex1dzc3LB3717k5uYaHO26dOmSQZz+fatQKB47wG1ZPLr/AMAff/xR4krdsWPHIioqCr/++iu2b9+OBg0aPPWz4FmcPn0af/zxB9asWWPQcT4uLq7S1klVD08vUo20Z88efPTRR/Dw8MCYMWMeG3f37t0Sbfov8Pz8fACQvpRLK4LK47vvvjPoZ7Zp0yakpaVh0KBBUluzZs2QnJyMgoICqS02NrbE0BLG5DZ48GBotVp88cUXBu2fffYZZDKZwfqfxeDBg5Genm4wllZRURGWLVsGOzs76XTLs5o0aRJmz56NqKiox8Y0bNgQHTp0wJo1awyeozNnzmDXrl0YPHhwudZta2tbYe+H4mrVqoXRo0djw4YNWL16Nby8vAyK8cfRb+cPP/xQIq+UlBQkJycbvL5led/rj8QUPzp3+PBhJCUlGTxOrVajsLAQ33zzjdSm0+mwfPlygzhHR0f07dsXX331FdLS0kqs/9atW0/dTgCIiYkx6Pt15MgRHD58uMT7t127dmjXrh2+/fZbbN68GaNGjUKtWpV3HKK050sIIV2xSzUDj3RRtbd9+3acP38eRUVFyMjIwJ49exAXFwc3Nzds2bLliYOhzps3D/v370dAQADc3NyQmZmJL7/8Eo0bN0bPnj0B/F0AOTg4YOXKlahduzZsbW3h7e0NDw+PcuVbt25d9OzZE+PHj0dGRgaWLFkCT09Pg47IkyZNwqZNmzBw4ECMGDECly9fxg8//GDQsd3Y3IYOHYp+/frh3//+N65evYr27dtj165d+OWXXzBlypQSyy6v119/HV999RXGjRuHlJQUuLu7Y9OmTTh48CCWLFlS5j41T+Pm5oY5c+Y8NW7hwoUYNGgQfHx8MHHiROTl5WHZsmWwt7cv0+NL07lzZ+zevRuLFy+Gi4sLPDw84O3tXa5lPWrs2LH4/PPPsXfvXnz66adlftzixYuhVqvRoUMHjBs3Di4uLjh37hy+/vprNGzYEBEREVJsWd73Q4YMQXR0NF5++WUEBATgypUrWLlyJVq3bo0HDx5IywoMDETXrl0xbdo0XLp0CS1btsSWLVukwq74UbLly5ejZ8+e8PLywmuvvYamTZsiIyMDSUlJuH79Ok6dOvXU7fT09ETPnj0RGhqK/Px8LFmyBPXq1cPMmTNLfS6nT58OABV+McKjWrZsiWbNmmH69Om4ceMGVCoVNm/ezD5aNY25Lpskqmz6S7v1/ywtLYWzs7Pw8/MTS5cuNRiaQO/RISPi4+PFsGHDhIuLi7C0tBQuLi5i9OjR4o8//jB43C+//CJat24tatWqZXDZeZ8+fUSbNm1Kze9xQ0asW7dORERECEdHR2FtbS0CAgIMLifXi4qKEo0aNRJKpVL06NFDHDt2rMQyn5Tbo0NGCCHE/fv3xdSpU4WLi4tQKBSiefPmYuHChUKn0xnEARBhYWElcnrcUBaPysjIEOPHjxf169cXlpaWwsvLq9RL9cszZMSTPG4Ykd27d4sePXoIa2troVKpxNChQ8XZs2cNYvTvjUeHUdAv88qVK1Lb+fPnRe/evYW1tbUAID0nxizjSc9lmzZthIWFhcHQCGWRnJwshgwZIurUqSNq1aolGjVqJCZNmlRiOWV53+t0OjF//nzh5uYmlEql6Nixo4iNjS31fXXr1i3xyiuviNq1awt7e3sxbtw4cfDgQQFA/PTTTwaxly9fFmPHjhXOzs5CoVCIRo0aiSFDhohNmzY9cdv0Q0YsXLhQREVFCVdXV6FUKkWvXr3EqVOnSn1MWlqakMvl4oUXXijzc1iWoWiEKH3IiLNnzwpfX19hZ2cn6tevL1577TVpqJXi7/+QkBBha2tbYpmPfj7R80cmRBXo9UpERGXWsWNH1K1bF/Hx8eZOpdxiYmLw8ssv48CBA+jRo4dZcrh9+zYaNmyIWbNm4cMPPzRLDlSzsE8XEdFz5NixYzh58mSpo5hXVY9eNanVarFs2TKoVCp06tTJTFkBq1evhlarLdPFCEQVgX26iIieA2fOnEFKSgqioqLQsGFDjBw50twpldnbb7+NvLw8+Pj4ID8/H9HR0Th06BDmz59fKUOqPM2ePXtw9uxZ/Oc//0FgYGCJKxuJKguLLiKi58CmTZswb948tGjRAuvWrXviBSBVTf/+/REVFYXY2Fg8fPgQnp6eWLZsGSZPnmyWfObNmyfdX3PZsmVmyYFqJvbpIiIiIjIB9ukiIiIiMgEWXUREREQmwD5dFUSn0+HmzZuoXbt2pd0ChIiIiKoWIQTu378PFxeXp94HlUVXBbl58yZcXV3NnQYRERGZwbVr19C4ceMnxrDoqiD6W5dcu3YNKpXKzNmQqRUWFmLXrl3w9/eHQqEwdzpEZELc/2s2jUYDV1fXMt3CjEVXBdGfUlSpVCy6aqDCwkLY2NhApVLxQ5eohuH+TwDK1LWIHemJiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAiy6iJ6RVqtFQkIC9u/fj4SEBGi1WnOnREREVRCLLqJnEB0dDU9PT/j5+WHx4sXw8/ODp6cnoqOjzZ0aERFVMSy6iMopOjoawcHB8PLyQmJiItatW4fExER4eXkhODiYhRcRERlg0UVUDlqtFtOmTcOQIUMQExMDb29vWFtbw9vbGzExMRgyZAimT5/OU41ERCRh0UVUDomJibh69Sref/99WFgY7kYWFhaIiIjAlStXkJiYaKYMiYioqjFr0eXu7g6ZTFbiX1hYGADg4cOHCAsLQ7169WBnZ4fhw4cjIyPDYBmpqakICAiAjY0NHB0dMWPGDBQVFRnE7Nu3D506dYJSqYSnpydWr15dIpfly5fD3d0dVlZW8Pb2xpEjRyptu+n5l5aWBgBo27ZtqfP17fo4IiIisxZdR48eRVpamvQvLi4OAPCPf/wDADB16lT8+uuv2LhxIxISEnDz5k0EBQVJj9dqtQgICEBBQQEOHTqENWvWYPXq1Zg1a5YUc+XKFQQEBKBfv344efIkpkyZgkmTJmHnzp1SzPr16xEeHo7Zs2fj+PHjaN++PdRqNTIzM030TNDzpmHDhgCAM2fOlDpf366PIyIigqhC/vWvf4lmzZoJnU4nsrKyhEKhEBs3bpTmnzt3TgAQSUlJQgghtm3bJiwsLER6eroUs2LFCqFSqUR+fr4QQoiZM2eKNm3aGKxn5MiRQq1WS9Ndu3YVYWFh0rRWqxUuLi4iMjKyzLlnZ2cLACI7O9u4jabnUlFRkXB3dxdDhw4VWq1WFBQUiJiYGFFQUCC0Wq0YOnSo8PDwEEVFReZOlYgqWfH9n2oeY77/a5m55pMUFBTghx9+QHh4OGQyGVJSUlBYWAhfX18ppmXLlmjSpAmSkpLQrVs3JCUlwcvLC05OTlKMWq1GaGgofv/9d3Ts2BFJSUkGy9DHTJkyRVpvSkoKIiIipPkWFhbw9fVFUlLSY/PNz89Hfn6+NK3RaAAAhYWFKCwsfKbngp4Pn376KUaNGoWXXnoJ06ZNQ15eHg4cOICoqChs27YNP/30E3Q6HXQ6nblTJaJKpP/M52d/zWTM615liq6YmBhkZWVh3LhxAID09HRYWlrCwcHBIM7JyQnp6elSTPGCSz9fP+9JMRqNBnl5ebh37x60Wm2pMefPn39svpGRkZg7d26J9l27dsHGxubpG0zPPaVSiZkzZ2LVqlXo37+/1O7k5ISZM2dCqVRi27ZtZsyQiExJ30WGapbc3Nwyx1aZouu///0vBg0aBBcXF3OnUiYREREIDw+XpjUaDVxdXeHv7w+VSmXGzMiUBg8ejDlz5mDfvn2Ii4uDn58f+vbtC7lcbu7UiMhECgsLpf1foVCYOx0yMf2ZrrKoEkXXX3/9hd27dxsMJuns7IyCggJkZWUZHO3KyMiAs7OzFPPoVYb6qxuLxzx6xWNGRgZUKhWsra0hl8shl8tLjdEvozRKpRJKpbJEu0Kh4E5XwygUCgwYMAD5+fkYMGAAX3+iGoqf/zWTMa95lRina9WqVXB0dERAQIDU1rlzZygUCsTHx0ttFy5cQGpqKnx8fAAAPj4+OH36tMFVhnFxcVCpVGjdurUUU3wZ+hj9MiwtLdG5c2eDGJ1Oh/j4eCmGiIiI6FmZ/UiXTqfDqlWrEBISglq1/n869vb2mDhxIsLDw1G3bl2oVCq8/fbb8PHxQbdu3QAA/v7+aN26NV599VUsWLAA6enp+OCDDxAWFiYdhXrzzTfxxRdfYObMmZgwYQL27NmDDRs2YOvWrdK6wsPDERISgi5duqBr165YsmQJcnJyMH78eNM+GURERFRtmb3o2r17N1JTUzFhwoQS8z777DNYWFhg+PDhyM/Ph1qtxpdffinNl8vliI2NRWhoKHx8fGBra4uQkBDMmzdPivHw8MDWrVsxdepULF26FI0bN8a3334LtVotxYwcORK3bt3CrFmzkJ6ejg4dOmDHjh0lOtcTERERlZdMCCHMnUR1oNFoYG9vj+zsbHakr4EKCwuxbds2DB48mH06iGoY7v81mzHf/1WiTxcRERFRdceii4iIiMgEWHQRERERmQCLLqJnpNVqkZCQgP379yMhIQFardbcKRERURXEoovoGURHR8PT0xN+fn5YvHgx/Pz84OnpaTDQLxEREcCii6jcoqOjERwcDC8vLyQmJmLdunVITEyEl5cXgoODWXgREZEBFl1E5aDVajFt2jQMGTIEMTEx8Pb2hrW1Nby9vRETE4MhQ4Zg+vTpPNVIREQSFl1E5ZCYmIirV6/i/fffh4WF4W5kYWGBiIgIXLlyBYmJiWbKkIiIqhoWXUTlkJaWBgBo27ZtqfP17fo4IiIiFl1E5dCwYUMAwJkzZ0qdr2/XxxEREbHoIiqHXr16wd3dHfPnz4dOpzOYp9PpEBkZCQ8PD/Tq1ctMGRIRUVXDoouoHORyOaKiohAbG4vAwEAkJycjLy8PycnJCAwMRGxsLBYtWgS5XG7uVImIqIqoZe4EiJ5XQUFB2LRpE6ZNm4bevXtL7R4eHti0aROCgoLMmB0REVU1LLqInkFQUBCGDRuGvXv3Yvv27Rg0aBD69evHI1xERFQCiy6iZySXy9GnTx/k5OSgT58+LLiIiKhU7NNFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAiy6iIiIiEyARRcRERGRCbDoIiIiIjIBFl1EREREJmD2ouvGjRv45z//iXr16sHa2hpeXl44duyYNF8IgVmzZqFhw4awtraGr68vLl68aLCMu3fvYsyYMVCpVHBwcMDEiRPx4MEDg5jffvsNvXr1gpWVFVxdXbFgwYISuWzcuBEtW7aElZUVvLy8sG3btsrZaCIiIqpxzFp03bt3Dz169IBCocD27dtx9uxZREVFoU6dOlLMggUL8Pnnn2PlypU4fPgwbG1toVar8fDhQylmzJgx+P333xEXF4fY2Fjs378fr7/+ujRfo9HA398fbm5uSElJwcKFCzFnzhx8/fXXUsyhQ4cwevRoTJw4ESdOnEBgYCACAwNx5swZ0zwZREREVL0JM3r33XdFz549Hztfp9MJZ2dnsXDhQqktKytLKJVKsW7dOiGEEGfPnhUAxNGjR6WY7du3C5lMJm7cuCGEEOLLL78UderUEfn5+QbrbtGihTQ9YsQIERAQYLB+b29v8cYbb5RpW7KzswUAkZ2dXaZ4ql4KCgpETEyMKCgoMHcqRGRi3P9rNmO+/2uZs+DbsmUL1Go1/vGPfyAhIQGNGjXCW2+9hddeew0AcOXKFaSnp8PX11d6jL29Pby9vZGUlIRRo0YhKSkJDg4O6NKlixTj6+sLCwsLHD58GC+//DKSkpLQu3dvWFpaSjFqtRqffvop7t27hzp16iApKQnh4eEG+anVasTExJSae35+PvLz86VpjUYDACgsLERhYeEzPzf0fNG/5nztiWoe7v81mzGvu1mLrj///BMrVqxAeHg43n//fRw9ehTvvPMOLC0tERISgvT0dACAk5OTweOcnJykeenp6XB0dDSYX6tWLdStW9cgxsPDo8Qy9PPq1KmD9PT0J67nUZGRkZg7d26J9l27dsHGxqasTwFVM3FxceZOgYjMhPt/zZSbm1vmWLMWXTqdDl26dMH8+fMBAB07dsSZM2ewcuVKhISEmDO1p4qIiDA4MqbRaODq6gp/f3+oVCozZkbmUFhYiLi4OPj5+UGhUJg7HSIyIe7/NZv+TFdZmLXoatiwIVq3bm3Q1qpVK2zevBkA4OzsDADIyMhAw4YNpZiMjAx06NBBisnMzDRYRlFREe7evSs93tnZGRkZGQYx+umnxejnP0qpVEKpVJZoVygU3OlqML7+RDUX9/+ayZjX3KxXL/bo0QMXLlwwaPvjjz/g5uYGAPDw8ICzszPi4+Ol+RqNBocPH4aPjw8AwMfHB1lZWUhJSZFi9uzZA51OB29vbylm//79Budd4+Li0KJFC+lKSR8fH4P16GP06yEiIiJ6FmYtuqZOnYrk5GTMnz8fly5dwo8//oivv/4aYWFhAACZTIYpU6bg448/xpYtW3D69GmMHTsWLi4uCAwMBPD3kbGBAwfitddew5EjR3Dw4EFMnjwZo0aNgouLCwDglVdegaWlJSZOnIjff/8d69evx9KlSw1OD/7rX//Cjh07EBUVhfPnz2POnDk4duwYJk+ebPLnhYiIiKohE1xN+US//vqraNu2rVAqlaJly5bi66+/Npiv0+nEhx9+KJycnIRSqRQDBgwQFy5cMIi5c+eOGD16tLCzsxMqlUqMHz9e3L9/3yDm1KlTomfPnkKpVIpGjRqJTz75pEQuGzZsEC+88IKwtLQUbdq0EVu3bi3zdnDIiJqNl4wT1Vzc/2s2Y77/ZUIIYe7CrzrQaDSwt7dHdnY2O9LXQIWFhdi2bRsGDx7MPh1ENQz3/5rNmO9/s98GiIiIiKgmYNFFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAiy6iIiIiEyARRcRERGRCbDoIiIiIjIBFl1EREREJsCii4iIiMgEWHQRERERmQCLLqJnpNVqkZCQgP379yMhIQFardbcKRERURXEoovoGURHR8PT0xN+fn5YvHgx/Pz84OnpiejoaHOnRkREVQyLLqJyio6ORnBwMDIyMgzaMzIyEBwczMKLiIgMsOgiKgetVovQ0FAIITBgwAAkJiZi3bp1SExMxIABAyCEQGhoKE81EhGRhEUXUTns27cPmZmZ6NmzJ3755Rd4e3vD2toa3t7e+OWXX9CjRw9kZmZi37595k6ViIiqCBZdROWgL6bmzp0LCwvD3cjCwgJz5swxiCMiImLRRURERGQCLLqIyqFv374AgNmzZ0On0xnM0+l0mDt3rkEcERERiy6icujbty8aNGiAAwcOYNiwYUhOTkZeXh6Sk5MxbNgwHDhwAI6Ojiy6iIhIUsvcCRA9j+RyOVauXInhw4cjPj4esbGx0jwbGxsAwIoVKyCXy82VIhERVTE80kVUTkFBQdi8eTMcHR0N2h0dHbF582YEBQWZKTMiIqqKzFp0zZkzBzKZzOBfy5YtpfkPHz5EWFgY6tWrBzs7OwwfPrzEQJSpqakICAiAjY0NHB0dMWPGDBQVFRnE7Nu3D506dYJSqYSnpydWr15dIpfly5fD3d0dVlZW8Pb2xpEjRyplm6n6E0KYOwUiIqqCzH6kq02bNkhLS5P+HThwQJo3depU/Prrr9i4cSMSEhJw8+ZNg6MHWq0WAQEBKCgowKFDh7BmzRqsXr0as2bNkmKuXLmCgIAA9OvXDydPnsSUKVMwadIk7Ny5U4pZv349wsPDMXv2bBw/fhzt27eHWq1GZmamaZ4Eei7pR6Rv166dweCo7dq144j0RERUkjCj2bNni/bt25c6LysrSygUCrFx40ap7dy5cwKASEpKEkIIsW3bNmFhYSHS09OlmBUrVgiVSiXy8/OFEELMnDlTtGnTxmDZI0eOFGq1Wpru2rWrCAsLk6a1Wq1wcXERkZGRZd6W7OxsAUBkZ2eX+TH0/CoqKhLu7u5i6NChQqvVioKCAhETEyMKCgqEVqsVQ4cOFR4eHqKoqMjcqRJRJSu+/1PNY8z3v9k70l+8eBEuLi6wsrKCj48PIiMj0aRJE6SkpKCwsBC+vr5SbMuWLdGkSRMkJSWhW7duSEpKgpeXF5ycnKQYtVqN0NBQ/P777+jYsSOSkpIMlqGPmTJlCgCgoKAAKSkpiIiIkOZbWFjA19cXSUlJj807Pz8f+fn50rRGowEAFBYWorCw8JmeE6r6EhIScPXqVXz//ffQarXSa67/f8aMGejduzf27t2LPn36mDNVIqpkj+7/VLMY87qbtejy9vbG6tWr0aJFC6SlpWHu3Lno1asXzpw5g/T0dFhaWsLBwcHgMU5OTkhPTwcApKenGxRc+vn6eU+K0Wg0yMvLw71796DVakuNOX/+/GNzj4yMlMZiKm7Xrl3S1WtUfe3fvx8AcP36ddy5c0dqj4uLAwDk5eUBALZv346cnBzTJ0hEJqff/6lmyc3NLXOsWYuuQYMGSX+3a9cO3t7ecHNzw4YNG2BtbW3GzJ4uIiIC4eHh0rRGo4Grqyv8/f2hUqnMmBmZgq2tLRYvXozGjRvD29sbhYWFiIuLg5+fHxQKBZKTkwH8/R7nkS6i6u3R/Z9qFv2ZrrIw++nF4hwcHPDCCy/g0qVL8PPzQ0FBAbKysgyOdmVkZMDZ2RkA4OzsXOIqQ/3VjcVjHr3iMSMjAyqVCtbW1pDL5ZDL5aXG6JdRGqVSCaVSWaJdoVBwp6sB+vXrB3d3dyxYsAAxMTFSu0KhgFwux8KFC+Hh4YF+/fpxrC6iGoKf/zWTMa+52a9eLO7Bgwe4fPkyGjZsiM6dO0OhUCA+Pl6af+HCBaSmpsLHxwcA4OPjg9OnTxtcZRgXFweVSoXWrVtLMcWXoY/RL8PS0hKdO3c2iNHpdIiPj5diiB4ll8sRFRWF2NhYBAYGGoxIHxgYiNjYWCxatIgFFxER/X8m6Nj/WNOmTRP79u0TV65cEQcPHhS+vr6ifv36IjMzUwghxJtvvimaNGki9uzZI44dOyZ8fHyEj4+P9PiioiLRtm1b4e/vL06ePCl27NghGjRoICIiIqSYP//8U9jY2IgZM2aIc+fOieXLlwu5XC527Nghxfz0009CqVSK1atXi7Nnz4rXX39dODg4GFwV+TS8erFm2rx5s3B3dxcApH8eHh5i8+bN5k6NiEyEVy/WbMZ8/5u16Bo5cqRo2LChsLS0FI0aNRIjR44Uly5dkubn5eWJt956S9SpU0fY2NiIl19+WaSlpRks4+rVq2LQoEHC2tpa1K9fX0ybNk0UFhYaxOzdu1d06NBBWFpaiqZNm4pVq1aVyGXZsmWiSZMmwtLSUnTt2lUkJycbtS0sumquoqIiERcXJ8LDw0VcXByHiSCqYVh01WzGfP/LhODw2RVBo9HA3t4e2dnZ7EhfAxUWFmLbtm0YPHgw+3QQ1TDc/2s2Y77/q1SfLiIiIqLqikUXERERkQmw6CJ6RlqtFgkJCdi/fz8SEhKg1WrNnRIREVVBLLqInkF0dDQ8PT3h5+eHxYsXw8/PD56enrzZNVENwR9dZAwWXUTlFB0djeDgYHh5eSExMRHr1q1DYmIivLy8EBwczMKLqJrjjy4yFq9erCC8erFm0Wq18PT0hJeXF2JiYqDVaqWrl+RyOQIDA3HmzBlcvHiRA6QSVUP6H10BAQHw9/fHH3/8gRdeeAG7du3C1q1bsWnTJgQFBZk7TTIBY77/WXRVEBZdNcu+ffvQr18/JCUloVu3biUuGU9KSkL37t2xd+9e9O3b19zpElEF0v/oql+/Pm7fvo2rV69K89zd3VG/fn3cuXOHP7pqCA4ZQVTJ0tLSAABt27Ytdb6+XR9HRNVHYmIirl69ipSUlFK7F6SkpODKlStITEw0d6pUxbDoIiqHhg0bAgDOnDlT6nx9uz6OiKqPGzduAAAGDhyImJgYeHt7w9raGt7e3oiJicHAgQMN4oj0WHQRlUOvXr3g7u6O+fPnQ6fTGczT6XSIjIyEh4cHevXqZaYMiaiy3Lp1CwAQFBQECwvDr1ELCwsEBgYaxBHplavoysrKwrfffouIiAjcvXsXAHD8+HFW9VRjyOVyREVFITY2FoGBgUhOTkZeXh6Sk5MRGBiI2NhYLFq0iP05iKqhBg0aAPi7M31pP7piYmIM4oj0ahn7gN9++w2+vr6wt7fH1atX8dprr6Fu3bqIjo5Gamoqvvvuu8rIk6jKCQoKwqZNmzBt2jT07t1bavfw8OCVS0TVWKNGjQAA27dvx7Bhw+Dn54eLFy/ir7/+QlxcHLZv324QR6Rn9NWLvr6+6NSpExYsWIDatWvj1KlTaNq0KQ4dOoRXXnnF4CqOmoRXL9ZcWq0We/fuxfbt2zFo0CD069ePR7iIqjH91YtyuRxXr141GBBVLpfD3d0dOp2OVy/WEMZ8/xt9pOvo0aP46quvSrQ3atQI6enpxi6O6Lknl8vRp08f5OTkoE+fPvyQJarm5HI5/vGPf2DhwoVwcnLC6NGjkZubCxsbG6xbtw6XL1/GjBkz+FlAJRhddCmVSmg0mhLtf/zxB89fExFRtafVarFx40Z06dIFt2/fxpIlS6R5Hh4e6NKlCzZt2oTIyEgWXmTA6I70L730EubNm4fCwkIAgEwmQ2pqKt59910MHz68whMkIiKqSvTjdC1btgyXLl1CXFwcwsPDERcXh4sXL+Lzzz/nOF1UKqOLrqioKDx48ACOjo7Iy8tDnz594Onpidq1a+M///lPZeRIRERUZRQfHFnfvaB3795S9wIOjkyPY/TpRXt7e8TFxeHAgQP47bff8ODBA3Tq1Am+vr6VkR8REVGVUnxw5G7dupWYz8GR6XGMLrr0evbsiZ49e1ZkLkRERFVe8cGR9WNy6XFwZHoSo4uuzz//vNR2mUwGKysreHp6onfv3uw8SERE1ZJ+cOTg4GAEBgZixowZ0uDICxcuRGxsLDZt2sTvQSrB6KLrs88+w61bt5Cbm4s6deoAAO7duwcbGxvY2dkhMzMTTZs2xd69e+Hq6lrhCRMREZkbB0em8jC6I/38+fPx4osv4uLFi7hz5w7u3LmDP/74A97e3li6dClSU1Ph7OyMqVOnVka+RFWOVqtFQkIC9u/fj4SEBIOBEomoent0fPFHbwtEVJzRI9I3a9YMmzdvRocOHQzaT5w4geHDh+PPP//EoUOHMHz48Bp15QZHpK+ZoqOjMW3aNIM7Mbi7uyMqKoq/dImqsejoaAQHB2PIkCGYOXMmrl+/jsaNG2PBggXS6UV+BtQMxnz/G32kKy0tDUVFRSXai4qKpBHpXVxccP/+fWMXTfRc0X/oenl5ITExEevWrUNiYiK8vLwQHByM6Ohoc6dIRJVAq9Vi2rRpGDJkCGJiYuDt7Q1ra2t4e3sjJiYGQ4YMwfTp03nUm0owuujq168f3njjDZw4cUJqO3HiBEJDQ9G/f38AwOnTp+Hh4VFxWRJVMcU/dDdv3oyHDx/i6NGjePjwITZv3swPXaJqTD846vvvvw8LC8OvUQsLC0RERHBwVCqV0UXXf//7X9StWxedO3eGUqmEUqlEly5dULduXfz3v/8FANjZ2SEqKqrCkyWqKvQfut27d0fz5s3h5+eHxYsXw8/PD82bN4ePjw8/dImqqeKDo5aGg6PS4xh99aKzszPi4uJw/vx5/PHHHwCAFi1aoEWLFlJMv379Ki5DoipI/2EaEREBa2trg3mZmZl4//33DeKIqPrg4KhUXuUeHLVly5Zo2bJlReZC9NxwdHSs0Dgien5wcFQqr3IVXdevX8eWLVuQmpqKgoICg3mLFy+ukMSIqrLifbX69++P9957T7p66ZNPPsHWrVtLxBFR9cDBUam8jC664uPj8dJLL6Fp06Y4f/482rZti6tXr0IIgU6dOlVGjkRVTkJCgsH08ePHcfHiRTRv3rxEnL+/vylTIyIT4OCoVB5GF10RERGYPn065s6di9q1a2Pz5s1wdHTEmDFjMHDgwMrIkajKuXbtGgBgwIAB2Llzp3RkCwBq1aqF/v37Y8+ePVIcEVU/QUFBGDZsGPbu3Yvt27dj0KBB6NevH49w0WMZXXSdO3cO69at+/vBtWohLy8PdnZ2mDdvHoYNG4bQ0NAKT5KoqtHf4io+Ph4BAQHw9/eXjnTt2rVLKsJ4Kyyi6k0ul6NPnz7IyclBnz59WHDRExk9ZIStra3Uj6thw4a4fPmyNO/27dsVlxlRFdanTx+D6Y4dO6JHjx7o2LHjE+OIqHrhbcDIGEYf6erWrRsOHDiAVq1aYfDgwZg2bRpOnz6N6OjoUi+dJaqOiv+ajY+PNzi9aGVlVWocEVUvj94GbPHixbwNGD2R0Ue6Fi9eDG9vbwDA3LlzMWDAAKxfvx7u7u7S4KhE1V1mZqb0d35+vsG84tPF44io+uBtwKg8jC66mjZtinbt2gH4+1TjypUr8dtvv2Hz5s1wc3MrdyKffPIJZDIZpkyZIrU9fPgQYWFhqFevHuzs7DB8+HBkZGQYPC41NRUBAQGwsbGBo6MjZsyYUeLekPv27UOnTp2gVCrh6emJ1atXl1j/8uXL4e7uDisrK3h7e+PIkSPl3haq/ooPevjoPeOLT3NwRKLqh/depPIyuui6du0arl+/Lk0fOXIEU6ZMwddff13uJI4ePYqvvvpKKub0pk6dil9//RUbN25EQkICbt68aXDIVqvVIiAgAAUFBTh06BDWrFmD1atXY9asWVLMlStXEBAQgH79+uHkyZOYMmUKJk2ahJ07d0ox69evR3h4OGbPno3jx4+jffv2UKvVPEpBj9W9e3fpnmuDBw/G0qVLMXnyZCxduhSDBw8G8Pc92Lp3727ONImoEvDei1Ruwkg9e/YU3333nRBCiLS0NFG7dm3h4+Mj6tevL+bOnWvs4sT9+/dF8+bNRVxcnOjTp4/417/+JYQQIisrSygUCrFx40Yp9ty5cwKASEpKEkIIsW3bNmFhYSHS09OlmBUrVgiVSiXy8/OFEELMnDlTtGnTxmCdI0eOFGq1Wpru2rWrCAsLk6a1Wq1wcXERkZGRZd6O7OxsAUBkZ2eXfePpubV7924BQAAQQ4YMEfv37xfr1q0T+/fvF0OGDJHm7d6929ypElEF+/HHHwUAcf/+fVFUVCTi4uJEeHi4iIuLE0VFRUKj0QgA4scffzR3qmQCxnz/G92R/syZM+jatSsAYMOGDfDy8sLBgwexa9cuvPnmmwZHmcoiLCwMAQEB8PX1xccffyy1p6SkoLCwEL6+vlJby5Yt0aRJEyQlJaFbt25ISkqCl5cXnJycpBi1Wo3Q0FD8/vvv6NixI5KSkgyWoY/Rn8YsKChASkoKIiIipPkWFhbw9fVFUlLSY/POz8836Luj0WgAAIWFhSgsLDTqOaDnT3x8PADggw8+wA8//FBicMQPPvgAH3/8MeLj4w3mEdHzr0GDBgCApUuX4ttvvy3RkX7ixIlSHL8Pqj9jXmOji67CwkIolUoAwO7du/HSSy8B+LsgMvbmvj/99BOOHz+Oo0ePlpiXnp4OS0tLODg4GLQ7OTkhPT1diilecOnn6+c9KUaj0SAvLw/37t2DVqstNeb8+fOPzT0yMhJz584t0b5r1y7Y2Ng89nFUPVy6dAkAYGlpiQULFmDHjh1IT0+Hs7MzBg4ciHPnzklx27ZtM2eqRFTBtFotVCoVPvjgA3Tu3Bn+/v6wtLSUfsR/+OGHsLe3h0aj4f5fA+Tm5pY51uiiq02bNli5ciUCAgIQFxeHjz76CABw8+ZN1KtXr8zLuXbtGv71r38hLi7O4BL750VERATCw8OlaY1GA1dXV/j7+0OlUpkxMzIFKysrbNy4EWvXrkVeXh5SU1Olebt374a1tTUAYOLEiejfv7+50iSiSqDVaqWDD2fOnEFKSoo0T9+uVCoxePBgDhtTA+jPdJWF0UXXp59+ipdffhkLFy5ESEgI2rdvDwDYsmWLdNqxLFJSUpCZmWlwv0atVov9+/fjiy++wM6dO1FQUICsrCyDo10ZGRlwdnYGADg7O5e4ylB/dWPxmEeveMzIyIBKpYK1tTXkcjnkcnmpMfpllEapVEo7V3EKhQIKhaIMzwA9z3x9faFSqXDhwoUSHWmvX78OnU4HlUoFX19ffugSVTMHDx7ErVu3AEAaLFxPP52ZmYnk5GT07dvX1OmRiRnznW/01Yt9+/bF7du3cfv2bfzvf/+T2l9//XWsXLmyzMsZMGAATp8+jZMnT0r/unTpgjFjxkh/KxQKqe8MAFy4cAGpqanw8fEBAPj4+OD06dMGVxnGxcVBpVKhdevWUkzxZehj9MuwtLRE586dDWJ0Oh3i4+OlGCJjyGQyc6dARJXoxo0b0t+P/vguPl08jggox5Eu4O9RtuvUqWPQ5u7ubtQyateujbZt2xq02draol69elL7xIkTER4ejrp160KlUuHtt9+Gj4+PNPK9v78/WrdujVdffRULFixAeno6PvjgA4SFhUlv/DfffBNffPEFZs6ciQkTJmDPnj3YsGGDwQji4eHhCAkJQZcuXdC1a1csWbIEOTk5GD9+vLFPDdUQ+/btg0ajQcuWLZGXl4e//vpLmufq6gorKyucP38e+/btw4ABA8yYKRFVNH2fYaDkj6zi08XjiAAjiq46deqU+gve3t4eL7zwAqZPnw4/P78KTe6zzz6DhYUFhg8fjvz8fKjVanz55ZfSfLlcjtjYWISGhsLHxwe2trYICQnBvHnzpBgPDw9s3boVU6dOxdKlS9G4cWN8++23UKvVUszIkSNx69YtzJo1C+np6ejQoQN27NhRonM9kd6+ffsA/D2oro+PD8LDw5GcnIxu3bph8eLFOHjwIPz8/Fh0EVVDxe8znJeXZzCv+DTvR0yPKnPRtWTJklLbs7KykJKSgiFDhmDTpk0YOnRouZPRf5HpWVlZYfny5Vi+fPljH+Pm5vbUq0P69u2LEydOPDFm8uTJmDx5cplzJQKAr776Cn5+ftDpdACAkydP4uuvv0ZwcLCZMyOiynLt2rUKjaOao8xFV0hIyBPnd+jQAZGRkc9UdBE9L/r27YuPP/4YGzZsKDFPp9NJ7exES1T96H9kVVQc1Rzl6tNVmiFDhhgMbkpUnZX19j68DRBR9VP8aneFQoGgoCDY2toiJycH0dHR0mCZj14VT1RhRVd+fj4sLS0ranFEVdoXX3xR5rgZM2ZUcjZEZErF+21ZWFhg/fr10nTxqxcf7e9FZPSQEY/z3//+Fx06dKioxRFVab/88kuFxhHR8+Phw4fS38VvB/fodPE4IsCII13FR18vLjs7G8ePH8cff/yB/fv3V1hiRFVZdnZ2hcYR0fPD1dX1qRdn6eOIiitz0fW4N5hKpYKfnx+io6Ph4eFRYYkRVWX6G95WVBwRPT969uyJLVu2lCmOqLgyF1179+6tzDyInitlvc+oMfcjJaLnQ6tWrSo0jmqOCuvTRVST/PnnnxUaR0TPj88//7xC46jmYNFFVA7379+v0Dgien7cu3evQuOo5mDRRVQOtWvXrtA4Inp+6K/Ul8vluH//PhYtWoTBgwdj0aJFuH//PuRyuUEckR6LLqJyKOv9FHnfRaLqx9PTEwCg1WoxYsQIXL16FUVFRbh69SpGjBgBrVZrEEekZ/TgqDk5ObC1ta2MXIieG7x6kajmun79uvT39u3bpb937dr12DgioBxHupycnDBhwgQcOHCgMvIhei7cvXu3QuOI6PnRrFmzCo2jmsPoouuHH37A3bt30b9/f7zwwgv45JNPcPPmzcrIjajKunHjRoXGEdHzY9KkSdLfVlZWBvOKTxePIwLKUXQFBgYiJiYGN27cwJtvvokff/wRbm5uGDJkCKKjo1FUVFQZeRJVKU5OTtLf1tbWBvOKTxePI6Lq4auvvpL+1ul0GDlyJMaNG4eRI0dCp9OVGkcEADIhhHjWhSxbtgwzZsxAQUEB6tevjzfffBPvvfcebGxsKiLH54JGo4G9vT2ys7OhUqnMnQ5Vsh49euDQoUMAgMGDB0OtVuPixYto3rw5du7ciW3btgEAunfvjoMHD5ozVSKqYIGBgfjll1/g4OCArKysEvP17cOGDUNMTIzJ8yPTMub73+iO9HoZGRlYs2YNVq9ejb/++gvBwcGYOHEirl+/jk8//RTJycklOhUSVRdpaWnS33v37pWKLMDwSFfxOCKqHnJycgAAWVlZGDx4MCwtLXH58mU0a9YMBQUF0ueBPo5Iz+iiKzo6GqtWrcLOnTvRunVrvPXWW/jnP/8JBwcHKaZ79+68/QFVG7m5uTh//rxBW/F+G8VPJwBA8YPHVlZWOH78eIlltmzZskYdCSaqTjp37ozdu3fDwsICZ86cQWpqKgDg9OnTaNKkCSwsLKDT6dC5c2czZ0pVjdFF1/jx4zFq1CgcPHgQL774YqkxLi4u+Pe///3MyRFVBefPn3/ih2d+fr7B9MOHD6W/z507V+pjU1JS0KlTp4pLkohMRj8UjE6nkwouveLTHDKGHmV00ZWWlvbUX+jW1taYPXt2uZMiqkpatmyJlJQUgzatVosePXqgsLAQMpkMbdp3xBWZMzxEOn4/dQJCCCgUChw8eFAanfrRZRLR88nR0bFC46jmKFPRpdFonjhdHDuRU3VjY2NT6lGpn376CcOHD4cQAmdO/n0K8cwj8x93NJiInl/p6enS39bW1sjLyyt1ungcEVDGosvBwQEymeyJMUIIyGQy6fYHRNVdUFAQNm/ejKlTpxqcUnBzc8PixYsRFBRkxuyIqLKcOnUKAODq6gq5XI6rV69K85ydnVFUVIRr165JcUR6ZSq69u7dW9l5ED2XgoKCMGzYMKzaGIuIHw8i8pUeGP+PIaWeUiSi509pF9LoBz2+du0aevXqhWEvB+HCleto4dEYx48dRWJiohTHC2mouAoZp4s4TldNd/KvOwhckYyY0G7o4FbP3OkQUQU5fvx4hV+FyAtpqpdKH6crKysLR44cQWZmZonL5ceOHVueRRIREVU5pV1IU1BQgB49ekCn06FHjx5o7tUJ0aduIah9A1w8fRwHDx6EhYUFDh48CEtLy1KXSTWT0UXXr7/+ijFjxuDBgwdQqVQGfb1kMhmLLiIiqjYedyHNtGnTsHDhQiQlJUl3nVidBKlrwbRp09CtWzeT5kpVn9H3Xpw2bRomTJiABw8eICsrC/fu3ZP+3b17tzJyJCIiqlIWLFiAGTNmlLjITCaTYcaMGViwYIGZMqOqzOii68aNG3jnnXfYCZCIiGq0BQsWIDc3F9M//Ai1Ow3B9A8/Qk5ODgsueiyjiy61Wo1jx45VRi5ERETPFUtLS4yZGIq6fm9izMTQUvtwEemVqU/Xli1bpL8DAgIwY8YMnD17Fl5eXlAoFAaxL730UsVmSERERFQNlKnoCgwMLNE2b968Em0cHJWIiIiodGUquh4dFoKIiIiIjGN0n67vvvsO+fn5JdoLCgrw3XffVUhSRERERNWN0UXX+PHjkZ2dXaL9/v37GD9+fIUkRURERFTdGF106W9s/ajr16/D3t6+QpIiIiIiqm7KXHR17NgRnTp1gkwmw4ABA9CpUyfpX/v27dGrVy/4+voatfIVK1agXbt2UKlUUKlU8PHxwfbt26X5Dx8+RFhYGOrVqwc7OzsMHz4cGRkZBstITU1FQEAAbGxs4OjoiBkzZqCoqMggZt++fejUqROUSiU8PT2xevXqErksX74c7u7usLKygre3N44cOWLUthARERE9SZlvA6S/gvHkyZNQq9Wws7OT5llaWsLd3R3Dhw83auWNGzfGJ598gubNm0MIgTVr1mDYsGE4ceIE2rRpg6lTp2Lr1q3YuHEj7O3tMXnyZAQFBUm3XNBqtQgICICzszMOHTqEtLQ0jB07FgqFAvPnzwcAXLlyBQEBAXjzzTexdu1axMfHY9KkSWjYsCHUajUAYP369QgPD8fKlSvh7e2NJUuWQK1W48KFC3B0dDRqm4iIiIhKJYy0evVqkZeXZ+zDyqxOnTri22+/FVlZWUKhUIiNGzdK886dOycAiKSkJCGEENu2bRMWFhYiPT1dilmxYoVQqVQiPz9fCCHEzJkzRZs2bQzWMXLkSKFWq6Xprl27irCwMGlaq9UKFxcXERkZWea8s7OzBQCRnZ1t3AZTtXDi6m3h9m6sOHH1trlTISIT4/5fsxnz/W/0Da9DQkIA/H21YmZmZonhJJo0aVKu4k+r1WLjxo3IycmBj48PUlJSUFhYaHDKsmXLlmjSpAmSkpLQrVs3JCUlwcvLC05OTlKMWq1GaGgofv/9d3Ts2BFJSUklTnuq1WpMmTJF2o6UlBRERERI8y0sLODr64ukpKTH5pufn29wFadGowEAFBYWorCwsFzPAT2/9Ke0i4qK+PoT1TDc/2s2Y15zo4uuixcvYsKECTh06JBBu/i/DvbGDo56+vRp+Pj44OHDh7Czs8PPP/+M1q1b4+TJk7C0tISDg4NBvJOTE9LT0wEA6enpBgWXfr5+3pNiNBoN8vLycO/ePWi12lJjzp8//9i8IyMjMXfu3BLtu3bt4n0pa6BrDwCgFpKTk3HjjLmzISJT4v5fs+Xm5pY51uiia9y4cahVqxZiY2PRsGHDUq9kNEaLFi1w8uRJZGdnY9OmTQgJCUFCQsIzLdMUIiIiEB4eLk1rNBq4urrC398fKpXKjJmROZxKvQucPoZu3bqhfZO65k6HiEyI+3/Npj/TVRZGF10nT55ESkoKWrZsaexDS2VpaQlPT08AQOfOnXH06FEsXboUI0eOREFBAbKysgyOdmVkZMDZ2RkA4OzsXOIqQ/3VjcVjHr3iMSMjAyqVCtbW1pDL5ZDL5aXG6JdRGqVSCaVSWaJdoVCUuB8lVX+1atWS/ufrT1SzcP+v2Yx5zY0ep6t169a4ffu2sQ8rM51Oh/z8fHTu3BkKhQLx8fHSvAsXLiA1NRU+Pj4AAB8fH5w+fRqZmZlSTFxcHFQqFVq3bi3FFF+GPka/DEtLS3Tu3NkgRqfTIT4+XoohIiIielZGH+n69NNPMXPmTMyfPx9eXl4lKjxjTq1FRERg0KBBaNKkCe7fv48ff/wR+/btw86dO2Fvb4+JEyciPDwcdevWhUqlwttvvw0fHx9069YNAODv74/WrVvj1VdfxYIFC5Ceno4PPvgAYWFh0lGoN998E1988QVmzpyJCRMmYM+ePdiwYQO2bt0q5REeHo6QkBB06dIFXbt2xZIlS5CTk8MR9omIiKjCGF106a8EHDBggEF7eTrSZ2ZmYuzYsUhLS4O9vT3atWuHnTt3ws/PDwDw2WefwcLCAsOHD0d+fj7UajW+/PJL6fFyuRyxsbEIDQ2Fj48PbG1tERISgnnz5kkxHh4e2Lp1K6ZOnYqlS5eicePG+Pbbb6UxugBg5MiRuHXrFmbNmoX09HR06NABO3bsKNG5noiIiKi8ZEIIYcwDntbJvU+fPs+U0PNKo9HA3t4e2dnZ7EhfA5386w4CVyQjJrQbOrjVM3c6RGRC3P9rNmO+/40+0lVTiyoiIiKiZ2F00QUAWVlZ+O9//4tz584BANq0aYMJEybwhtdEREREj2H01YvHjh1Ds2bN8Nlnn+Hu3bu4e/cuFi9ejGbNmuH48eOVkSMRERHRc8/oI11Tp07FSy+9hG+++UYam6SoqAiTJk3ClClTsH///gpPkoiIiOh5Z3TRdezYMYOCC/h7QLiZM2eiS5cuFZocERERUXVh9OlFlUqF1NTUEu3Xrl1D7dq1KyQpIiIiourG6KJr5MiRmDhxItavX49r167h2rVr+OmnnzBp0iSMHj26MnIkIiIieu4ZfXpx0aJFkMlkGDt2LIqKigD8fd+h0NBQfPLJJxWeIBEREVF1YHTRZWlpiaVLlyIyMhKXL18GADRr1gw2NjYVnhwRERFRdVGucboAwMbGBl5eXhWZCxEREVG1Veaia8KECWWK+9///lfuZIiIiIiqqzIXXatXr4abmxs6duwII2/XSERERFTjlbnoCg0Nxbp163DlyhWMHz8e//znP1G3bt3KzI2IiIio2ijzkBHLly9HWloaZs6ciV9//RWurq4YMWIEdu7cySNfRERERE9h1DhdSqUSo0ePRlxcHM6ePYs2bdrgrbfegru7Ox48eFBZORIRERE994weHFV6oIUFZDIZhBDQarUVmRMRERFRtWNU0ZWfn49169bBz88PL7zwAk6fPo0vvvgCqampsLOzq6wciYiIiJ57Ze5I/9Zbb+Gnn36Cq6srJkyYgHXr1qF+/fqVmRsRERFRtVHmomvlypVo0qQJmjZtioSEBCQkJJQaFx0dXWHJEREREVUXZS66xo4dC5lMVpm5EBEREVVbRg2OSkRERETlU+6rF4mIiIio7Fh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAmW+4TVRdXQjKw/3cgqeeTmXb+VI/9eq9ey7VR1bSzRysH7m5RDR43H/J1OTCSGEuZOoDjQaDezt7ZGdnQ2VSmXudKgMbmTlof+ifcgv0pk7lRKUtSywZ3pffvASVRLu/1RRjPn+N+vpxcjISLz44ouoXbs2HB0dERgYiAsXLhjEPHz4EGFhYahXrx7s7OwwfPhwZGRkGMSkpqYiICAANjY2cHR0xIwZM1BUVGQQs2/fPnTq1AlKpRKenp5YvXp1iXyWL18Od3d3WFlZwdvbG0eOHKnwbaaq415OQZX8wAWA/CJdhfwCJ6LScf8nczBr0ZWQkICwsDAkJycjLi4OhYWF8Pf3R05OjhQzdepU/Prrr9i4cSMSEhJw8+ZNBAUFSfO1Wi0CAgJQUFCAQ4cOYc2aNVi9ejVmzZolxVy5cgUBAQHo168fTp48iSlTpmDSpEnYuXOnFLN+/XqEh4dj9uzZOH78ONq3bw+1Wo3MzEzTPBlERERUrVWp04u3bt2Co6MjEhIS0Lt3b2RnZ6NBgwb48ccfERwcDAA4f/48WrVqhaSkJHTr1g3bt2/HkCFDcPPmTTg5OQEAVq5ciXfffRe3bt2CpaUl3n33XWzduhVnzpyR1jVq1ChkZWVhx44dAABvb2+8+OKL+OKLLwAAOp0Orq6uePvtt/Hee+89NXeeXnz+nLmRjSHLDpg7jceKfbsn2jayN3caRNUS93+qKMZ8/1epjvTZ2dkAgLp16wIAUlJSUFhYCF9fXymmZcuWaNKkiVR0JSUlwcvLSyq4AECtViM0NBS///47OnbsiKSkJINl6GOmTJkCACgoKEBKSgoiIiKk+RYWFvD19UVSUlKpuebn5yM/P1+a1mg0AIDCwkIUFhY+w7NApvLoKeiqpqioiO8lokrC/Z8qijGvU5UpunQ6HaZMmYIePXqgbdu2AID09HRYWlrCwcHBINbJyQnp6elSTPGCSz9fP+9JMRqNBnl5ebh37x60Wm2pMefPny8138jISMydO7dE+65du2BjY1PGrSZzuvYAqEK7QAkHDhzAX3bmzoKoeuL+TxUlNze3zLFV5h0XFhaGM2fO4MCBqnu4t7iIiAiEh4dL0xqNBq6urvD39+fpxefE7zc1WHQ62dxpPFbPnj3RxoXvJaLKwP2fKor+TFdZVImia/LkyYiNjcX+/fvRuHFjqd3Z2RkFBQXIysoyONqVkZEBZ2dnKebRqwz1VzcWj3n0iseMjAyoVCpYW1tDLpdDLpeXGqNfxqOUSiWUSmWJdoVCAYVCUcYtJ3OqiPF0KlOtWrX4XiKqJNz/qaIY8zqZ9epFIQQmT56Mn3/+GXv27IGHh4fB/M6dO0OhUCA+Pl5qu3DhAlJTU+Hj4wMA8PHxwenTpw2uMoyLi4NKpULr1q2lmOLL0Mfol2FpaYnOnTsbxOh0OsTHx0sxRERERM/CrKV+WFgYfvzxR/zyyy+oXbu21AfL3t4e1tbWsLe3x8SJExEeHo66detCpVLh7bffho+PD7p16wYA8Pf3R+vWrfHqq69iwYIFSE9PxwcffICwsDDpSNSbb76JL774AjNnzsSECROwZ88ebNiwAVu3bpVyCQ8PR0hICLp06YKuXbtiyZIlyMnJwfjx403/xBAREVG1Y9aia8WKFQCAvn37GrSvWrUK48aNAwB89tlnsLCwwPDhw5Gfnw+1Wo0vv/xSipXL5YiNjUVoaCh8fHxga2uLkJAQzJs3T4rx8PDA1q1bMXXqVCxduhSNGzfGt99+C7VaLcWMHDkSt27dwqxZs5Ceno4OHTpgx44dJTrXExEREZVHlRqn63nGcbqePxynh6jm4v5PFeW5uQ0QERERUU3BoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJVO2bTxFVonztQ1hY3TB3Go+Vr30IgOP0EFUG7v9kDiy6qMa6mfMXbD2WmTuNx7qZ0wGdwTsiEFUG7v9kDiy6qMZysXVDzpW3zZ3GY7n0czN3CkTVFvd/MgcWXVRjKeVW0D1sZO40HksptzJ3CkTVFvd/Mgd2pCciIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAiy6iIiIiEyARRcRERGRCbDoIiKiGqeOrSWUtarmV6CylgXq2FqaOw2qBLXMnQAREZGpNXKwxp7pfXEvp+CZl3UhLRvTNp1GVLAXWjS0f+bl1bG1RCMH62deDlU9LLqIiKhGauRgXSHFTVFREQCgWQNbtG307EUXVV9V89gqkQnw9AIREZkSj3RRjcXTC0REZEosuqhG4+kFIiIylap5boWIiIiommHRRURERGQCZi269u/fj6FDh8LFxQUymQwxMTEG84UQmDVrFho2bAhra2v4+vri4sWLBjF3797FmDFjoFKp4ODggIkTJ+LBgwcGMb/99ht69eoFKysruLq6YsGCBSVy2bhxI1q2bAkrKyt4eXlh27ZtFb69REREVHOZtejKyclB+/btsXz58lLnL1iwAJ9//jlWrlyJw4cPw9bWFmq1Gg8fPpRixowZg99//x1xcXGIjY3F/v378frrr0vzNRoN/P394ebmhpSUFCxcuBBz5szB119/LcUcOnQIo0ePxsSJE3HixAkEBgYiMDAQZ86cqbyNJyIioppFVBEAxM8//yxN63Q64ezsLBYuXCi1ZWVlCaVSKdatWyeEEOLs2bMCgDh69KgUs337diGTycSNGzeEEEJ8+eWXok6dOiI/P1+Keffdd0WLFi2k6REjRoiAgACDfLy9vcUbb7xR5vyzs7MFAJGdnV3mx1D1ceLqbeH2bqw4cfW2uVMhIhPj/l+zGfP9X2WvXrxy5QrS09Ph6+srtdnb28Pb2xtJSUkYNWoUkpKS4ODggC5dukgxvr6+sLCwwOHDh/Hyyy8jKSkJvXv3hqXl/x/zSK1W49NPP8W9e/dQp04dJCUlITw83GD9arW6xOnO4vLz85Gfny9NazQaAEBhYSEKCwufdfPpOaO/erGoqIivP1ENw/2/ZjPmNa+yRVd6ejoAwMnJyaDdyclJmpeeng5HR0eD+bVq1ULdunUNYjw8PEosQz+vTp06SE9Pf+J6ShMZGYm5c+eWaN+1axdsbGzKsolUjVx7AAC1kJycjBs8K01Uo3D/r9lyc3PLHFtli66qLiIiwuDomEajgaurK/z9/aFSqcyYGZnDqdS7wOlj6NatG9o3qWvudIjIhLj/12z6M11lUWWLLmdnZwBARkYGGjZsKLVnZGSgQ4cOUkxmZqbB44qKinD37l3p8c7OzsjIyDCI0U8/LUY/vzRKpRJKpbJEu0KhgEKhKMsmUjVSq1Yt6X++/kQ1C/f/ms2Y17zKjtPl4eEBZ2dnxMfHS20ajQaHDx+Gj48PAMDHxwdZWVlISUmRYvbs2QOdTgdvb28pZv/+/QbnXOPi4tCiRQvUqVNHiim+Hn2Mfj1EREREz8qsRdeDBw9w8uRJnDx5EsDfnedPnjyJ1NRUyGQyTJkyBR9//DG2bNmC06dPY+zYsXBxcUFgYCAAoFWrVhg4cCBee+01HDlyBAcPHsTkyZMxatQouLi4AABeeeUVWFpaYuLEifj999+xfv16LF261ODU4L/+9S/s2LEDUVFROH/+PObMmYNjx45h8uTJpn5KiIiIqLoywdWUj7V3714BoMS/kJAQIcTfw0Z8+OGHwsnJSSiVSjFgwABx4cIFg2XcuXNHjB49WtjZ2QmVSiXGjx8v7t+/bxBz6tQp0bNnT6FUKkWjRo3EJ598UiKXDRs2iBdeeEFYWlqKNm3aiK1btxq1LRwyombjJeNENRf3/5rNmO9/mRBCmLHmqzY0Gg3s7e2RnZ3NjvQ10Mm/7iBwRTJiQruhg1s9c6dDRCbE/b9mM+b7v8r26SIiIiKqTlh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiIiIhNg0UVERERkAiy6iIiIiEyARRcRERGRCbDoIiIiIjIBFl1EREREJsCii4iIiMgEWHQRERERmQCLLiIiIiITYNFFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCLLqIiIiITIBFFxEREZEJsOgiIiIiMgEWXUREREQmwKKLiIiIyARYdBERERGZAIsuIiKictJqtTiWdAA5ZxNwLOkAtFqtuVOiKoxF1yOWL18Od3d3WFlZwdvbG0eOHDF3SkREVAVFR0fD09MTr40OxO1fF+K10YHw9PREdHS0uVOjKopFVzHr169HeHg4Zs+ejePHj6N9+/ZQq9XIzMw0d2pERFSFREdHIzg4GF5eXlgTvQOuUzdiTfQOeHl5ITg4mIUXlaqWuROoShYvXozXXnsN48ePBwCsXLkSW7duxf/+9z+89957Zs6OiIhMLTc3F+fPnzdo02q1ePvtt9GrVy/MmjULFzM0KLx7AwpLL8yaNQvZ2dl455134OrqCrlcXmKZLVu2hI2Njak2gaoQFl3/p6CgACkpKYiIiJDaLCws4Ovri6SkpBLx+fn5yM/Pl6Y1Gg0AoLCwEIWFhZWfMJlMbm4uLly48MSYP9KykZ9+CWdOWqIgw/6py2zRogU/dImeA2fOnIG3t3ep827evIkXX3xRmn5ljeH8rl27lvq4w4cPo2PHjhWWI5mXMd/5LLr+z+3bt6HVauHk5GTQ7uTkVOJXDgBERkZi7ty5Jdp37drFL9Nq5vLly5g2bVqZYl9d8/QYAIiKikKzZs2eISsiMoX8/HxERUUZtB0/fhxr167F/PnzoVQqUagD7j4E6loBCgvg4cOH+Pe//40xY8agU6dOJZZ59epVpKWlmWoTqJLl5uaWOZZFVzlFREQgPDxcmtZoNHB1dYW/vz9UKpUZM6OKlpubi549ez4x5kFePnYmHoW614uws1Y+dZk80kX0/EpISMDatWvRq1cveHt7o7CwEHFxcfDz84NCoUBycjIAYNy4cejTp4+Zs6XKpj/TVRYsuv5P/fr1IZfLkZGRYdCekZEBZ2fnEvFKpRJKZckvV4VCAYVCUWl5kunZ29s/9jSBXmFhIe5n3UWv7t34+hNVc/369YO7uzsWLFiAmJgYqV2hUEAul2PhwoXw8PBAv379Su3TRdWLMZ/5vHrx/1haWqJz586Ij4+X2nQ6HeLj4+Hj42PGzIiIqCqRy+WIiopCbGwsAgMDkZycjLy8PCQnJyMwMBCxsbFYtGgRCy4qgUe6igkPD0dISAi6dOmCrl27YsmSJcjJyZGuZiQiIgKAoKAgbNq0CdOmTUPv3r2ldg8PD2zatAlBQUFmzI6qKhZdxYwcORK3bt3CrFmzkJ6ejg4dOmDHjh0lOtcTEREFBQVh2LBh2Lt3L7Zv345BgwbxlCI9EYuuR0yePBmTJ082dxpERPQckMvl6NOnD3JyctCnTx8WXPRE7NNFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiIiE2DRRURERGQCHJG+ggghAAAajcbMmZA5FBYWIjc3FxqNxqg7zhPR84/7f82m/97X1wFPwqKrgty/fx8A4OrqauZMiIiIyNTu378Pe3v7J8bIRFlKM3oqnU6Hmzdvonbt2pDJZOZOh0xMo9HA1dUV165dg0qlMnc6RGRC3P9rNiEE7t+/DxcXF1hYPLnXFo90VRALCws0btzY3GmQmalUKn7oEtVQ3P9rrqcd4dJjR3oiIiIiE2DRRURERGQCLLqIKoBSqcTs2bOhVCrNnQoRmRj3fyordqQnIiIiMgEe6SIiIiIyARZdRERERCbAoouIiIjIBFh0EZnY+fPn0a1bN1hZWaFDhw7mToeoRpLJZIiJiXlizLhx4xAYGGiSfKhm4OCoRCY2e/Zs2Nra4sKFC7CzszN3OkQ13tWrV+Hh4YETJ04Y/BBaunRpme6n96zGjRuHrKyspxaB9Pxj0UVkIgUFBbC0tMTly5cREBAANzc3c6dERE9Q1lHGicqKpxeJnmDTpk3w8vKCtbU16tWrB19fX+Tk5KBv376YMmWKQWxgYCDGjRsnTbu7u+Ojjz7C2LFjoVKp8Prrr0MmkyElJQXz5s2DTCbDnDlzTLo9RDWFu7s7lixZYtDWoUOHUvc5Dw8PAEDHjh0hk8nQt29fACVPL/bt2xdvv/02pkyZgjp16sDJyQnffPMNcnJyMH78eNSuXRuenp7Yvn279BitVouJEyfCw8MD1tbWaNGiBZYuXSrNnzNnDtasWYNffvkFMpkMMpkM+/btAwBcu3YNI0aMgIODA+rWrYthw4bh6tWrFfH0kJmw6CJ6jLS0NIwePRoTJkzAuXPnsG/fPgQFBRl1umHRokVo3749Tpw4gQ8//BBpaWlo06YNpk2bhrS0NEyfPr0St4CIyuLIkSMAgN27dyMtLQ3R0dGPjV2zZg3q16+PI0eO4O2330ZoaCj+8Y9/oHv37jh+/Dj8/f3x6quvIjc3FwCg0+nQuHFjbNy4EWfPnsWsWbPw/vvvY8OGDQCA6dOnY8SIERg4cCDS0tKQlpaG7t27o7CwEGq1GrVr10ZiYiIOHjwIOzs7DBw4EAUFBZX/pFCl4OlFosdIS0tDUVERgoKCpFOBXl5eRi2jf//+mDZtmkFbrVq1YGdnB2dn5wrLlYjKr0GDBgCAevXqPXW/bN++PT744AMAQEREBD755BPUr18fr732GgBg1qxZWLFiBX777Td069YNCoUCc+fOlR7v4eGBpKQkbNiwASNGjICdnR2sra2Rn59vsO4ffvgBOp0O3377LWQyGQBg1apVcHBwwL59++Dv71+hzwGZBosuosdo3749BgwYAC8vL6jVavj7+yM4OBh16tQp8zK6dOlSiRkSkam1a9dO+lsul6NevXoGP8acnJwAAJmZmVLb8uXL8b///Q+pqanIy8tDQUHBU69cPnXqFC5duoTatWsbtD98+BCXL1+ugC0hc2DRRfQYcrkccXFxOHToEHbt2oVly5bh3//+Nw4fPgwLC4sSpxkLCwtLLMPW1tZU6RJRMWXdR42lUCgMpmUymUGb/qiUTqcDAPz000+YPn06oqKi4OPjg9q1a2PhwoU4fPjwE9fz4MEDdO7cGWvXri0xT39kjp4/LLqInkAmk6FHjx7o0aMHZs2aBTc3N/z8889o0KAB0tLSpDitVoszZ86gX79+ZsyWiPQe3Uc1Gg2uXLlSaqylpSWAv/fjinbw4EF0794db731ltT26JEqS0vLEuvu1KkT1q9fD0dHR6hUqgrPi8yDHemJHuPw4cOYP38+jh07htTUVERHR+PWrVto1aoV+vfvj61bt2Lr1q04f/48QkNDkZWVZe6Uiej/9O/fH99//z0SExNx+vRphISEQC6Xlxrr6OgIa2tr7NixAxkZGcjOzq6wPJo3b45jx45h586d+OOPP/Dhhx/i6NGjBjHu7u747bffcOHCBdy+fRuFhYUYM2YM6tevj2HDhiExMRFXrlzBvn378M477+D69esVlh+ZFosuosdQqVTYv38/Bg8ejBdeeAEffPABoqKiMGjQIEyYMAEhISEYO3Ys+vTpg6ZNm/IoF1EVEhERgT59+mDIkCEICAhAYGAgmjVrVmpsrVq18Pnnn+Orr76Ci4sLhg0bVmF5vPHGGwgKCsLIkSPh7e2NO3fuGBz1AoDXXnsNLVq0QJcuXdCgQQMcPHgQNjY22L9/P5o0aYKgoCC0atUKEydOxMOHD3nk6zkmE6YYbpeIiIiohuORLiIiIiITYNFFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbAoouIiIjIBFh0EREREZkAiy4iIiOsXr0aDg4O5k6DiJ5DLLqIiB4xbtw4yGQyyGQyWFpawtPTE/PmzUNRUZG5UyOi51gtcydARFQVDRw4EKtWrUJ+fj62bduGsLAwKBQKNGzY0NypEdFzike6iIhKoVQq4ezsDDc3N4SGhsLX1xdbtmwpEXf58mUMGzYMTk5OsLOzw4svvojdu3cbxLi7u2P+/PmYMGECateujSZNmuDrr7821aYQURXBoouIqAysra1RUFBQov3BgwcYPHgw4uPjceLECQwcOBBDhw5FamqqQVxUVBS6dOmCEydO4K233kJoaCguXLhgqvSJqApg0UVE9ARCCOzevRs7d+5E//79S8xv37493njjDbRt2xbNmzfHRx99hGbNmpU4KjZ48GC89dZb8PT0xLvvvov69etj7969ptoMIqoCWHQREZUiNjYWdnZ2sLKywqBBgzBy5EjMmTOnRNyDBw8wffp0tGrVCg4ODrCzs8O5c+dKHOlq166d9LdMJoOzszMyMzMrezOIqAphR3oiolL069cPK1asgKWlJVxcXFCrVukfl9OnT0dcXBwWLVoET09PWFtbIzg4uMSpSIVCYTAtk8mg0+kqLX8iqnpYdBERlcLW1haenp5PjTt48CDGjRuHl19+GcDfR76uXr1aydkR0fOIpxeJiJ5B8+bNER0djZMnT+LUqVN45ZVXeASLiErFoouI6BksXrwYderUQffu3TF06FCo1Wp06tTJ3GkRURUkE0IIcydBREREVN3xSBcRERGRCbDoIiIiIjIBFl1EREREJsCii4iIiMgEWHQRERERmQCLLiIiIiITYNFFREREZAIsuoiIiIhMgEUXERERkQmw6CIiIiIyARZdRERERCbw/wBWBJHqoPFWbQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "monthly_usage_with_plan = user_revenue.groupby(['user_id', 'month', 'plan'])['internet_sum'].sum().reset_index()\n",
    "\n",
    "monthly_usage_with_plan.boxplot(column='internet_sum', by='plan', grid=True, patch_artist=True)\n",
    "plt.title('Distribution of Monthly Usage by Plan')\n",
    "plt.suptitle('') \n",
    "plt.xlabel('Plan')\n",
    "plt.ylabel('Monthly Usage')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate conclusions on how the users tend to consume the internet traffic? Is their behaviour different between the plans?]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I've noticed that ultimate plan users have more internet traffic than surf plan users."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Revenue"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Likewise you have studied the user behaviour, statistically describe the revenue between the plans.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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7qefflLbtm3VsGFDffjhhypWrJjc3d0VERGR4YbwrEgf7ejevftN3/DXqFHjttspXLiw9TtgmjdvrsqVK6t169aaOXOmhg0bZt1XYGDgTWcHNL85bdOmjfLnz6/ly5erXr16Wr58uVxcXGzeRKWlpclisWjt2rU29zakSx+JSZfZMpJsRqsye7MqyeYNVfq+pX++sPVmX9T67/3b68iRIwoMDMzym9vbsfd8Zfb6s/c1nJVznhVpaWl6/PHHNWLEiEz709+I34q3t/dNv6foTvaR2fnJijp16qh8+fIaOnSoIiMj9cwzz9zRdjKTHec7u35mt9KzZ0+9++67Wr16tbp27aolS5aodevW8vPzy9L6JUuWvOXPMjMTJ07UW2+9pb59+2r8+PHy9/eXi4uLhg4dmumoryPOA3C/IiQB97nFixcrMDBQs2fPztC3atUqffXVV5o7d668vLzUsGFDFStWTMuWLVODBg30/fff64033rBZp3z58jp48KCaNm160zfjt7Ny5Up5enpq/fr18vDwsLZHRETYLFemTBmlpaUpMjLSZuTg37MzFSlSRAUKFFBqaqrdbzpupVWrVgoLC9PEiRM1cOBAeXt7q3z58tq4caPq169/2zeY3t7eat26tVasWKFp06Zp2bJleuyxx2xuri5fvrwMw1BwcHCW3iRnRfqnxXFxcTbt6Z/qm/ct/XNpYHaet3Tbt2/XiRMnsnz5UVZkx/nKjtewWZEiReTr66sjR47cdr9XrlzJkXPtyH2k69q1qyZMmKAqVarcNGSXKVNGknTs2LEMfUePHlXhwoVvO3qSmez4ud3MmTNnMoxu/f7775JkM8lEtWrVVKtWLS1evFglS5ZUdHS0Zs2alWN1SdKXX36pxo0ba/78+TbtcXFxKly4cI7uG8hruCcJuI9dvXpVq1atUuvWrfXUU09leAwZMkSXL1/W119/Lemf77B56qmntGbNGi1atEg3btywudRO+mfWqNOnT+uTTz7JdH+JiYm3rcvV1VUWi8VmZCMqKirDrGLp0wl/+OGHNu3/fiPi6uqqjh07auXKlZm+UU2fGvlO/Oc//9GFCxesx9upUyelpqZq/PjxGZa9ceNGhmDSuXNnnTlzRvPmzdPBgwcznM8OHTrI1dVVY8eOzfDprmEYunDhgt01p4cf8/0nqampGS5FDAkJUfny5fXee+9ZL4szu5vzdvLkSfXu3Vv58uXTq6++esfb+bfsOF/Z8Ro2c3FxUfv27bVmzRrt2bMnQ396nZ06ddL27du1fv36DMvExcXpxo0bdu03M47YR7pnn31Wo0eP1tSpU2+6TLFixVSzZk199tlnNr8bR44c0XfffaeWLVve0b69vb0z/K5llxs3buijjz6yPr9+/bo++ugjFSlSRCEhITbL9ujRQ999951mzJihgICAHP8SWFdX1wyv+xUrVuj06dM5ul8gL2IkCbiPff3117p8+bLatm2baX/dunWtXyyb/ua9c+fOmjVrlkaPHq3q1aurSpUqNuv06NFDy5cv13PPPafNmzerfv36Sk1N1dGjR7V8+XKtX78+05vXzVq1aqVp06bpiSee0DPPPKNz585p9uzZqlChgs29NSEhIerYsaNmzJihCxcuWKcAT/9U1/xp8uTJk7V582bVqVNH/fv3V9WqVXXx4kXt27dPGzdu1MWLF+/oHLZo0ULVqlXTtGnTNHjwYIWFhWngwIGaNGmSDhw4oGbNmsnd3V3Hjx/XihUrNHPmTD311FPW9Vu2bKkCBQpo+PDh1jBnVr58eU2YMEEjR45UVFSU2rdvrwIFCigyMlJfffWVBgwYYPMdVVnx4IMPqm7duho5cqQuXrwof39/LV26NMMbZBcXF82bN08tWrTQgw8+qD59+qhEiRI6ffq0Nm/eLF9fX61Zs+a2+9u3b58+//xzpaWlKS4uTrt379bKlStlsVi0aNGiLF3qmFXZcb6y4zX8bxMnTtR3332nsLAw67TiMTExWrFihbZu3aqCBQvq1Vdf1ddff63WrVurd+/eCgkJUWJiog4fPqwvv/xSUVFRdz0a4Ih9pCtTpkyG7yrLzLvvvqsWLVooNDRU/fr1s04B7ufnl6X1MxMSEqKNGzdq2rRpKl68uIKDg1WnTp072ta/FS9eXO+8846ioqL0wAMPaNmyZTpw4IA+/vjjDPe8PfPMMxoxYoS++uorDRo0KNMp0LNT69atNW7cOPXp00f16tXT4cOHtXjx4pt+JxuAu+Do6fQAOE6bNm0MT09PIzEx8abL9O7d23B3d7dOnZ2WlmaUKlXKkGRMmDAh03WuX79uvPPOO8aDDz5oeHh4GIUKFTJCQkKMsWPHWqd6Ngwjw/TZZvPnzzcqVqxoeHh4GJUrVzYiIiKs0/eaJSYmGoMHDzb8/f0NHx8fo3379saxY8cMScbkyZNtlj179qwxePBgo1SpUoa7u7sRFBRkNG3a1Pj4449ve67SpzfOzIIFCwxJRkREhLXt448/NkJCQgwvLy+jQIECRvXq1Y0RI0YYZ86cybB+t27dDElGeHj4Tfe/cuVKo0GDBoa3t7fh7e1tVK5c2Rg8eLBx7Ngx6zJhYWHGgw8+mGHdXr16GWXKlLFpO3HihBEeHm54eHgYRYsWNV5//XVjw4YNGabfNgzD2L9/v9GhQwcjICDA8PDwMMqUKWN06tTJ2LRp003rNYz/n0Y6/eHm5mb4+/sbderUMUaOHGmd5tzsbqcAz47zZRh3/xr+99TMhmEYJ0+eNHr27GkUKVLE8PDwMMqVK2cMHjzYZgrmy5cvGyNHjjQqVKhg5MuXzyhcuLBRr14947333rNOL30ztzoes6zsIyvTt2d2zDf7HUmX2RTghmEYGzduNOrXr294eXkZvr6+Rps2bYxff/3VZpmbvQ4ym9L+6NGjRsOGDQ0vLy9DkvVnYc82MpN+jvfs2WOEhoYanp6eRpkyZYwPPvjgpuu0bNnSkGT8/PPPt9y22a3+NpplNgX4K6+8YhQrVszw8vIy6tevb2zfvt0ICwuzmXo8/fdsxYoVNttL/7mb/5YByJzFMLh7D8C95cCBA6pVq5Y+//zzO/rSRgDILk8++aQOHz6c4V5JAPc27kkCkKtdvXo1Q9uMGTPk4uKihg0bOqEiAPhHTEyMvv32W/Xo0cPZpQDIZtyTBCBXmzJlivbu3avGjRvLzc1Na9eu1dq1azVgwIAMUzUDgCNERkZq27Ztmjdvntzd3W2+fBbA/YGQBCBXq1evnjZs2KDx48frypUrKl26tMaMGZNhanIAcJQffvhBffr0UenSpfXZZ58pKCjI2SUByGbckwQAAAAAJtyTBAAAAAAmhCQAAAAAMLnv70lKS0vTmTNnVKBAAZsvngQAAACQtxiGocuXL6t48eJycbn5eNF9H5LOnDnDDFgAAAAArE6dOqWSJUvetP++D0kFChSQ9M+J8PX1dXI1AAAAAJwlISFBpUqVsmaEm7nvQ1L6JXa+vr6EJAAAAAC3vQ2HiRsAAAAAwISQBAAAAAAmhCQAAAAAMLnv70nKqtTUVKWkpDi7DNyEu7u7XF1dnV0GAAAA8oA8H5IMw1BsbKzi4uKcXQpuo2DBggoKCuL7rgAAAJCj8nxISg9IgYGByp8/P2/AcyHDMJSUlKRz585JkooVK+bkigAAAHA/y9MhKTU11RqQAgICnF0ObsHLy0uSdO7cOQUGBnLpHQAAAHJMnp64If0epPz58zu5EmRF+s+Je8cAAACQk/J0SErHJXb3Bn5OAAAAcARCEgAAAACYEJLucWXLltWMGTOcXQYAAABw3yAkAQAAAIAJIQkAAAAATAhJuVyjRo00ZMgQDRkyRH5+fipcuLDeeustGYaR6fLTpk1T9erV5e3trVKlSun555/XlStXrP0LFixQwYIFtX79elWpUkU+Pj564oknFBMT46hDAgAAAHI1QtI94LPPPpObm5t27dqlmTNnatq0aZo3b16my7q4uOj999/XL7/8os8++0zff/+9RowYYbNMUlKS3nvvPS1atEg//vijoqOjNXz4cEccCgAAAJDr5ekvk71XlCpVStOnT5fFYlGlSpV0+PBhTZ8+Xf3798+w7NChQ63/Llu2rCZMmKDnnntOH374obU9JSVFc+fOVfny5SVJQ4YM0bhx43L8OAAAAIB7ASNJ94C6devafEdQaGiojh8/rtTU1AzLbty4UU2bNlWJEiVUoEAB9ejRQxcuXFBSUpJ1mfz581sDkiQVK1ZM586dy9mDAAAAAO4RhKT7SFRUlFq3bq0aNWpo5cqV2rt3r2bPni1Jun79unU5d3d3m/UsFstN73ECAAAA8hout7sH7Ny50+b5jh07VLFiRbm6utq07927V2lpaZo6dapcXP7Jv8uXL3dYnQAAAMD9gJB0D4iOjtawYcM0cOBA7du3T7NmzdLUqVMzLFehQgWlpKRo1qxZatOmjbZt26a5c+c6oWJkMMYvG7YRf/fbAAAAwG1xud09oGfPnrp69aoeffRRDR48WC+99JIGDBiQYbmHHnpI06ZN0zvvvKNq1app8eLFmjRpkhMqBgAAAO5dFuM+vxklISFBfn5+io+Pl6+vr03ftWvXFBkZqeDgYHl6ejqpwltr1KiRatasqRkzZji7FKe7F35eN8VIEgAAwD/u9n3RXbwnulU2MGMkCQAAAABMuCcJgGM48VMjALkEfwcA3CMISbncli1bnF0CAAAAkKdwuR0AAAAAmBCSAAAAAMCEy+0AAADgGMz2insEIQkAAEdh4gLwGgDuCVxuBwAAAAAmjCQBAByDT9ABgL+F9whGkmB19OhR1a1bV56enqpZs6azywEAAACcgpGkTJR97VuH7i9qciuH7u9mRo8eLW9vbx07dkw+Pj7OLgcAAABwCkaSoOvXr0uSTpw4oQYNGqhMmTIKCAhwclUAAACAcxCS7lFffvmlqlevLi8vLwUEBCg8PFyJiYlq1KiRhg4darNs+/bt1bt3b+vzsmXLavz48erZs6d8fX01YMAAWSwW7d27V+PGjZPFYtGYMWMcejwAAABAbuHUkFS2bFlZLJYMj8GDB0uSrl27psGDBysgIEA+Pj7q2LGjzp4968ySc4WYmBh17dpVffv21W+//aYtW7aoQ4cOMgwjy9t477339NBDD2n//v166623FBMTowcffFCvvPKKYmJiNHz48Bw8AgAAACD3cuo9Sbt371Zqaqr1+ZEjR/T444/r6aefliS9/PLL+vbbb7VixQr5+flpyJAh6tChg7Zt2+asknOFmJgY3bhxQx06dFCZMmUkSdWrV7drG02aNNErr7xi0+bm5iYfHx8FBQVlW60ATJjRCACAe4JTQ1KRIkVsnk+ePFnly5dXWFiY4uPjNX/+fC1ZskRNmjSRJEVERKhKlSrasWOH6tat64ySc4WHHnpITZs2VfXq1dW8eXM1a9ZMTz31lAoVKpTlbdSuXTsHKwQAAADuXbnmnqTr16/r888/V9++fa33x6SkpCg8PNy6TOXKlVW6dGlt3779pttJTk5WQkKCzeN+4+rqqg0bNmjt2rWqWrWqZs2apUqVKikyMlIuLi4ZLrtLSUnJsA1vb29HlQsAAADcU3LNFOCrV69WXFycdYKB2NhY5cuXTwULFrRZrmjRooqNjb3pdiZNmqSxY8fmYKU54Mz+W/cXr5WhyWKxqH79+qpfv75GjRqlMmXK6KuvvlKRIkUUExNjXS41NVVHjhxR48aNs7tq+9zuGG8nk3MAAAAA5IRcE5Lmz5+vFi1aqHjx4ne1nZEjR2rYsGHW5wkJCSpVqtTdlper7Ny5U5s2bVKzZs0UGBionTt36vz586pSpYq8vb01bNgwffvttypfvrymTZumuLg4Z5cMAAAA3DNyRUg6efKkNm7cqFWrVlnbgoKCdP36dcXFxdmMJp09e/aWEwt4eHjIw8PjrurJ9i93vdtRlH/x9fXVjz/+qBkzZighIUFlypTR1KlT1aJFC6WkpOjgwYPq2bOn3Nzc9PLLLzt/FAkAAAC4h+SKkBQREaHAwEC1avX/4SQkJETu7u7atGmTOnbsKEk6duyYoqOjFRoa6qxSc4UqVapo3bp1mfa5u7vrww8/1IcffnjT9aOiojJtP3DgQDZUBwAAANzbnB6S0tLSFBERoV69esnN7f/L8fPzU79+/TRs2DD5+/vL19dXL7zwgkJDQ/P0zHYAAAAAcpbTQ9LGjRsVHR2tvn37ZuibPn26XFxc1LFjRyUnJ6t58+a3HCEBAAAAgLvl9JDUrFmzDFNWp/P09NTs2bM1e/ZsB1cFAAAAIK/KNd+TBAAAAAC5ASEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQdB+yWCxavXr1LZfp3bu32rdv75B6AAAAgHuJ078nKVca4+fY/Q3YkmObjoqKUnBwsPbv36+aNWta22fOnHnT76fKTr1791ZcXJxWfzg6x/cFAAAAZAdCUh7l5+fgIAgAAADcI7jc7h5UtmxZzZgxw6atZs2aGjNmTIZlg4ODJUm1atWSxWJRo0aNJGW83K5Ro0Z64YUXNHToUBUqVEhFixbVJ598osTERPXp00cFChRQhQoVtHbtWus6qamp6tevn4KDg+Xl5aVKlSpp5syZ1v4xY8bos88+03//+19ZSjwsS4mHteXnPZKkU6dj1Wngf1SwSkP5P9hI7fq8rKhTZ7LnBAEAAAB3gZB0n9u1a5ckaePGjYqJidGqVatuuuxnn32mwoULa9euXXrhhRc0aNAgPf3006pXr5727dunZs2aqUePHkpKSpIkpaWlqWTJklqxYoV+/fVXjRo1Sq+//rqWL18uSRo+fLg6deqkJ554QjH7v1PM/u9Ur/ZDSklJUfNug1XAJ79+WjVf21Z/Kh/v/Hqi2xBdv56S8ycFAAAAuAVC0n2uSJEikqSAgAAFBQXJ39//pss+9NBDevPNN1WxYkWNHDlSnp6eKly4sPr376+KFStq1KhRunDhgg4dOiRJcnd319ixY1W7dm0FBwerW7du6tOnjzUk+fj4yMvLSx4eHgoKLKygwMLKl89dy77+Tmlphua9N0rVq1RUlYrlFDFtjKJPx2rL9j05f1IAAACAW+CeJFjVqFHD+m9XV1cFBASoevXq1raiRYtKks6dO2dtmz17tj799FNFR0fr6tWrun79us0EEZk5+Ovv+iPqlAo80MCm/Vpysk5E/SWFZcPBAAAAINuVfe3bu95GlGc2FJLDCEn3IBcXlwwz06Wk3P1lau7u7jbPLRaLTZvFYpH0z2V2krR06VINHz5cU6dOVWhoqAoUKKB3331XO3fuvOV+riReVUiNKlo8a0KGviIBhe72MAAAAIC7Qki6BxUpUkQxMTHW5wkJCYqMjMx02Xz58kn6Z5KF7LZt2zbVq1dPzz//vLXtxIkTGfb/730/XL2ylq35ToGF/eVbwCfb6wIAAADuBvck3YOaNGmiRYsW6aefftLhw4fVq1cvubq6ZrpsYGCgvLy8tG7dOp09e1bx8fHZVkfFihW1Z88erV+/Xr///rveeust7d6922aZsmXL6tChQzr2R5T+vnhJKSkp6tahhQoXKqh2fYbpp537FBl9Wlt+3qMX35qiv86czbb6AAAAgDvBSFJmxmRfkJAkndmfrZsbOXKkIiMj1bp1a/n5+Wn8+PE3HUlyc3PT+++/r3HjxmnUqFF67LHHtGXLlmypY+DAgdq/f786d+4si8Wirl276vnnn7eZJrx///7asmWLarfsriuJSdq84mM1qldbP66ap/+8/b46PDtclxOTVCIoUE0bPCLfAt7ZUhsAAABwpwhJ9yBfX18tXbrUpq1Xr17Wf//7fqVnn31Wzz77rE3bggULbJ5nFpyioqIytJm37eHhoYiICEVERNgsM2nSJOu/ixQpou+++y5DUAwKLKzPZo7LsH0AAADA2bjcDgAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSlHGiA+RO/JwAAADgCHk6JLm7u0uSkpKSnFwJsiL955T+cwMAAAByQp6eAtzV1VUFCxbUuXPnJEn58+eXxWLJ/h3duMsRkGvXsqcOZ7qLc2AYUtKFCzp37pwKFix40y/OBQAAALJDng5JkhQUFCRJ1qCUI+LO3936iZl/Uew95W7PQUEvFSxY0PrzAgAAAHJKng9JFotFxYoVU2BgoFJSUnJmJx88fXfrD9mTPXU4092cA8OQ+7BDjCABAADAIfJ8SErn6uqac2/Cr5y6u/U9PbOnDme623NAQAIAAICD5OmJGwAAAADg3whJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMDEzdkFAAAA4N5Q9rVv72r9KM9sKgTIYYwkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgwux0AAMgSZjYDkFcwkgQAAAAAJk4PSadPn1b37t0VEBAgLy8vVa9eXXv27LH2G4ahUaNGqVixYvLy8lJ4eLiOHz/uxIoBAAAA3M+cGpIuXbqk+vXry93dXWvXrtWvv/6qqVOnqlChQtZlpkyZovfff19z587Vzp075e3trebNm+vatWtOrBwAAADA/cqp9yS98847KlWqlCIiIqxtwcHB1n8bhqEZM2bozTffVLt27SRJCxcuVNGiRbV69Wp16dLF4TUDAAAAuL85dSTp66+/Vu3atfX0008rMDBQtWrV0ieffGLtj4yMVGxsrMLDw61tfn5+qlOnjrZv357pNpOTk5WQkGDzAAAAAICscmpI+vPPPzVnzhxVrFhR69ev16BBg/Tiiy/qs88+kyTFxsZKkooWLWqzXtGiRa19/zZp0iT5+flZH6VKlcrZgwAAAABwX3FqSEpLS9PDDz+siRMnqlatWhowYID69++vuXPn3vE2R44cqfj4eOvj1KlT2VgxAAAAgPudU0NSsWLFVLVqVZu2KlWqKDo6WpIUFBQkSTp79qzNMmfPnrX2/ZuHh4d8fX1tHgAAAACQVU6duKF+/fo6duyYTdvvv/+uMmXKSPpnEoegoCBt2rRJNWvWlCQlJCRo586dGjRokKPLBQDkcXyZKgDkDU4NSS+//LLq1auniRMnqlOnTtq1a5c+/vhjffzxx5Iki8WioUOHasKECapYsaKCg4P11ltvqXjx4mrfvr0zSwcAAABwn3JqSHrkkUf01VdfaeTIkRo3bpyCg4M1Y8YMdevWzbrMiBEjlJiYqAEDBiguLk4NGjTQunXr5OnJx3EAAAAAsp9TQ5IktW7dWq1bt75pv8Vi0bhx4zRu3DgHVgUAAAAgr3LqxA0AAAAAkNsQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAICJm7MLAAAAAO4VZV/79q7Wj/LMpkKQowhJAAAAWcQbZCBv4HI7AAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACAiVND0pgxY2SxWGwelStXtvZfu3ZNgwcPVkBAgHx8fNSxY0edPXvWiRUDAAAAuN85fSTpwQcfVExMjPWxdetWa9/LL7+sNWvWaMWKFfrhhx905swZdejQwYnVAgAAALjfuTm9ADc3BQUFZWiPj4/X/PnztWTJEjVp0kSSFBERoSpVqmjHjh2qW7euo0sFAAAAkAc4fSTp+PHjKl68uMqVK6du3bopOjpakrR3716lpKQoPDzcumzlypVVunRpbd++/abbS05OVkJCgs0DAAAAALIqW0JSXFzcHa1Xp04dLViwQOvWrdOcOXMUGRmpxx57TJcvX1ZsbKzy5cunggUL2qxTtGhRxcbG3nSbkyZNkp+fn/VRqlSpO6oNAAAAQN5kd0h65513tGzZMuvzTp06KSAgQCVKlNDBgwft2laLFi309NNPq0aNGmrevLn+97//KS4uTsuXL7e3LKuRI0cqPj7e+jh16tQdbwsAAABA3mN3SJo7d651dGbDhg3asGGD1q5dqxYtWujVV1+9q2IKFiyoBx54QH/88YeCgoJ0/fr1DKNUZ8+ezfQepnQeHh7y9fW1eQAAAABAVtkdkmJjY60h6ZtvvlGnTp3UrFkzjRgxQrt3776rYq5cuaITJ06oWLFiCgkJkbu7uzZt2mTtP3bsmKKjoxUaGnpX+wEAAACAm7E7JBUqVMh6Cdu6deusEysYhqHU1FS7tjV8+HD98MMPioqK0s8//6wnn3xSrq6u6tq1q/z8/NSvXz8NGzZMmzdv1t69e9WnTx+FhoYysx0AAACAHGP3FOAdOnTQM888o4oVK+rChQtq0aKFJGn//v2qUKGCXdv666+/1LVrV124cEFFihRRgwYNtGPHDhUpUkSSNH36dLm4uKhjx45KTk5W8+bN9eGHH9pbMgAAAABkmd0hafr06SpbtqxOnTqlKVOmyMfHR5IUExOj559/3q5tLV269Jb9np6emj17tmbPnm1vmQAAAABwR+wOSe7u7ho+fHiG9pdffjlbCgIAAAAAZ7qj70latGiRGjRooOLFi+vkyZOSpBkzZui///1vthYHAAAAAI5md0iaM2eOhg0bphYtWiguLs46WUPBggU1Y8aM7K4PAAAAABzK7pA0a9YsffLJJ3rjjTfk6upqba9du7YOHz6crcUBAAAAgKPZHZIiIyNVq1atDO0eHh5KTEzMlqIAAAAAwFnsDknBwcE6cOBAhvZ169apSpUq2VETAAAAADiN3bPbDRs2TIMHD9a1a9dkGIZ27dqlL774QpMmTdK8efNyokYAAAAAcBi7Q9Kzzz4rLy8vvfnmm0pKStIzzzyj4sWLa+bMmerSpUtO1AgAAAAADmN3SJKkbt26qVu3bkpKStKVK1cUGBiY3XUBAAAAgFPYHZIiIyN148YNVaxYUfnz51f+/PklScePH5e7u7vKli2b3TUCAAAAgMPYPXFD79699fPPP2do37lzp3r37p0dNQEAAACA09gdkvbv36/69etnaK9bt26ms94BAAAAwL3E7pBksVh0+fLlDO3x8fFKTU3NlqIAAAAAwFnsDkkNGzbUpEmTbAJRamqqJk2apAYNGmRrcQAAAADgaHZP3PDOO++oYcOGqlSpkh577DFJ0k8//aSEhAR9//332V4gAAAAADiS3SNJVatW1aFDh9SpUyedO3dOly9fVs+ePXX06FFVq1YtJ2oEAAAAAIe5o+9JKl68uCZOnJjdtQAAcrGyr317V+tHeWZTIQAA5LA7CklxcXHatWuXzp07p7S0NJu+nj17ZkthAAAAAOAMdoekNWvWqFu3brpy5Yp8fX1lsVisfRaLhZAEAAAA4J5md0h65ZVX1LdvX02cOFH58+fPiZoAINe520vNJC43AwDgXmH3xA2nT5/Wiy++SEACAAAAcF+yOyQ1b95ce/bsyYlaAAAAAMDp7L7crlWrVnr11Vf166+/qnr16nJ3d7fpb9u2bbYVBwAAAACOZndI6t+/vyRp3LhxGfosFotSU1PvvioAAAAAcBK7Q9K/p/wGAAAAgPuJ3fckmV27di276gAAAACAXMHukJSamqrx48erRIkS8vHx0Z9//ilJeuuttzR//vxsLxAAAAAAHMnukPT2229rwYIFmjJlivLly2dtr1atmubNm5etxQEAAACAo9kdkhYuXKiPP/5Y3bp1k6urq7X9oYce0tGjR7O1OAAAAABwtDv6MtkKFSpkaE9LS1NKSkq2FAUAAAAAzmJ3SKpatap++umnDO1ffvmlatWqlS1FAQAAAICz2D0F+KhRo9SrVy+dPn1aaWlpWrVqlY4dO6aFCxfqm2++yYkaAacr+9q3d7V+lGc2FQIAAIAcZ/dIUrt27bRmzRpt3LhR3t7eGjVqlH777TetWbNGjz/+eE7UCAAAAAAOY9dI0o0bNzRx4kT17dtXGzZsyKmaAAAAAMBp7BpJcnNz05QpU3Tjxo2cqgcAAAAAnMruy+2aNm2qH374ISdqAQAAAACns3vihhYtWui1117T4cOHFRISIm9vb5v+tm3bZltxAAAAAOBodoek559/XpI0bdq0DH0Wi0Wpqal3XxUAAAAAOIndISktLS0n6gAAAACAXMHue5LMrl27ll11AAAAAECuYHdISk1N1fjx41WiRAn5+Pjozz//lCS99dZbmj9/frYXCAAAAACOZHdIevvtt7VgwQJNmTJF+fLls7ZXq1ZN8+bNy9biAAAAAMDR7A5JCxcu1Mcff6xu3brJ1dXV2v7QQw/p6NGj2VocAAAAADia3SHp9OnTqlChQob2tLQ0paSkZEtRAAAAAOAsdoekqlWr6qeffsrQ/uWXX6pWrVrZUhQAAAAAOIvdU4CPGjVKvXr10unTp5WWlqZVq1bp2LFjWrhwob755pucqBEAAAAAHMbukaR27dppzZo12rhxo7y9vTVq1Cj99ttvWrNmjR5//PGcqBEAAAAAHCZLI0nvv/++BgwYIE9PT0VHR6tBgwbasGFDTtcGAAAAAA6XpZGkYcOGKSEhQZIUHBys8+fP52hRAAAAAOAsWQpJxYsX18qVK3Xy5EkZhqG//vpL0dHRmT7u1OTJk2WxWDR06FBr27Vr1zR48GAFBATIx8dHHTt21NmzZ+94HwAAAABwO1m63O7NN9/UCy+8oCFDhshiseiRRx7JsIxhGLJYLEpNTbW7iN27d+ujjz5SjRo1bNpffvllffvtt1qxYoX8/Pw0ZMgQdejQQdu2bbN7HwAAAACQFVkKSQMGDFDXrl118uRJ1ahRQxs3blRAQEC2FHDlyhV169ZNn3zyiSZMmGBtj4+P1/z587VkyRI1adJEkhQREaEqVapox44dqlu3brbsHwAAAADM7Jq4oVq1aoqIiFBoaKi8vLyypYDBgwerVatWCg8PtwlJe/fuVUpKisLDw61tlStXVunSpbV9+/abhqTk5GQlJydbn6ffSwUAAAAAWWH3xA19+/bV5cuXs2XnS5cu1b59+zRp0qQMfbGxscqXL58KFixo0160aFHFxsbedJuTJk2Sn5+f9VGqVKlsqRUAAABA3pClkaT0iRtatmxpnbjh2rVrmS5bunTpLO341KlTeumll7RhwwZ5enpmveLbGDlypIYNG2Z9npCQQFACAAAAkGVOm7hh7969OnfunB5++GFrW2pqqn788Ud98MEHWr9+va5fv664uDib0aSzZ88qKCjoptv18PCQh4dHlmoAAAAAgH9z2sQNTZs21eHDh23a+vTpo8qVK+s///mPSpUqJXd3d23atEkdO3aUJB07dkzR0dEKDQ29q30DAAAAwM1kKSRJUoECBawTN9SvX/+uR2vSt2fm7e2tgIAAa3u/fv00bNgw+fv7y9fXVy+88IJCQ0OZ2Q4AAABAjslySErXq1evnKgjU9OnT5eLi4s6duyo5ORkNW/eXB9++KHD9g8AAAAg78lSSPL399fvv/+uwoULq1ChQrJYLDdd9uLFi3dczJYtW2yee3p6avbs2Zo9e/YdbxNA9ij72rd3tX5U9s3PAgAAkKOyFJKmT5+uAgUKWP99q5AEAAAAAPeyLIUk8yV2vXv3zqlaAAAAAMDp7L4nKT4+Xhs2bFBUVJQsFovKlSunpk2bytfXNyfqAwAAAACHsiskff755xoyZIgSEhJs2v38/DR37lx17tw5W4sDAAAAAEdzyeqC+/btU58+fdS+fXvt379fV69eVVJSkvbs2aM2bdqoR48eOnjwYE7WCgAAAAA5LssjSbNmzVL79u21YMECm/aHH35YCxcuVFJSkmbOnKlPP/00u2sEAAAAAIfJ8kjStm3bNHDgwJv2P/fcc9q6dWu2FAUAAAAAzpLlkHTmzBk98MADN+1/4IEHdPr06WwpCgAAAACcJcshKSkpSZ6eN/82SA8PD127di1bigIAAAAAZ7Frdrv169fLz88v0764uLjsqAcAAAAAnMqukGT+UtnMWCyWuyoGAAAAAJwtyyEpLS0tJ+sAAAAAgFwhy/ckAQAAAEBeQEgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmdxSS4uLiNG/ePI0cOVIXL16UJO3bt0+nT5/O1uIAAAAAwNHs+p4kSTp06JDCw8Pl5+enqKgo9e/fX/7+/lq1apWio6O1cOHCnKgTAAAAABzC7pGkYcOGqXfv3jp+/Lg8PT2t7S1bttSPP/6YrcUBAAAAgKPZHZJ2796tgQMHZmgvUaKEYmNjs6UoAAAAAHAWu0OSh4eHEhISMrT//vvvKlKkSLYUBQAAAADOYndIatu2rcaNG6eUlBRJksViUXR0tP7zn/+oY8eO2V4gAAAAADiS3SFp6tSpunLligIDA3X16lWFhYWpQoUKKlCggN5+++2cqBEAAAAAHMbu2e38/Py0YcMGbd26VYcOHdKVK1f08MMPKzw8PCfqAwAAAACHsjskpWvQoIEaNGiQnbUAAAAAgNPZHZLef//9TNstFos8PT1VoUIFNWzYUK6urnddHAAAAAA4mt0hafr06Tp//rySkpJUqFAhSdKlS5eUP39++fj46Ny5cypXrpw2b96sUqVKZXvBAAAAAJCT7J64YeLEiXrkkUd0/PhxXbhwQRcuXNDvv/+uOnXqaObMmYqOjlZQUJBefvnlnKgXAAAAAHKU3SNJb775plauXKny5ctb2ypUqKD33ntPHTt21J9//qkpU6YwHTgAAACAe5LdI0kxMTG6ceNGhvYbN24oNjZWklS8eHFdvnz57qsDAAAAAAezOyQ1btxYAwcO1P79+61t+/fv16BBg9SkSRNJ0uHDhxUcHJx9VQIAAACAg9gdkubPny9/f3+FhITIw8NDHh4eql27tvz9/TV//nxJko+Pj6ZOnZrtxQIAAABATrP7nqSgoCBt2LBBR48e1e+//y5JqlSpkipVqmRdpnHjxtlXIQAAAAA40B1/mWzlypVVuXLl7KwFuVjZ1769q/WjPLOpEAAAACCH3VFI+uuvv/T1118rOjpa169ft+mbNm1athQGAAAAAM5gd0jatGmT2rZtq3Llyuno0aOqVq2aoqKiZBiGHn744ZyoEQAAAAAcxu6JG0aOHKnhw4fr8OHD8vT01MqVK3Xq1CmFhYXp6aefzokaAQAAAMBh7A5Jv/32m3r27ClJcnNz09WrV+Xj46Nx48bpnXfeyfYCAQAAAMCR7A5J3t7e1vuQihUrphMnTlj7/v777+yrDAAAAACcwO57kurWrautW7eqSpUqatmypV555RUdPnxYq1atUt26dXOiRgAAAABwGLtD0rRp03TlyhVJ0tixY3XlyhUtW7ZMFStWZGY7AAAAAPc8u0JSamqq/vrrL9WoUUPSP5fezZ07N0cKAwAAAABnsOueJFdXVzVr1kyXLl3KqXoAAAAAwKnsnrihWrVq+vPPP3OiFgAAAABwOrtD0oQJEzR8+HB98803iomJUUJCgs0DAAAAAO5ldk/c0LJlS0lS27ZtZbFYrO2GYchisSg1NTX7qgMAAAAAB7M7JG3evDkn6gAAAACAXMHukBQWFpYTdQAAAABArmD3PUmS9NNPP6l79+6qV6+eTp8+LUlatGiRtm7datd25syZoxo1asjX11e+vr4KDQ3V2rVrrf3Xrl3T4MGDFRAQIB8fH3Xs2FFnz569k5IBAAAAIEvsDkkrV65U8+bN5eXlpX379ik5OVmSFB8fr4kTJ9q1rZIlS2ry5Mnau3ev9uzZoyZNmqhdu3b65ZdfJEkvv/yy1qxZoxUrVuiHH37QmTNn1KFDB3tLBgAAAIAsu6PZ7ebOnatPPvlE7u7u1vb69etr3759dm2rTZs2atmypSpWrKgHHnhAb7/9tnx8fLRjxw7Fx8dr/vz5mjZtmpo0aaKQkBBFRETo559/1o4dO+wtGwAAAACyxO6QdOzYMTVs2DBDu5+fn+Li4u64kNTUVC1dulSJiYkKDQ3V3r17lZKSovDwcOsylStXVunSpbV9+/abbic5OZlpyQEAAADcMbtDUlBQkP74448M7Vu3blW5cuXsLuDw4cPy8fGRh4eHnnvuOX311VeqWrWqYmNjlS9fPhUsWNBm+aJFiyo2Nvam25s0aZL8/Pysj1KlStldEwAAAIC8y+6Q1L9/f7300kvauXOnLBaLzpw5o8WLF2v48OEaNGiQ3QVUqlRJBw4c0M6dOzVo0CD16tVLv/76q93bSTdy5EjFx8dbH6dOnbrjbQEAAADIe+yeAvy1115TWlqamjZtqqSkJDVs2FAeHh4aPny4XnjhBbsLyJcvnypUqCBJCgkJ0e7duzVz5kx17txZ169fV1xcnM1o0tmzZxUUFHTT7Xl4eMjDw8PuOgAAAABAuoORJIvFojfeeEMXL17UkSNHtGPHDp0/f17jx4/PloLS0tKUnJyskJAQubu7a9OmTda+Y8eOKTo6WqGhodmyLwAAAAD4N7tHkj7//HN16NBB+fPnV9WqVe9q5yNHjlSLFi1UunRpXb58WUuWLNGWLVu0fv16+fn5qV+/fho2bJj8/f3l6+urF154QaGhoapbt+5d7RcAAAAAbsbukaSXX35ZgYGBeuaZZ/S///1Pqampd7zzc+fOqWfPnqpUqZKaNm2q3bt3a/369Xr88cclSdOnT1fr1q3VsWNHNWzYUEFBQVq1atUd7w8AAAAAbsfukaSYmBitW7dOX3zxhTp16qT8+fPr6aefVrdu3VSvXj27tjV//vxb9nt6emr27NmaPXu2vWUCAAAAwB2xeyTJzc1NrVu31uLFi3Xu3DlNnz5dUVFRaty4scqXL58TNQIAAACAw9g9kmSWP39+NW/eXJcuXdLJkyf122+/ZVddAAAAAOAUdo8kSVJSUpIWL16sli1bqkSJEpoxY4aefPJJ/fLLL9ldHwAAAAA4lN0jSV26dNE333yj/Pnzq1OnTnrrrbeYkhsAAADAfcPukOTq6qrly5erefPmcnV1tek7cuSIqlWrlm3FAQAAAICj2R2SFi9ebPP88uXL+uKLLzRv3jzt3bv3rqYEBwAAAABnu6N7kiTpxx9/VK9evVSsWDG99957atKkiXbs2JGdtQEAAACAw9k1khQbG6sFCxZo/vz5SkhIUKdOnZScnKzVq1eratWqOVUjAAAAADhMlkeS2rRpo0qVKunQoUOaMWOGzpw5o1mzZuVkbQAAAADgcFkeSVq7dq1efPFFDRo0SBUrVszJmgAAAADAabI8krR161ZdvnxZISEhqlOnjj744AP9/fffOVkbAAAAADhclkNS3bp19cknnygmJkYDBw7U0qVLVbx4caWlpWnDhg26fPlyTtYJAAAAAA5h9+x23t7e6tu3r7Zu3arDhw/rlVde0eTJkxUYGKi2bdvmRI0AAAAA4DB3PAW4JFWqVElTpkzRX3/9pS+++CK7agIAAAAAp7mrkJTO1dVV7du319dff50dmwMAAAAAp8mWkAQAAAAA9wtCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJg4NSRNmjRJjzzyiAoUKKDAwEC1b99ex44ds1nm2rVrGjx4sAICAuTj46OOHTvq7NmzTqoYAAAAwP3OqSHphx9+0ODBg7Vjxw5t2LBBKSkpatasmRITE63LvPzyy1qzZo1WrFihH374QWfOnFGHDh2cWDUAAACA+5mbM3e+bt06m+cLFixQYGCg9u7dq4YNGyo+Pl7z58/XkiVL1KRJE0lSRESEqlSpoh07dqhu3brOKBsAAADAfSxX3ZMUHx8vSfL395ck7d27VykpKQoPD7cuU7lyZZUuXVrbt2/PdBvJyclKSEiweQAAAABAVjl1JMksLS1NQ4cOVf369VWtWjVJUmxsrPLly6eCBQvaLFu0aFHFxsZmup1JkyZp7Nix2Vpb2de+vav1ozyzqRAAAAAAOS7XjCQNHjxYR44c0dKlS+9qOyNHjlR8fLz1cerUqWyqEAAAAEBekCtGkoYMGaJvvvlGP/74o0qWLGltDwoK0vXr1xUXF2czmnT27FkFBQVlui0PDw95eHjkdMkAAAAA7lNOHUkyDENDhgzRV199pe+//17BwcE2/SEhIXJ3d9emTZusbceOHVN0dLRCQ0MdXS4AAACAPMCpI0mDBw/WkiVL9N///lcFChSw3mfk5+cnLy8v+fn5qV+/fho2bJj8/f3l6+urF154QaGhocxsBwAAACBHODUkzZkzR5LUqFEjm/aIiAj17t1bkjR9+nS5uLioY8eOSk5OVvPmzfXhhx86uFIAAAAAeYVTQ5JhGLddxtPTU7Nnz9bs2bMdUBEAAACAvC7XzG4HAAAAALkBIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAICJU0PSjz/+qDZt2qh48eKyWCxavXq1Tb9hGBo1apSKFSsmLy8vhYeH6/jx484pFgAAAECe4NSQlJiYqIceekizZ8/OtH/KlCl6//33NXfuXO3cuVPe3t5q3ry5rl275uBKAQAAAOQVbs7ceYsWLdSiRYtM+wzD0IwZM/Tmm2+qXbt2kqSFCxeqaNGiWr16tbp06eLIUgEAAADkEbn2nqTIyEjFxsYqPDzc2ubn56c6depo+/btN10vOTlZCQkJNg8AAAAAyKpcG5JiY2MlSUWLFrVpL1q0qLUvM5MmTZKfn5/1UapUqRytEwAAAMD9JdeGpDs1cuRIxcfHWx+nTp1ydkkAAAAA7iG5NiQFBQVJks6ePWvTfvbsWWtfZjw8POTr62vzAAAAAICsyrUhKTg4WEFBQdq0aZO1LSEhQTt37lRoaKgTKwMAAABwP3Pq7HZXrlzRH3/8YX0eGRmpAwcOyN/fX6VLl9bQoUM1YcIEVaxYUcHBwXrrrbdUvHhxtW/f3nlFAwAAALivOTUk7dmzR40bN7Y+HzZsmCSpV69eWrBggUaMGKHExEQNGDBAcXFxatCggdatWydPT09nlQwAAADgPufUkNSoUSMZhnHTfovFonHjxmncuHEOrAoAAABAXpZr70kCAAAAAGcgJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADAhJAEAAACACSEJAAAAAEwISQAAAABgQkgCAAAAABNCEgAAAACYEJIAAAAAwISQBAAAAAAmhCQAAAAAMCEkAQAAAIAJIQkAAAAATAhJAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMCEkAQAAAAAJoQkAAAAADC5J0LS7NmzVbZsWXl6eqpOnTratWuXs0sCAAAAcJ/K9SFp2bJlGjZsmEaPHq19+/bpoYceUvPmzXXu3DlnlwYAAADgPpTrQ9K0adPUv39/9enTR1WrVtXcuXOVP39+ffrpp84uDQAAAMB9yM3ZBdzK9evXtXfvXo0cOdLa5uLiovDwcG3fvj3TdZKTk5WcnGx9Hh8fL0lKSEi44zrSkpPueF1JSrAYd7W+7qL27JLXz4HTj1/iHNzjxy9xDu7145c4B3n9+CXOgdOPX+Ic3OPHLzn3HKRnAsO4dQ0W43ZLONGZM2dUokQJ/fzzzwoNDbW2jxgxQj/88IN27tyZYZ0xY8Zo7NixjiwTAAAAwD3k1KlTKlmy5E37c/VI0p0YOXKkhg0bZn2elpamixcvKiAgQBaLxeH1JCQkqFSpUjp16pR8fX0dvv/cIK+fg7x+/BLnQOIc5PXjlzgHef34Jc5BXj9+iXMgOf8cGIahy5cvq3jx4rdcLleHpMKFC8vV1VVnz561aT979qyCgoIyXcfDw0MeHh42bQULFsypErPM19c3z/4ypMvr5yCvH7/EOZA4B3n9+CXOQV4/folzkNePX+IcSM49B35+frddJldP3JAvXz6FhIRo06ZN1ra0tDRt2rTJ5vI7AAAAAMguuXokSZKGDRumXr16qXbt2nr00Uc1Y8YMJSYmqk+fPs4uDQAAAMB9KNeHpM6dO+v8+fMaNWqUYmNjVbNmTa1bt05FixZ1dmlZ4uHhodGjR2e4BDAvyevnIK8fv8Q5kDgHef34Jc5BXj9+iXOQ149f4hxI9845yNWz2wEAAACAo+Xqe5IAAAAAwNEISQAAAABgQkgCAAAAABNCEgAAAACYEJIAOARzxAAAgHtFrp8CHMD9wcPDQwcPHlSVKlWcXQoAOERMTIzmzJmjrVu3KiYmRi4uLipXrpzat2+v3r17y9XV1dklArgJRpIc7NSpU+rbt6+zy8hRV69e1datW/Xrr79m6Lt27ZoWLlzohKoc57ffflNERISOHj0qSTp69KgGDRqkvn376vvvv3dydTlv2LBhmT5SU1M1efJk6/O8JDExUREREXrjjTf0wQcf6MKFC84uKUft27dPkZGR1ueLFi1S/fr1VapUKTVo0EBLly51YnWO8cILL+inn35ydhlO9cEHH6hnz57Wn/eiRYtUtWpVVa5cWa+//rpu3Ljh5Apz1p49e1SlShX973//U0pKio4fP66QkBB5e3tr+PDhatiwoS5fvuzsMgHcjAGHOnDggOHi4uLsMnLMsWPHjDJlyhgWi8VwcXExGjZsaJw5c8baHxsbe18f/9q1a418+fIZ/v7+hqenp7F27VqjSJEiRnh4uNGkSRPD1dXV2LRpk7PLzFEWi8WoWbOm0ahRI5uHxWIxHnnkEaNRo0ZG48aNnV1mjqpSpYpx4cIFwzAMIzo62ihbtqzh5+dnPPLII4a/v78RGBho/Pnnn06uMufUqFHD2LBhg2EYhvHJJ58YXl5exosvvmjMmTPHGDp0qOHj42PMnz/fyVXmrPS/gRUrVjQmT55sxMTEOLskhxo/frxRoEABo2PHjkZQUJAxefJkIyAgwJgwYYIxceJEo0iRIsaoUaOcXWaOql+/vjFmzBjr80WLFhl16tQxDMMwLl68aNSsWdN48cUXnVWewyQnJxvLli0zhg4danTp0sXo0qWLMXToUGP58uVGcnKys8tzutjYWGPs2LHOLiPHnTp1yrh8+XKG9uvXrxs//PCDEyq6PUJSNvvvf/97y8f06dPv65DQvn17o1WrVsb58+eN48ePG61atTKCg4ONkydPGoZx/4ek0NBQ44033jAMwzC++OILo1ChQsbrr79u7X/ttdeMxx9/3FnlOcSkSZOM4ODgDGHQzc3N+OWXX5xUlWNZLBbj7NmzhmEYRrdu3Yx69eoZcXFxhmEYxuXLl43w8HCja9euziwxR3l5eRlRUVGGYRhGrVq1jI8//timf/HixUbVqlWdUZrDWCwWY+PGjcZLL71kFC5c2HB3dzfatm1rrFmzxkhNTXV2eTmufPnyxsqVKw3D+OfDQVdXV+Pzzz+39q9atcqoUKGCs8pzCC8vL+PEiRPW56mpqYa7u7sRGxtrGIZhfPfdd0bx4sWdVZ5DHD9+3ChXrpzh6elphIWFGZ06dTI6depkhIWFGZ6enkaFChWM48ePO7tMp7rfPzw/c+aM8cgjjxguLi6Gq6ur0aNHD5uwlJvfFxKSsln6p4cWi+Wmj9z6YsgOgYGBxqFDh6zP09LSjOeee84oXbq0ceLEiVz9y5AdfH19rX/wU1NTDTc3N2Pfvn3W/sOHDxtFixZ1VnkOs2vXLuOBBx4wXnnlFeP69euGYeTdkFSuXDnju+++s+nftm2bUapUKWeU5hABAQHGnj17DMP452/CgQMHbPr/+OMPw8vLyxmlOYz5NXD9+nVj2bJlRvPmzQ1XV1ejePHixuuvv35fvzn08vKyfjhmGIbh7u5uHDlyxPo8KirKyJ8/vzNKc5gyZcoYW7dutT4/c+aMYbFYjKSkJMMwDCMyMtLw9PR0VnkOER4ebrRr186Ij4/P0BcfH2+0a9fOaNasmRMqc5yDBw/e8rFs2bL7+n1Rz549jTp16hi7d+82NmzYYISEhBi1a9c2Ll68aBjGPyHJYrE4ucrMcU9SNitWrJhWrVqltLS0TB/79u1zdok56urVq3Jz+//5QCwWi+bMmaM2bdooLCxMv//+uxOrcwyLxSJJcnFxkaenp/z8/Kx9BQoUUHx8vLNKc5hHHnlEe/fu1fnz51W7dm0dOXLEel7yivTjvXbtmooVK2bTV6JECZ0/f94ZZTlEixYtNGfOHElSWFiYvvzyS5v+5cuXq0KFCs4ozSnc3d3VqVMnrVu3Tn/++af69++vxYsXq1KlSs4uLccEBQVZ70s9fvy4UlNTbe5T/eWXXxQYGOis8hyiffv2eu6557Ru3Tpt3rxZ3bp1U1hYmLy8vCRJx44dU4kSJZxcZc7atm2bJkyYIF9f3wx9vr6+Gj9+/H1/717NmjVVq1Yt1axZM8OjVq1a6tKli7NLzFEbN27U+++/r9q1ays8PFzbtm1TsWLF1KRJE128eFGScu37A2a3y2YhISHau3ev2rVrl2m/xWK5r6dCrly5svVmVbMPPvhAktS2bVtnlOUwZcuW1fHjx1W+fHlJ0vbt21W6dGlrf3R0dIY3zPcrHx8fffbZZ1q6dKnCw8OVmprq7JIcqmnTpnJzc1NCQoKOHTumatWqWftOnjypgIAAJ1aXs9555x3Vr19fYWFhql27tqZOnaotW7aoSpUqOnbsmHbs2KGvvvrK2WU6RenSpTVmzBiNHj1aGzdudHY5OaZbt27q2bOn2rVrp02bNmnEiBEaPny4Lly4IIvForfffltPPfWUs8vMURMmTFBMTIzatGmj1NRUhYaG6vPPP7f2WywWTZo0yYkV5ryCBQsqKirK5u+fWVRUlAoWLOjYohzM399fU6ZMUdOmTTPt/+WXX9SmTRsHV+U48fHxKlSokPW5h4eHVq1apaefflqNGze2+Z3IbQhJ2ezVV19VYmLiTfsrVKigzZs3O7Aix3ryySf1xRdfqEePHhn6PvjgA6WlpWnu3LlOqMwxBg0aZBMG/v0fw9q1a9WkSRNHl+VUXbp0UYMGDbR3716VKVPG2eU4xOjRo22e+/j42Dxfs2aNHnvsMUeW5FDFixfX/v37NXnyZK1Zs0aGYWjXrl06deqU6tevr23btql27drOLjNHlSlT5pbTO1ssFj3++OMOrMixxo4dKy8vL23fvl39+/fXa6+9poceekgjRoxQUlKS2rRpo/Hjxzu7zBzl4+OjZcuW6dq1a7px40aGvwPNmjVzUmWO8+yzz6pnz55666231LRpUxUtWlSSdPbsWW3atEkTJkzQCy+84OQqc1ZISIjOnDlz0///4uLi7usPz8uVK6dDhw6pYsWK1jY3NzetWLFCTz/9tFq3bu3E6m7NYtzPPxkAAAA4zTvvvKOZM2cqNjbWelmVYRgKCgrS0KFDNWLECCdXmLO++uorJSYmqnv37pn2X7p0SV9//bV69erl4Moc4z//+Y8OHDig9evXZ+i7ceOGOnbsqDVr1igtLc0J1d0aIQkAAAA5KjIyUrGxsZL+uWctODjYyRXBEW7cuKGkpKRM70tL7z99+nSuvNKEiRsAAACQo4KDgxUaGqrQ0FBrQDp16pT69u3r5Mqc634/B25ubjcNSJIUExOjsWPHOrCirGMkCQAAAA538OBBPfzww3luYh+zvH4OcvPxM3EDAAAAst3XX399y/4///zTQZU4T14/B/fy8TOSBAAAgGzn4uJy268+sVgsuXIUIbvk9XNwLx8/9yQBAAAg2xUrVkyrVq1SWlpapo99+/Y5u8Qcl9fPwb18/IQkAAAAZLuQkBDt3bv3pv23G2G4H+T1c3AvHz/3JAEAACDbvfrqq0pMTLxpf4UKFbR582YHVuR4ef0c3MvHzz1JAAAAAGDC5XYAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAC4BYvFotWrVzu7DACAAxGSAAC5Uu/evWWxWPTcc89l6Bs8eLAsFot69+6dbfsbM2aMatasmW3bAwDcuwhJAIBcq1SpUlq6dKmuXr1qbbt27ZqWLFmi0qVLO7EyAMD9jJAEAMi1Hn74YZUqVUqrVq2ytq1atUqlS5dWrVq1rG3Jycl68cUXFRgYKE9PTzVo0EC7d++29m/ZskUWi0WbNm1S7dq1lT9/ftWrV0/Hjh2TJC1YsEBjx47VwYMHZbFYZLFYtGDBAuv6f//9t5588knlz59fFStW1Ndff53zBw8AcBpCEgAgV+vbt68iIiKszz/99FP16dPHZpkRI0Zo5cqV+uyzz7Rv3z5VqFBBzZs318WLF22We+ONNzR16lTt2bNHbm5u6tu3rySpc+fOeuWVV/Tggw8qJiZGMTEx6ty5s3W9sWPHqlOnTjp06JBatmypbt26Zdg2AOD+QUgCAORq3bt319atW3Xy5EmdPHlS27ZtU/fu3a39iYmJmjNnjt599121aNFCVatW1SeffCIvLy/Nnz/fZltvv/22wsLCVLVqVb322mv6+eefde3aNXl5ecnHx0dubm4KCgpSUFCQvLy8rOv17t1bXbt2VYUKFTRx4kRduXJFu3btctg5AAA4lpuzCwAA4FaKFCmiVq1aacGCBTIMQ61atVLhwoWt/SdOnFBKSorq169vbXN3d9ejjz6q3377zWZbNWrUsP67WLFikqRz587d9v4m83re3t7y9fXVuXPn7uq4AAC5FyEJAJDr9e3bV0OGDJEkzZ49+4634+7ubv23xWKRJKWlpdm1Xvq6WVkPAHBv4nI7AECu98QTT+j69etKSUlR8+bNbfrKly+vfPnyadu2bda2lJQU7d69W1WrVs3yPvLly6fU1NRsqxkAcO9iJAkAkOu5urpaL51zdXW16fP29tagQYP06quvyt/fX6VLl9aUKVOUlJSkfv36ZXkfZcuWVWRkpA4cOKCSJUuqQIEC8vDwyNbjAADcGwhJAIB7gq+v7037Jk+erLS0NPXo0UOXL19W7dq1tX79ehUqVCjL2+/YsaNWrVqlxo0bKy4uThEREdn6ZbUAgHuHxTAMw9lFAAAAAEBuwT1JAAAAAGBCSAIAAAAAE0ISAAAAAJgQkgAAAADAhJAEAAAAACaEJAAAAAAwISQBAAAAgAkhCQAAAABMCEkAAAAAYEJIAgAAAAATQhIAAAAAmBCSAAAAAMDk/wDz2UZtAveRAAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "revenue_differences = user_revenue.groupby(['plan', 'month'])['monthly_revenue'].mean().reset_index()\n",
    "rev_dif_pivot = revenue_differences.pivot(index='month', columns='plan', values='monthly_revenue')\n",
    "rev_dif_pivot.plot(kind='bar', figsize=(10, 6))\n",
    "plt.title('Average Revenue Difference Per Month by Plan')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Average Differences')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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aChu3bqF1atXAwCioqLg6OiI1q1b48mTJ1i2bBni4+Oxa9cuqY+QkBCMHDkSHTp0QMeOHREVFYXc3FzprjAiIiIijQagY8eOoVevXtLzkJAQAMDIkSMRExOD1NRUpKSkSMvz8/MxefJk3Lp1C0ZGRmjbti327Nmj0kdAQADu3LmDmTNnIi0tDe7u7oiNjS01MZqIiIjkSyGEEJoeRG2TnZ0NMzMzZGVlVcvlsNAtZ0q1+d+cV2791sZTpZ8jBruqfTxERESvghd5/67zc4CIiIiIXhQDEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJDgMQERERyQ4DEBEREckOAxARERHJjkYD0P79+zFgwADY2tpCoVBg69atFdZv2bIFffr0gaWlJUxNTeHl5YWdO3eq1MyaNQsKhULl0aJFi2rcCyIiIqprNBqAcnNz4ebmhkWLFlWqfv/+/ejTpw+2b9+O48ePo1evXhgwYACSkpJU6lq3bo3U1FTpcfDgweoYPhEREdVROprcuJ+fH/z8/CpdHxUVpfL8888/x6+//or//e9/aNeundSuo6MDpVKprmESERHRK6ZOzwEqLi7Gw4cP0aBBA5X2y5cvw9bWFk2bNsWIESOQkpKioRESERFRbaTRM0Av6+uvv0ZOTg6GDh0qtXl6eiImJgYuLi5ITU1FeHg4unXrhrNnz8LExKTMfvLy8pCXlyc9z87OrvaxExERkebU2QC0bt06hIeH49dff4WVlZXU/vQltbZt28LT0xP29vbYuHEjRo8eXWZfERERCA8Pr/YxExERUe1QJy+BrV+/Hu+//z42btwIb2/vCmvNzc3RvHlzXLlypdya0NBQZGVlSY8bN26oe8hERERUi1QpAP3999/qHkel/fTTTwgKCsJPP/2Efv36Pbc+JycHV69ehY2NTbk1+vr6MDU1VXkQERHRq6tKAahZs2bo1asXfvzx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VSvo6+sjJSUFPXr0KHe9t99+G9OnT8fx48exefNmREdHS8vat2+PtLQ06OjowMHBocpjs7S0RGpqqvQ8OzsbycnJat9OiaioKJiamsLb2/ul+mnfvj0uXbokhczqXu9pbdu2xapVq1BQUFAqKFlbW8PW1hZ///03RowYUeVtEL1KGICIZGzIkCH4+OOPsWjRIkyZMgVTpkzBpEmTUFxcjK5duyIrKwuHDh2CqakpRo4cCeCfy1edO3fG6NGjUVRUhDfeeEPqz9vbG15eXvD398e8efPQvHlz3L59G9u2bcOgQYNKXfopz2uvvYaYmBgMGDAA5ubmmDlzpsqZipfZTmZmJtLS0pCXl4e//voLS5YswdatW7F69eoqnT162syZM9G/f380adIEb731FrS0tHDq1CmcPXsWc+fOVft6TwsODsa3336LYcOGITQ0FGZmZjh8+DA6duwIFxcXhIeH46OPPoKZmRl8fX2Rl5eHY8eO4cGDBwgJCXmp/Saqi3gXGJGM6ejoIDg4GPPmzUNubi7mzJmDGTNmICIiAi1btoSvry+2bdtW6tLQiBEjcOrUKQwaNEjl0otCocD27dvRvXt3BAUFoXnz5hg2bBiuX78Oa2vrSo8rNDQUPXr0QP/+/dGvXz/4+/vDyclJLdsJCgqCjY0NWrRogXHjxqFevXo4evQo3n777UqPrzw+Pj74/fffsWvXLvzrX/9Cp06dsGDBAukOOXWv97SGDRsiPj4eOTk56NGjBzw8PLB06VLpbND777+PZcuWYeXKlXB1dUWPHj0QExPz0pf9iOoqfhI0ERERyQ7PABEREZHsMAARERGR7DAAERERkewwABEREZHsMAARERGR7DAAERERkewwABEREZHsMAARERGR7DAAERERkewwABEREZHsMAARERGR7DAAERERkez8PyjnoNMRGLQlAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rev_diff = user_revenue.groupby(['plan','month'])['monthly_revenue'].sum().reset_index()\n",
    "for plan in rev_diff['plan'].unique():\n",
    "    plt.hist(rev_diff.loc[rev_diff['plan'] == plan, 'monthly_revenue'],\n",
    "             bins=30,\n",
    "             alpha=0.6,\n",
    "             label=plan)\n",
    "\n",
    "plt.xlabel('Revenue Difference')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Differences in Revenue by Plan')\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "rev_diff = user_revenue.groupby(['user_id', 'month'])['monthly_revenue'].sum().reset_index()\n",
    "rev_mean= rev_diff['monthly_revenue'].mean()\n",
    "rev_variance= rev_diff['monthly_revenue'].var() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "62.208008757972635"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rev_mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2070.984354577875"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rev_variance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Hhrj4uKCvXv36jo1IiIiIgCNbM4SERERUWPDYomIiIhIDRZLRERERGqwWCIiIiJSg8USERERkRosloiIiIjUYLFEREREpAaLJSIiIiI1WCwRERERqcFiiYiIiEgNFktEREREarBYIiIiIlKDxRIRERGRGiyWiIiIiNRgsURERESkBoslIiIiIjVYLBERERGpwWKJiIiISA0WS0RERERqsFgiIiIiUoPFEhEREZEaLJaIiIiI1GCxRERERKQGiyUiIiIiNVgsEREREanBYomIiIhIDRZLRERERGqwWCIiIiJSg8USERERkRosloiIiIjUYLFEREREpAaLJSIiIiI1WCwRERERqcFiiYiIiEgNFktEREREarBYIiIiIlKDxRIRERGRGiyWiIiIiNRgsURERESkBoslIiIiIjVYLBERERGpwWKJiIiISA0WS0RERERqsFgiIiIiUoPFEhEREZEaLJaIiIiI1GCxRERERKQGiyUiIiIiNRpNsbRixQpIJBLMmjVLbLt37x6mT5+OVq1awdraGiNHjkReXp7K87KzszFs2DBYWlrC0dERc+fORVVVVQNnT0RERM1VoyiWjh8/jk8++QQ9evRQaZ89ezZ++ukn7Ny5EykpKfjnn38QFhYm9isUCgwbNgyVlZU4cuQItm7dii1btmDBggUNfQhERETUTBk/zpMKCwuxa9cuXL16FXPnzoWdnR1OnToFJycntG3bVqt9lZSUYOzYsfjss8/w3nvvie1FRUX44osvsH37dgwePBgAsHnzZnTt2hUZGRnw9vbGvn378Pvvv2P//v1wcnJCz549sXTpUrzzzjtYtGgRTE1N63zNiooKVFRUiNvFxcUAALlcDrlcru2Pg5o45XvO957I8PD8N2yavu9aF0tnz56Fn58fbG1tkZWVhWnTpsHOzg5xcXHIzs7Gtm3btNrf9OnTMWzYMPj5+akUSydPnoRcLoefn5/Y1qVLF3To0AHp6enw9vZGeno6PD094eTkJMYEBgYiIiICFy5cQK9evep8zeXLl2Px4sW12vft2wdLS0ut8qfmIykpSd8pEJGe8Pw3TGVlZRrFaV0sRUZGYtKkSVi5ciVsbGzE9uDgYLz88sta7eubb77BqVOncPz48Vp9ubm5MDU1RYsWLVTanZyckJubK8bULJSU/cq+h4mOjkZkZKS4XVxcjPbt2yMg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mgVTk8BiiYiImgw3WzdsHBT72CNL165dQ8JPPwEAOnTogKd790ZpSQmsrK1x6uRJ8Z5wIcOHo3379irP1XRkyc3WTZtDoiZAIqi7k62BKC4uhq2tLYqKiiCTyfSdDj3C+RtFCPnoV32noVbCzOfQva2tvtMgogcoFArIZDKUlZU9NMbS0hLFxcWQSqUNmBnpg6af/5zgTUREBkMqlSI2NlZtTGxsLAslUsFiiYiIDEpYWBi+//57uLi4qLS7urri+++/R1hYmJ4yo8aKc5aIiMjghIWFYcSIEUhOTkZiYiKCgoIwaNAgjihRnVgsERGRQZJKpfD19UVpaSl8fX1ZKNFD8TIcERERkRosloiIiIjUYLFEREREpAaLJSIiIiI1WCwRERERqcFiiYiIiEgNFktEREREarBYIiIiIlKDxRIRERGRGiyWiIiIiNRgsURERESkBu8NR01OheIejMxv6DsNtSoU9wDY6jsNIiLSARZL1OT8U/o3rNw+0ncaav1T2hO94aTvNIiISAdYLFGT08bKBaWZM/WdhlptBrnoOwUiItIRFkvU5JhJzVF9r62+01DLTGqu7xSIiEhHOMGbiIiISA0WS0RERERqsFgiIiIiUoPFEhEREZEaLJaIiIiI1GCxRERERKQGiyUiIiIiNVgsUZPT0soUZsaN91fXzNgILa1M9Z0GERHpCBelpCanbQsLHIwaiDullWrj7t27h8ysrEfuT1FVhTNnzqBnz56QGqs/JdxcXWFurn7ByZZWpmjbwuKRr0tERE0DiyVqktq2sNCgILFFn06Pvj+bXC6Hxb1bCB78LExMTHSTIBERNRuN91oGERERUSPAYomIiIhIDRZLRERERGqwWCIiIiJSg8USERERkRrNpljasGEDXP//17q9vLxw7NgxfadEREREzUCzKJa+/fZbREZGYuHChTh16hSeeuopBAYGIj8/X9+pERERURPXLIqlmJgYTJs2DZMnT4aHhwc2bdoES0tLfPnll/pOjYiIiJq4Jr8oZWVlJU6ePIno6GixzcjICH5+fkhPT6/zORUVFaioqBC3i4uLAdxfnFAul9dvwtToKN9zvvdEhofnv2HT9H1v8sXSrVu3oFAo4OSkulKzk5MT/vjjjzqfs3z5cixevLhW+759+2BpaVkveVLjl5SUpO8UiEhPeP4bprKyMo3imnyx9Dii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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rev_diff = user_revenue.groupby(['user_id', 'month', 'plan'])['monthly_revenue'].sum().reset_index()\n",
    "\n",
    "rev_diff.boxplot(column='monthly_revenue', by='plan', grid=True, patch_artist=True)\n",
    "plt.title('Difference in Revenue by Plan')\n",
    "plt.suptitle('') \n",
    "plt.xlabel('Plan')\n",
    "plt.ylabel('Monthly Revenue')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate conclusions about how the revenue differs between the plans.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Statistically, I've noticed the Ultimate Plan produces significantly more revenue per user then the Surf Plan each month."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v1</b>\n",
    " \n",
    "Great analysis!, also each section has correct cunclusions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Test statistical hypotheses"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Test the hypothesis that the average revenue from users of the Ultimate and Surf calling plans differs.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "ultimate = user_revenue[user_revenue['plan'] == 'ultimate']['monthly_revenue']\n",
    "surf = user_revenue[user_revenue['plan'] == 'surf']['monthly_revenue']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Null Hypotheses\n",
    "There is no difference in the average monthly revenue between Ultimate and Surf plan users."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alternative Hypotheses\n",
    "There is a difference in the average monthly revenue between Ultimate and Surf plan users."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "p-value: 8.530525302626667e-24\n",
      "We reject the null hypothesis\n"
     ]
    }
   ],
   "source": [
    "# Test the hypotheses\n",
    "\n",
    "alpha=0.05\n",
    "p_val = stats.ttest_ind(ultimate, surf, equal_var=False)\n",
    "print('p-value:',p_val.pvalue)\n",
    "\n",
    "if p_val.pvalue < alpha:\n",
    "    print(\"We reject the null hypothesis\")\n",
    "else:\n",
    "    print(\"We can't reject the null hypothesis\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is a statistically significant difference in average monthly revenue between Ultimate and Surf plan users."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v1:</b> </a>\n",
    "\n",
    "Good attempt; however you must explicitly write your null hypothesis and the alternative."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v2</b>\n",
    " \n",
    "Done."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Test the hypothesis that the average revenue from users in the NY-NJ area is different from that of the users from the other regions.]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "nynj_region= user_revenue[user_revenue['city'].str.contains('New York-Newark-Jersey City, NY-NJ-PA MSA')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "other_regions= user_revenue[~user_revenue['city'].str.contains('New York-Newark-Jersey City, NY-NJ-PA MSA')]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Formulate the null and the alternative hypotheses, choose the statistical test, decide on the alpha value.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Null Hypotheses\n",
    "There is no difference in the average monthly revenue between users in the NY–NJ region and users in other regions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alternative Hypotheses\n",
    "The average monthly revenue of users in the NY–NJ region differs from that of users in other regions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "p-value: 0.020128295172528086\n",
      "We reject the null hypothesis\n"
     ]
    }
   ],
   "source": [
    "# Test the hypotheses\n",
    "\n",
    "alpha = 0.05\n",
    "nynj_revenue = nynj_region['monthly_revenue']\n",
    "other_revenue = other_regions['monthly_revenue']\n",
    "\n",
    "p_regions = stats.ttest_ind(nynj_revenue, other_revenue, equal_var=False)\n",
    "print('p-value:', p_regions.pvalue)\n",
    "if p_regions.pvalue < alpha:\n",
    "    print(\"We reject the null hypothesis\")\n",
    "else:\n",
    "    print(\"We can't reject the null hypothesis\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The average monthly revenue of users in the NY–NJ region differs from that of users in other regions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "<b>Reviewer's comment v1:</b> </a>\n",
    "\n",
    "Good attempt; however you must explicitly write your null hypothesis and the alternative."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v2</b>\n",
    " \n",
    "Done."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## General conclusion\n",
    "\n",
    "[List your important conclusions in this final section, make sure they cover all those important decisions (assumptions) that you've made and that led you to the way you processed and analyzed the data.]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data Preparation\n",
    "\n",
    "Several columns were initially stored as object datatypes, so I converted them into appropriate datetime formats to ensure accurate time-based analysis.\n",
    "\n",
    "I applied the ceil() function to round up call durations to the nearest minute, ensuring consistent and realistic billing and usage calculations."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Behavioral Insights\n",
    "\n",
    "There were no major behavioral differences between users of the two calling plans in terms of average call durations.\n",
    "\n",
    "The main behavioral difference appeared in call frequency: as total call minutes increased (approaching ~80,000), the frequency of calls among Ultimate plan users plateaued — suggesting that they are not constrained by usage limits, unlike Surf plan users.\n",
    "\n",
    "Ultimate plan users sent slightly more messages per month compared to Surf plan users.\n",
    "\n",
    "Ultimate plan users also demonstrated higher internet traffic, indicating heavier data consumption."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Revenue Insights\n",
    "\n",
    "Statistical testing showed that the Ultimate Plan produces significantly more revenue per user than the Surf Plan each month.\n",
    "\n",
    "When testing the hypothesis that average revenue differs between users in the NY–NJ area and other regions, the p-value = 0.0201, which is less than α = 0.05 → Reject the null hypothesis.\n",
    "\n",
    "Conclusion: There is a statistically significant difference in average revenue between NY–NJ users and users in other regions.\n",
    "\n",
    "When testing the hypothesis that average revenue differs between Ultimate and Surf plan users, the p-value = 8.53×10⁻²⁴, also less than α = 0.05 → Reject the null hypothesis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Overall Summary\n",
    "\n",
    "After cleaning, transforming, and analyzing the dataset:\n",
    "\n",
    "Data quality and type conversions were crucial for accurate analysis.\n",
    "\n",
    "Behaviorally, Ultimate users tend to use more data and messages but have similar calling patterns.\n",
    "\n",
    "Statistically, both regional location (NY–NJ vs. others) and plan type (Ultimate vs. Surf) have significant effects on average revenue."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"background-color: #d4edda; color: #155724; padding: 15px; border-radius: 4px; border: 1px solid #c3e6cb;\">\n",
    "\n",
    "<b>Reviewer's comment v1</b>\n",
    " \n",
    "Great conclusions!"
   ]
  }
 ],
 "metadata": {
  "ExecuteTimeLog": [
   {
    "duration": 828,
    "start_time": "2021-11-16T09:21:11.304Z"
   },
   {
    "duration": 893,
    "start_time": "2021-11-16T09:21:17.728Z"
   },
   {
    "duration": 1150,
    "start_time": "2021-11-16T09:21:29.568Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T09:24:14.495Z"
   },
   {
    "duration": 120,
    "start_time": "2021-11-16T09:24:46.630Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T09:28:27.882Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T09:29:54.281Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T09:30:45.936Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T09:31:06.300Z"
   },
   {
    "duration": 113,
    "start_time": "2021-11-16T09:31:37.208Z"
   },
   {
    "duration": 143,
    "start_time": "2021-11-16T09:31:48.656Z"
   },
   {
    "duration": 98,
    "start_time": "2021-11-16T09:31:55.678Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T09:32:08.535Z"
   },
   {
    "duration": 111,
    "start_time": "2021-11-16T09:32:10.120Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T09:32:15.732Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T09:32:29.423Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:03:03.074Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:10:01.288Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:10:46.923Z"
   },
   {
    "duration": 121,
    "start_time": "2021-11-16T10:37:46.494Z"
   },
   {
    "duration": 125,
    "start_time": "2021-11-16T10:38:20.632Z"
   },
   {
    "duration": 112,
    "start_time": "2021-11-16T10:46:53.001Z"
   },
   {
    "duration": 110,
    "start_time": "2021-11-16T10:48:25.775Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:50:18.720Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T10:50:37.649Z"
   },
   {
    "duration": 2,
    "start_time": "2021-11-16T10:50:51.884Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:51:56.237Z"
   },
   {
    "duration": 101,
    "start_time": "2021-11-16T10:53:13.791Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:55:59.186Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:56:10.751Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:56:49.038Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:56:49.174Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T10:56:49.414Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:56:49.680Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T10:56:50.370Z"
   },
   {
    "duration": 114,
    "start_time": "2021-11-16T10:59:34.518Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:01:41.201Z"
   },
   {
    "duration": 116,
    "start_time": "2021-11-16T11:01:48.754Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:02:16.685Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:02:19.479Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:02:47.067Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:02:49.353Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:03:07.835Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:03:07.953Z"
   },
   {
    "duration": 112,
    "start_time": "2021-11-16T11:07:52.072Z"
   },
   {
    "duration": 187,
    "start_time": "2021-11-16T11:09:23.468Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T11:10:01.455Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:10:05.069Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T11:10:13.376Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:10:14.434Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:10:22.853Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T11:27:29.279Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-16T11:29:08.919Z"
   },
   {
    "duration": 118,
    "start_time": "2021-11-16T11:29:46.703Z"
   },
   {
    "duration": 437,
    "start_time": "2021-11-16T11:36:02.181Z"
   },
   {
    "duration": 157,
    "start_time": "2021-11-16T11:36:14.388Z"
   },
   {
    "duration": 207,
    "start_time": "2021-11-16T11:47:15.898Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:53:52.092Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:53:52.236Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T11:59:12.005Z"
   },
   {
    "duration": 112,
    "start_time": "2021-11-16T12:00:33.446Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T12:02:14.453Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-16T12:02:39.512Z"
   },
   {
    "duration": 106,
    "start_time": "2021-11-16T12:03:03.460Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:37:21.139Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:37:22.229Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:38:38.806Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:38:41.958Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:43:46.551Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T20:58:21.835Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T20:59:21.872Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T20:59:45.352Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T20:59:49.646Z"
   },
   {
    "duration": 159,
    "start_time": "2021-11-17T21:02:26.949Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:03:53.461Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:03:53.694Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:05:28.145Z"
   },
   {
    "duration": 116,
    "start_time": "2021-11-17T21:05:57.787Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:06:37.993Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:06:38.261Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:11:54.358Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:12:43.846Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:13:08.773Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:14:44.441Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:15:42.059Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:15:51.995Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:15:53.923Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:15:55.282Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:16:28.492Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:16:32.603Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:17:06.941Z"
   },
   {
    "duration": 98,
    "start_time": "2021-11-17T21:18:05.733Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:21:35.255Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:21:37.804Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:23:06.071Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:23:24.799Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:23:32.591Z"
   },
   {
    "duration": 98,
    "start_time": "2021-11-17T21:28:31.559Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:28:45.448Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:29:17.303Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:29:29.617Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:29:32.681Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:36:11.474Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:36:14.791Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:36:53.943Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:36:56.165Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:37:16.590Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:37:22.702Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:38:03.479Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:38:08.601Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:38:12.928Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:38:48.896Z"
   },
   {
    "duration": 2,
    "start_time": "2021-11-17T21:38:49.171Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:39:57.889Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:39:58.057Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:41:20.108Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:41:20.629Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:42:49.136Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:43:15.137Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:43:16.766Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:43:31.711Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:43:36.312Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:45:08.825Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:45:10.119Z"
   },
   {
    "duration": 4,
    "start_time": "2021-11-17T21:45:13.748Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:45:22.219Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:45:33.412Z"
   },
   {
    "duration": 2,
    "start_time": "2021-11-17T21:46:01.885Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-17T21:46:03.628Z"
   },
   {
    "duration": 107,
    "start_time": "2021-11-17T21:47:32.512Z"
   },
   {
    "duration": 103,
    "start_time": "2021-11-17T21:50:36.243Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-18T06:28:31.440Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-18T06:29:00.168Z"
   },
   {
    "duration": 3,
    "start_time": "2021-11-18T06:31:27.008Z"
   },
   {
    "duration": 2,
    "start_time": "2021-11-18T06:35:34.288Z"
   },
   {
    "duration": 2,
    "start_time": "2021-11-18T06:38:04.527Z"
   }
  ],
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.23"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

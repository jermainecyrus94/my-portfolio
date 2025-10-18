{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"border: solid blue 2px; padding: 15px; margin: 10px\">\n",
    "  <b>Overall Summary of the Project – Iteration 2</b><br><br>\n",
    "\n",
    "  Hi Jermaine, I’m <b>Victor Camargo</b> (<a href=\"https://hub.tripleten.com/u/e9cc9c11\" target=\"_blank\">TripleTen Hub profile</a>). Thank you for addressing all the issues from the previous iteration.<br><br>\n",
    "\n",
    "  Your project now meets the requirements and the implementation is clear, well-structured, and correct. Great job overall — approved.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style=\"border: solid blue 2px; padding: 15px; margin: 10px\">\n",
    "  <b>Overall Summary of the Project – Iteration 1</b><br><br>\n",
    "\n",
    "  Hi Jermaine, I’m <b>Victor Camargo</b> (<a href=\"https://hub.tripleten.com/u/e9cc9c11\" target=\"_blank\">TripleTen Hub profile</a>). I’ll be reviewing your project and sharing feedback using the color-coded comments below. Thanks for submitting your work!<br><br>\n",
    "\n",
    "  <b>Nice work on:</b><br>\n",
    "  ✔️ Correctly importing the dataset and inspecting its structure<br>\n",
    "  ✔️ Cleaning and standardizing column names for consistency<br>\n",
    "  ✔️ Building clear, reusable functions to filter and categorize data<br>\n",
    "  ✔️ Demonstrating good practices like verifying corrections after cleaning<br><br>\n",
    "\n",
    "  A few things still need your attention before approval:<br>\n",
    "  🔴 In your <code>get_top_movies_from_decade()</code> function, you overwrite the decade filter when applying the IMDb score filter. You should apply the score filter on the already decade-filtered subset instead of resetting to <code>df</code>.<br><br>\n",
    "\n",
    "  <hr>\n",
    "\n",
    "  🔹 <b>Legend:</b><br>\n",
    "  🟢 Green = well done<br>\n",
    "  🟡 Yellow = suggestions<br>\n",
    "  🔴 Red = must fix<br>\n",
    "  🔵 Blue = your comments or questions<br><br>\n",
    "  \n",
    "  <b>Please ensure</b> that all cells run smoothly from top to bottom and display their outputs before submitting — this helps keep your analysis easy to follow.  \n",
    "  <b>Kind reminder:</b> try not to move, change, or delete reviewer comments, as they are there to track progress and provide better support during your revisions.<br><br>\n",
    "\n",
    "  <b>Feel free to reach out if you need help in Questions channel.</b><br>\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JKIIqy01lgHq"
   },
   "source": [
    "# Project: Data Analysis with Pandas\n",
    "\n",
    "In this project, you will work with a dataset containing information about movies and shows. You will use the pandas library to read, clean, and analyze the data. This project will help you practice working with DataFrames, indexing, and data manipulation using pandas.\n",
    "\n",
    "\n",
    "## Dataset Description\n",
    "\n",
    "The dataset `movies_and_shows.csv` contains information about various movies and shows, including:\n",
    "\n",
    "- **name**: The name of the actor or actress.\n",
    "- **Character**: The character they played.\n",
    "- **r0le**: The role type (e.g., ACTOR).\n",
    "- **TITLE**: The title of the movie or show.\n",
    "- **Type**: Whether it's a MOVIE or SHOW.\n",
    "- **release Year**: The year it was released.\n",
    "- **genres**: A list of genres the movie or show belongs to.\n",
    "- **imdb sc0re**: The IMDb score of the movie or show.\n",
    "- **imdb v0tes**: The number of votes on IMDb.\n",
    "\n",
    "Here's a small sample of the dataset:\n",
    "\n",
    "| name              | Character                         | r0le   | TITLE        |  Type | release Year | genres             | imdb sc0re | imdb v0tes |\n",
    "|-------------------|-----------------------------------|--------|--------------|-------|--------------|--------------------|------------|------------|\n",
    "| Robert De Niro    | Travis Bickle                     | ACTOR  | Taxi Driver  | MOVIE | 1976         | ['drama', 'crime'] | 8.2        | 808582     |\n",
    "| Jodie Foster      | Iris Steensma                     | ACTOR  | Taxi Driver  | MOVIE | 1976         | ['drama', 'crime'] | 8.2        | 808582     |\n",
    "| Albert Brooks     | Tom                               | ACTOR  | Taxi Driver  | MOVIE | 1976         | ['drama', 'crime'] | 8.2        | 808582     |\n",
    "| Harvey Keitel     | Matthew 'Sport' Higgins           | ACTOR  | Taxi Driver  | MOVIE | 1976         | ['drama', 'crime'] | 8.2        | 808582     |\n",
    "| Cybill Shepherd   | Betsy                             | ACTOR  | Taxi Driver  | MOVIE | 1976         | ['drama', 'crime'] | 8.2        | 808582     |\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "csnpkGaRlkVj"
   },
   "source": [
    "## Getting Started\n",
    "\n",
    "Let's begin by setting up our environment.\n",
    "\n",
    "### Importing Libraries\n",
    "\n",
    "First, we need to import the necessary libraries.\n",
    "\n",
    "**Instructions:**\n",
    "\n",
    "- Import the `pandas` library, which we will use for data manipulation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "xVSzQhyjlg2F"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "#Import the pandas library as 'pd'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "C2Ks4kU9lsH7"
   },
   "source": [
    "We will load the dataset into a pandas DataFrame to begin our analysis.\n",
    "\n",
    "**Instructions:**\n",
    "\n",
    "- Read the `movies_and_shows.csv` file into a DataFrame. It is in the /datasets directory so the full path to include in the read_csv method will be \"/datasets/movies_and_shows.csv\"\n",
    "- Display the first few rows of the DataFrame to get an initial look at the data.\n",
    "\n",
    "**Hints:**\n",
    "\n",
    "- Use `pd.read_csv()` to read the CSV file and store it in a variable called \"df\".\n",
    "- Use the `.head()` method to display the first few rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "afwv-RRIlwcF"
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('/datasets/movies_and_shows.csv')  # Read the dataset into a DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "iHI5NhB6mYel"
   },
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
       "      <th>name</th>\n",
       "      <th>Character</th>\n",
       "      <th>r0le</th>\n",
       "      <th>TITLE</th>\n",
       "      <th>Type</th>\n",
       "      <th>release Year</th>\n",
       "      <th>genres</th>\n",
       "      <th>imdb sc0re</th>\n",
       "      <th>imdb v0tes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Robert De Niro</td>\n",
       "      <td>Travis Bickle</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Taxi Driver</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>1976</td>\n",
       "      <td>['drama', 'crime']</td>\n",
       "      <td>8.2</td>\n",
       "      <td>808582.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Jodie Foster</td>\n",
       "      <td>Iris Steensma</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Taxi Driver</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>1976</td>\n",
       "      <td>['drama', 'crime']</td>\n",
       "      <td>8.2</td>\n",
       "      <td>808582.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Albert Brooks</td>\n",
       "      <td>Tom</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Taxi Driver</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>1976</td>\n",
       "      <td>['drama', 'crime']</td>\n",
       "      <td>8.2</td>\n",
       "      <td>808582.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             name      Character   r0le        TITLE   Type  release Year  \\\n",
       "0  Robert De Niro  Travis Bickle  ACTOR  Taxi Driver  MOVIE          1976   \n",
       "1    Jodie Foster  Iris Steensma  ACTOR  Taxi Driver  MOVIE          1976   \n",
       "2   Albert Brooks            Tom  ACTOR  Taxi Driver  MOVIE          1976   \n",
       "\n",
       "               genres  imdb sc0re  imdb v0tes  \n",
       "0  ['drama', 'crime']         8.2    808582.0  \n",
       "1  ['drama', 'crime']         8.2    808582.0  \n",
       "2  ['drama', 'crime']         8.2    808582.0  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display the first few rows of the DataFrame\n",
    "df.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "otEIbWKZmmaT"
   },
   "source": [
    "Understanding the structure and content of your data is crucial before performing any analysis.\n",
    "\n",
    "**Instructions:**\n",
    "\n",
    "- Use the `.info()` method to get information about the DataFrame.\n",
    "- Identify any issues with the Column names."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "v7Oa8Zuzmjo1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 85579 entries, 0 to 85578\n",
      "Data columns (total 9 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0      name       85579 non-null  object \n",
      " 1   Character     85579 non-null  object \n",
      " 2   r0le          85579 non-null  object \n",
      " 3   TITLE         85578 non-null  object \n",
      " 4     Type        85579 non-null  object \n",
      " 5   release Year  85579 non-null  int64  \n",
      " 6   genres        85579 non-null  object \n",
      " 7   imdb sc0re    80970 non-null  float64\n",
      " 8   imdb v0tes    80853 non-null  float64\n",
      "dtypes: float64(2), int64(1), object(6)\n",
      "memory usage: 5.9+ MB\n"
     ]
    }
   ],
   "source": [
    "# Get information about the DataFrame and print the column names\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Excellent start! You correctly imported the pandas library, loaded the dataset, and displayed the first rows with <code>head()</code>. Also, using <code>df.info()</code> to check data structure and column names is a great practice for understanding your dataset early on.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "_rsPAidUm3lS"
   },
   "source": [
    "## Task 1: Data Cleaning\n",
    "\n",
    "Let's clean the data to fix issues with the column names\n",
    "\n",
    "**Instructions:**\n",
    "- Rename the columns to correct any errors and make them consistent.\n",
    "\n",
    "**Hints:**\n",
    "\n",
    "- Use the `.rename()` method to rename columns.\n",
    "- Pass a dictionary to the `columns` parameter of `.rename()`, where the keys are the old column names and the values are the new names.\n",
    "- Remove unnecessary whitespace from the column names."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['   name', 'Character', 'r0le', 'TITLE', '  Type', 'release Year',\n",
       "       'genres', 'imdb sc0re', 'imdb v0tes'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "FkIUzgKPm4Rz"
   },
   "outputs": [],
   "source": [
    "# Rename columns to make them consistent and correct errors\n",
    "df.columns = df.columns.str.strip().str.lower().str.replace('0','o').str.replace(' ','_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "cHi0aQgunByj"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['name', 'character', 'role', 'title', 'type', 'release_year', 'genres',\n",
       "       'imdb_score', 'imdb_votes'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the updated column names to confirm changes\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Great job cleaning and standardizing the column names. Using <code>str.strip()</code>, <code>str.lower()</code>, <code>str.replace()</code>, and underscores ensures consistent formatting and prevents potential errors when referencing columns later in the analysis.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "z6ShKY5boqj1"
   },
   "source": [
    "## Task 2: Correcting a Misspelled Name in the Data\n",
    "\n",
    "While analyzing the dataset, you notice that some names are misspelled or contain special characters due to encoding issues. Accurate data is essential for reporting and recommendations, so let’s correct one of these entries.\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Locate the Row with the Incorrect Name**:\n",
    "   - Use `.loc[]` to retrieve the row where `name` is `\"In??s Prieto\"`.\n",
    "   - You can locate a row based on the index (85576) and column name called \"name\".\n",
    "   - Print the row to verify that you have the correct one.\n",
    "\n",
    "\n",
    "2. **Correct the Name**:\n",
    "   - Using `.loc[]`, update the `name` column for this row to \"Ines Prieto.\"\n",
    "   \n",
    "3. **Verify the Correction**:\n",
    "   - Print the row again to ensure that the name has been corrected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "JeEDNCYsoo0z"
   },
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
       "      <th>name</th>\n",
       "      <th>character</th>\n",
       "      <th>role</th>\n",
       "      <th>title</th>\n",
       "      <th>type</th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>imdb_score</th>\n",
       "      <th>imdb_votes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>77798</th>\n",
       "      <td>In??s Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85576</th>\n",
       "      <td>In??s Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>the movie</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               name character   role    title       type  release_year  \\\n",
       "77798  In??s Prieto     Fanny  ACTOR  Lokillo      MOVIE          2021   \n",
       "85576  In??s Prieto     Fanny  ACTOR  Lokillo  the movie          2021   \n",
       "\n",
       "           genres  imdb_score  imdb_votes  \n",
       "77798  ['comedy']         3.8        68.0  \n",
       "85576  ['comedy']         3.8        68.0  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Locate the row with the incorrect name\n",
    "df[df['name']=='In??s Prieto']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#df = df.replace({\"In??s Prieto\" :\"Ines Prieto\"})\n",
    "df.loc[df['name']=='In??s Prieto',\"name\"]='Ines Prieto'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "IgEGbcNVqLnU"
   },
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
       "      <th>name</th>\n",
       "      <th>character</th>\n",
       "      <th>role</th>\n",
       "      <th>title</th>\n",
       "      <th>type</th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>imdb_score</th>\n",
       "      <th>imdb_votes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [name, character, role, title, type, release_year, genres, imdb_score, imdb_votes]\n",
       "Index: []"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['name']=='In??s Prieto']# Verify the correction\n"
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
       "      <th>name</th>\n",
       "      <th>character</th>\n",
       "      <th>role</th>\n",
       "      <th>title</th>\n",
       "      <th>type</th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>imdb_score</th>\n",
       "      <th>imdb_votes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>77798</th>\n",
       "      <td>Ines Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85576</th>\n",
       "      <td>Ines Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>the movie</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              name character   role    title       type  release_year  \\\n",
       "77798  Ines Prieto     Fanny  ACTOR  Lokillo      MOVIE          2021   \n",
       "85576  Ines Prieto     Fanny  ACTOR  Lokillo  the movie          2021   \n",
       "\n",
       "           genres  imdb_score  imdb_votes  \n",
       "77798  ['comedy']         3.8        68.0  \n",
       "85576  ['comedy']         3.8        68.0  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['name']=='Ines Prieto']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Well done identifying and correcting the inconsistent name entry. Using <code>df.loc[]</code> to replace the incorrect value and then verifying both the old and new entries shows good attention to detail and ensures data quality.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vLIvSF0hsYpE"
   },
   "source": [
    "## Task 3: Finding All Movies and Shows Featuring Ines Prieto\n",
    "\n",
    "Now that we've corrected the spelling of \"Ines Prieto\" in the dataset, let's find all the TV shows and movies she has acted in. This type of filtering is helpful for generating actor-specific profiles or building a list of their works.\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Filter by Actor’s Name**:\n",
    "   - Use a filtering condition to select rows where the `name` column is equal to `\"Ines Prieto\"`.\n",
    "   \n",
    "2. **Display Relevant Columns**:\n",
    "   - From each matching row, retrieve only the `title`, `release_year`, `imdb_score`, and `genres` columns for a clear, concise output.\n",
    "\n",
    "**Hint:**\n",
    "\n",
    "To filter rows based on a specific value in a column, use a condition inside df[ ... ]. In this case, check if the name column equals \"Ines Prieto\". Then, select only the columns you need (like title, release_year, imdb_score, and genres) by specifying them in double brackets [ [ ... ] ].\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
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
       "      <th>name</th>\n",
       "      <th>character</th>\n",
       "      <th>role</th>\n",
       "      <th>title</th>\n",
       "      <th>type</th>\n",
       "      <th>release_year</th>\n",
       "      <th>genres</th>\n",
       "      <th>imdb_score</th>\n",
       "      <th>imdb_votes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>77798</th>\n",
       "      <td>Ines Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>MOVIE</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85576</th>\n",
       "      <td>Ines Prieto</td>\n",
       "      <td>Fanny</td>\n",
       "      <td>ACTOR</td>\n",
       "      <td>Lokillo</td>\n",
       "      <td>the movie</td>\n",
       "      <td>2021</td>\n",
       "      <td>['comedy']</td>\n",
       "      <td>3.8</td>\n",
       "      <td>68.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              name character   role    title       type  release_year  \\\n",
       "77798  Ines Prieto     Fanny  ACTOR  Lokillo      MOVIE          2021   \n",
       "85576  Ines Prieto     Fanny  ACTOR  Lokillo  the movie          2021   \n",
       "\n",
       "           genres  imdb_score  imdb_votes  \n",
       "77798  ['comedy']         3.8        68.0  \n",
       "85576  ['comedy']         3.8        68.0  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['name']=='Ines Prieto']"
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
       "      <th>title</th>\n",
       "      <th>release_year</th>\n",
       "      <th>imdb_score</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>77798</th>\n",
       "      <td>Lokillo</td>\n",
       "      <td>2021</td>\n",
       "      <td>3.8</td>\n",
       "      <td>['comedy']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85576</th>\n",
       "      <td>Lokillo</td>\n",
       "      <td>2021</td>\n",
       "      <td>3.8</td>\n",
       "      <td>['comedy']</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         title  release_year  imdb_score      genres\n",
       "77798  Lokillo          2021         3.8  ['comedy']\n",
       "85576  Lokillo          2021         3.8  ['comedy']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['name']=='Ines Prieto',['title','release_year','imdb_score','genres']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Nice work filtering the DataFrame to check specific records after the correction. Selecting particular columns like <code>title</code>, <code>release_year</code>, <code>imdb_score</code>, and <code>genres</code> helps focus on the most relevant information for your analysis.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "eksJ9sXXr1UU"
   },
   "outputs": [],
   "source": [
    "# Filter rows where the actor's name is \"Ines Prieto\" and display the title, release_year, genres, and imdb_score\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "vYrm6MhERlZc"
   },
   "outputs": [],
   "source": [
    "# Display the result\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "HtmXfQHHutNk"
   },
   "source": [
    "## Task 4: Finding Highly Rated Movies\n",
    "\n",
    "We want to identify movies with an IMDb rating of at least **9.0**. This list could be helpful for curating a \"Top Movies\" section based on high ratings.\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Filter for High IMDb Scores**:\n",
    "   - First, filter the DataFrame to include only rows where the `imdb_score` is greater than 9.0.\n",
    "\n",
    "2. **Extract the Titles**:\n",
    "   - From this filtered DataFrame, select only the `title` column, which contains the names of the movies.\n",
    "\n",
    "3. **Get Unique Titles**:\n",
    "   - Convert the resulting list of titles to a set to remove any duplicate titles. Using `set()` will keep only unique movie names.\n",
    "\n",
    "   - *Example*: `unique_titles = set(high_score_titles)`\n",
    "\n",
    "4. **Print the Unique Titles**:\n",
    "   - Display the final set of unique movie titles to see the list of top-rated movies.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "B_smQ3cAtAXk"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Kota Factory', 'Breaking Bad', 'My Mister', 'Reply 1988', 'Major', 'The Last Dance', 'Avatar: The Last Airbender', 'Our Planet'}\n"
     ]
    }
   ],
   "source": [
    "goodmovies = df[df.imdb_score>9]# Filter for movies with an IMDb score above 9.0\n",
    "\n",
    "\n",
    "goodmovies = goodmovies['title']# Extract the 'title' column from the filtered DataFrame\n",
    "\n",
    "\n",
    "goodmovies = set(goodmovies)# Get a unique set of titles\n",
    "\n",
    "\n",
    "print(goodmovies)# Print the unique titles\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Great approach to filtering and isolating high-rated titles. Converting the filtered results into a set ensures uniqueness, and printing them provides a clear overview of which movies scored above 9. This is a clean and efficient workflow.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PrlORh6mwoZs"
   },
   "source": [
    "## Task 5: Creating a Function to Find Unique Top-Rated Movies\n",
    "\n",
    "In this task, we’ll create a function to find unique movies with an IMDb score above a certain threshold that the user provides.\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Define the Function**:\n",
    "   - Start by creating a function called `get_unique_top_movies` that takes one parameter, `min_score`.\n",
    "\n",
    "2. **Filter the Data**:\n",
    "   - Inside the function, create a new variable (e.g., `high_score_df`) that stores rows where the `imdb_score` is greater than or equal to `min_score`.\n",
    "\n",
    "3. **Extract Movie Titles**:\n",
    "   - In a new variable (e.g., `high_score_titles`), select the `title` column from the filtered DataFrame.\n",
    "\n",
    "4. **Remove Duplicate Titles**:\n",
    "   - Convert `high_score_titles` to a set using `set(high_score_titles)` to automatically remove duplicates, ensuring each title appears only once.\n",
    "\n",
    "5. **Return the Unique Titles**:\n",
    "   - Make sure the function returns the `unique_titles` set.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "pamLDfY9vErT"
   },
   "outputs": [],
   "source": [
    "# Define the function\n",
    "def get_unique_top_movies(min_score):\n",
    "    goodmovies= df[df.imdb_score>min_score] # Filter for movies with IMDb score above min_score\n",
    "\n",
    "\n",
    "    goodmovies= goodmovies['title']# Extract the 'title' column\n",
    "\n",
    "\n",
    "    goodmovies= set(goodmovies) # Remove duplicate titles\n",
    "\n",
    "\n",
    "    return goodmovies# Return unique titles\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "kUUJMTWgww1E"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Kota Factory', 'Breaking Bad', 'My Mister', 'Reply 1988', 'Major', 'The Last Dance', 'Avatar: The Last Airbender', 'Our Planet'}\n"
     ]
    }
   ],
   "source": [
    "# Test the function\n",
    "print(get_unique_top_movies(9.0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Excellent use of a reusable function. Wrapping the filtering logic into <code>get_unique_top_movies()</code> makes the code more flexible and maintainable. Testing it with a threshold of 9.0 also confirms it works as intended.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "YvWTywMQxynt"
   },
   "source": [
    "## Task 6: Creating a Function to Find Top Movies from a Specific Decade\n",
    "\n",
    "Let’s create a function to retrieve movies from a particular decade with high IMDb ratings. This function can be useful for generating lists of top-rated movies from different time periods.\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Define the Function**:\n",
    "   - Create a function called `get_top_movies_from_decade` that accepts `decade_start` and `min_score` as parameters.\n",
    "\n",
    "2. **Filter by Decade**:\n",
    "   - Inside the function, filter the DataFrame to include only movies where `release_year` is within the specified decade.\n",
    "   - *Hint*: You can achieve this by checking that `release_year` is between `decade_start` and `decade_start + 9`\n",
    "\n",
    "3. **Filter by IMDb Score**:\n",
    "   - Further filter this subset to include only movies where `imdb_score` is greater than or equal to `min_score`.\n",
    "\n",
    "4. **Extract Movie Titles**:\n",
    "   - From the resulting DataFrame, select the `title` column and remove duplicates using set().\n",
    "\n",
    "5. **Return the List of Titles**:\n",
    "   - Return the set of the best movies from that decade.\n",
    "\n",
    "By completing this task, you’ll have a function that returns unique, top-rated movies from a specified decade. This is useful for highlighting standout movies from different eras, perfect for “Best of the Decade” features!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "H6pJpElgxxtT"
   },
   "outputs": [],
   "source": [
    "# Define the function\n",
    "def get_top_movies_from_decade(decade_start, min_score):\n",
    "    # Filter for movies released within the decade\n",
    "    goodmovies= df[(df['release_year']>= decade_start)&(df['release_year']<= decade_start+9)]\n",
    "    \n",
    "\n",
    "    # Further filter by IMDb score\n",
    "    goodmovies= goodmovies[(goodmovies.imdb_score >= min_score)]\n",
    "\n",
    "    # Extract and remove duplicate titles\n",
    "    goodmovies= set(goodmovies['title'])\n",
    "    # Return unique titles\n",
    "    return goodmovies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "id": "r_q7imodyIbz"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'GoodFellas', 'One Piece', 'Se7en', 'Neon Genesis Evangelion', 'Cowboy Bebop', 'Bill Hicks: Revelations', 'Forrest Gump', 'L??on: The Professional'}\n"
     ]
    }
   ],
   "source": [
    "# Test the function\n",
    "print(get_top_movies_from_decade(1990, 8.5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-danger\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  You have done a great work so far, but there is a logical issue in this function. After filtering by release year, you overwrite the DataFrame with a new filter on <code>imdb_score</code> using <code>df</code> again instead of applying it to the already decade-filtered subset. This means the decade filter is ignored, and you only get titles filtered by score.  \n",
    "\n",
    "  To fix this, make sure to apply the second filter on the subset (e.g., <code>goodmovies = goodmovies[goodmovies.imdb_score >= min_score]</code>) so both conditions are respected.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5olBh5JRzYgN"
   },
   "source": [
    "\n",
    "## Task 7: Creating a Function to List All Actors in a Given Title\n",
    "\n",
    "Imagine you want to list all the actors in a specific movie or show. Let’s create a function that takes a `title` as input and returns the names of all actors in that title, combined into a single string.\n",
    "\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Define the Function**:\n",
    "   - Create a function called `get_actors_for_title` that accepts one parameter, `title`.\n",
    "   \n",
    "2. **Filter by Title and Role**:\n",
    "   - Inside the function, filter the DataFrame to select rows where the `title` column matches the provided `title` parameter and the `role` column is `\"ACTOR\"` (to ensure you only retrieve actors).\n",
    "\n",
    "3. **Extract Actor Names**:\n",
    "   - From this filtered DataFrame, select only the `name` column to get the actor names.\n",
    "\n",
    "4. **Combine Names into a Single String**:\n",
    "   - Use `', '.join()` to combine the list of actor names into a single string, with each name separated by a comma.\n",
    "\n",
    "5. **Return the Result**:\n",
    "   - Return the resulting string of actor names.\n",
    "\n",
    "\n",
    "This function will allow you to retrieve and format a list of actors for any movie or show title, which is useful for creating cast lists or displaying actors for specific titles."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "hSCm5mYRziCD"
   },
   "outputs": [],
   "source": [
    "# Define the function\n",
    "def get_actors_for_title(title):\n",
    "    # Filter for rows with the specified title and role as 'ACTOR'\n",
    "    goodmovies=df[(df.title==title)&(df.role==\"ACTOR\")]\n",
    "    \n",
    "\n",
    "    # Extract the 'name' column for actor names\n",
    "    reallygoodmovies= goodmovies.name\n",
    "\n",
    "    # Combine names into a single string\n",
    "    goodmovies=','.join(reallygoodmovies)\n",
    "\n",
    "    # Return the result\n",
    "    return goodmovies\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "id": "BCnnBFUdzj20"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Robert De Niro,Jodie Foster,Albert Brooks,Harvey Keitel,Cybill Shepherd,Peter Boyle,Leonard Harris,Diahnne Abbott,Gino Ardito,Martin Scorsese,Murray Moston,Richard Higgs,Bill Minkin,Bob Maroff,Victor Argo,Joe Spinell,Robinson Frank Adu,Brenda Dickson,Norman Matlock,Harry Northup,Harlan Cary Poe,Steven Prince,Peter Savage,Nicholas Shields,Ralph S. Singleton,Annie Gagen,Carson Grant,Mary-Pat Green,Debbi Morgan,Don Stroud,Copper Cunningham,Garth Avery,Nat Grant,Billie Perkins,Catherine Scorsese,Charles Scorsese,Odunlade Adekola,Ijeoma Grace Agu\n"
     ]
    }
   ],
   "source": [
    "# Test the function\n",
    "print(get_actors_for_title(\"Taxi Driver\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Great job implementing the <code>get_actors_for_title()</code> function. Filtering by both <code>title</code> and <code>role</code> ensures accuracy, and joining the actor names into a single string makes the output clear and easy to read.\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Iu7Zzk7M0o_9"
   },
   "source": [
    "## Task 8: Creating a Function to Categorize Movies by IMDb Score\n",
    "\n",
    "Let’s categorize movies and shows based on their IMDb scores to provide a quick evaluation of their popularity or quality. We’ll create a function that takes in a `title` and returns a rating category based on the movie or show’s IMDb score.\n",
    "\n",
    "### Rating Categories\n",
    "\n",
    "- **Excellent**: IMDb score of 9.0 or higher\n",
    "- **Good**: IMDb score between 7.0 and 8.9\n",
    "- **Average**: IMDb score between 5.0 and 6.9\n",
    "- **Low**: IMDb score below 5.0\n",
    "\n",
    "### Instructions\n",
    "\n",
    "1. **Define the Function**:\n",
    "   - Create a function called `categorize_imdb_score` that accepts one parameter, `title`.\n",
    "\n",
    "2. **Filter by Title**:\n",
    "   - Inside the function, filter the DataFrame to find the row where `title` matches the given title.\n",
    "\n",
    "3. **Retrieve IMDb Score**:\n",
    "   - If the title exists, retrieve the `imdb_score` for that movie or show.\n",
    "   - If the title is not found, return `\"Title not found\"`.\n",
    "\n",
    "4. **Categorize Score with `if-else`**:\n",
    "   - Use `if-elif-else` statements to evaluate the `imdb_score` and return one of the rating categories based on the ranges provided.\n",
    "\n",
    "5. **Return the Category**:\n",
    "   - Return the appropriate category based on the score.\n",
    "\n",
    "This function allows you to quickly categorize movies or shows by their IMDb score, which could be helpful for creating rating tags or recommending top-rated content."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "id": "ZfrrGY7h0zYT"
   },
   "outputs": [],
   "source": [
    "# Define the function\n",
    "def categorize_imdb_score(title):\n",
    "    # Filter for the row with the specified title\n",
    "    goodmovies= df[df['title']==title]\n",
    "    # Check if title exists\n",
    "    if len(goodmovies)==0:\n",
    "        return \"Title not found\"\n",
    "    \n",
    "\n",
    "    # Retrieve the IMDb score for the movie\n",
    "    moviescore= goodmovies.iloc[0]['imdb_score'].item()\n",
    "\n",
    "    # Categorize score using if-else and return the ranking accordingly\n",
    "    if moviescore >=9:\n",
    "        return \"Excellent\"\n",
    "    elif moviescore >=7:\n",
    "        return \"Good\"\n",
    "    elif moviescore >=5:\n",
    "        return \"Average\"\n",
    "    else:\n",
    "        return \"Low\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "id": "4wqHjcFZ01Qk"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good\n"
     ]
    }
   ],
   "source": [
    "# Test the function\n",
    "print(categorize_imdb_score(\"Taxi Driver\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-success\">\n",
    "  <b>Reviewer’s comment – Iteration 1:</b><br>\n",
    "  Nicely done with the <code>categorize_imdb_score()</code> function. You included an existence check for missing titles, retrieved the score correctly, and applied clear conditional logic to return categories like Excellent, Good, Average, and Low. This makes the function both robust and easy to interpret.\n",
    "</div>\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

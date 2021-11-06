# Obtaining the Container-Ship Data

## Step 1: Extracting the ship ids and generating the URLs
- On searching for containerships on fleetmon.com, we obtain a list of 400+ container-ships
- Each ship has its own dedicated page with all its particulars listed over there
- In order to navigate to a ship's page, all we need is a unique id corresponding to that ship
- Once we have the unique ids corresponding to all the ships, we can create a dynamic URL and navigate to all the ship pages by just changing the ship id in the URL
- Ids of all the container-ships have been collected and put into vessel_data.xlsx (achieved by using javascript and Chrome developer console)

## Step 2: Scraping the data

- In the main scrapper python script, we run through 'vessel_data.xlsx' to generate the URLs corresponding to each ship and store them in a list
- Now that we have the URLs, all we have to do is to navigate each one of them, scrape the necessary data and save it in a dataframe
- In order to navigate to the URL and gather the necessary data, we need an account on fleetmon which can be easily created for free
- Once we have the account, we loop on the list of URLs one by one
- In order to automate the URL navigation process, selenium web-driver has been used
- In order to navigate to a URL, selenium opens the fleetmon page, logs in using the credentials and then navigates to the URL corresponding to a ship
- In order to scrape the data from the ship's page, we have used Beautiful-Soup (bs4)

## Step 3: Storing and Exporting the scraped data

- The data scrapped by beautiful soup is stored as a row in a pandas dataframe
- This process is repeated for all the URLs (400+)
- Once the dataframe has been completely built, the scraped data is exported into an excel file named 'output.xlsx'

## Step 4: Cleaning the data

- For ships where major data was missing, the rows have been manually deleted (~15-16 ships)
- After clearing, the data file was renamed to 'semi_final.xlsx'
- Since the engine data corresponding to the ships obtained after scraping contained a lot more data than required, the power corresponding to each ship is extracted and rest of the data is discarded before being fed into the Neural Network


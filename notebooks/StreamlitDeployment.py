import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# Streamlit Title
st.title("Car Listings Scraper")

# Streamlit description
st.write("This app scrapes car listings based on transmission type, drivetrain, fuel type, and zip code.")

# Allow user to input zip code
zip_code = st.text_input("Enter Zip Code", value="94089")  # Default zip code is 94089

# Allow user to input parameters for scraping
selected_fuel_type = st.selectbox('Select Fuel Type', ["Hybrid"])
selected_transmission_type = st.selectbox('Select Transmission Type', ["Automatic"])
selected_drivetrain_type = st.selectbox('Select Drivetrain Type', ["All-Wheel Drive"])

# Initialize lists to store data
car_names = []
prices = []
dealer_names = []
transmission_list = []
drivetrain_list = []
fuel_type_list = []
ratings = []
reviews = []
locations = []
mileages = []

# Button to trigger the scraping
if st.button('Start Scraping'):
    # Full path to your ChromeDriver binary
    service = Service('/path/to/your/chromedriver')

    # Initialize Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Base URL with dealership filter and radius filter, and the dynamic zip code
    base_url = f"https://www.cars.com/shopping/results/?dealer_id=&include_shippable=true&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=75&mileage_max=&monthly_payment=&page_size=20&seller_type[]=dealership&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip={zip_code}"

    # Initialize the WebDriver with headless options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Construct the URL dynamically
    url = f"{base_url}&transmission_slugs[]={selected_transmission_type.lower()}&drivetrain_slugs[]={selected_drivetrain_type.lower()}&fuel_slugs[]={selected_fuel_type.lower()}&page=1"

    # Open the URL
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(3)  # Reduced wait time

    # Try to find the vehicle elements
    vehicle_elements = driver.find_elements(By.CLASS_NAME, 'vehicle-card-main')

    # Loop through the vehicle elements and extract data
    for vehicle in vehicle_elements:
        try:
            # Extract car name
            name = vehicle.find_element(By.CLASS_NAME, 'title').text if vehicle.find_element(By.CLASS_NAME, 'title') else 'N/A'
            car_names.append(name)

            # Extract price
            price = vehicle.find_element(By.CLASS_NAME, 'primary-price').text if vehicle.find_element(By.CLASS_NAME, 'primary-price') else 'N/A'
            prices.append(price)

            # Extract dealer name
            dealer_name = vehicle.find_element(By.CLASS_NAME, 'dealer-name').text if vehicle.find_element(By.CLASS_NAME, 'dealer-name') else 'N/A'
            dealer_names.append(dealer_name)

            # Append the transmission, drivetrain, and fuel type
            transmission_list.append(selected_transmission_type)
            drivetrain_list.append(selected_drivetrain_type)
            fuel_type_list.append(selected_fuel_type)

            # Extract rating
            rating = vehicle.find_element(By.CSS_SELECTOR, 'spark-rating').get_attribute('rating') if vehicle.find_element(By.CSS_SELECTOR, 'spark-rating') else 'N/A'
            ratings.append(rating)

            # Extract reviews count
            reviews_count = vehicle.find_element(By.CLASS_NAME, 'sds-rating__link').text.strip('()') if vehicle.find_element(By.CLASS_NAME, 'sds-rating__link') else 'N/A'
            reviews.append(reviews_count)

            # Extract location
            location = vehicle.find_element(By.CLASS_NAME, 'miles-from').text if vehicle.find_element(By.CLASS_NAME, 'miles-from') else 'N/A'
            locations.append(location)

            # Extract mileage
            mileage = vehicle.find_element(By.CLASS_NAME, 'mileage').text if vehicle.find_element(By.CLASS_NAME, 'mileage') else 'N/A'
            mileages.append(mileage)

        except Exception as e:
            st.write(f"Skipping vehicle due to missing data: {e}")
            continue

    # Close the browser
    driver.quit()

    # After extracting data, create the DataFrame
    df = pd.DataFrame({
        'Car Name': car_names,
        'Price': prices,
        'Dealer Name': dealer_names,
        'Transmission Type': transmission_list,
        'Drivetrain': drivetrain_list,
        'Fuel Type': fuel_type_list,
        'Rating': ratings,
        'Reviews': reviews,
        'Location': locations,
        'Mileage': mileages
    })

    # Display the DataFrame
    st.write(df)

    # Provide a CSV download link
    st.download_button(
        label="Download data as CSV",
        data=df.to_csv(index=False),
        file_name='car_listings.csv',
        mime='text/csv'
    )

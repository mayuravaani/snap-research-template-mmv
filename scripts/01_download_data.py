import pandas as pd
import requests


def download_weather_data():
    # Using the Open-Meteo free weather API - getting weather data for Wellington
    url = "https://api.open-meteo.com/v1/forecast?latitude=-41.2866&longitude=174.7756&daily=temperature_2m_max,wind_speed_10m_max&timezone=Pacific%2FAuckland"

    try:
        # Download the data
        response = requests.get(url)
        response.raise_for_status()

        # Convert to pandas DataFrame
        data = response.json()
        df = pd.DataFrame(
            {
                "date": data["daily"]["time"],
                "max_temp": data["daily"]["temperature_2m_max"],
                "max_wind_speed": data["daily"]["wind_speed_10m_max"],
            }
        )

        # Save to CSV
        output_path = "welly_weather_forecast.csv"
        df.to_csv(output_path, index=False)
        print(f"Data successfully downloaded and saved to '{output_path}'")
        print("\nFirst few rows of data:")
        print(df.head())

    except requests.RequestException as e:
        print(f"Error downloading data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")


# Run the function
if __name__ == "__main__":
    download_weather_data()

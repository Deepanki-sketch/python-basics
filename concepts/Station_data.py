"""
Fetch Meteostat daily weather data via curl.exe, using the ACTUAL schema:
year,month,day,temp,temp_source,tmin,tmin_source,tmax,tmax_source,
rhum,rhum_source,prcp,prcp_source,wspd,wspd_source,pres,pres_source,
cldc,cldc_source
"""

import subprocess
import gzip
import io
import sys
import pandas as pd

STATION_ID = "43003"     # Bombay/Santacruz - 99.7% day coverage, ~100% temp/humidity/pressure
YEARS = [2018, 2019, 2020, 2021, 2022]     # change this to your desired year range
OUTPUT_CSV = "weather_data.csv"

COLUMNS = ["year", "month", "day", "temp", "temp_source", "tmin", "tmin_source",
           "tmax", "tmax_source", "rhum", "rhum_source", "prcp", "prcp_source",
           "wspd", "wspd_source", "pres", "pres_source", "cldc", "cldc_source"]

all_years = []

for year in YEARS:
    url = f"https://data.meteostat.net/daily/{year}/{STATION_ID}.csv.gz"
    print(f"Downloading {url} ...")
    result = subprocess.run(["curl.exe", "-s", "-f", url], capture_output=True)

    if result.returncode != 0:
        print(f"  -> curl failed for {year}, skipping.")
        continue

    raw = gzip.decompress(result.stdout)
    df_year = pd.read_csv(io.BytesIO(raw), header=0, names=COLUMNS, skiprows=1)
    all_years.append(df_year)
    print(f"  -> got {len(df_year)} rows for {year}")

if not all_years:
    print("\nNo data retrieved. Check STATION_ID.")
    sys.exit(1)

df = pd.concat(all_years, ignore_index=True)
df["timestamp"] = pd.to_datetime(df[["year", "month", "day"]])

# ------------------------------------------------------------------
# Check completeness BEFORE building the final file - sparse columns
# will silently wreck an anomaly detector if you don't know about them
# ------------------------------------------------------------------
print(f"\nTotal rows: {len(df)}")
print("\nData completeness (% of rows with a real value):")
for col in ["temp", "tmin", "tmax", "rhum", "prcp", "wspd", "pres", "cldc"]:
    pct = 100 * df[col].notna().mean()
    print(f"  {col:6s}: {pct:5.1f}%")

out = pd.DataFrame({
    "timestamp": df["timestamp"],
    "temperature_c": df["temp"],
    "humidity_pct": df["rhum"],
    "pressure_hpa": df["pres"],
})

out.to_csv(OUTPUT_CSV, index=False)
print(f"\nSaved to {OUTPUT_CSV}")
print("\nIf humidity_pct or pressure_hpa show low completeness above, "
      "this station isn't a great fit for your anomaly-detection project - "
      "consider trying the OTHER nearby station (43064) or a different "
      "location and comparing completeness before committing to one.")
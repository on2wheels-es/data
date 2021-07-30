![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project: On2wheels.es 🚴‍♂️


---


## Context ✏

**On2wheels.es** is a cycling stage planner that will find the best cycling destinations in Spain for a given date based on historical weather data and a private database of more than 8000 bike routes. Future stages of development will bring added functionality in the shape of accomodation recommendations (via Booking) and the best places to eat (via Tripadvisor).


---


## Project aim ✔

The aim of the **data** section of this project is the following, divided into phases:

**Phase 1:**

  - Obtain and geolocate Spain's mountain passes. 🟢
  - Download the best routes (including *gpx*) to climb all mountain passes. 🟢
  - Create a dataset of all mountain passes geolocated. 🟢
  - Create a dataset with the best route to climb each port. 🟢
  - Create a dataset of all towns that have 3 or more such routes nearby. 🟢
  - Create a custom weather index to give each destination a weather score based on historical data. 🟢
  - Build an **API** that uses the weather index and returns the 5 best destinations for a given date. 🟢
  - Host the **API** on a private server so that it can handle calls 24/7. 🟢
  - Deploy the website on the server. 🟡
  - Add images to the best ports and cycling destination. 🔴

**Phase 2:**

  - Geolocate the maximum number of ports, including start and finish coordinates. 🔴
  - Create interactive visualizations for each port's altimetry. 🔴
  - Integrate Booking and Tripadvisor. 🔴
  - Migrate all routes dataframes to **Geopandas**. 🔴
  - Add images to all ports and destinations. 🔴
  - Improve the weather API using secondary sources for weather data. 🔴
 
**Phase 3:**

  - Create a scoring system for bike routes. 🔴
  - Recommend routes based on user fitness. 🔴
  - Use user activity (Strava rides) to discover new popular routes. 🔴
  - Discover best places to stop (bars) and to take pictures. 🔴
  - Automated gpx parsing and feed into the system. 🔴
  - Fully automated best-route selection. End goal. 🔴


---


## Setup & environment ⚙

This project is being created using **Python 3.8.8**. Some of the original data and dataframes are missing because they came from private sources.


---


## Notes and warnings ⁉

Take special care when trying to replicate any *gpx* parsing or mapping, since both **Gpxpy** and **Folium** can be quite picky when it comes to formatting and file encoding.

---

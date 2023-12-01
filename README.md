# Utilizing AI for Nationwide Lead Water Service Line Prediction
Lead contamination in drinking water, especially harmful to children, prompted the US EPA to mandate public water systems to identify lead service lines (LSL) by Oct 16, 2024 and replace LSL subsequently. Predictive modeling is approved by USEPA as one LSL identification method. However, existing models lack effectiveness in data-scarce regions. This project proposes a cross-regional predictive model fueled by socio-economic, environmental and parcel data. By capturing complex interactions, it improves LSL prediction in data-scarce regions and can potentially revolutionize nationwide LSL identification. This approach aspires to reduce lead in drinking water at an accelerated pace when resources are limited. Along with XGBoost, LightGBM, and artificial neural network machine learning models, we created a user interface where users can see which parcels of land are more/less likely to have lead service lines.

1. Datasets \
   a. Parcel data was scraped from renter.com and zillow.com using their respective APIs.\
   b. Lead service line data was collected by scraping ArcGIS maps of lead service line presence.\
   c. Census data was collected fromo data.census.gov.\ 

2. Modeling \
  a. Explore, train, and evaluate multiple algorithms to select the best model for the project objectives.\
  b. Explore and select services like wandb or MLflow for proper versioning of datasets and models \
  c. Explore interpretation tool to explain what happens in the model, such as DiCE \
  d. Explore and select a suitable model hosting service and create model endpoints.

3. User Interface \
   Create model endpoints to be called from a lead service line map where users can: \
  a. Enter a property address (by typing into a search field or clicking on a parcel on the map) and get back predicted probabilities of the property having a lead service line on the utility side and on the customer side. Click here for an example: https://d2u44yafpgs75b.cloudfront.net/map. \
  b. Upload a list of property addresses in CSV format and receive a predicted lead service line probabilities in downloadable table format: https://app.akkio.com/deployments/xD47fjwIsPZwKcVJywac\
### Credits
Special thanks to Dan Wang and Hung Bui, who actively supported our efforts both with their knowledge and insights throughout the process.

Our team with links to reach us are down below:
- [Andrew Kerr][https://www.linkedin.com/in/andrewkerr82310/]
- [Akash Iyer][https://www.linkedin.com/in/akash-v-iyer]
- [Phuc Pham][]
- [Jasmine Andrade][https://www.linkedin.com/in/jasmine-andrade-742b61233/]
- [Melad Mayaar][https://www.linkedin.com/in/ahmad-melad-mayaar-7109a3235/]
- [Pranav Walimbe][https://www.linkedin.com/in/pranav-walimbe-9218461a6/]

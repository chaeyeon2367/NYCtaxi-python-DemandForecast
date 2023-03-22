<br/>
<br/>

# NYC Taxi Data Demand Forecast🚕

<br/>
<br/>

### 1. Objective
- Adapt to cloud environments using BigQuery (SQL)
- Improve baseline through machine learning modeling
- Simple Feature Engineering (Lag Value, Day of Week, Time of Day) 
- Models : Linear Model, XGBoost, LightGBM, Random Forest
- Save model parameters using Sacred
- Train/Predict scheduling with Google Cloud Composer(Airflow)

<br/>

### 2. Mobility data type
- Vehicle data
  * Route, coordinate, spatial data - sensor data
- Customer Data
  * Basic Customer Data - Service History - App Log Data
- Public data
  * Weather data
  * Regional data (administrative area units, etc.)
  
  
 <br/> 
  
### 3. Apache Airflow
<img width="159" alt="Capture d’écran 2023-03-22 à 11 17 27" src="https://user-images.githubusercontent.com/63314860/226873490-8234301f-c018-4277-b4c7-a0398fec4cef.png">



- A tool for easily controlling repetitive workflows 
- Can repeat periodic crontab tasks.
- Can concatenate consecutive. ex) Feature Engineering -> Model Train -> Model Predict - UI is provided.

#### Basic UI
<img width="834" alt="Capture d’écran 2023-03-22 à 11 25 14" src="https://user-images.githubusercontent.com/63314860/226874867-34a6026e-99cc-46c6-95da-8f8f76b73dc5.png">
<br/>



### 4. Google Cloud Composer
<img width="169" alt="Capture d’écran 2023-03-22 à 11 27 52" src="https://user-images.githubusercontent.com/63314860/226875386-31f95327-6765-422a-9a32-e5dd490cd5f8.png">

 1) Things to do if we run Apache Airflow directly 
     - Airflow's Database setting (default : sqlite)
     - Set up Celery, Redis, Kubernetes, etc.
 

 2) Modeling
    - Runs primarily in a Jupyter Notebook
    - Save best algorithms, parameters, etc.

 3) Code modification and separation
    - Modify the files I was using in Jupyter Notebook into script format 
    - Remove the cohesiveness of Train / Predict

 
 4) Create a Composer DAG
    - DAG means Directed Acyclic Graph and can be thought of as a collection of workflows and tasks.
    - Utilize the already created Bash Operator, Python Operator, BigQuery Operator, etc.
    

<br/>

### 5. Point of Improvement

- Feature Engineering
  * Creating additional features to improve the predictive accuracy of your model. 
  * Mean Encoding : Performing statistical operations with target values based on categorical features.
  * Weather features (temperature, precipitation, etc.) 
  * Holiday features
  
  
- Time units
  * Predicted every 60 minutes, but is it right?
  * Extract data in half-hourly increments and see if the distributions for 0-30 minutes and 30-60 minutes are similar 
    => If they are not, we can change the forecast to every 30 minutes.
    
- Geographic Units
  * Is zip_code really a good unit?
  * zip_code is an arbitrary division of the country and different zip's have different sizes 
  * How to use 'geohash', 'h3', etc (using BigQuery UDF)  (Re: https://zzsza.github.io/gcp/2019/09/20/bigquery-udf/)
       * GeoHash : Hierarchical spatial data structure that divides space into a grid Converts to a short string of letters and numbers
       * H3 : a hierarchical spatial data structure created by Uber that divides space into hexagons. The hexagons are equidistant from each other.
       
       
       
- Improving Models
  * Creating new machine learning models
  * Hyper-parameter tuning (and by extension, AutoML -> Microsoft NNI, etc.) (RE: https://github.com/microsoft/nni 
  * Demand forecasting using deep learning 
       *RE 1) https://www.kakaobrain.com/blog/42 
       *RE 2) https://www.kakaobrain.com/blog/43
       
       
- Learning Methods
  * Train / Test only, but split into Train / Valid / Test
  * Setting the learning data period to vary over time instead of only in January
  
  
  <br/>
  <br/>
  <br/>
  
  

# Serverless function for email notifications
The serverless function example project is made with Digital Ocean CLI tool (doctl).

After installing doctl, make sure serverless is installed running the comand `doctl serverless status`.
It should return `Error: serverless support is installed but not connected to a functions namespace (use doctl serverless connect).`
Otherwise install serverless by running comand `doctl serverless install`. 

Sample project in Python made with comand `doctl serverless init --language python distance_serverless_function`.

Project.yaml file can be changed to add triggers and configuration. 
Current configuration has no timed triggers. The function is triggered (called) from order-management microservice when order status changes.

Invoking function trough cli: `doctl serverless functions invoke sample/distance_calc`

Checking the logs (limited to 5 logs): `doctl serverless activations logs  --limit 5`

Deploying the fucntion: `doctl serverless deploy distance_serverless_function`

This function serves to access the Google Maps API, specifically the Distance Matrix API, and calculate the distance and travel time required for the delivery to arrive from the restaurant to the customer.


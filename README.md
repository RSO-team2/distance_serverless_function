# Serverless function for email notifications
The serverless function example project is made with Digital Ocean CLI tool (doctl).

After installing doctl, make sure serverless is installed running the comand `doctl serverless status`.
It should return `Error: serverless support is installed but not connected to a functions namespace (use doctl serverless connect).`
Otherwise install serverless by running comand `doctl serverless install`. 

Sample project in Python made with comand `doctl serverless init --language python smtp-serverless-function`.

Project.yaml file can be changed to add triggers and configuration. 
Current configuration has no timed triggers. The function is triggered (called) from order-management microservice when order status changes.

Invoking function trough cli: `doctl serverless functions invoke sample/smtp`

Checking the logs (limited to 5 logs): `doctl serverless activations logs  --limit 5`

Deploying the fucntion: `doctl serverless deploy smtp-serverless-function`

This function serves as an email notification system using SMTP protocol. The chosen SMTP provider is mailsender. The function recieves two URL arguments: the user email and order status and sends an email with said status to said user email. In case of error it returns an error JSON object. More details about calling the function is available in Postman API documentation (https://documenter.getpostman.com/view/26454602/2sAYQWKZR5). 


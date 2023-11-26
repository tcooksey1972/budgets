# AWS Budget Management System

## Overview
This project implements a budget management system for AWS to monitor and control AWS spending in development accounts. It utilizes AWS Budgets, AWS Config, Lambda, SNS, and SCPs to ensure spending does not exceed a predefined budget.  
Comprehensive isntructions can be found in the comments of the cloudformation templates and in the Setupinstruciotns.md

## Below are some helpful links to read over to help understand this project and get started.

## Getting Started with AWS Budgets:Blog
    https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-budgets/

## Configuring Budget Actions:Documentation
    https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html

## Features
- **Budget Tracking**: Set up budgets in AWS to monitor spending.
- **Automated Alerts**: Receive alerts at 60%, 80%, 90%, and 100% of budget usage.
- **Resource Control**: Automatically restrict resource creation when the budget limit is reached.
- **Monthly Reset**: Scheduled automation to lift restrictions at the start of each month.

## Repository Structure
- `/lambda_functions`: Contains Lambda function scripts for managing SCPs.
- `/policies`: Includes policy documents for SCPs and other configurations.

## Setup Instructions
### Step 1: Set Up AWS Budgets
...

### Step 2: Set Up SNS Topic
...

### Step 3: Create Lambda Functions
See Lambda's 

## Testing
- **Simulate Budget Alerts**: Test the setup by simulating budget alerts.
- **Monitor Logs**: Check AWS CloudWatch logs for function execution details and troubleshooting.

## Additional Information
- Ensure all Lambda functions have the necessary IAM permissions.
- Customize the Lambda functions and SCPs according to your AWS environment needs.

## Contributing
Feel free to contribute to this project by submitting pull requests or suggesting improvements.

## License
Creative Commons

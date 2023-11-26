# AWS Budget Management System Implementation Guide

## 1: Set Up AWS Budgets
**Objective:** Establish a cost monitoring system to track and manage AWS spending.

1. **Log into AWS Management Account:** Access the AWS Management Console with an account that has administrative privileges to set up budgets and configure alerts.
2. **Navigate to AWS Budgets:** AWS Budgets allows setting custom budgets to track cost and usage from the AWS dashboard.
3. **Create a New Budget:**
   - **Select “Create budget”**: Initiates the process of defining a new budget.
   - **Choose “Cost budget”**: Specifies tracking costs, not usage or other metrics.
   - **Set budget details**: Establish a monthly budget of $1,000 to cap spending for each development account.
4. **Configure Alerts:**
   - **Alerts at 60%, 80%, 90%, 100% of the budget**: Notifies at various stages of budget consumption for proactive management of resources and costs.
   - **100% alert to SNS topic**: Crucial for triggering actions to prevent further resource creation when the budget limit is reached.

## 2: Set Up SNS (Simple Notification Service) Topic
**Objective:** Create a communication channel for sending budget alerts.

1. **Create an SNS Topic:** An SNS topic named “BudgetAlerts” is created to aggregate and forward notifications from AWS Budgets.
2. **Set Up Email Subscription:**
   - **Optional email alerts:** Subscribe your email to the SNS topic to receive direct notifications about budget status.

## 3: Create Lambda Functions
**Objective:** Automate the enforcement and re-enablement of budget compliance policies.

1. **Create a Lambda for Disabling Accounts:**
   - **Lambda setup:** Triggered when the budget reaches 100%, enforcing restrictions on resource creation by attaching an SCP (Service Control Policy).
   - **Python/Node.js runtime:** Choice of runtime depends on your team's expertise and preference.
   - **IAM permissions:** The function requires permissions to modify SCPs.
2. **Create a Lambda for Re-enabling Accounts:**
   - **Monthly reset function:** Scheduled to run at the start of each month to lift the restrictions imposed by the SCP.

## 4: Set Up EventBridge
**Objective:** Automate the scheduling of the re-enabling Lambda function.

1. **Create a Rule for Monthly Reset:**
   - **Automated triggering:** EventBridge rule to automatically trigger the Lambda function responsible for removing the SCPs at the beginning of each month.

## 5: Create and Attach Service Control Policies (SCPs)
**Objective:** Define policies that limit account actions when budget thresholds are exceeded.

1. **Create SCP to Restrict Resource Creation:**
   - **Policy creation:** A new SCP is created to prevent resource creation, stopping new expenses from being incurred in the account.
2. **Attach/Detach SCP Using Lambda:**
   - **Automated SCP management:** The Lambda functions manage the attachment and detachment of this SCP based on budget consumption.

## 6: Subscribe Lambda to SNS Topic
**Objective:** Link the budget alert system with the enforcement mechanism.

1. **Link Lambda to SNS Topic:**
   - **Integration of services:** Connects the Lambda function to the SNS topic to ensure automatic triggering upon budget alert publication.

## 7: Test Your Setup
**Objective:** Validate the functionality of the entire system.

1. **Simulate Budget Alerts:**
   - **Testing:** Simulate budget alerts to ensure the system works as expected and that Lambda functions are triggered appropriately.
2. **Monitor the Lambda Logs:**
   - **Verification and troubleshooting:** Regular monitoring of CloudWatch logs for identifying issues and confirming actions.

## Additional Considerations
- **IAM Permissions:** Ensuring correct IAM permissions is critical for the proper functioning of Lambda functions.
- **Error Handling:** Implement robust error handling in Lambda functions for effective management of unexpected situations.
- **Notification Channels:** Integrate additional notification channels to improve visibility and response to budget status.
- **Customization:** Customize Lambda functions and SCPs based on your specific AWS environment and requirements.

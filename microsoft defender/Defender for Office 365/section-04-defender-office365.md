# SIMULATION: Create a Safe Attachments Policy for Sales Group with Dynamic Delivery & Redirect

## Configuration Steps:

1. **Navigation**: Email and collaboration → Policies and rules → Threat policies

2. **Select Safe Attachments**: Click on "Safe Attachments" option

3. **Create Policy**: Click "Create" button

4. **Basic Configuration** - Fill in the required fields:
   - **Policy name**: Name of the policy (e.g., "Sales Group - Safe Attachments")
   - **Description**: Explain the policy purpose (e.g., "Scan attachments for Sales group with Dynamic Delivery")
   - Click "Next" to proceed

5. **Define Recipients** - Specify who this policy applies to:
   - **Users**: Select individual mailboxes
   - **Groups**: Select distribution groups or security groups
     - *Note: If the group doesn't exist, create it first in the admin panel and assign members*
   - **Domains**: Use with caution - applies to all users in specified domain
   - Example: Select "Sales Group"

6. **Safe Attachments Action Settings** - Choose how attachments are handled:
   - **Off** - No scanning; attachments pass through untouched
   - **Monitor** - Message delivered immediately; scan results logged only (no message quarantine)
   - **Block** - Message quarantined if malware detected; admin must approve every release request regardless of quarantine policy settings
   - **Dynamic Delivery** *(selected in this example)* - Message body delivered instantly; attachments reattached after scanning completes
     - Best option when immediate access to email is needed
     - Hosted mailboxes only
     - Useful for compliance: confirm whether attachments were actually delivered

7. **Quarantine Policy** - Configure release request handling:
   - Select who is responsible for approving quarantine release requests
   - Assign to specific admin or security team member
   - Define notification preferences

8. **Enable Redirect Option** (optional):
   - **Requires**: Monitor mode or Dynamic Delivery
   - **Function**: Sends a copy of messages with monitored attachments to specified email address
   - **Use case**: Security Operations Center (SOC) analysis and monitoring
   - **Example**: Redirect to SOC@company.com for threat investigation

9. **Review and Confirm**: Verify all settings

10. **Activate Policy**: Enable the policy to apply protection

---

## Safe Attachments Policy Best Practices:

- **Dynamic Delivery + Redirect**: Combine for optimal user experience and security monitoring
- **Group-based Application**: Apply to specific departments (Sales, Finance, etc.) before organization-wide rollout
- **Regular Monitoring**: Review quarantine logs and SOC redirect emails for threat trends
- **Testing**: Start with "Monitor" mode before switching to "Block"
- **Notification Setup**: Ensure admins receive release request notifications

---
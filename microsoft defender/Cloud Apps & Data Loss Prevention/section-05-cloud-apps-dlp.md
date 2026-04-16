# Create a Custom DLP Policy Using Full Name Policy

1. Open **Microsoft Purview**.
2. Navigate to the **Data Loss Prevention** tab.
3. Go to **Policies** and click **Create Policy**.
4. Choose between **Enterprise Application** or **Inline Web Traffic**. Since we want to detect uses of full names in applications like Outlook or Excel, select the **first option (Enterprise Application)**.
5. Several built-in categories are available, but we need to create a **custom policy**.
6. Provide a **name** and **description** for the policy.
7. Assign **Admin Units** — these define the scope to specific users or groups.
8. Select where to **apply the policy**. In this case, we want to enforce it only on **Exchange emails**.
9. Define the **policy settings**. Although default settings are available, since this is a custom policy, we need to configure them manually.
10. Enter a **name** and **description** for the rule.
11. Add **conditions** — these define the criteria that must be met for the rule to trigger:
   - Set the sender condition to members of the **Sales group**.
   - Add a second condition: **Content contains** → click **Add** and select **All Full Names**.
12. Enable **User Notifications** and **Policy Tips** — this will alert the user when they are about to violate the policy.
13. Finally, choose whether to run the policy in **Simulation Mode** or activate it immediately. In this case, select **Turn it on immediately**.
Task:
Create a safe attachment policy for Sales group ( create group) with Dynamic Deliver & redirect to admin or selected user

Solution:
1) Email and collaboration tab
2) Policies and rules tab
3) Threat policies tab
4) Safe Attachments option
5) Create
6) We can specify name of policy and description -> Next button
7) We can type Users, Groups and Domain ( be careful) ( if we dont have group we can cretae and assign members in admin panel )
8) We can choose settings for safe attachments action:
    - Off -> No scanning. Attachments pass through untouched.
    - Monitor -> Message delivered regardless; scan results logged only.
    - Block -> Message quarantined if malware detected. Quarantine policy is ignored for malware — admin must approve every release request regardless of policy settings.
    - Dynamic Delivery -> Message body delivered instantly; attachments reattached after scanning. Hosted mailboxes only - good option when we want to know if attachments was delivered
9) In quarantine policy we can pick who is responsible to release request
10) Enable redirect option works with Monitor. Sends a copy of messages with monitored attachments to the specified email address — useful for SOC analysis


***
Other than Safe Attachments oplicy we can a lot of options:

Templated policies:
Preset Security Policies -> Easily configure protection by applying all policies at once using recommended protection templates 
Configuration analyzer -> Identify issues in your current policy configuration to improve your security 

Policies
-Anti-phishing -> Protect users from phishing attacks, and configure safety tips on suspicious messages 
-Anti-spam -> Protect your organization's email from spam, including what actions to take if spam is detected
-Anti-malware -> Protect your organization's email from malware, including what actions to take and who to notify if malware is detected 
-Safe Attachments -> Protect your organization from malicious content in email attachments and files in SharePoint, OneDrive, and Teams 
-Safe Links -> Protect your users from opening and sharing malicious links in email messages and Office apps 

Rules
-Tenant Allow/Block Lists-> Manage allow or block entries for your organization 
-Email authentication settings-> Settings for Authenticated Received Chain (ARC) and DKIM in your organization
-Advanced delivery-> Manage overrides for special system use cases 
-Enhanced filtering-> Configure Exchange Online Protection (EOP) scanning to work correctly when your domain's MX record doesn't route email to EOP first 
-Quarantine policies-> Apply custom rules to quarantined messages by using default quarantine policies or creating your own 
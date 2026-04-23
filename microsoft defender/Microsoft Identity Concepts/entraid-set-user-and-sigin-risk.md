# SIMULATION: Configure Entra ID Risk-Based Conditional Access for User & Sign-In Risks

1. **Navigation**: entra.microsoft.com → ID Protection → Risk-based Conditional Access

2. **Create New Policy**: Click "New policy" to create a conditional access rule

3. **Policy Name** - Assign a descriptive name:
   - Example: "High Risk - Require MFA"
   - This identifies the policy purpose

4. **Assignments Configuration** - Define scope and target:
   - **Users**: 
     - Select specific users or groups
     - Or choose "All users"
   - **Target Resources**:
     - Select cloud apps and resources to protect
     - Example: Microsoft 365 apps, custom applications
   - **Network Conditions** (optional):
     - Specify trusted/untrusted networks
     - Configure location-based restrictions

5. **User Risk Conditions** - Configure account compromise detection:
   - **Risk Level**: Choose from Low, Medium, or High
   - **What it does**: Runs 24/7 to detect account anomalies
   - **Example triggers**: 
     - Impossible travel scenarios
     - Login from unfamiliar location at unusual time
     - Suspicious account activity patterns
   - **Action**: When triggered, require additional authentication

6. **Sign-In Risk Conditions** - Configure login attempt evaluation:
   - **Risk Level**: Choose from Low, Medium, or High
   - **What it does**: Evaluates each login in real-time
   - **Example triggers**:
     - Atypical sign-in properties
     - Unfamiliar login locations
     - Suspicious authentication patterns
   - **Action**: Block or require verification
   - **Important Note**: Deploy User Risk and Sign-in Risk as separate policies - avoid combining them on one rule as both conditions rarely occur together

7. **Grant Access Controls** - Choose enforcement actions:
   - **Require authentication strength** - blocks legacy authentication protocols
   - **Require passwordless MFA** - Windows Hello, Authenticator app, FIDO2 keys *(selected in this example)*
   - **Require multi-factor authentication** - traditional MFA verification
   - **Require compliant device** - only managed/compliant devices
   - **Require Hybrid Azure AD joined device** - domain-joined devices only
   - **Block access** - deny access completely (for highest risk scenarios)

8. **Session Controls** (optional) - Manage session behavior:
   - Control login frequency and session duration
   - Limit concurrent sessions per user
   - Example: Re-authenticate every 4 hours

9. **Review Policy** - Verify all settings:
   - Check assignments and conditions
   - Confirm enforcement actions
   - Consider using "Report-only mode" for testing first

10. **Enable Policy**: Switch toggle to "On" to activate the conditional access rule

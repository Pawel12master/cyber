# SIMULATION: Create an endpoint device group "BIA" in Microsoft 365 Defender

## Configuration Steps:

1. **Navigation**: Defender → Settings → Endpoints
2. **Select Section**: Click on the "Device group" tab
3. **Add Group**: Click "Add device group"
4. **Basic Configuration** - Fill in the required fields:
   - **Device group name**: Name of the group (e.g., "Białystok Devices")
   - **Remediation level**: Choose the level of automated threat remediation:
     - **No automated response** - notifications only
     - **Full** - automatically removes all threats
     - **Semi** - requires approval for major threats
     - **Moderate** - remediates low-severity threats *(selected in this example)*
     - **Light** - remediates only high-confidence threats
5. **Membership Criteria** - Define conditions for device inclusion:
   - In this example: devices whose name **starts with "BIA"**
6. **Preview**: Click "Preview devices" to see which devices will be included in this group
7. **Confirmation**: Click "Next" (or "Create") to complete the setup
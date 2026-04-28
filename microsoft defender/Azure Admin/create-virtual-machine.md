# Assignment: Create a Windows Virtual Machine in Azure

## Step 1 – Navigate to Virtual Machines
Go to **Home → All Services → Compute → Virtual Machines**, or use the search bar at the top and type *"Virtual Machines"*. Click **Create → Azure Virtual Machine**.

---

## Step 2 – Project Details: Subscription & Resource Group
Select your subscription (*Azure subscription 1*) and assign the machine to the **SentinelRG** Resource Group. Grouping resources in a dedicated RG makes cost management easier and allows you to delete all related resources at once when no longer needed.

---

## Step 3 – Instance Details: Name & Region
Name the machine (e.g. *EU-Win-11-Test*) and select a **Region**. US East is one of the cheapest and most feature-complete regions. If latency matters, consider **West Europe (Amsterdam)** or **North Europe (Dublin)** for lower ping from Poland.

Set **Availability Zone** to *Zone 1* for basic redundancy. For a test machine this is sufficient – production workloads should consider multi-zone deployments.

---

## Step 4 – Security Type
Set to **Standard**. This skips Trusted Launch (Secure Boot + vTPM), which is unnecessary for a test environment and simplifies the setup. You configure security controls manually as needed.

---

## Step 5 – Image
Select **Windows 11 Enterprise Cloud PC, version 25H2 – x64 Gen2**. Note that *Preview* images may be less stable than GA releases. For more stable test environments consider **Windows 11 Pro** or **Windows Server 2022 Datacenter** (cheaper to run long-term).

---

## Step 6 – Size
Choose a cost-effective size such as **Standard_DC1s_v3** (1 vCPU, 8 GiB RAM, ~$70/month). For an even cheaper option, the **Standard_B2ms** (2 vCPU, 8 GiB RAM, ~$60/month) from the Burstable series is better suited for test VMs that are not under constant load. Always check the current pricing in the **See all sizes** panel.

> 💡 You can further reduce costs by enabling **Azure Spot Discount** if the machine is non-critical and you can tolerate occasional evictions.

---

## Step 7 – Administrator Account
Create a local admin account with a username (e.g. *test-user*) and a strong password. Avoid using obvious usernames like *admin* or *administrator* as these are common targets for brute-force attacks even on test machines.

---

## Step 8 – Inbound Port Rules
Allow **RDP (3389)** for remote access. Be aware that Azure warns this exposes the port to all public IP addresses. For better security even on test machines, consider restricting access to your own IP address via the **Networking tab → NSG rules** after creation, or enable **Just-in-Time VM Access** through Microsoft Defender for Cloud.

---

## Step 9 – Disks
Select **Standard HDD** as the OS disk type – the cheapest option, sufficient for a non-production machine. If you need better performance (e.g. for software testing with heavy I/O), **Standard SSD** is a reasonable step up at a small additional cost. Premium SSD is unnecessary for testing purposes.

---

## Step 10 – Networking
Leave default settings. Azure will automatically create a **Virtual Network, Subnet, Public IP, and Network Security Group (NSG)**. The NSG will contain the RDP rule defined in the previous step. No changes needed for a basic test VM.

---

## Step 11 – Management: Microsoft Entra ID
Enable **Login with Microsoft Entra ID**. This joins the machine to the Azure AD environment, allowing sign-in with your organizational Microsoft account instead of the local credentials. Useful for centralized access management.

---

## Step 12 – Auto-shutdown & Backup
Enable **Auto-shutdown** and set a daily shutdown time (e.g. *19:00*). This is a critical cost-saving measure – a forgotten running VM accumulates charges continuously. Backup is not needed for a disposable test machine.

---

## Step 13 – Monitoring
Disable **Boot diagnostics**, **OS guest diagnostics**, and alerts if you prefer to configure monitoring manually later. For a test VM this is acceptable. In production, always enable at minimum boot diagnostics and basic CPU/memory alerts.

---

## Step 14 – Review + Create
Azure will validate the configuration. Review the estimated monthly cost shown at the bottom. Click **Create** and wait for deployment (~2–3 minutes). Once deployed, connect via **RDP** using the public IP address and the credentials set in Step 7.

---

> 💡 **Cost tip:** When not actively using the VM, **Stop (deallocate)** it from the Azure portal. A deallocated VM does not incur compute charges – you only pay for the disk storage.
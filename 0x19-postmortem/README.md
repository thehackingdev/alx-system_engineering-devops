Postmortem: Website Outage on 2024-07-22
Issue Summary
Duration: 2 hours and 15 minutes (12:45 PM EAT - 3:00 PM EAT)
Impact: The company's primary website was completely inaccessible to all users during this period. This resulted in significant disruption to customer service, sales, and online operations.Root Cause: A misconfigured firewall rule was blocking incoming traffic to the website's servers.

Timeline
12:45 PM EAT: The first reports of the outage were received from customers.
12:50 PM EAT: The operations team initiated an investigation into the issue.
1:15 PM EAT: The team suspected a network connectivity problem and began troubleshooting the network infrastructure.
1:45 PM EAT: After ruling out network issues, the investigation focused on the web servers and application code.
2:30 PM EAT: A misconfigured firewall rule was identified as the root cause.
2:45 PM EAT: The firewall rule was corrected.
3:00 PM EAT: The website was restored to full functionality.
Root Cause and Resolution
The outage was caused by a misconfigured firewall rule that was blocking incoming HTTP traffic to the website's servers. This rule had been inadvertently added during a recent security update.

To resolve the issue, the misconfigured firewall rule was removed and the firewall was restarted. This allowed incoming traffic to reach the web servers and restored the website's functionality.

Corrective and Preventative Measures
Review firewall configuration: Conduct a thorough review of all firewall rules to ensure they are accurate and up-to-date.
Implement change management procedures: Establish strict change management procedures to prevent accidental configuration changes.
Enhance monitoring: Improve monitoring capabilities to detect issues more quickly and proactively.
Conduct regular security audits: Conduct regular security audits to identify and address potential vulnerabilities.
Provide training: Provide training to staff members on firewall management and security best practices.
Specific Tasks:

Firewall review: Conduct a comprehensive review of all firewall rules within the next week.
Change management policy: Develop and implement a formal change management policy within the next month.
Monitoring enhancements: Add additional monitoring metrics for network traffic, server load, and firewall rules.
Security audit: Schedule a security audit to be conducted within the next quarter.
Training sessions: Conduct training sessions on firewall management and security best practices for relevant staff members.

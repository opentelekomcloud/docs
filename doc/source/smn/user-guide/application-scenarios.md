# Application Scenarios<a name="smn_pd_22000"></a>

-   **System notifications**

    After events or alarms are triggered, SMN can send notifications to specified users by email, SMS message, or HTTP/HTTPS message. For example, Cloud Trace Service \(CTS\) detects key cloud service operations and uses SMN to notify you and other users.

-   **Integrating with cloud services**

    SMN can functions as a message middleware to connect cloud services, reducing system complexity and improving efficiency. For example, Cloud Eye does not have to be integrated with Object Storage Service \(OBS\) to interact with each other. Instead, they are connected by SMN. Therefore, faults in one service will not affect the other.

-   **Off-peak traffic control**

    If there is a discrepancy between processing capabilities of the upstream and downstream systems, SMN can cache data to reduce downstream pressure to reduce breakdowns, enhance availability, and mitigate complexity in the system.



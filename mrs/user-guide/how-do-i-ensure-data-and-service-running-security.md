# How Do I Ensure Data and Service Running Security?<a name="EN-US_TOPIC_0125375514"></a>

MRS is a platform for massive data management and analysis and features high security. It ensures user data and service running security from the following aspects:

-   Network isolation

    The public cloud divides the entire network into two planes: the service plane and management plane. The two planes are physically isolated to ensure security of the service and management networks.

    -   Service plane

        Network plane where cluster components are running. It provides service channels for users and delivers data access, task submitting, and computing functions.

    -   Management plane

        Public cloud console. It is used to apply for and manage MRS.


-   Host security

    Users can deploy third-party antivirus software based on their service requirements. For the operating system \(OS\) and interfaces, MRS provides the following security protection measures:

    -   Hardening OS kernel security
    -   Installing the latest OS patch
    -   Controlling the OS rights
    -   Managing OS interfaces
    -   Preventing the OS protocols and interfaces from attacks

-   Data security

    MRS stores data on the OBS platform, ensuring data security.

-   Data integrity

    After processing data, MRS encrypts and transmits data to the OBS system through SSL, ensuring data integrity.



# Configuring a Lifecycle Rule<a name="en-us_topic_0045853854"></a>

You can configure a lifecycle management rule for a bucket, and applicable objects in the bucket will be managed by the rule.

## Procedure<a name="s359ce6c524924685935216cccfb24694"></a>

1.  Log in to OBS Browser.
2.  Click the blank area in the row of the bucket for which you want to configure a lifecycle rule and choose  **More**  \>  **Configure Lifecycle Rule**.
3.  In the  **Configure Lifecycle Rule**  dialog box, click  **Create**. The dialog box in  [Figure 1](#fig49848587164214)  is displayed.

    **Figure  1**  Creating a lifecycle rule<a name="fig49848587164214"></a>  
    ![](figures/creating-a-lifecycle-rule-5.png "creating-a-lifecycle-rule-5")

4.  Configure a lifecycle rule.

    **Basic Information**:

    -   **Status**: 

        Select  **Enable**  to enable the lifecycle rule.

    -   **Rule Name**: 

        Identify lifecycle rules. The  **Rule Name**  contains a maximum of 255 characters.

    -   **Applies To**: Can be set to  **Object name prefix**  or  **Bucket**.
        -   **Object name prefix**: Objects that have the specified prefix will be managed by the lifecycle rule. The prefix cannot start with a slash \(/\), cannot have consecutive slashes \(/\), and cannot contain the following special characters:  **\\:\*?"<\>|**
        -   **Bucket**: All objects in the bucket will be managed by the lifecycle rule.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   When  **Object name prefix**  is selected and the specified prefix and the prefix of an existing lifecycle rule overlap, OBS regards the two rules as one and disables the one to be configured. For example, if a rule with prefix  **abc**  exists in the system, another rule whose prefix starts with  **abc**  cannot be configured.
    >-   If a lifecycle rule whose  **Applies To**  is set to  **Object name prefix**  has been configured, you cannot configure a lifecycle rule whose  **Applies To**  is set to  **Bucket**.
    >-   If a lifecycle rule has been configured for the entire bucket, no more rules that apply to object name prefix can be added.

    **Current Version**  or  **Historical Version**:

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   **Current Version**  and  **Historical Version**  are two concepts for  **Versioning**. If  **Versioning**  is enabled, uploading objects with the same name to the same path generates different versions. The object uploaded lastly is called  **Current Version**, and the object uploaded earlier is called  **Historical Version**.
    >-   You can configure either, both, or neither of the versions.

    -   **Transition to Warm**: You can specify the number of days after which objects that have been last updated and meet specified conditions are automatically transitioned to  **Warm**. This number must be at least 30.
    -   **Transition to Cold**: You can specify the number of days after which objects that have been last updated and meet specified conditions are automatically transitioned to  **Cold**. If objects are configured to be transitioned to both  **Warm**  and  **Cold**, the number of days for transition to  **Cold**  must be at least 30 days later than that for transition to  **Warm**. If only transition to Cold is enabled and transition to  **Warm**  is disabled, there is no limit on the number of days for transition.
    -   Deleted upon expiration: You can specify the number of days after which objects that have been last updated and meet the specified conditions are automatically deleted. The expiration time must be greater than the two transition times.

    For example, the following files are stored in OBS on January 7, 2015:

    -   log/test1.log
    -   log/test2.log
    -   doc/example.doc
    -   doc/good.txt

    The following files are stored in OBS on January 10, 2015:

    -   log/clientlog.log
    -   log/serverlog.log
    -   doc/work.doc
    -   doc/travel.txt

        If the expiration time of objects prefixed with  **log**  is set to January 11, 2015 on January 10, 2015, OBS will delete objects  **log/test1.log**,  **log/test2.log**,  **log/clientlog.log**, and  **log/serverlog.log**  on January 12, 2015.

        On the current day, if you set the objects with the name prefix  **log**  to be transitioned to  **Warm**  30 days later, transitioned to  **Cold**  60 days later, and deleted 100 days later, then OBS will transition  **log/clientlog.log**,  **log/serverlog.log**,  **log/test1.log**, and  **log/test2.log**  to  **Warm**  on the 31st day, transition them to  **Cold**  the 61st day, and delete them on the 101st day.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >The storage class transition and deletion of an object may be delayed after the time condition is met. Generally, the delay does not exceed 48 hours. If you change the configurations of an existing lifecycle rule, the effective time of the lifecycle rule will change according to the new configurations.

5.  Click  **Save**.
6.  In the  **Create Lifecycle Rule**  dialog box, click  **Save**.
7.  In the displayed dialog box, click  **Close**  to close the dialog box.


# Why Cannot I Perform Index Backup?<a name="css_02_0029"></a>

Index backup is implemented by creating cluster snapshots. If you cannot perform index backup, perform the following steps:

## Check Whether the Account or IAM User Has the Index Backup Permission<a name="section131139185321"></a>

1.  Log in to the IAM management console.
2.  Check the user group, to which the account or the IAM user belongs.

    For details, see  [Viewing or Modifying User Information](https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0046661675.html).

3.  Check whether the permissions assigned to the user group contain the following:  **Tenant Administrator**  for project  **OBS**  in region  **Global service**  and  **CSS Administrator**  in the current region.

    For details, see  [Viewing and Modifying User Group Information](https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0085605493.html).

    -   If neither of the preceding permissions is contained, go to  [4](#li6702956162617).
    -   If both of the preceding permissions are contained, contact the customer service.

4.  <a name="li6702956162617"></a>Add the following permissions to the user group:  **Tenant Administrator**  for project  **OBS**  in region  **Global service**  and  **CSS Administrator**  in the current region.

    For details, see  [Viewing and Modifying User Group Information](https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0085605493.html).



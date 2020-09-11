# Effect<a name="obs_03_0115"></a>

A bucket policy can either allow or deny the access requests that match the configuration.

-   **Allow**: Indicates that access requests are allowed, if they match the configurations of the bucket policy.
-   **Deny**: Indicates that access requests are denied, if they match the configurations of the bucket policy.

When a bucket policy contains both the allow and deny effects, the deny effect prevails. The following figure shows the judgment process.

**Figure  1**  Determining a bucket policy when the allow and deny statements conflict<a name="fig15111849151"></a>  
![](figures/determining-a-bucket-policy-when-the-allow-and-deny-statements-conflict.png "determining-a-bucket-policy-when-the-allow-and-deny-statements-conflict")

1.  A user initiates an access request.
2.  OBS preferentially searches for deny \(explicit deny\) effects from bucket policies. If a deny statement is found, OBS directly rejects the access. The access request ends.
3.  If there is no deny statement, OBS searches for allow statements.
    -   If an allow statement is found, OBS allows the access.
    -   If no allow statement is found, OBS rejects the access. The access request ends.

4.  If an error occurs during the judgment, an error message is generated and returned to the user who initiates the access request.


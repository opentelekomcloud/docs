# Why Is the Message "Connect IAM Timeout" Displayed When I Attempt to Access DMS?<a name="EN-US_TOPIC_0128036929"></a>

## Symptom<a name="section1296910476388"></a>

An error message "Connect IAM Timeout" is displayed when I attempt to use the API to access DMS.

```
Get quota fail: 401
{"message": "Connect IAM Timeout", "request_id": 
"5ACB6B21-DAF6-47C8-B7A4-45A7BDC57FC6"}
```

## Possible Cause<a name="section144290562385"></a>

The AK/SK pair is deleted on the web-based DMS console.

## Troubleshooting Method<a name="section1212331917398"></a>

1.  Log in to the management console.
2.  Click the username and select  **My Credential**  from the drop-down list.
3.  Click  **Access Keys**.
4.  Click  **Add Access Key**.
5.  Enter  **Login Password**  and  **Verification Code**  and click  **OK**. Download the access key and keep it secure.
6.  Use the new AK/SK pair to access DMS.


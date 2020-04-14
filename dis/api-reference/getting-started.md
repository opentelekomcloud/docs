# Getting Started<a name="dis_02_0003"></a>

This section describes how to create a DIS stream by calling APIs.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The token obtained on IAM is valid for only 24 hours. If you want to use one token for authentication, you can cache it to avoid frequent calling.  

## Involved APIs<a name="section101152312311"></a>

If you use a token for authentication, you must obtain the token and add  **X-Auth-Token**  to the request header of the API when making an API call.

-   API for obtaining tokens from IAM
-   API for creating a DIS stream

## Procedure<a name="section84735913247"></a>

1.  Obtain the token by following instructions in  [Token-based Authentication](authentication.md#en-us_topic_0121671869_section2417768214391).
2.  Send  **POST https://Endpoint of DIS/v2/\{project\_id\}/streams**.
3.  Add  **X-Auth-Token**  to the request header.
4.  Specify the following parameters in the request body:

    ```
    {
    	"stream_name": "dis-DLpR",
    	"partition_count": 1,
    	"stream_type": "COMMON",
    	"data_type": "BLOB",
    	"data_duration": 24
    }
    ```

    If the request is successful, 201 Created is returned.

    If the request fails, an error code and error information are returned. For details, see section  [Error Codes](error-codes.md).



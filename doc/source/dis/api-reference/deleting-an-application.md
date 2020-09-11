# Deleting an Application<a name="dis_02_0402"></a>

## Function<a name="section41939787192343"></a>

This API is used to delete an application.

## URI<a name="section39571706192343"></a>

-   URI format

    DELETE /v2/\{project\_id\}/apps/\{app\_name\}

-   Parameter description

    None


## Request<a name="section31421545192343"></a>

-   Example request

    ```
    DELETE 
    https://{endpoint}/v2/{project_id}/apps/apptest        
    ```

-   Parameter description

    None


## Response<a name="section52057961192343"></a>

-   If the DIS stream was successfully deleted, a 204 response with an empty response body is returned. For details about status codes, see  [Status Codes](status-codes.md).
-   If the DIS stream failed to be created, identify the failure cause according to the response body and the instructions in  [Error Codes](error-codes.md).

## Status Code<a name="section49045827192343"></a>

-   Normal

    204 NOCONTENT

-   Failed

    For more information, see  [Error Codes](error-codes.md).



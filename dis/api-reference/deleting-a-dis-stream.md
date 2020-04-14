# Deleting a DIS Stream<a name="dis_02_0017_01"></a>

## Function<a name="section6066224117376"></a>

This API is used to delete a DIS stream after pushing or pulling data to or from the stream or if the stream does not run properly.

Before deleting a stream, you need to specify the stream name.

## URI<a name="section6514164517376"></a>

-   URI format

    DELETE /v2/\{project\_id\}/streams/\{stream\_name\}

-   Parameter description

    None


## Request<a name="section5421239117376"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v2/{project_id}/streams/stream_test
    ```

-   Parameter description

    None


## Response<a name="section6576977617376"></a>

-   If the DIS stream was successfully deleted, a 204 response with an empty response body is returned. For details about status codes, see  [Status Codes](status-codes.md).
-   If the DIS stream failed to be created, identify the failure cause according to the response body and the instructions in  [Error Codes](error-codes.md).

## Status Code<a name="section2384767417376"></a>

-   Normal

    204 NOCONTENT

-   Failed

    For more information, see  [Error Codes](error-codes.md).



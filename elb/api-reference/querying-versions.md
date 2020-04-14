# Querying Versions<a name="EN-US_TOPIC_0109430491"></a>

## Function<a name="en-us_topic_0049143278_section64833508"></a>

Queries all available versions.

If there is no version added to the URL, all available versions are returned.

## URI<a name="en-us_topic_0049143278_section46630661"></a>

GET /

## Request<a name="en-us_topic_0049143278_section17022773"></a>

None

## Response<a name="en-us_topic_0049143278_section18987236"></a>

None

## Example<a name="section1481434242515"></a>

-   Example request

    ```
    GET /
    ```


-   Example response

    ```
    {
       "versions": [
          {
              "status": "CURRENT",
              "id": "v2.0",
              "links": [
             {
                "href": "http://192.168.82.231:9696/v2.0",
                "rel": "self"
             }
            ]
           }
         ]
    }
    ```



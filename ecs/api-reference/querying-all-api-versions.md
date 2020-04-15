# Querying All API Versions<a name="EN-US_TOPIC_0065792793"></a>

## Function<a name="section54478915181842"></a>

This API is used to query all available Nova versions.

To support function extension, Nova APIs can be distinguished by version. There are two types of versions:

-   Major version: Independent URL
-   Microversion: Used by the HTTP request header X-OpenStack-Nova-API-Version. Since microversion 2.27, the new microversion header OpenStack-API-Version has been supported.

## URI<a name="section53791107181842"></a>

GET /

## Request<a name="section108201017144216"></a>

None

## Response<a name="section89511024194216"></a>

None

## Example Request<a name="section39878380181842"></a>

```
GET https://{endpoint}/
```

## Example Response<a name="section569124244211"></a>

```
{
 "versions": [{
  "links": [{
   "rel": "self",
   "href": "https://ecs.service.domain.com:443/v2/"
  }],
  "id": "v2.0",
  "updated": "2001-09-21T12:33:21Z",
  "status": "SUPPORTED"
 }]
}
```

## Returned Values<a name="section12571834"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


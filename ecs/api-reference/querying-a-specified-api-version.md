# Querying a Specified API Version<a name="EN-US_TOPIC_0065792794"></a>

## Function Description<a name="section553655182144"></a>

This API is used to query the information of a specified version.

To support function extension, Nova APIs can be distinguished by version. There are two types of versions:

-   Major version: Independent URL
-   Microversion: Used by the HTTP request header X-OpenStack-Nova-API-Version. Since version 2.27, the new microversion header OpenStack-API-Version has been supported.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the OpenStack-API-Version request header is used, the version is in the format of "compute microversion".  
    >For example, if  **key**  is set to  **OpenStack-API-Version**, set  **value**  to  **compute 2.27**.  


## URI<a name="section961608182144"></a>

GET /\{api\_version\}

[Table 1](#table46110007)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="18.291829182918292%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.111811181118114%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="63.596359635963594%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="18.291829182918292%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="18.111811181118114%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.596359635963594%" headers="mcps1.2.4.1.3 "><p id="p37195178"><a name="p37195178"></a><a name="p37195178"></a>Specifies an API version, such as V2.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section108201017144216"></a>

None

## Response<a name="section89511024194216"></a>

None

## Example Request<a name="section19667838182144"></a>

```
GET https://{endpoint}/v2
```

## Example Response<a name="section20327115469"></a>

```
{
 "version": {
  "min_version": "",
  "media-types": [{
   "type": "application/vnd.openstack.compute+json;version=2",
   "base": "application/json"
  }],
  "links": [{
   "rel": "self",
   "href": "https://ecs.service.domain.com:443/v2/"
  },
  {
   "rel": "describedby",
   "href": "http://docs.openstack.org/",
   "type": "text/html"
  }],
  "id": "v2.0",
  "updated": "1999-02-20T11:33:21Z",
  "version": "",
  "status": "SUPPORTED"
 }
}
```

## Returned Values<a name="section12571834"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


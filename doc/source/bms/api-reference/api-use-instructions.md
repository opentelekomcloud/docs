# API Use Instructions<a name="EN-US_TOPIC_0171226371"></a>

-   BMS does not have independent endpoints. When API calls are made to the BMS service, ECS APIs are used. Therefore, ensure that you use the ECS service endpoints when you make calls to the BMS service APIs.
-   For details about network service APIs, see  _Virtual Private Cloud API Reference_.
-   To support function extension, Nova APIs can be distinguished by version. There are two types of versions:
    -   Major version: independent URL
    -   Microversion: Used by the HTTP request header X-OpenStack-Nova-API-Version. Since microversion 2.27, the new microversion header OpenStack-API-Version has been supported.



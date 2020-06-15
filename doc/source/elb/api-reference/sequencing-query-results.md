# Sequencing Query Results<a name="EN-US_TOPIC_0109430489"></a>

APIs v2.0 enable the system to sort queried results based on customized keys by adding the  **sort\_key**  and  **sort\_dir**  parameters to the URL of the list request.  **sort\_key**  specifies the parameter used for sequencing results, and  **sort\_dir**  specifies whether results are displayed in ascending or descending order. These APIs allow sorting query results by multiple criteria. The number of  **sort\_key**  parameters must be equal to that of  **sort\_dir**  parameters. Otherwise, 400 status code is returned.

## Example Request<a name="en-us_topic_0049143235_section10739296"></a>

```
GET /v2.0/networks?sort_key=name&sort_dir=asc&sort_key=status&sort_dir=desc
```

## Example Response<a name="en-us_topic_0049143235_section29544808"></a>

```
{
    "networks": [
        {
            "status": "ACTIVE",
            "subnets": [],
            "name": "liudongtest ",
            "admin_state_up": false,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "60c809cb-6731-45d0-ace8-3bf5626421a9"
        },
        {
            "status": "ACTIVE",
            "subnets": [
                "132dc12d-c02a-4c90-9cd5-c31669aace04"
            ],
            "name": "publicnet",
            "admin_state_up": true,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "9daeac7c-a98f-430f-8e38-67f9c044e299"
        },
        {
            "status": "ACTIVE",
            "subnets": [
                "e25189a8-54df-4948-9396-d8291ffc92a0"
            ],
            "name": "testnet01",
            "admin_state_up": true,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "3d42a0d4-a980-4613-ae76-a2cddecff054"
        }
    ]
}
```


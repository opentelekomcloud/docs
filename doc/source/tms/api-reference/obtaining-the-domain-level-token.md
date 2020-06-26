# Obtaining the Domain-Level Token<a name="EN-US_TOPIC_0186103096"></a>

```

Content-Type: application/json

{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "username",
                    "password": "********",
                    "domain": {
                        "name": "domainname"
                    }
                }
            }
        },
        "scope": {
            "domain": {
                "id": "xxxxxxxxxxxxxxxxxx"
            }
        }
    }
}
```


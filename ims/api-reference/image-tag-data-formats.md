# Image Tag Data Formats<a name="EN-US_TOPIC_0020092110"></a>

## Description<a name="section45233201155329"></a>

You can attach a custom tag to a private image to facilitate private image management. 

## Data Formats<a name="section1440214081613"></a>

Data format of  **tag**

-   The data format is  _key.value_. If a key is added, a tag is added. In other cases, the tag is modified.
-   The tag key can contain a maximum of 36 characters, and the tag value can contain a maximum of 43 characters. The tag value can be an empty character string.
-   The tag can contain only digits, letters, underscores \(\_\), and hyphens \(-\).

Data format of  **image\_tags**

-   The data format is  _\{"key": "keyA", "value": "valueA"\}_. If the added key A exists, the tag is updated.
-   The tag key can contain a maximum of 36 characters, and the tag value can contain a maximum of 43 characters. The tag value can be an empty character string.
-   If the first and last characters of the tag key and value are spaces, the system deletes the space by default.

## Data Formats \(Native OpenStack\)<a name="section159141650141610"></a>

Data format of  **tag**

-   The data format is  _key_. If a key is added, a tag is added. In other cases, the tag is modified.
-   The tag key can contain a maximum of 255 characters.
-   The tag can contain only digits, letters, underscores \(\_\), and hyphens \(-\).


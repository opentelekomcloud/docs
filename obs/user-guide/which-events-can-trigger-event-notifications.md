# Which Events Can Trigger Event Notifications?<a name="obs_faq_0051"></a>

OBS supports event notification for the following event types:

-   **ObjectCreated**: Indicates all kinds of object creation operations, including PUT, POST, and COPY of objects, as well as the merging of parts.
-   **Put**: Uploads an object using the PUT method.
-   **Post**: Uploads an object using the POST method.
-   **Copy**: Uploads an object using the COPY method.
-   **CompleteMultipartUpload**: Merges parts of multipart tasks.
-   **ObjectRemoved**: Deletes an object.
-   **Delete**: Deletes an object with a specified version ID.
-   **DeleteMarkerCreated**: Deletes an object without specifying a version ID.


# What Do I Do If I Cannot Create an Image in the ZVHD2 Format Using an API?<a name="EN-US_TOPIC_0096558549"></a>

## Symptom<a name="section68201641162612"></a>

When you create a ZVHD2 image using an API, the image is created in the ZVHD format.

## Solution<a name="section35241152710"></a>

Check whether your token contains the  **op\_gated\_lld**  role \(**op\_gated\_lld**  is the OBT tag, which can be viewed in the body of the response message of the API used to obtain a user token\). The ZVHD2 image has the lazy loading feature. If the current environment does not support this feature or this feature is in the OBT phase, the ZVHD2 image will fail to be created.

Contact the customer service to ensure that the current environment supports the lazy loading feature, obtain a new token, and use the new token to create an image.


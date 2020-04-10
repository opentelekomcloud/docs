# What Do I Do If an Exception Occurs When I Start an ECS Created from an Image Using the UEFI Boot Mode?<a name="EN-US_TOPIC_0161870891"></a>

## Symptom<a name="section4353658111611"></a>

An ECS created from a private image using the UEFI boot mode cannot start.

## Possible Causes<a name="section194097751714"></a>

The image OS uses the UEFI boot mode, but the uefi attribute is not added to the image attributes.

## Handling Method <a name="section178071112161718"></a>

1.  Delete the ECS that fails to start.
2.  Call the API to update the image attributes and change the value of  **hw\_firmware\_type**  to  **uefi**.

    API URI: PATCH /v2/cloudimages/\{image\_id\}

    For details about how to call the API, see "Updating Image Information" in  _Image Management Service API Reference_.

3.  Use the updated image to create an ECS again.


# Expanding the Capacity of an EVS Disk<a name="EN-US_TOPIC_0093492522"></a>

## Scenarios<a name="section127252030132218"></a>

When your disk space is insufficient, you can handle the insufficiency by expanding the disk capacity.

## Procedure<a name="section718121118257"></a>

The capacity of an EVS disk can be expanded in either of the following ways:

-   Create an EVS disk and attach it to an ECS.
-   Expand the capacity of an existing EVS disk. The capacities of both system disks and data disks can be expanded.

    You can expand the disk capacities when the EVS disks are in the  **In-use**  or  **Available**  state.

    -   Expanding an  **In-use**  EVS disk means that the to-be-expanded EVS disk has been attached to an ECS. Only certain ECS OSs support the expansion of  **In-use**  EVS disks. For details, see "Expanding an  **In-use**  EVS Disk" in  _Elastic Volume Service User Guide_.
    -   Expanding an  **Available**  EVS disk means that the to-be-expanded EVS disk has not been attached to an ECS. For details, see "Expanding an Available EVS Disk" in  _Elastic Volume Service User Guide_.



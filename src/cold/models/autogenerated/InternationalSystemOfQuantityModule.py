
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandardizedPhysicalQuantityModule import StandardizedPhysicalQuantity







class InternationalSystemOfQuantity(StandardizedPhysicalQuantity):
    """
    Class representing the `InternationalSystemOfQuantity` entity, which inherits from:
    - StandardizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f35cff4d_dc09_44cf_a729_22fb79e3bfb2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InternationalSystemOfQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InternationalSystemOfQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_f35cff4d_dc09_44cf_a729_22fb79e3bfb2',
    
    class_name='InternationalSystemOfQuantity',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f35cff4d_dc09_44cf_a729_22fb79e3bfb2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InternationalSystemOfQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    
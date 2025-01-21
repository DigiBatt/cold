
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalQuantityModule import PhysicalQuantity







class StandardizedPhysicalQuantity(PhysicalQuantity):
    """
    Class representing the `StandardizedPhysicalQuantity` entity, which inherits from:
    - PhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9c407ac0_fd4c_4178_8763_95fad9fe29ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardizedPhysicalQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandardizedPhysicalQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_9c407ac0_fd4c_4178_8763_95fad9fe29ec',
    
    class_name='StandardizedPhysicalQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9c407ac0_fd4c_4178_8763_95fad9fe29ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardizedPhysicalQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
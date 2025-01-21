
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalObjectModule import PhysicalObject







class CompositePhysicalObject(PhysicalObject):
    """
    Class representing the `CompositePhysicalObject` entity, which inherits from:
    - PhysicalObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_57d977ab_0036_4779_b59a_e47620afdb9c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompositePhysicalObject'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompositePhysicalObject(
    
    class_iri='https://w3id.org/emmo#EMMO_57d977ab_0036_4779_b59a_e47620afdb9c',
    
    class_name='CompositePhysicalObject',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_57d977ab_0036_4779_b59a_e47620afdb9c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompositePhysicalObject',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
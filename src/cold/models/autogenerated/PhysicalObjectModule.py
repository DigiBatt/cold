
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicallyInteractingConvexModule import PhysicallyInteractingConvex







class PhysicalObject(PhysicallyInteractingConvex):
    """
    Class representing the `PhysicalObject` entity, which inherits from:
    - PhysicallyInteractingConvex

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_38b579de_4331_40e0_803d_09efa298e726'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalObject'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalObject(
    
    class_iri='https://w3id.org/emmo#EMMO_38b579de_4331_40e0_803d_09efa298e726',
    
    class_name='PhysicalObject',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_38b579de_4331_40e0_803d_09efa298e726',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalObject',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    
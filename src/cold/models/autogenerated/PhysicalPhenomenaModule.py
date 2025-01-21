
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicallyInteractingModule import PhysicallyInteracting







class PhysicalPhenomena(PhysicallyInteracting):
    """
    Class representing the `PhysicalPhenomena` entity, which inherits from:
    - PhysicallyInteracting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5cc4e111_3eb1_44a3_9369_5af3846cf605'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalPhenomena'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalPhenomena(
    
    class_iri='https://w3id.org/emmo#EMMO_5cc4e111_3eb1_44a3_9369_5af3846cf605',
    
    class_name='PhysicalPhenomena',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5cc4e111_3eb1_44a3_9369_5af3846cf605',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalPhenomena',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
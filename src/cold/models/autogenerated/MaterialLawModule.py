
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NaturalLawModule import NaturalLaw







class MaterialLaw(NaturalLaw):
    """
    Class representing the `MaterialLaw` entity, which inherits from:
    - NaturalLaw

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f19ff3b4_6bfe_4c41_a2b2_9affd39c140b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialLaw'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaterialLaw(
    
    class_iri='https://w3id.org/emmo#EMMO_f19ff3b4_6bfe_4c41_a2b2_9affd39c140b',
    
    class_name='MaterialLaw',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f19ff3b4_6bfe_4c41_a2b2_9affd39c140b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialLaw',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
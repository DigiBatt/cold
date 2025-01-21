
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StateOfMatterModule import StateOfMatter



from .ContinuumSubstanceModule import ContinuumSubstance







class Fluid(StateOfMatter, ContinuumSubstance):
    """
    Class representing the `Fluid` entity, which inherits from:
    - StateOfMatter, ContinuumSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_87ac88ff_8379_4f5a_8c7b_424a8fff1ee8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Fluid'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Fluid(
    
    class_iri='https://w3id.org/emmo#EMMO_87ac88ff_8379_4f5a_8c7b_424a8fff1ee8',
    
    class_name='Fluid',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_87ac88ff_8379_4f5a_8c7b_424a8fff1ee8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Fluid',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CondensedMatterModule import CondensedMatter



from .ContinuumSubstanceModule import ContinuumSubstance







class Solid(CondensedMatter, ContinuumSubstance):
    """
    Class representing the `Solid` entity, which inherits from:
    - CondensedMatter, ContinuumSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a2b006f2_bbfd_4dba_bcaa_3fca20cd6be1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Solid'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Solid(
    
    class_iri='https://w3id.org/emmo#EMMO_a2b006f2_bbfd_4dba_bcaa_3fca20cd6be1',
    
    class_name='Solid',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a2b006f2_bbfd_4dba_bcaa_3fca20cd6be1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Solid',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
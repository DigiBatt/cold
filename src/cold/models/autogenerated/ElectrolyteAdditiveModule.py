
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AdditiveModule import Additive







class ElectrolyteAdditive(Additive):
    """
    Class representing the `ElectrolyteAdditive` entity, which inherits from:
    - Additive

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_554286d4_1f46_44c0_bebc_4ddae00dbce1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrolyteAdditive'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrolyteAdditive(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_554286d4_1f46_44c0_bebc_4ddae00dbce1',
    
    class_name='ElectrolyteAdditive',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_554286d4_1f46_44c0_bebc_4ddae00dbce1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrolyteAdditive',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
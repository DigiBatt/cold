
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormFactorModule import FormFactor







class Coin(FormFactor):
    """
    Class representing the `Coin` entity, which inherits from:
    - FormFactor

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2522cbd8_5382_457f_b9b5_775860f83357'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Coin'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Coin(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2522cbd8_5382_457f_b9b5_775860f83357',
    
    class_name='Coin',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2522cbd8_5382_457f_b9b5_775860f83357',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Coin',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormFactorModule import FormFactor







class Pouch(FormFactor):
    """
    Class representing the `Pouch` entity, which inherits from:
    - FormFactor

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_af751d07_f0b7_43c7_911d_cba864189b2b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Pouch'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Pouch(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_af751d07_f0b7_43c7_911d_cba864189b2b',
    
    class_name='Pouch',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_af751d07_f0b7_43c7_911d_cba864189b2b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Pouch',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
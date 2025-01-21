
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticArrangementModule import HolisticArrangement







class Assembled(HolisticArrangement):
    """
    Class representing the `Assembled` entity, which inherits from:
    - HolisticArrangement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_52bbaaee_1145_4be3_8a5c_b366851ea1b9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Assembled'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Assembled(
    
    class_iri='https://w3id.org/emmo#EMMO_52bbaaee_1145_4be3_8a5c_b366851ea1b9',
    
    class_name='Assembled',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_52bbaaee_1145_4be3_8a5c_b366851ea1b9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Assembled',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
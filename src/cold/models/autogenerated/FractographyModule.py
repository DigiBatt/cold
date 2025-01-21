
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OpticalTestingModule import OpticalTesting







class Fractography(OpticalTesting):
    """
    Class representing the `Fractography` entity, which inherits from:
    - OpticalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Fractography'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Fractography'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Fractography(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Fractography',
    
    class_name='Fractography',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Fractography',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Fractography',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
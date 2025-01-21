
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SamplePreparationModule import SamplePreparation







class Milling(SamplePreparation):
    """
    Class representing the `Milling` entity, which inherits from:
    - SamplePreparation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Milling'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Milling'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Milling(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Milling',
    
    class_name='Milling',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Milling',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Milling',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
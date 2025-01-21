
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SamplePreparationModule import SamplePreparation







class Polishing(SamplePreparation):
    """
    Class representing the `Polishing` entity, which inherits from:
    - SamplePreparation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Polishing'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Polishing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Polishing(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Polishing',
    
    class_name='Polishing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Polishing',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Polishing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
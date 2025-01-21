
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataProcessingModule import DataProcessing







class CharacterisationDataValidation(DataProcessing):
    """
    Class representing the `CharacterisationDataValidation` entity, which inherits from:
    - DataProcessing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationDataValidation'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationDataValidation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationDataValidation(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationDataValidation',
    
    class_name='CharacterisationDataValidation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationDataValidation',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationDataValidation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
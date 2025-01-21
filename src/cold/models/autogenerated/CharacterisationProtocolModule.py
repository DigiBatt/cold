
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationProcedureModule import CharacterisationProcedure







class CharacterisationProtocol(CharacterisationProcedure):
    """
    Class representing the `CharacterisationProtocol` entity, which inherits from:
    - CharacterisationProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationProtocol'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationProtocol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationProtocol(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationProtocol',
    
    class_name='CharacterisationProtocol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationProtocol',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationProtocol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
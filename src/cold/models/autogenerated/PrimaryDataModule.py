
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationDataModule import CharacterisationData







class PrimaryData(CharacterisationData):
    """
    Class representing the `PrimaryData` entity, which inherits from:
    - CharacterisationData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PrimaryData'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PrimaryData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PrimaryData(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#PrimaryData',
    
    class_name='PrimaryData',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PrimaryData',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PrimaryData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    
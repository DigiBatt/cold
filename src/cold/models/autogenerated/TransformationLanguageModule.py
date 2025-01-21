
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstructionLanguageModule import ConstructionLanguage







class TransformationLanguage(ConstructionLanguage):
    """
    Class representing the `TransformationLanguage` entity, which inherits from:
    - ConstructionLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ea00dafc_ac92_4e67_aa65_ce5a29e77fcf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransformationLanguage'`
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
    obj = TransformationLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_ea00dafc_ac92_4e67_aa65_ce5a29e77fcf',
    
    class_name='TransformationLanguage',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ea00dafc_ac92_4e67_aa65_ce5a29e77fcf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransformationLanguage',
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
    

    
    

    

    
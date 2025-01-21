
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputerLanguageModule import ComputerLanguage







class ModellingLanguage(ComputerLanguage):
    """
    Class representing the `ModellingLanguage` entity, which inherits from:
    - ComputerLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_18c4634c_b821_49a3_beff_5eb7515ffc40'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ModellingLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ModellingLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_18c4634c_b821_49a3_beff_5eb7515ffc40',
    
    class_name='ModellingLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_18c4634c_b821_49a3_beff_5eb7515ffc40',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ModellingLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    
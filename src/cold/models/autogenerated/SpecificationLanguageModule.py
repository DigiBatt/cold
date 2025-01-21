
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputerLanguageModule import ComputerLanguage







class SpecificationLanguage(ComputerLanguage):
    """
    Class representing the `SpecificationLanguage` entity, which inherits from:
    - ComputerLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fb294e8d_603c_4fe5_bd71_8f4d152b2fb5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpecificationLanguage'`
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
    obj = SpecificationLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_fb294e8d_603c_4fe5_bd71_8f4d152b2fb5',
    
    class_name='SpecificationLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fb294e8d_603c_4fe5_bd71_8f4d152b2fb5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpecificationLanguage',
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
    

    
    

    

    
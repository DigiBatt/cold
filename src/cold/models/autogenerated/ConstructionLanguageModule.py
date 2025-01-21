
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputerLanguageModule import ComputerLanguage







class ConstructionLanguage(ComputerLanguage):
    """
    Class representing the `ConstructionLanguage` entity, which inherits from:
    - ComputerLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3ab914c1_5d8d_4a6e_804b_84aa89623c48'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstructionLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstructionLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_3ab914c1_5d8d_4a6e_804b_84aa89623c48',
    
    class_name='ConstructionLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3ab914c1_5d8d_4a6e_804b_84aa89623c48',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstructionLanguage',
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
    

    
    

    

    
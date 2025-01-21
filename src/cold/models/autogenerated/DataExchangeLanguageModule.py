
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputerLanguageModule import ComputerLanguage







class DataExchangeLanguage(ComputerLanguage):
    """
    Class representing the `DataExchangeLanguage` entity, which inherits from:
    - ComputerLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_13fea749_0b3b_4756_9c81_22cce620fc25'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataExchangeLanguage'`
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
    obj = DataExchangeLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_13fea749_0b3b_4756_9c81_22cce620fc25',
    
    class_name='DataExchangeLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_13fea749_0b3b_4756_9c81_22cce620fc25',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataExchangeLanguage',
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
    

    
    

    

    
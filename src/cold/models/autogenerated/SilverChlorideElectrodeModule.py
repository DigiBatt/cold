
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReferenceElectrodeModule import ReferenceElectrode







class SilverChlorideElectrode(ReferenceElectrode):
    """
    Class representing the `SilverChlorideElectrode` entity, which inherits from:
    - ReferenceElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6ec59f99_5f26_4a7d_9b90_b52e0f8ad190'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SilverChlorideElectrode'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SilverChlorideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6ec59f99_5f26_4a7d_9b90_b52e0f8ad190',
    
    class_name='SilverChlorideElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6ec59f99_5f26_4a7d_9b90_b52e0f8ad190',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SilverChlorideElectrode',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    
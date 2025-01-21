
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputerScienceModule import ComputerScience







class ComputerLanguage(ComputerScience):
    """
    Class representing the `ComputerLanguage` entity, which inherits from:
    - ComputerScience

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_19fe0747_6954_40cb_9f8f_b87498bc8e78'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ComputerLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ComputerLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_19fe0747_6954_40cb_9f8f_b87498bc8e78',
    
    class_name='ComputerLanguage',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_19fe0747_6954_40cb_9f8f_b87498bc8e78',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ComputerLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    
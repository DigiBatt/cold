
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectivePropertyModule import ObjectiveProperty







class ModelledProperty(ObjectiveProperty):
    """
    Class representing the `ModelledProperty` entity, which inherits from:
    - ObjectiveProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d0200cf1_e4f4_45ae_873f_b9359daea3cd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ModelledProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ModelledProperty(
    
    class_iri='https://w3id.org/emmo#EMMO_d0200cf1_e4f4_45ae_873f_b9359daea3cd',
    
    class_name='ModelledProperty',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d0200cf1_e4f4_45ae_873f_b9359daea3cd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ModelledProperty',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
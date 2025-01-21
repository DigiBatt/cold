
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticObjectModule import SemioticObject







class Declared(SemioticObject):
    """
    Class representing the `Declared` entity, which inherits from:
    - SemioticObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c9805ac9_a943_4be4_ac4b_6da64ba36c73'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Declared'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Declared(
    
    class_iri='https://w3id.org/emmo#EMMO_c9805ac9_a943_4be4_ac4b_6da64ba36c73',
    
    class_name='Declared',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c9805ac9_a943_4be4_ac4b_6da64ba36c73',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Declared',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
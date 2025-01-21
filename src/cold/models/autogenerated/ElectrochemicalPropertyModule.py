
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NominalPropertyModule import NominalProperty







class ElectrochemicalProperty(NominalProperty):
    """
    Class representing the `ElectrochemicalProperty` entity, which inherits from:
    - NominalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_900e357f_2ee3_425a_a0b6_322661117787'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalProperty(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_900e357f_2ee3_425a_a0b6_322661117787',
    
    class_name='ElectrochemicalProperty',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_900e357f_2ee3_425a_a0b6_322661117787',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalProperty',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
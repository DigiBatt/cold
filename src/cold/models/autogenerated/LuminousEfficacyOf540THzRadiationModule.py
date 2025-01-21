
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIExactConstantModule import SIExactConstant







class LuminousEfficacyOf540THzRadiation(SIExactConstant):
    """
    Class representing the `LuminousEfficacyOf540THzRadiation` entity, which inherits from:
    - SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_506f7823_52bc_40cb_be07_b3b1e10cce13'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LuminousEfficacyOf540THzRadiation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LuminousEfficacyOf540THzRadiation(
    
    class_iri='https://w3id.org/emmo#EMMO_506f7823_52bc_40cb_be07_b3b1e10cce13',
    
    class_name='LuminousEfficacyOf540THzRadiation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_506f7823_52bc_40cb_be07_b3b1e10cce13',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LuminousEfficacyOf540THzRadiation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
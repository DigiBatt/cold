
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FractionUnitModule import FractionUnit







class PressureFractionUnit(FractionUnit):
    """
    Class representing the `PressureFractionUnit` entity, which inherits from:
    - FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9d09022c_e7ae_4379_a765_4803a8a502a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PressureFractionUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PressureFractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_9d09022c_e7ae_4379_a765_4803a8a502a1',
    
    class_name='PressureFractionUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9d09022c_e7ae_4379_a765_4803a8a502a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PressureFractionUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
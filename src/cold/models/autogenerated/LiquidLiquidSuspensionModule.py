
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SuspensionModule import Suspension



from .LiquidModule import Liquid







class LiquidLiquidSuspension(Suspension, Liquid):
    """
    Class representing the `LiquidLiquidSuspension` entity, which inherits from:
    - Suspension, Liquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_47fe2379_be21_48d1_9ede_402f0faf494b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidLiquidSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidLiquidSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_47fe2379_be21_48d1_9ede_402f0faf494b',
    
    class_name='LiquidLiquidSuspension',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_47fe2379_be21_48d1_9ede_402f0faf494b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidLiquidSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
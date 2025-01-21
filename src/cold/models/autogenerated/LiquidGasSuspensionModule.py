
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SuspensionModule import Suspension



from .LiquidModule import Liquid







class LiquidGasSuspension(Suspension, Liquid):
    """
    Class representing the `LiquidGasSuspension` entity, which inherits from:
    - Suspension, Liquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_42185fe7_122c_4e0c_a3cd_659d3e21c389'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidGasSuspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidGasSuspension(
    
    class_iri='https://w3id.org/emmo#EMMO_42185fe7_122c_4e0c_a3cd_659d3e21c389',
    
    class_name='LiquidGasSuspension',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_42185fe7_122c_4e0c_a3cd_659d3e21c389',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidGasSuspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    
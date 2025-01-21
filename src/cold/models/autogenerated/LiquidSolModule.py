
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolModule import Sol



from .LiquidModule import Liquid







class LiquidSol(Sol, Liquid):
    """
    Class representing the `LiquidSol` entity, which inherits from:
    - Sol, Liquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4354ac74_7425_43ab_92e4_6dc19d1afee9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidSol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidSol(
    
    class_iri='https://w3id.org/emmo#EMMO_4354ac74_7425_43ab_92e4_6dc19d1afee9',
    
    class_name='LiquidSol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4354ac74_7425_43ab_92e4_6dc19d1afee9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidSol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
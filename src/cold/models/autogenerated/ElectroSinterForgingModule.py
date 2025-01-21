
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class ElectroSinterForging(Sintering):
    """
    Class representing the `ElectroSinterForging` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1b01c9c6_6367_498c_a04d_1a37499b3eff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectroSinterForging'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectroSinterForging(
    
    class_iri='https://w3id.org/emmo#EMMO_1b01c9c6_6367_498c_a04d_1a37499b3eff',
    
    class_name='ElectroSinterForging',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1b01c9c6_6367_498c_a04d_1a37499b3eff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectroSinterForging',
        alias="class_name"
    )
    

    
    

    

    
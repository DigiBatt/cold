
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolidAerosolModule import SolidAerosol







class Smoke(SolidAerosol):
    """
    Class representing the `Smoke` entity, which inherits from:
    - SolidAerosol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5a2af26d_99de_4e5e_b1cd_514be71420c3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Smoke'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Smoke(
    
    class_iri='https://w3id.org/emmo#EMMO_5a2af26d_99de_4e5e_b1cd_514be71420c3',
    
    class_name='Smoke',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5a2af26d_99de_4e5e_b1cd_514be71420c3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Smoke',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
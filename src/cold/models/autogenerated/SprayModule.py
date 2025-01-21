
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasLiquidSuspensionModule import GasLiquidSuspension







class Spray(GasLiquidSuspension):
    """
    Class representing the `Spray` entity, which inherits from:
    - GasLiquidSuspension

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_498aad49_f8d4_40a4_a9eb_efd563a0115f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Spray'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Spray(
    
    class_iri='https://w3id.org/emmo#EMMO_498aad49_f8d4_40a4_a9eb_efd563a0115f',
    
    class_name='Spray',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_498aad49_f8d4_40a4_a9eb_efd563a0115f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Spray',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermalCuttingModule import ThermalCutting







class FlameCutting(ThermalCutting):
    """
    Class representing the `FlameCutting` entity, which inherits from:
    - ThermalCutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e258099f_5361_463c_ba1d_51d7d730630f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FlameCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FlameCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_e258099f_5361_463c_ba1d_51d7d730630f',
    
    class_name='FlameCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e258099f_5361_463c_ba1d_51d7d730630f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FlameCutting',
        alias="class_name"
    )
    

    
    

    

    
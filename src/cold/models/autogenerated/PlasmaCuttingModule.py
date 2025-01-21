
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermalCuttingModule import ThermalCutting







class PlasmaCutting(ThermalCutting):
    """
    Class representing the `PlasmaCutting` entity, which inherits from:
    - ThermalCutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e2b08775_a0f6_4bf7_b228_53dc2299f114'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PlasmaCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PlasmaCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_e2b08775_a0f6_4bf7_b228_53dc2299f114',
    
    class_name='PlasmaCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e2b08775_a0f6_4bf7_b228_53dc2299f114',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PlasmaCutting',
        alias="class_name"
    )
    

    
    

    

    
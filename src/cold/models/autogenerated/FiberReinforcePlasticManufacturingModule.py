
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromLiquidModule import FormingFromLiquid







class FiberReinforcePlasticManufacturing(FormingFromLiquid):
    """
    Class representing the `FiberReinforcePlasticManufacturing` entity, which inherits from:
    - FormingFromLiquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c2d9d370_f9eb_40be_b01e_7ceba8f7457f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FiberReinforcePlasticManufacturing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FiberReinforcePlasticManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_c2d9d370_f9eb_40be_b01e_7ceba8f7457f',
    
    class_name='FiberReinforcePlasticManufacturing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c2d9d370_f9eb_40be_b01e_7ceba8f7457f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FiberReinforcePlasticManufacturing',
        alias="class_name"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class Ablation(SeparateManufacturing):
    """
    Class representing the `Ablation` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1a2cbca8_3d3b_4e2c_9a71_e39273937786'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Ablation'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Ablation(
    
    class_iri='https://w3id.org/emmo#EMMO_1a2cbca8_3d3b_4e2c_9a71_e39273937786',
    
    class_name='Ablation',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1a2cbca8_3d3b_4e2c_9a71_e39273937786',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Ablation',
        alias="class_name"
    )
    

    
    

    

    
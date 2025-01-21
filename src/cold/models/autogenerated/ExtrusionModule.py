
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing



from .FormingFromPlasticModule import FormingFromPlastic







class Extrusion(ReshapeManufacturing, FormingFromPlastic):
    """
    Class representing the `Extrusion` entity, which inherits from:
    - ReshapeManufacturing, FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c9a2307d_51d0_426b_ae2f_85f5a44934e0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Extrusion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Extrusion(
    
    class_iri='https://w3id.org/emmo#EMMO_c9a2307d_51d0_426b_ae2f_85f5a44934e0',
    
    class_name='Extrusion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c9a2307d_51d0_426b_ae2f_85f5a44934e0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Extrusion',
        alias="class_name"
    )
    

    
    

    

    
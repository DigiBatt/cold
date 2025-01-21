
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPowderModule import FormingFromPowder







class ThermalSprayingForming(FormingFromPowder):
    """
    Class representing the `ThermalSprayingForming` entity, which inherits from:
    - FormingFromPowder

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_16c41198_3881_4a34_bae5_993f88823993'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermalSprayingForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermalSprayingForming(
    
    class_iri='https://w3id.org/emmo#EMMO_16c41198_3881_4a34_bae5_993f88823993',
    
    class_name='ThermalSprayingForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_16c41198_3881_4a34_bae5_993f88823993',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermalSprayingForming',
        alias="class_name"
    )
    

    
    

    

    
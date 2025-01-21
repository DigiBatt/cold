
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquationModule import Equation







class AlgebricEquation(Equation):
    """
    Class representing the `AlgebricEquation` entity, which inherits from:
    - Equation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_98d65021_4574_4890_b2fb_46430841077f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlgebricEquation'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlgebricEquation(
    
    class_iri='https://w3id.org/emmo#EMMO_98d65021_4574_4890_b2fb_46430841077f',
    
    class_name='AlgebricEquation',
    
    example="example_value",
    
    hasSpatialPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_98d65021_4574_4890_b2fb_46430841077f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlgebricEquation',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    

    
    

    

    
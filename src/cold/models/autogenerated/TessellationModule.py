
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReductionisticModule import Reductionistic





from .TileModule import Tile





class Tessellation(Reductionistic):
    """
    Class representing the `Tessellation` entity, which inherits from:
    - Reductionistic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ee0466e4_780d_4236_8281_ace7ad3fc5d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tessellation'`
        - **Alias**: `class_name`
    
    - `hasDirectPart` (`Optional[Tile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDirectPart`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tessellation(
    
    class_iri='https://w3id.org/emmo#EMMO_ee0466e4_780d_4236_8281_ace7ad3fc5d2',
    
    class_name='Tessellation',
    
    hasDirectPart="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ee0466e4_780d_4236_8281_ace7ad3fc5d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tessellation',
        alias="class_name"
    )
    
    hasDirectPart: Optional[Tile] = Field(
        None,
        alias="hasDirectPart"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasDirectPart", pre=True, always=True)
    def validate_hasDirectPart(cls, value):
        if value is not None and not isinstance(value, Tile):
            raise ValueError(f"Field 'hasDirectPart' must be an instance of 'Tile' or its subclass.")
        return value
    
    

    

    
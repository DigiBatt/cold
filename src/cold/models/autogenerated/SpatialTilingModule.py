
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation







class SpatialTiling(SpatioTemporalTessellation):
    """
    Class representing the `SpatialTiling` entity, which inherits from:
    - SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8944581c_64da_46a9_be29_7074f7cc8098'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpatialTiling'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpatialTiling(
    
    class_iri='https://w3id.org/emmo#EMMO_8944581c_64da_46a9_be29_7074f7cc8098',
    
    class_name='SpatialTiling',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8944581c_64da_46a9_be29_7074f7cc8098',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpatialTiling',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
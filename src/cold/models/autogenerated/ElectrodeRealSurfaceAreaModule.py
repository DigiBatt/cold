
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeSurfaceAreaModule import ElectrodeSurfaceArea







class ElectrodeRealSurfaceArea(ElectrodeSurfaceArea):
    """
    Class representing the `ElectrodeRealSurfaceArea` entity, which inherits from:
    - ElectrodeSurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a82e16c3_b766_482f_be94_b8e9af37f6fc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeRealSurfaceArea'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodeRealSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a82e16c3_b766_482f_be94_b8e9af37f6fc',
    
    class_name='ElectrodeRealSurfaceArea',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a82e16c3_b766_482f_be94_b8e9af37f6fc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeRealSurfaceArea',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
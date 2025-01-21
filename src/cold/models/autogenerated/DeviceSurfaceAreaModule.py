
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SurfaceAreaModule import SurfaceArea







class DeviceSurfaceArea(SurfaceArea):
    """
    Class representing the `DeviceSurfaceArea` entity, which inherits from:
    - SurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde4e5f_ace4_41d1_b4d8_cbd63e6376e6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeviceSurfaceArea'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DeviceSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde4e5f_ace4_41d1_b4d8_cbd63e6376e6',
    
    class_name='DeviceSurfaceArea',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ccde4e5f_ace4_41d1_b4d8_cbd63e6376e6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DeviceSurfaceArea',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeSurfaceAreaModule import ElectrodeSurfaceArea







class ElectrochemicallyActiveSurfaceArea(ElectrodeSurfaceArea):
    """
    Class representing the `ElectrochemicallyActiveSurfaceArea` entity, which inherits from:
    - ElectrodeSurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bad1b6f4_1b26_40e2_b552_6d53873e3973'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicallyActiveSurfaceArea'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicallyActiveSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bad1b6f4_1b26_40e2_b552_6d53873e3973',
    
    class_name='ElectrochemicallyActiveSurfaceArea',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bad1b6f4_1b26_40e2_b552_6d53873e3973',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicallyActiveSurfaceArea',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
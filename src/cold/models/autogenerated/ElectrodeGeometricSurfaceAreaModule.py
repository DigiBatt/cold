
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeSurfaceAreaModule import ElectrodeSurfaceArea







class ElectrodeGeometricSurfaceArea(ElectrodeSurfaceArea):
    """
    Class representing the `ElectrodeGeometricSurfaceArea` entity, which inherits from:
    - ElectrodeSurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa7790d6_07bb_4b0f_9965_55966828f5f3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeGeometricSurfaceArea'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodeGeometricSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa7790d6_07bb_4b0f_9965_55966828f5f3',
    
    class_name='ElectrodeGeometricSurfaceArea',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa7790d6_07bb_4b0f_9965_55966828f5f3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeGeometricSurfaceArea',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
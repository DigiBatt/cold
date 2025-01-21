
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VolumetricSurfaceAreaModule import VolumetricSurfaceArea







class PositiveElectrodeActiveMaterialVolumetricSurfaceArea(VolumetricSurfaceArea):
    """
    Class representing the `PositiveElectrodeActiveMaterialVolumetricSurfaceArea` entity, which inherits from:
    - VolumetricSurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a1e73c5_e91b_4365_88d4_1e1f476bf776'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeActiveMaterialVolumetricSurfaceArea'`
        - **Alias**: `class_name`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PositiveElectrodeActiveMaterialVolumetricSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a1e73c5_e91b_4365_88d4_1e1f476bf776',
    
    class_name='PositiveElectrodeActiveMaterialVolumetricSurfaceArea',
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0a1e73c5_e91b_4365_88d4_1e1f476bf776',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeActiveMaterialVolumetricSurfaceArea',
        alias="class_name"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
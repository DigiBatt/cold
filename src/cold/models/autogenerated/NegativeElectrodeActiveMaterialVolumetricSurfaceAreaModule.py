
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VolumetricSurfaceAreaModule import VolumetricSurfaceArea







class NegativeElectrodeActiveMaterialVolumetricSurfaceArea(VolumetricSurfaceArea):
    """
    Class representing the `NegativeElectrodeActiveMaterialVolumetricSurfaceArea` entity, which inherits from:
    - VolumetricSurfaceArea

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f9b91e_a770_4e9b_837e_fa2a76019111'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActiveMaterialVolumetricSurfaceArea'`
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
    obj = NegativeElectrodeActiveMaterialVolumetricSurfaceArea(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f9b91e_a770_4e9b_837e_fa2a76019111',
    
    class_name='NegativeElectrodeActiveMaterialVolumetricSurfaceArea',
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5f9b91e_a770_4e9b_837e_fa2a76019111',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActiveMaterialVolumetricSurfaceArea',
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
    

    
    

    

    
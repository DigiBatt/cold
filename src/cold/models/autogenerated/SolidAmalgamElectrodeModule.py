
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetalElectrodeModule import MetalElectrode





from .ActiveMaterialModule import ActiveMaterial





class SolidAmalgamElectrode(MetalElectrode):
    """
    Class representing the `SolidAmalgamElectrode` entity, which inherits from:
    - MetalElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_65c90d8d_9712_4f3f_b830_d8163ec4cfcc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidAmalgamElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidAmalgamElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_65c90d8d_9712_4f3f_b830_d8163ec4cfcc',
    
    class_name='SolidAmalgamElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_65c90d8d_9712_4f3f_b830_d8163ec4cfcc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidAmalgamElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    hasActiveMaterial: Optional[ActiveMaterial] = Field(
        None,
        alias="hasActiveMaterial"
    )
    

    
    @validator("hasActiveMaterial", pre=True, always=True)
    def validate_hasActiveMaterial(cls, value):
        if value is not None and not isinstance(value, ActiveMaterial):
            raise ValueError(f"Field 'hasActiveMaterial' must be an instance of 'ActiveMaterial' or its subclass.")
        return value
    
    

    

    
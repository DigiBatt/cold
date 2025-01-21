
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetalElectrodeModule import MetalElectrode



from .ZincBasedElectrodeModule import ZincBasedElectrode





from .ActiveMaterialModule import ActiveMaterial





class ZincElectrode(MetalElectrode, ZincBasedElectrode):
    """
    Class representing the `ZincElectrode` entity, which inherits from:
    - MetalElectrode, ZincBasedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_424bf750_7df5_49b5_ba73_ba74397a166b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincElectrode'`
        - **Alias**: `class_name`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_424bf750_7df5_49b5_ba73_ba74397a166b',
    
    class_name='ZincElectrode',
    
    hasActiveMaterial="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_424bf750_7df5_49b5_ba73_ba74397a166b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincElectrode',
        alias="class_name"
    )
    
    hasActiveMaterial: Optional[ActiveMaterial] = Field(
        None,
        alias="hasActiveMaterial"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasActiveMaterial", pre=True, always=True)
    def validate_hasActiveMaterial(cls, value):
        if value is not None and not isinstance(value, ActiveMaterial):
            raise ValueError(f"Field 'hasActiveMaterial' must be an instance of 'ActiveMaterial' or its subclass.")
        return value
    
    

    

    
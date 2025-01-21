
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidMetalElectrodeModule import LiquidMetalElectrode





from .ActiveMaterialModule import ActiveMaterial





class MercuryElectrode(LiquidMetalElectrode):
    """
    Class representing the `MercuryElectrode` entity, which inherits from:
    - LiquidMetalElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df78745e_f9db_4830_88f0_8ce074fcb8ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MercuryElectrode'`
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
    obj = MercuryElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df78745e_f9db_4830_88f0_8ce074fcb8ff',
    
    class_name='MercuryElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df78745e_f9db_4830_88f0_8ce074fcb8ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MercuryElectrode',
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
    
    

    

    
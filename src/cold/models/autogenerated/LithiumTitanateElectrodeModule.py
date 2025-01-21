
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TitaniumBasedElectrodeModule import TitaniumBasedElectrode



from .MetalOxideElectrodeModule import MetalOxideElectrode





from .ActiveMaterialModule import ActiveMaterial





class LithiumTitanateElectrode(TitaniumBasedElectrode, MetalOxideElectrode):
    """
    Class representing the `LithiumTitanateElectrode` entity, which inherits from:
    - TitaniumBasedElectrode, MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d0fe07e_a629_479c_ab24_2846f209bb0b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumTitanateElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumTitanateElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d0fe07e_a629_479c_ab24_2846f209bb0b',
    
    class_name='LithiumTitanateElectrode',
    
    elucidation="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6d0fe07e_a629_479c_ab24_2846f209bb0b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumTitanateElectrode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
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
    
    

    

    
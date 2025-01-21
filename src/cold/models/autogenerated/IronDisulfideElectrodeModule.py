
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IronBasedElectrodeModule import IronBasedElectrode



from .ActiveElectrodeModule import ActiveElectrode





from .ActiveMaterialModule import ActiveMaterial





class IronDisulfideElectrode(IronBasedElectrode, ActiveElectrode):
    """
    Class representing the `IronDisulfideElectrode` entity, which inherits from:
    - IronBasedElectrode, ActiveElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2726dd5_69f0_4cb1_bd3c_4c48813e57e7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronDisulfideElectrode'`
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
    obj = IronDisulfideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2726dd5_69f0_4cb1_bd3c_4c48813e57e7',
    
    class_name='IronDisulfideElectrode',
    
    hasActiveMaterial="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d2726dd5_69f0_4cb1_bd3c_4c48813e57e7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronDisulfideElectrode',
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
    
    

    

    
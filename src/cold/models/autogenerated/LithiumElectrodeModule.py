
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumBasedElectrodeModule import LithiumBasedElectrode





from .ActiveMaterialModule import ActiveMaterial





class LithiumElectrode(LithiumBasedElectrode):
    """
    Class representing the `LithiumElectrode` entity, which inherits from:
    - LithiumBasedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_55775b50_b9d9_4d68_8cb5_38fcd7b9b54d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumElectrode'`
        - **Alias**: `class_name`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_55775b50_b9d9_4d68_8cb5_38fcd7b9b54d',
    
    class_name='LithiumElectrode',
    
    hasActiveMaterial="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_55775b50_b9d9_4d68_8cb5_38fcd7b9b54d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumElectrode',
        alias="class_name"
    )
    
    hasActiveMaterial: Optional[ActiveMaterial] = Field(
        None,
        alias="hasActiveMaterial"
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
    
    

    

    
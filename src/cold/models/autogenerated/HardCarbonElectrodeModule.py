
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CarbonBasedElectrodeModule import CarbonBasedElectrode



from .ActiveElectrodeModule import ActiveElectrode





from .ActiveMaterialModule import ActiveMaterial





class HardCarbonElectrode(CarbonBasedElectrode, ActiveElectrode):
    """
    Class representing the `HardCarbonElectrode` entity, which inherits from:
    - CarbonBasedElectrode, ActiveElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6235cc7c_2eee_432a_93af_47d7e05db007'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardCarbonElectrode'`
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
    obj = HardCarbonElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6235cc7c_2eee_432a_93af_47d7e05db007',
    
    class_name='HardCarbonElectrode',
    
    hasActiveMaterial="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6235cc7c_2eee_432a_93af_47d7e05db007',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardCarbonElectrode',
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
    
    

    

    
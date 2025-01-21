
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetalOxideElectrodeModule import MetalOxideElectrode





from .ActiveMaterialModule import ActiveMaterial





class FluorineDopedTinOxideElectrode(MetalOxideElectrode):
    """
    Class representing the `FluorineDopedTinOxideElectrode` entity, which inherits from:
    - MetalOxideElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_339e1ba1_2006_4f22_aac4_3ce75edf1088'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FluorineDopedTinOxideElectrode'`
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
    obj = FluorineDopedTinOxideElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_339e1ba1_2006_4f22_aac4_3ce75edf1088',
    
    class_name='FluorineDopedTinOxideElectrode',
    
    elucidation="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_339e1ba1_2006_4f22_aac4_3ce75edf1088',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FluorineDopedTinOxideElectrode',
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
    
    

    

    
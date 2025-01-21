
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CarbonBasedElectrodeModule import CarbonBasedElectrode



from .ActiveElectrodeModule import ActiveElectrode





from .ActiveMaterialModule import ActiveMaterial





class GraphiteElectrode(CarbonBasedElectrode, ActiveElectrode):
    """
    Class representing the `GraphiteElectrode` entity, which inherits from:
    - CarbonBasedElectrode, ActiveElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c831d963_629a_41ab_850f_97fb6841b739'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GraphiteElectrode'`
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
    obj = GraphiteElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c831d963_629a_41ab_850f_97fb6841b739',
    
    class_name='GraphiteElectrode',
    
    hasActiveMaterial="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c831d963_629a_41ab_850f_97fb6841b739',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GraphiteElectrode',
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
    
    

    

    
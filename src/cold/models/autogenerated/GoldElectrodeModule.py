
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GoldBasedElectrodeModule import GoldBasedElectrode





from .ActiveMaterialModule import ActiveMaterial





class GoldElectrode(GoldBasedElectrode):
    """
    Class representing the `GoldElectrode` entity, which inherits from:
    - GoldBasedElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6fec8cc1_4e6c_428e_8343_6cf3c286a185'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GoldElectrode'`
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
    obj = GoldElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6fec8cc1_4e6c_428e_8343_6cf3c286a185',
    
    class_name='GoldElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6fec8cc1_4e6c_428e_8343_6cf3c286a185',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GoldElectrode',
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
    
    

    

    
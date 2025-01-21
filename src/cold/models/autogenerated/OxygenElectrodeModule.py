
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasDiffusionElectrodeModule import GasDiffusionElectrode







class OxygenElectrode(GasDiffusionElectrode):
    """
    Class representing the `OxygenElectrode` entity, which inherits from:
    - GasDiffusionElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e2c91edd_dd01_4309_9735_6fe5280261d4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OxygenElectrode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OxygenElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e2c91edd_dd01_4309_9735_6fe5280261d4',
    
    class_name='OxygenElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e2c91edd_dd01_4309_9735_6fe5280261d4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OxygenElectrode',
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
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SupercapacitorModule import Supercapacitor







class ElectrochemicalDoubleLayerCapacitor(Supercapacitor):
    """
    Class representing the `ElectrochemicalDoubleLayerCapacitor` entity, which inherits from:
    - Supercapacitor

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b91180e7_97ae_49e2_bf82_5bf720e7fa66'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalDoubleLayerCapacitor'`
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
    obj = ElectrochemicalDoubleLayerCapacitor(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b91180e7_97ae_49e2_bf82_5bf720e7fa66',
    
    class_name='ElectrochemicalDoubleLayerCapacitor',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b91180e7_97ae_49e2_bf82_5bf720e7fa66',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalDoubleLayerCapacitor',
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
    

    
    

    

    
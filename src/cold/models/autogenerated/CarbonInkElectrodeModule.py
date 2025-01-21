
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CarbonPasteElectrodeModule import CarbonPasteElectrode







class CarbonInkElectrode(CarbonPasteElectrode):
    """
    Class representing the `CarbonInkElectrode` entity, which inherits from:
    - CarbonPasteElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec6f3d6f_bdf5_418f_9314_3ef2ff528103'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonInkElectrode'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CarbonInkElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec6f3d6f_bdf5_418f_9314_3ef2ff528103',
    
    class_name='CarbonInkElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec6f3d6f_bdf5_418f_9314_3ef2ff528103',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonInkElectrode',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    
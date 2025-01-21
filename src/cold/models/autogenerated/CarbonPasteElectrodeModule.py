
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InertElectrodeModule import InertElectrode







class CarbonPasteElectrode(InertElectrode):
    """
    Class representing the `CarbonPasteElectrode` entity, which inherits from:
    - InertElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b0a0dddb_d942_4af2_b6a7_d7165f4253f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CarbonPasteElectrode'`
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
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CarbonPasteElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b0a0dddb_d942_4af2_b6a7_d7165f4253f1',
    
    class_name='CarbonPasteElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b0a0dddb_d942_4af2_b6a7_d7165f4253f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CarbonPasteElectrode',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MercuryElectrodeModule import MercuryElectrode







class DroppingMercuryElectrode(MercuryElectrode):
    """
    Class representing the `DroppingMercuryElectrode` entity, which inherits from:
    - MercuryElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b76a778f_253f_4210_a67f_fb6444d0de26'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DroppingMercuryElectrode'`
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
    obj = DroppingMercuryElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b76a778f_253f_4210_a67f_fb6444d0de26',
    
    class_name='DroppingMercuryElectrode',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b76a778f_253f_4210_a67f_fb6444d0de26',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DroppingMercuryElectrode',
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
    

    
    

    

    
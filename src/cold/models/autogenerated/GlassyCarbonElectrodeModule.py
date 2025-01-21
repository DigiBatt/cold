
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InertElectrodeModule import InertElectrode







class GlassyCarbonElectrode(InertElectrode):
    """
    Class representing the `GlassyCarbonElectrode` entity, which inherits from:
    - InertElectrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_057bb143_639c_472b_99ed_ffa1867f6e63'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GlassyCarbonElectrode'`
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
    obj = GlassyCarbonElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_057bb143_639c_472b_99ed_ffa1867f6e63',
    
    class_name='GlassyCarbonElectrode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_057bb143_639c_472b_99ed_ffa1867f6e63',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GlassyCarbonElectrode',
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
    

    
    

    

    
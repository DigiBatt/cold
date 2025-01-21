
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodeReactionModule import ElectrodeReaction







class AnodicReaction(ElectrodeReaction):
    """
    Class representing the `AnodicReaction` entity, which inherits from:
    - ElectrodeReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a0580fa9_5073_44af_b33e_7adbc83892d0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnodicReaction'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AnodicReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a0580fa9_5073_44af_b33e_7adbc83892d0',
    
    class_name='AnodicReaction',
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a0580fa9_5073_44af_b33e_7adbc83892d0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnodicReaction',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    